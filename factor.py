# This program tries the accumulator
def main():
    n = int(input("Please, enter a whole number: "))
    fact = 1
    for factor in range(2, n + 1):
        fact = fact * factor
    print(float(fact))


main()
