#!/usr/bin/python

import subprocess
import random
import string

# enter client name from user
client = raw_input("Enter client name: ")

# generate random string from letters,num, and symbols with a 30 char range
def gen_key():
    return ''.join(random.choice(string.letters + string.digits + "!@#$%^&*") for i in range(30))

# find company name from pstdatabase.txt
existing_companies = set()
with open('pskdatabase.txt', 'r') as f:
    for line in f:
        company = line[:-37]
        existing_companies.add(company)

# check to see if company already exists in database
if client in existing_companies:
    raise Exception('Company already exists in database, enter your input in again.')

# find PSK from pstdatabase.txt
existing_keys = set()
with open('pskdatabase.txt', 'r') as f:
    for line in f:
        key = line[-31:][:-1]
        existing_keys.add(key)

# build keys until unique
for _ in range(30):
    new_key = gen_key()
    if not new_key in existing_keys:
        print new_key
        break

# if key in database 30 times in a row, raise exception
if new_key in existing_keys:
    raise Exception('Could not generate unique key.')


# append random string to file pskdatabase.txt with user input
PSKclient = client + " PSK: " + new_key + '\n'
with open('pskdatabase.txt','a') as f:
    f.write(PSKclient)

