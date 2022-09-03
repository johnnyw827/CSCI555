import pexpect


formatSymbol = ["#", ">>>", "> ", "$ "]


def send_command(child, command):
    child.sendline(command)
    child.expect(formatSymbol)
    print(child.before.decode("UTF-8"))


def connect(user, host, password):
    ssh_newkey = "Are you sure you want to continue connecting?"
    connStr = "ssh " + user + "@" + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "[P|p]assword: "])
    if ret == 0:
        print("ret==0", "[-] Error Connecting")
        return
    if ret == 1:
        print("ret==1")
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, "[P|p]assword: "])
        if ret == 0:
            print("ret==0", "[-] Error Connecting")
            return
    child.sendline(password)
    child.expect(formatSymbol)
    return child


def main():
    host = input("Enter the host name or IP: ")
    user = input("Enter the user account: ")
    password = input("Enter the password: ")
    child = connect(user, host, password)
    send_command(child, "ls")


if __name__ == "__main__":
    main()