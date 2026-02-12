print("this will always run")

def main():
    print(f"First module is being run directly, __name__ is {__name__}")


if __name__ == "__main__":
    main()