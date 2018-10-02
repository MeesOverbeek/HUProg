def newPassword(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) > 6:
        return True
    else:
        return False

#function checks wether the oldpassword is different from the old password (done through !=)
#it also checks wether the password is long enough (done through > 6)
#if BOTH conditions or met, True will be returned, Else False

#next up, the input will give the required parameters for the function
inputOldpassword = input("Geef hier uw oude paswoord: ")
inputNewpassword = input("Geef hier uw nieuwe paswoord: ")

#prints True or False based on the given values
print(newPassword(inputNewpassword, inputOldpassword))