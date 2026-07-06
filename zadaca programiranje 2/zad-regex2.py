import re

email_regex = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"

eduid_regex = r"^[a-zA-Z]+\.[a-zA-Z]+\d*@sum\.ba$"

email = input("Unesite e-mail: ")
eduid = input("Unesite eduId: ")

if re.match(email_regex, email):
    print("E-mail je validan.")
else:
    print("E-mail nije validan.")

if re.match(eduid_regex, eduid):
    print("eduId je validan.")
else:
    print("eduId nije validan.")