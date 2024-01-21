def get_city_cleaned(user_input):
    
    return user_input.strip().lower()


def is_gainesville(city):
    
    return True if city == "gainesville" else False


def main():
    user_input = input("Enter your current city: ")
    city = get_city_cleaned(user_input)
    print(is_gainesville(city))
    
if __name__ == "__main__":
    main()