from re import A
from time import sleep

re=1
pi=3.14159265358979323846264338327950288
print("███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗")
print("████╗░████║██╔══██╗████╗░██║██║░░██║")
print("██╔████╔██║███████║██╔██╗██║███████║")
print("██║╚██╔╝██║██╔══██║██║╚████║██╔══██║")
print("██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║")
print("╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝")
print(" ")
while re==1:
    x=str(input("Sử dụng đường kính(bk) hay bán kính(dk): "))
    if x=="dk":
        dk=float(input("Đường kính: "))
        dt=pi*dk/2*dk/2
        cv=pi*dk
        print("Chu vi: " , (round(cv,4)))
        print("Diện tích: " , (round(dt,4)))
        print("Xong")
        re=re+1
        rere=str(input("Có muốn tính lại không(y/n): "))
        if rere=="y":
            re=re-1
        if rere=="n":
            print("BYE")
            sleep(0.5)

    if x=="bk":
        bk=float(input("Bán kính: "))
        cv1=pi*bk*2
        dt1=pi*bk**2
        print("Chu vi: " , (round(cv1,4)))
        print("Diện tích: " , (round(dt1,4)))
        print("Xong")
        re=re+1
        rerere=str(input("Có muốn tính lại không(y/n): "))
        if rerere=="y":
            re=re-1
        if rerere=="n":
            print("BYE")
            sleep(0.5)
