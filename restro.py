a="Pizza-$100";b="Chilli Potato-$60";c="Rajma Chawal-$150";d="Paneer and Naan-$200";e="Mango Shake-$50";f="Cold Coffee-$50";g="Gulab Jamun-$30";h="Ice Cream-$20";li2=[0]
print("Menu---->")
for i in range(0,2):
    print("--'Starter'--")
    print(f"1.{a}\n2.{b}")
    ch1=int(input("Enter your choice(1/2/3 for nothing)"))
    if ch1==1:
        st=a
    elif ch1==2:
        st=b
    elif ch1==3:
        st=0
    else:
        print("Wrong choice")
        st=0
    print("--'Meal'--")
    print(f"1.{c}\n2.{d}")
    ch2=int(input("Enter your choice(1/2/3 for nothing)"))
    if ch2==1:
        me=c
    elif ch2==2:
        me=d
    elif ch2==3:
        me=0
    else:
        print("Wrong choice")
        me=0
    print("--'Drink'--")
    print(f"1.{e}\n2.{f}")
    ch3=int(input("Enter your choice(1/2/3 for nothing)"))
    if ch3==1:
        dr=e
    elif ch3==2:
        dr=f
    elif ch3==3:
        dr=0
    else:
        print("Wrong choice")
        dr=0
    print("--'Dessert'--")
    print(f"1.{g}\n2.{h}")
    ch4=int(input("Enter your choice(1/2/3 for nothing)"))
    if ch4==1:
        de=g
    elif ch4==2:
        de=h
    elif ch4==3:
        de=0
    else:
        print("Wrong choice")
        de=0
    if i==0:
        li=[st,me,dr,de]
    if i==1:
        li2=[st,me,dr,de]
    count=str(input("Do you want to select more(y/n):"))
    if count=="y":
        continue
    elif count=="n":
        break
    else:
        print("wrong choice")
        break
print("----------Your Choice--------->>")
print(li)
print(li2)  
    