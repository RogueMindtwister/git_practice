from finance import *

def main():
    print("Hello world!")
    for n in range(10):
        print(f"Number {n} cubed: {n**3}")
        print(f"Number {n} to the fifth: {n**5}")

    print(get_interest_rate())
    print(get_interest(1375.50, 0.02))

if __name__ == '__main__':
    main()