from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()
    hostname = input('hostname: ')
    username = input('username: ')
    password = getpass.getpass('password: ')
    s.login(hostname, username, password)

except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)