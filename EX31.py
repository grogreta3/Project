import re

email = input("Please type in an email address: ")

while email != "0":

    if re.match("\A(?P<name>[\w\-_.?]+)@(?P<domain>[\w\-_.?]+).(?P<toplevel>[\w]+)\Z", email, re.IGNORECASE):
        print("Email is valid")
        email = input("Please type in an email address: ")
        continue
    else:
        print("Email is invalid")
        email = input("Please type in an email address: ")
