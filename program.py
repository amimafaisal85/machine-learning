# # finding the smaleest of three numbers

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# c = int(input("Enter 3rd number:"))

# if  a < b and a < c:
#     print("Smallest number is: ", a)
# elif    b < a and b < c:
#     print("Smallest number is: ", b)
# else:
#     print("Smallest number is: ", c)
    


#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# movies=[]
# movies.append(input("Enter your first movie"))
# movies.append(input("Enter your second movie"))
# movies.append(input("Enter your third movie"))
# print("your favourite movies are:", movies)


#dictinary

# dic ={
#     "name" : "amima",
#     "age" : "19",
                     
# }


# words ={
#     "table":{
#         "a pice of furniture":"lists of fact anf figures",
#         "cat":"a small animal"}
# }
# print(words)


# myset ={"java","c++","java","python","c++","python"}
# print(myset)
# print(len(myset))



# dic={}
# dic.update({"maths":78})
# print(dic)

# dic ={
#     "name":"amima"
# }
# dic.update({"name":"amna"})
# print(dic)

# i=1
# mydic={}
# while i<=3:
#     subject =input("Enter your subject name ")
#     marks= int(input("Enter your marks "))
#     mydic.update({subject:marks})
#     i=i+1


# print(mydic)


# set={9,"9.0"}
# print(set)


#Print numbers from 1 to 10 using a while loop.

# num = 1 
# while num <=10:
#     print(num)
#     num += 1

#Ask the user for their name repeatedly until they type "stop".

# num = int(input("Enter a number (0 to stop): "))

# while num != 0:
#     print("You entered:", num)
#     num = int(input("Enter a number (0 to stop): "))

# print("Loop stopped because you typed 0.")

#Write a program that prints numbers from 10 down to 1, then prints "Done!".

# i = 10
# while i > 0 :
#     print(i)
#     i= i-1

# print("Done")

# dictionary 

# mydic = {
#     "name" :"amima",
#     "age" : 19,
#     "grade" : "A"

# }

# print(type(mydic))
# print(mydic)
# print(len(mydic))


# dictionary (adding new key-vale pair, changing values, remove a key-vale pair)

# person ={
#     "name": "amima",
#     "age" : 19,
#     "city" : "lahore"
# }

# print(person["name"])
# person["country"]="pakistan"
# print(person)

#changing values
#person["name"] = "amima"
#print(person)

#remove a key-vale pair
# person.pop("city")
# print(person)

# car ={
#     "brand": "toyota", "model": "corolla", "year": 2020}

#print(car["brand"])
# print(car.get("brand"))

# print(car.keys())

# print(car.values())

# print(car.items())

# car.update({"color":"black"})
# print(car)

# car.clear()
# print(car)

#while loopc(printing numbers from 1 to 10)

# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# def print_len(l):
#     print(len(l))


# l=[2, 3, 4, 5 ]
# print_len(l)

# def amima(l):
#     print(l)

# l=[1,23,4]
# amima(l)

# def factorial():
#     i=1
#     ans=1
#     while i<=5:
#         ans=ans*i
#         i=i+1
#     print(ans)
# factorial()


# for i in range(1,11):
    # print(i*2)

#print numbers from 10 down to 1
# for i in range(10, 0, -1):
#     print(i)

# print all mutiples of 3 between 3 and 30

# for i in range(3, 31, 3):
#     print(i)

# print number from 0 to 50, stepping by 5

# for i in range(0, 50 , 5):
#     print(i)

# print odd numbers from 1 to 15
# for i in range(1, 16, 2):
#     print(i)


# print reverse numbers (100,90,80,.....,10)

# for i in range(100, 0, -10):
#     print(i)

# num = int(input("enter a number"))
# for i in range(0, n+1):
#     print(i)

# def print_name(name):
#     for i in range(5):
#         print(name)


# print_name("Amima")

# def add(a,b):
#     print(a+b)

# result= add(3,4)
# print(result)

# square of  a number

# def square(num):
#     return num * num

# print(square(4))

# def greet(name):
#     print(f"hello,{name}")

# greet("amima")    

# def hello(i):
#     if(i==5): #stop condition
#         return

#     print(i)
#     hello(i+1) #recursion call

# hello(1)

# def printlist(l,i,length):
#     if 1==length:
#         return
#     print(l[i])
#     printlist(l,i+1,length)

# l=[4,2,3,4]
# printlist(l,0,4)

# class car:
#     name=""
#     color="red"
#     def__init__(self,name,color):
#         self.name-=name
#         self.color=color
#         print("contructor call")

#   class student:
#     name=""
#     urdu=1
#     english=2
#     math=3
#     def __init__(self,name,urdu,english,math):
#         self.name=name
#         self.urdu=urdu
#         self.english=english
#         self.math=math

#     def printaverage(self):
#         sum=self.urdu self.english self.math


# class bankaccount:
#     def __init__(self, name, password, bankaccount, balannce=0):
#         self.name=name
#         self.password=password
#         self.bankaccount=account
#         self.balance=balance

   
#     def creditcard(money):
#         creditcard+=money
#         print(creditcard)
    
#     def debitcard(selfmoney):
#         debitcard-=selfmoney
#         print(debitcard)

#     name=input("enter your name")
#     bankaccount=input("enter your bank account")
#     password=("enter your password")

#     for i in range(2):
#         print(name, bankaccount, password)
#     while True:
#     choice = show_menu()

#     if choice == "1":
#         amount = float(input("Enter amount to deposit: "))
#         account.deposit(amount)
#     elif choice == "2":
#         amount = float(input("Enter amount to withdraw: "))
#         account.withdraw(amount)
#     elif choice == "3":
#         account.show_balance()
#     elif choice == "4":
#         print("Thank you! Goodbye.")
#         break
#     else:
#         print("Invalid choice, try again.")

# class BankAccount:
#     def __init__(self, name, accountnumber, password, balance=0):
#         self.name = name
#         self.accountnumber = accountnumber
#         self.password = password
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")

#     def show_balance(self):
#         print(f"Current balance: {self.balance}")


# name = input("Enter your name: ")
# account_number = input("Enter your bank account number: ")
# password = input("Enter your password: ")

# account = BankAccount(name, account_number, password)

# while True:
#     choice = show_menu()

#     if choice == "1":
#         amount = float(input("Enter amount to deposit: "))
#         account.deposit(amount)
#     elif choice == "2":
#         amount = float(input("Enter amount to withdraw: "))
#         account.withdraw(amount)
#     elif choice == "3":
#         account.show_balance()
#     elif choice == "4":
#         print("Thank you! Goodbye.")
#         break
#     else:
#         print("Invalid choice, try again.")

# class BankAccount:
#     def __init__(self, name, accountnumber, password, balance=0):
#         self.name = name
#         self.accountnumber = accountnumber
#         self.password = password
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")

#     def show_balance(self):
#         print(f"Current balance: {self.balance}")

# name = input("Enter your name: ")
# account_number = input("Enter your bank account number: ")
# password = input("Enter your password: ")

# account = BankAccount(name, account_number, password)

# while True:
#    print("1. Deposit")
#    print("2. Withdraw")
#    print("3. Check Balance")
#    print("4. Exit")

# choice = input("Choose an option: ")

#     if choice == "1":
#         amount = float(input("Enter amount to deposit: "))
#         account.deposit(amount)
#     elif choice == "2":
#         amount = float(input("Enter amount to withdraw: "))
#         account.withdraw(amount)
#     elif choice == "3":
#         account.show_balance()
#     elif choice == "4":
#         print("Thank you! Goodbye.")
#         break
#     else:
#         print("Invalid choice, try again.")

class BankAccount:
    def __init__(self, name, accountnumber, password, balance=0):
        self.name = name
        self.accountnumber = accountnumber
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"Current balance: {self.balance}")


name = input("Enter your name: ")
account_number = input("Enter your bank account number: ")
password = input("Enter your password: ")

account = BankAccount(name, account_number, password)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Thank you! Goodbye.")
        break
    else:
        print("Invalid choice, try again.")
