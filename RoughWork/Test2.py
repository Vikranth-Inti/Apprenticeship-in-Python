import requests
import time
import requests, random
import logging

#STATUS
requests.get("https://instagram.com/")
usernames = [line.strip() for line in open("wordlist.txt")]
for username in usernames:
    r = requests.get("https://instagram.com/{username}")
    time.sleep(100)
    if r.status_code == 200:
        print("{username} is taken")
        with open("unavailable.txt", 'a') as f:
            f.write("{username}\n")
    if r.status_code == 404:
        print("{username} is available!")
        with open("available.txt", 'a') as f:
            f.write("{username}\n")
    if r.status_code == 429:
        print(r.status_code)