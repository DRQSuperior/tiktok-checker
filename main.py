from pystyle import Colors, Colorate
import requests
import random
import time
import os

endpoint = "https://tiktok.com/@{username}?is_copy_url=1&is_from_webapp=v1"

def check(username):
    response = requests.get(endpoint.format(username=username))
    
    if response.status_code == 200:
        html = response.content.decode("utf-8")
        id = html.split('"id":"')[1].split('"')[0]
        followers = html.split('"followerCount":')[1].split(",")[0]
        print(Colorate.Horizontal(Colors.red_to_purple, "[+] User exists: {username} | Followers: {followers} | ID: {id}".format(username=username, followers=followers, id=id)))
        with open("usernames.txt", "r") as f:
            usernames = f.read().splitlines()
        usernames.remove(username)
        with open("usernames.txt", "w") as f:
            f.write("\n".join(usernames))
    else:
        print(Colorate.Horizontal(Colors.green_to_blue, "[-] User doesn't exist or is banned: {username}".format(username=username)))
        with open("hits.txt", "a") as f:
            f.write(username + "\n")
        with open("usernames.txt", "r") as f:
            usernames = f.read().splitlines()
        usernames.remove(username)
        with open("usernames.txt", "w") as f:
            f.write("\n".join(usernames))
    
def generate(amount, length, chars):
    usernames = []
    for i in range(amount):
        username = ""
        for i in range(length):
            username += random.choice(chars)
        usernames.append(username)
    with open("usernames.txt", "w") as f:
        f.write("\n".join(usernames))
    print(Colorate.Horizontal(Colors.blue_to_purple, "Generated {amount} usernames".format(amount=amount)))
    time.sleep(5)
    os.system("cls")
    menu()

def menu():
    print(Colorate.Horizontal(Colors.blue_to_purple, "TikTok Username Checker by @drqsuperior__"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "----------------------------------------"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[1] Check Usernames"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[2] Generate Usernames"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[3] Exit"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "----------------------------------------"))
    option = input(Colorate.Horizontal(Colors.blue_to_purple, "Option: "))
    if option == "1":
        with open("usernames.txt", "r") as f:
            usernames = f.read().splitlines()
        for username in usernames:
            check(username)
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
            generate(amount, length, chars)
        elif usenumbers == "n":
            chars = "abcdefghijklmnopqrstuvwxyz"
            amount = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Amount: ")))
            length = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Length: ")))
            generate(amount, length, chars)
        else:
            print("Invalid option")
            time.sleep(2)
            os.system("cls")
            menu()
        generate(amount, length)
    elif option == "3":
        exit()
    else:
        print("Invalid option")
        time.sleep(2)
        os.system("cls")
        menu()

if __name__ == "__main__":
    menu()