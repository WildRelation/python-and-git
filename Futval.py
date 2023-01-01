def main():
    print("This program calculates the value of your principal in 10 years")

    principal = eval(input("How much money do you have?: "))
    APR = eval(input("Indicate your APR expressed as a decimal number"))

    for i in range(10):
        principal= principal * (1+APR)
        
    print ("The future value of your principal is", principal)

main()