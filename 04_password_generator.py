import secrets, string

def generate(length=12, symbols=True):
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += "!@#$%^&*()-_=+"
    return "".join(secrets.choice(chars) for _ in range(length))

def main():
    length = int(input("Length (default 12): ") or 12)
    symbols = input("Include symbols? (y/n): ").lower() != "n"
    print("Password:", generate(length, symbols))

if __name__ == "__main__":
    main()
