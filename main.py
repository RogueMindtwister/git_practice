def main():
    print("Hello world!")
    num = int(input("Please enter a number between 1 and 25: "))
    while num < 1 or num > 25:
        num = int(input("Invalid number entered, must be between 1 and 25. Enter again: "))
    for n in range(1, num+1):
        print(f"Number {n} cubed: {n**3}")
        print(f"Number {n} to the fifth: {n**5}")



if __name__ == '__main__':
    main()