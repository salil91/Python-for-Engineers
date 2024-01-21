import argparse
from datetime import date

def get_args():
    """Gets command line arguments"""
    
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()
    
    # Add arguments
    parser.add_argument("--name", "-n", default="user", help="User's name")
    parser.add_argument("--birthyear", "-y", default=1970, type=int, help="User's birth year")
    
    # Parse arguments
    args = parser.parse_args()
    
    return args


def main():
    """Says hello to the user"""
    args = get_args()
    name = args.name.strip().capitalize()
    age = date.today().year - args.birthyear
    
    print(f"\nHello, {name}! You are {age} years old today.")


if __name__ == "__main__":
    main()