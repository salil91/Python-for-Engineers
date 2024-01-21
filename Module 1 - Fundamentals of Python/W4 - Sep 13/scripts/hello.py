def get_name():
    """Gets user's name"""
    name = input("What is your name? ").strip().capitalize()
    
    # setting a default value if the user provides no input.
    if name == "":
        name = "user"
        
    return name


def main():
    """Says hello to the user"""
    name = get_name()
    print(f"\nHello, {name}!")
    
    
if __name__ == "__main__":
    main()