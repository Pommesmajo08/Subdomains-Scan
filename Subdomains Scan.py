import requests

log = open("data/Log.txt", "w")
log.write("")
log.close()
domain = input("Bitte füge hier eine Valide Domain ein!")
file = open("data/subdomains.txt")
subdomains = []
for i in file.readlines():
    subdomains.append(i.replace("\n", ""))
print(f"----- Checking {len(subdomains)} Subdomains -----")
log = open("data/Log.txt", "a")
log.write(f"----- Checking {len(subdomains)} Subdomains -----\n")
log.close()
found = []
for sub in subdomains:
    url = f"http://{sub}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        found.append(sub)
        print(f"[+++] Found : {sub}")
        log = open("data/Log.txt", "a")
        log.write(f"[+++] Found : {sub}\n")
log.close()