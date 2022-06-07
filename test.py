
#   intro

greeting = "Hello World"

print(len(greeting))
print(greeting[1])
print(greeting.upper())


w_amount = 100
account_num = 12345678

def cash_withdrawal(amount, accnum):
    print(f"Withdrawing {amount} from account {accnum}")

cash_withdrawal(w_amount, account_num)
cash_withdrawal(300,50449921)
cash_withdrawal(30,50449921)

print (int("54"))
print (int(5.4))

print (float(54))
print (float("54"))

print (str(54))
print (str(54.0))


print ("what is your name")
name = input()

if name:
    print(f"hello {name}, How are you?")
else:
    print("You did not give me your name")    


def add_up():
    num1=input("What is the first number youd like to add up? \n")
    num2=input("What is the second number youd like to add up? \n")

    try:
        print(f"{num1}+{num2} is {(int(num1) + int(num2))}!")
    except:
        print ("\n ERROR: please inpute only numberical values. \n")
    print("********************")
    add_up()
add_up()    





