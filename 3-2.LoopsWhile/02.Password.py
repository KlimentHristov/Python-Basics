username = input()
password = input()
entrancePass = input()

while entrancePass != password:
    entrancePass = input()
print(f"Welcome {username}!")