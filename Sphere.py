import math
def main():
    radius = float((input("Type the radius of the sphere ")))
    Vol = (4 * math.pi * radius ** 3)/3

    print(Vol)
    print()
    print("Do you want to calculate sphere's are as well?")

    answer = input ("Enter y/n (YES OR NO): ")
    if answer == "y":
        A = 4 * math.pi * radius ** 2
        print(A)
    else:
        print("Thank you for using my program :)")


main()