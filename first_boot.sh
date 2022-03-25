#!/bin/bash

# Authoriser clef publique pour root
mkdir /root/.ssh
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpf4CbfkUpKP7TSRc0lsLsImzZpVNLy3B9/aEV/6DZLc1YJmdXWjA6muAv+wvLMf3EpNA5wX74Xn/6+k5wI3Hf14A5qVo7iulUbcE0av3x3HUbUn047RSUF/mRC2OEoTdDn78S6qOzehUbB3hb4g/jqsBC7OvUWJKYQZA6vqPrqW7t1/34u0x9iPT63zNDL16Xo1MjIjptedst7Q4svyoTYky8uWm8k7DE3WRMEU8TesV9c8/0lqgPCBAYx8HbhuFAQh1JKb5mlCC3l0R45YXKRK2YYVlQdZYRqZO3LNtZnwyFTVBaG3PUyn8PuQJZm1PAvJ6nYQC94gqwkzxsMlRVQwt6bymgD5aGpjr2/0hVttnHV3ciMDXMBxy9nXEAitCWVpIE/BEJEITNyrvD+WzT9UHGKxIFX0cbgvs6pjlmJQNWoa+UytBjkW3qQIMriU91OUACqeL91H4RboDVwBBxMhqyzRua+U6U6IvH4dA5RicaRol6QSUfLnZM0SpAWFM=" >> /root/.ssh/authorized_keys
echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
chmod 755 /root/.ssh
chmod 644 /root/.ssh/authorized_keys
systemctl restart ssh

# Créer utilisateur hackerman avec mot de passe: Password1
chmod 770 /home/dietpi
useradd -p saMNhdbYqwtng hackerman
usermod -aG sudo hackerman
usermod -aG sudo dietpi
usermod -d /home/dietpi hackerman

# Install & configure vsftpd
wget https://raw.githubusercontent.com/PatStLouis/IdO_2022/main/vsftpd.conf
apt install vsftpd -y

mv /etc/vsftpd.conf /etc/vsftpd.conf.bak
mv ./vsftpd.conf /etc/vsftpd.conf
chmod 644 /etc/vsftpd.conf
mkdir -p /srv/vsftpd/root/public
touch /srv/vsftpd/banne
chown -R ftp:ftp /srv/vsftpd/
chmod -R 555 /srv/vsftpd/
chmod 775 /srv/vsftpd/root/public

systemctl start vsftpd
systemctl enable vsftpd
systemctl restart vsftpd

