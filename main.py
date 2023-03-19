from pystyle import Colors, Colorate
import requests
import random
import time
import os
import concurrent.futures

endpoint = "https://tiktok.com/@{username}?is_copy_url=1&is_from_webapp=v1"
checked_usernames = 0

def make_dir():
    if not os.path.exists("usernames.txt"):
        with open("usernames.txt", "w") as f:
            f.write("")
    if not os.path.exists("hits.txt"):
        with open("hits.txt", "w") as f:
            f.write("")

def read_hits():
    with open("hits.txt", "r") as f:
        return set(f.read().splitlines())

def set_title():
    global checked_usernames
    os.system(f"title TikTok Username Checker  [+] Checked usernames: {checked_usernames}/{len(read_usernames())}  [+] Hits: {len(read_hits())}")

def read_usernames():
    with open("usernames.txt", "r") as f:
        return set(f.read().splitlines())

def write_usernames(usernames):
    with open("usernames.txt", "w") as f:
        f.write("\n".join(usernames))

def check_username(username):
    global checked_usernames
    checked_usernames += 1
    set_title()

    response = requests.get(endpoint.format(username=username))
    
    if response.status_code == 200:
        html = response.content.decode("utf-8")
        id = html.split('"id":"')[1].split('"')[0]
        followers = html.split('"followerCount":')[1].split(",")[0]
        print(Colorate.Horizontal(Colors.red_to_purple, f"[-] Username taken: {username} | Followers: {followers} | ID: {id}"))
        return True
    else:
        print(Colorate.Horizontal(Colors.green_to_blue, f"[+] Username available: {username} | Followers: 0 | ID: 0"))
        with open("hits.txt", "a") as f:
            f.write(username + "\n")
        return False

def check_usernames(usernames):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(check_username, usernames))
    new_usernames = {username for username, exists in zip(usernames, results) if not exists}
    return new_usernames

def generate_usernames(amount, length, chars):
    usernames = set()
    while len(usernames) < amount:
        os.system("cls")
        print(Colorate.Horizontal(Colors.blue_to_purple, f"Usernames generated: {len(usernames)}"))
        username = ''.join(random.sample(chars, length))
        if not username.isdigit() and username not in usernames:
            usernames.add(username)
    write_usernames(usernames)
    print(Colorate.Horizontal(Colors.blue_to_purple, f"Generated {len(usernames)} usernames"))
    time.sleep(5)
    os.system("cls")
    menu()

def menu():
    print(Colorate.Horizontal(Colors.blue_to_purple, "TikTok Username Checker by @drqsuperior__"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "----------------------------------------"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[1] Check Usernames"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[2] Generate Usernames"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[3] Github"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[4] Exit"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "----------------------------------------"))
    option = input(Colorate.Horizontal(Colors.blue_to_purple, "Option: "))
    print(Colorate.Horizontal(Colors.blue_to_purple, "----------------------------------------"))
    if option == "1":
        with open("usernames.txt", "r") as f:
            usernames = f.read().splitlines()
        for username in usernames:
            check_username(username)
        print(Colorate.Horizontal(Colors.blue_to_purple, "Finished checking all usernames"))
        time.sleep(5)
        os.system("cls")
        menu()
    elif option == "2":
        usenumbers = input(Colorate.Horizontal(Colors.blue_to_purple, "Use numbers? (y/n): "))
        if usenumbers == "y":
            chars = "abcdefghijklmnopqrstuvwxyz1234567890"
            amount = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Amount: ")))
            length = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Length: ")))
            generate_usernames(amount, length, chars)
        elif usenumbers == "n":
            chars = "abcdefghijklmnopqrstuvwxyz"
            amount = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Amount: ")))
            length = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Length: ")))
            generate_usernames(amount, length, chars)
        else:
            print("Invalid option")
            time.sleep(2)
            os.system("cls")
            menu()
        generate_usernames(amount, length)
    elif option == "3":
        os.system("start https://github.com/DRQSuperior/tiktok-checker")
        time.sleep(2)
        os.system("cls")
        menu()
    elif option == "4":
        exit()
    else:
        print("Invalid option")
        time.sleep(2)
        os.system("cls")
        menu()

if __name__ == "__main__":
    os.system("cls")
    make_dir()
    set_title()
    menu()
