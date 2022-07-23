from hashlib import sha256
import re
re.escape("")
print("""
                          | |   | |               | |
  ___  _ __  _   _  _ __  | |_  | |_  ___    ___  | |
 / __|| '__|| | | || '_ \ | __| | __|/ _ \  / _ \ | |
| (__ | |   | |_| || |_) || |_  | |_| (_) || (_) || |
 \___||_|    \__, || .__/  \__|  \__|\___/  \___/ |_|
              __/ || |     by ilies                          
             |___/ |_|                               
""")
print
entree = input("entrez le nom du fichier a chiffrer: ")
sortie = input("entrez le nom du fichier qui sera crypté :")
key = input("entrez une clé :")
keys = sha256(key.encode('utf-8')).digest()

ket = sha256(key.encode('utf-8')).digest()

with open(entree, 'rb') as f_entree:
    with open(sortie, 'wb') as f_sortie:
        i = 0
        while f_entree.peek():
          c = ord(f_entree.read(1))
          j = i % len(keys)
          b = bytes([c^keys[j]])
          f_sortie.write(b)
          i = i + 1

print("Fichier crypté avec succes, il est disponible dans le fichier:")
print (sortie)

