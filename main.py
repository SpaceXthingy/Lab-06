def encode():
    user_password = input("password ")
    new_user_password = ""
    for i in range(len(user_password)):
        new_user_password = new_user_password + (str(int(user_password[i]) + 3))[-1]
    return (new_user_password)

def decode(encoded_password):
    new_user_password = ""
    for i in range(len(encoded_password)):
        new_user_password = new_user_password + (str(int(encoded_password[i]) - 3))[-1]

    return new_user_password



