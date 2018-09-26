def newPassword(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) > 6:
        return True
    else:
        return False

inputOldpassword = input("Geef hier uw oude paswoord: ")
inputNewpassword = input("Geef hier uw nieuwe paswoord: ")

print(newPassword(inputNewpassword, inputOldpassword))