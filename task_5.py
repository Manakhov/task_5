import re


mail_user = input()
if re.fullmatch(r"[^_\W]+@[^_\W]+[.][^_\W]+", mail_user):
    print("Good")
else:
    print("Bad")
