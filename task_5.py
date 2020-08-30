import re


mail_user = input("Please enter your mail: ")
if re.fullmatch(r"[\da-zA-Z]+@[\da-zA-Z]+[.][\da-zA-Z]+", mail_user):
    print("Good")
else:
    print("Bad")
