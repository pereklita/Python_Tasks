guest_name=input("Enter your name ")
def love(guest_name):
    if guest_name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {0}!".format(guest_name)
print(love(guest_name))

