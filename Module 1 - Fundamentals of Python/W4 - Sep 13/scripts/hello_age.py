from datetime import date

def get_name():
    """Gets user's name"""
    name = input("What is your name? ").strip().capitalize()
    
    # setting a default value if the user provides no input.
    if name == "":
        name = "user"
        
    return name


def get_birthyear():
    """Gets user's birth year"""
    year = input("What is your birthyear? ").strip()
    
    # setting a default value if the user provides no input.
    if year == "":
        year = 1970
        print("Using default birthyear of 1970.")
    else:
        year = int(year)
        
    return year


def main():
    """Says hello to the user"""
    name = get_name()
    
    birthyear = get_birthyear()
    age = date.today().year - birthyear
    
    print(f"\nHello, {name}! You are {age} years old today.")
    

if __name__ == "__main__":
    main()