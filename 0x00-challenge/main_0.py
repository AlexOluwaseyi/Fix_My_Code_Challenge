#!/usr/bin/python3
User = __import__('3-user').User

if __name__ == '__main__':
    print("Correction test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = "pwdCorrection"
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if setter to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if setter to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right \
password")

    if user_1.is_valid_password("NotMine"):
        print("is_valid_password should return False if it's not the right \
password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")

    if user_2.is_valid_password("Nop nop"):
        print("is_valid_password should return False if no password set \
before")
