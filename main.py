def encode(password):
    passcode = []
    for i in range(len(password)):
        passcode.append(chr(ord(password[i]) + 3))

    return "".join(passcode)

def decode(password):
    decoded = []
    for i in range(len(password)):
        decoded.append(chr(ord(password[i]) - 3))

    return "".join(decoded)

if __name__ == "__main__":

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu = input("Please enter an option: ")
        if menu == "1":
            password = (input("Enter your password to encode: "))
            code = encode(password)
            print("Your password has been encoded and stored!")

        if menu == "2":
            dec = decode(code)
            print(f"The encoded password is {code}, and the original password is {dec}")
            
        if menu == "3":
            exit()


