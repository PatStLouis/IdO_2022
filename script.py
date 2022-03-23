import paramiko
import nmap
import json

def scan_reseau(reseau):
    hosts = []
    nm = nmap.PortScanner()
    nm.scan(hosts=f'{reseau}/24', arguments='-sn')
    for host in nm.all_hosts():
        print(host)
        # if nm[host]:
        #     hosts.append(host)
    return hosts

def conn_password(host, username, password):
    result = False
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, 22, username, password)
            stdin, stdout, stderr = ssh.exec_command("whoami")
            output = stdout.read()
            ssh.close()
        except:
            output = False

    if output:
        result = True
        
    return result

def conn_priv_key(host, username, keyfile):
    result = False
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, 22, username, keyfile)
            stdin, stdout, stderr = ssh.exec_command("whoami")
            output = stdout.read()
            ssh.close()
        except:
            output = False

    if output:
        result = True

    return result

def main():
    final_score = {}
    hosts = scan_reseau("192.168.1.0")
    # for host in hosts:
    #     vuln1 = conn_password(host, "dietpi", "dietpi")
    #     vuln2 = conn_priv_key(host, "dietpi", "./id_ed25519.pub")
    #     vuln3 = conn_password(host, "hackerman", "Password1")
    #     vuln4 = "TODO" # Serveur FTP
    #     vuln5 = "TODO" # Cronjob? Serveur web?
    #     results = {
    #         "vuln1": vuln1,
    #         "vuln2": vuln2,
    #         "vuln3": vuln3,
    #         "vuln4": vuln4,
    #         "vuln5": vuln5
    #     }
    #     final_score[host] = results

    # with open("./final_score.json", "w") as f:
    #     final_score = json.dumps(final_score, indent=5)
    #     f.write(final_score)

main()
