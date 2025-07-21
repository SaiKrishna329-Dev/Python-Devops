import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Process command line arguments")
    parser.add_argument("--num1", type=int, required=True, help="First number")
    parser.add_argument("--num2", type=int, required=True, help="Second number")
    parser.add_argument("--operation", type=str,
                        choices=["add", "subtract", "multiply", "divide"],
                        required=True, help="Operation to perform")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.operation == "add":
        print(f"The result of addition is: {args.num1 + args.num2}")
    elif args.operation == "subtract":
        print(f"The result of subtraction is: {args.num1 - args.num2}")
    elif args.operation == "multiply":
        print(f"The result of multiplication is: {args.num1 * args.num2}")
    elif args.operation == "divide":
        if args.num2 != 0:
            print(f"The result of division is: {args.num1 / args.num2}")
        else:
            print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()
    
# Example usage of argparse to handle command line arguments:
# This script uses argparse to parse command line arguments for a simple calculator.
# It takes two numbers and an operation (add, subtract, multiply, divide) as input
# and performs the specified operation on the numbers.