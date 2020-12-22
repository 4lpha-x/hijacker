#!/bin/python3
# Author : HACKE-RC commonly known as RC
# Description : hijacker by RC - A python tool to find all the broken links of a page.
# Developer contact: @coder_rc on twitter. You can request new feature by tagging me on any of your tweet.

#Importing the codes that i haven't coded or you can say I am importing modules.
import os #For system level operations
import threading #For speed++
from sys import argv #For command line args
import urllib3 #For sending GET Requests
import requests #For doing nothing
from bs4 import BeautifulSoup #For parsing html and extracting urls from a tag
import re #For doing research or re.search

class Scanner():
    '''Hmmm...
    Debug me...'''
    @staticmethod
    def banner(reason=0):
        '''
        Just for printing banner!
        '''
        banner = r"""
 _   _ _  _            _             
| | | (_)(_) __ _  ___| | _____ _ __ 
| |_| | || |/ _` |/ __| |/ / _ \ '__|
|  _  | || | (_| | (__|   <  __/ |   
|_| |_|_|/ |\____|\___|_|\_\___|_|   
       |__/                        
"""
        if reason==0:
            print("[?] Arguments Missing [?]")
        else:
            pass
        print(banner)
        print("\t\t\t\t\tv1.0")
        print(f"------------ Hijacker by RC ------------")
        print("----- github.com/HACKE-RC/Hijacker -----")
        print("A python tool to find all the broken links of a page.")
        print("Usage:")
        print("\thijacker [ website ] [ optional args ]")
        print("Optional Arguments:\n\t-v, --verbose\tEnable verbose mode")
        exit(1)
    @staticmethod
    def do_scan(url):
        link = url
        try:
            if verbose:
                print(f"[v] Scanning on {url}... [v]")
            res = http.request("GET", link)
            if verbose:
                    print(f"[v] URL => {url} has status code => {res.status} [v]")
            if res.status==200:
                pass
            elif res.status==400 and "twitter.com" in url:
                pass
            elif re.search("Sorry, that page doesn’t exist!", res.data):
                print(f"The URL => {link} appears to be dead...")
                print(f"Results show that URL => {link} is likely a twitter profile.")
            elif re.search("This page isn't available", res.data):
                print(f"The URL => {link} appears to be dead...")
                print(f"Results show that URL => {link} is likely a facebook/instagram page/profile.")
            elif re.search("Not found", res.data) or re.search("Not Found". res.data) or re.search("not found", res.data):
                print(f"The URL => {link} appears to be dead...")
            elif re.search("not exits", res.data) or re.search("Not exits". res.data) or re.search("Not Exits", res.data):
                print(f"The URL => {link} appears to be dead...")
            else:
                print(f"The URL => {link} appears to be dead...")
        except KeyboardInterrupt:
            print("Bye Bye!")
            exit(0)
        except:
            print(f"The URL => {link} appears to be dead...")

#Colors
green = "\033[1;32;40m"
red = "\033[1;31;40m"
drk = "\033[1;30;40m"
white = "\033[1;37;40m"

urllib3.disable_warnings() #For disabling all the useless/usefull warnings from urllib3 
http = urllib3.PoolManager(cert_reqs='CERT_NONE') #For using no certificates for http requests

result = open('results.txt', 'a') #Opening a results file in append mode.

#Usage
usage = f"{red}[?] Arguments Missing [?]\n\n{green}Usage : {white} webScrap url\n\n{red}Example : {white} webScrap https://www.example.com"

#Checking the arguments length of command line arguments passed
if (len(argv) <= 1):
    Scanner.banner(1)

ur = argv[1]

if ur == "-h" or ur == "--help":
    Scanner.banner(1)
    exit(0)

if "." not in ur: #Checking if the url supplied is valid or not
    print("[ ERR ] Please supply a valid url [ ERR ]")
    Scanner.banner(1)
    exit(0)
for i in argv:
    if "--verbose" in i or "-v" in i:
        verbose = True
    else:
        verbose = False
try:
    tempvar = verbose
except:
    pass

print("[ INF ] Checking the connection of the host... [ INF ]")
try:
    # url = requests.get(ur) - Not using this beacause this willn't work if a user will a url without specifying the http or https protocol.
    url = http.request("GET", ur)
except KeyboardInterrupt:
    print("Bye Bye!")
    exit(0)
except:
    print(f"{red}The host/domain you provided appears to be dead or you have some issues with internet.")
    exit(0)
print(f"{white}[i] Connected [i]")
# cont = url.content
cont = url.data
soup = BeautifulSoup(cont, 'html.parser')
anc = soup.find_all('a')
all_links = set()


def full(link):
    try:
        link.get('href')
    except:
        pass
    if link.get('href') != "#":
        if link.get('href').startswith('http'):
            wr = link.get('href')
            all_links.add(wr)
        else:
            link1 = f"{ur}{link.get('href')}"
            all_links.add(link1)
            result.write(link1)  

for link in anc:
    try:
        thread = threading.Thread(target=full, args=(link,))
        thread.start()
    except KeyboardInterrupt:
        print("Bye Bye!")
        exit(0)

final = list(all_links)
final = '\n'.join(final)
result.write(final+"\n")
print(f"Found total {len(all_links)} links.")
print("Scanning links...")

if __name__ == "__main__":
    for link in all_links:
        thread = threading.Thread(target=Scanner.do_scan, args=(link,))
        thread.start()
