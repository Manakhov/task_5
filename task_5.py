import re


vault = {'whitelist': ['good@good.good', 'notbad@notbad.notbad'],
         'blacklist': ['penis@penis.penis', 'bad@bad.bad']}
print("Write 'exit' to exit.")
while True:
    mail_user = input("Please enter your mail: ")
    if mail_user == 'exit':
        break
    if re.fullmatch(r"[\da-zA-Z]+@[\da-zA-Z]+[.][\da-zA-Z]+", mail_user):
        print("Good.")
        if mail_user in vault['whitelist']:
            print("Your mail in whitelist.")
        elif mail_user in vault['blacklist']:
            print("Your mail in blacklist.")
    else:
        print("Bad.")
