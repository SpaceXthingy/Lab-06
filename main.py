def encode():
    user_password = input("password ")
    new_user_password = ""
    for i in range(len(user_password)):
        new_user_password = new_user_password + (str(int(user_password[i]) + 3))[-1]
    print(new_user_password)

encode()


#def decode():


