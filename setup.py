import os


try:
    os.mkdir("data")
except FileExistsError:
    print("Der Ordner data existiert bereits!")
try:
    f = open("data/subdomains.txt", "r")
    f.read()
    f.close()
except FileNotFoundError:
    print("Du must zuerst die Datei: subdomains.txt herunterladen! Kopiere sie nun in den Data ordner und starte das Programm erneut!")
    taste = input("Verstanden?")
    exit(-1)
except FileExistsError:
    print("Der Data ordner existiert bereits!")
except:
    print("Etwas ist schiefgelaufen!")
print("Setup Erfolgreich abgeschlossen! Nun kannst du die Subdomains Scan.py ausführen!")
