def check_age(age):
    if age < 13:
        return "you are a child"
    elif age < 20:
        return "you are a teenager"
    elif age < 65:
        return " wewe dedi tu wallai"
    else:
        return "sasa wewe uko wapi bro!"
    age = int(input("Enter your age:"))
    print(check_age(age))