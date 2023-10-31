def encode(user_input):
    new_user_password = ""
    for i in range(len(user_input)):
        new_user_password = new_user_password + (str(int(user_input[i]) + 3))[-1]
    return (new_user_password)

def decode(encoded_password):
    new_user_password = ""
    for i in range(len(encoded_password)):
        new_user_password = new_user_password + (str(10 + int(encoded_password[i]) - 3))[-1]

    return new_user_password

encoded_pass = ""
decoded_pass = ""


def main():
    menu = True
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
            print()
        if menu_option == 2:
            decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass} ")
            print()
        if menu_option == 3:
            break


if __name__ == "main":
    main()

