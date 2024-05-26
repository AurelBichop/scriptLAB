#!/usr/bin/python3

import hashlib

valeurDeHachage = input("Entrer votre texte a Hacker menu menu ...\n --> ")

hashObjet1 = hashlib.md5()

hashObjet1.update(valeurDeHachage.encode())

print(hashObjet1.hexdigest())
