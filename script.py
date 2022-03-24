import paramiko
import socket
import nmap
import json
import time

RESEAU = "192.168.0.0"

def trouver_son_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def scan_reseau(reseau):
    hosts = []
    print(
        f"""
    Scan du réseau {reseau}/24 en cours...
    ==============

    """
    )
    nm = nmap.PortScanner()
    nm.scan(hosts=f"{reseau}/24", arguments="-sn")
    all_hosts = nm.all_hosts()
    # Retirer la Gateway
    all_hosts.remove("192.168.0.1")
    # Retirer notre IP
    all_hosts.remove(trouver_son_ip())
    print(
        f"""
    Adresses trouvées
    =================
    {all_hosts}

    """
    )

    return all_hosts


def conn_password(host, username, password):
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, 22, username=username, password=password)
            stdin, stdout, stderr = ssh.exec_command("whoami")
            output = stdout.read()
            output = output.decode("utf-8").strip()
            ssh.close()
        except:
            """ TODO tester et fixer les exceptions
            paramiko.ssh_exception.AuthenticationException
            """
            return False
    if output == username:
        return True
    return False



def conn_priv_key(host, username, keyfile):
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, username=username, key_filename=keyfile)
            stdin, stdout, stderr = ssh.exec_command("whoami")
            output = stdout.read()
            output = output.decode("utf-8").strip()
            ssh.close()
        except:
            """ TODO tester et fixer les exceptions
            paramiko.ssh_exception.AuthenticationException
            """
            return False

    if output == username:
        return True
    return False


def main():
    final_score = {}
    hosts = scan_reseau(RESEAU)
    time.sleep(5)
    # Décommenter cette ligne pour assigner une liste d'ip statiques.
    # hosts = ["192.168.0.18"] 
    for host in hosts:
        print(
            f"""

        Tentatives de piratage sur {host}
        ==========================
        """
        )
        print("Mot de passe par défault")
        vuln1 = conn_password(host, "dietpi", "dietpi")
        print("Clef publique authorisée")
        vuln2 = conn_priv_key(host, "dietpi", "./id_rsa.pub")
        print("Utilisateur caché")
        vuln3 = conn_password(host, "hackerman", "Password1")
        print("Serveur FTP insécure")
        vuln4 = "TODO"  # Serveur FTP
        print("Cronjob")
        vuln5 = "TODO"  # Cronjob? Serveur web?
        results = {
            "vuln1": vuln1,
            "vuln2": vuln2,
            "vuln3": vuln3,
            "vuln4": vuln4,
            "vuln5": vuln5,
        }
        final_score[host] = results

    with open("./final_score.json", "w") as f:
        final_score = json.dumps(final_score, indent=5)
        f.write(final_score)

    print(r"""
        .__________________________________________.
        |                                          |
        | Terminé, les résultats sont enregistrés! |
        |__________________________________________|  
            ^
           / 
      __  /    
    _|  |__    )
    ( O_O)    (
    __|__      )
   /  |  \__@c|_|
  /   |      
 @   / \
   _/   \_
    
    """)

main()
