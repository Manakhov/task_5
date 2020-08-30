import re


def check_mail(mail, dict_white_black):
    if re.fullmatch(r"[\da-zA-Z]+@[\da-zA-Z]+[.][\da-zA-Z]+", mail):
        print("Good.")
        if mail in dict_white_black['whitelist']:
            print("Your mail in whitelist.")
        elif mail in dict_white_black['blacklist']:
            print("Your mail in blacklist.")
        return True
    else:
        return False


def check_password(password):
    if re.search(r"\s", password):
        print("The password must not be any non-displayable symbols.")
        return False
    elif len(password) < 8:
        print("The password length must be at least 8.")
        return False
    elif len(re.findall(r"\d", password)) < 3 or \
            len(re.findall(r"[a-zA-Z]", password)) < 3 or \
            len(re.findall(r"[\W_]", password)) < 1:
        print("The password must be at least 3 digits, 3 letters, 1 symbol.")
        return False
    return True


vault = {'whitelist': ['good@good.good', 'notbad@notbad.notbad'],
         'blacklist': ['penis@penis.penis', 'bad@bad.bad']}
print("Write 'exit' to exit.")
while True:
    mail_user = input("Please enter your mail: ")
    if mail_user == 'exit':
        break
    if check_mail(mail_user, vault):
        while True:
            password_user = input("Please enter your password: ")
            if check_password(password_user):
                break
    else:
        print("Bad.")
