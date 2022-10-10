from time import sleep
import subprocess
import platform
import os

os.system('cls')
print("███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗")
print("████╗░████║██╔══██╗████╗░██║██║░░██║")
print("██╔████╔██║███████║██╔██╗██║███████║")
print("██║╚██╔╝██║██╔══██║██║╚████║██╔══██║")
print("██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║")
print("╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝")
print(" ")

y=3

while y==3:
    operating_sys = platform.system()

    def ping(ip):
        ping_command = ['ping', ip, '-n', '1'] if operating_sys == 'Windows' else ['ping', ip, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False
    
        ping_output = subprocess.run(ping_command,shell=shell_needed,stdout=subprocess.PIPE)
        success = ping_output.returncode
        tr= ip + " : " + "Online"
        fl= ip + " : " + "TimeOut"
        return tr if success == 0 else fl

    print(ping("1.vpscuamanh.tk"))
    print(ping("2.vpscuamanh.tk"))
    print(ping("3.vpscuamanh.tk"))
    print(ping("4.vpscuamanh.tk"))
    print(ping("manhchu.cf"))
    y=y+1
    print(" ")
    re=str(input("Có muốn ping lại không(y/n): "))
    if re=="y":
        y=y-1
    if re=="n":
        print("BYE")
        sleep(0.5)
