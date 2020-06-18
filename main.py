def main():
    print("Hello world!")
    num = int(input("Please enter a number between 1 and 25: "))
    while num < 1 or num > 25:
        num = int(input("Invalid number entered, must be between 1 and 25. Enter again: "))
    for n in range(1, num+1):
        print(f"Number {n} cubed: {n**3}")
        print(f"Number {n} to the fifth: {n**5}")

    print("------FACTORIAL TESTING-----")
    print(fact(8))
    comprhensions()

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

# A function that demonstrates list comprehensions
def comprhensions():
    numbers = [1, 5, 6, 73, 3, 32, 16, 7, 55, 21, 75]

    altered_numbers = [number ** 2 for number in numbers]
    print(altered_numbers)

if __name__ == '__main__':
    main()