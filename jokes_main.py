from joke import get_random_joke

def main():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    while True:
        user_response = input("Do you want to hear a joke? (yes/no): ").strip().lower()
        if user_response == 'yes':
            joke = get_random_joke()
            print(f"Here's a joke for you: {joke}")
        elif user_response == 'no':
            print("Okay, have a great day!")
            break

if __name__ == "__main__":
    main()