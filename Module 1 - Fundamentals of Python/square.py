def square_number(x: float) -> float:
    squared = x*x
    print(f"The square of {number} is {squared}")

    return squared


number = float(input("Enter a number: "))
squared_number = square_number(number)
print(f"Squared Number: {squared_number}")
