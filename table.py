def table():
    count=int(input("Enter number you want table of(1-10): "))
    if count<=0:
        print("Enter number greater than zero")
    elif count>10:
        print("Enter number smaller than or equal to 10")
    if count>0 and count<=10:
        print(f"Table of {count}")
        for i in range(1,11):
            print(f"{count}X{i}={count*i}")
table()