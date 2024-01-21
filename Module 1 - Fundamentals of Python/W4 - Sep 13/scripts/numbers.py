import argparse

def get_args():
    """Gets command line arguments"""
    
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()
    
    # Add argument with any number of inputs
    parser.add_argument("numbers", nargs="*", type=int, help="Numbers to be added")
    
    # Add argument as a flag
    parser.add_argument("--verbose", action="store_true", default=False, help="Flag for verbose print")
    
    # Parse arguments
    args = parser.parse_args()
    
    return args


def main():
    """Says hello to the user"""
    args = get_args()
    numbers_sum = sum(args.numbers)
    
    if args.verbose:
        print(f"\nThe sum of all the entered numbers is {numbers_sum}.")
    else:
        print(f"\nSum = {numbers_sum}")


if __name__ == "__main__":
    main()