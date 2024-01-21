def get_int():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            pass

        
def square(number):
    
    return number**2


def cube(number):
    
    return number**3


def main():
    number = get_int()
    print(f"The square of {number} is {square(number)}")
    print(f"The cube of {number} is {cube(number)}")



if __name__ == "__main__":
    main()