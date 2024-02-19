def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    number = int(input("Enter a positive number: "))
    if number <= 0:
        print("Please enter a positive number.")
    else:
        factors = find_factors(number)
        print("Factors of", number, "are:", factors)

if __name__ == "__main__":
    main()
