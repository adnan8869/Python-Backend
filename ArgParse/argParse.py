import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="First number")
    parser.add_argument("--number2", help="Second number")
    parser.add_argument("--operation", help="Operation to perform", choices=["add", "subtract", "multiply", "divide"])


    args = parser.parse_args()

    print(f"Number1: {args.number1}")
    print(f"Number2: {args.number2}")
    print(f"operation: {args.operation}")
    
    #inputs added by command line as returns as a string.
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = 0
    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "subtract":
        result = n1 - n2
    elif args.operation == "multiply":
        result = n1 * n2
    elif args.operation == "divide":
        result = n1 / n2

    print(f"Result: {result}")