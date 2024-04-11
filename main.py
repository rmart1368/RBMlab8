def encode(password):
    passcode = []
    for i in range(len(password)):
        passcode.append(chr(ord(password[i]) + 1))

    return "".join(passcode)


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
            pass
        if menu == "3":
            exit()
