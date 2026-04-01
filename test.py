print("WELCOM TO MY GPA CALCULATER")
name = input("Enter your name :-- ")
englishth = int(input("ENGLISH TH :--"))
englishin = int(input("ENGLISH IN:--"))

nepalith = int(input("NEPALI TH :--"))
nepaliin = int(input("NEPALI IN :--"))

socialth = int(input("SOCIAL TH :--"))
socialin = int(input("SOCIAL IN :--"))

businessth = int(input("BUSINESS TH :--"))
businessin = int(input("BUSINESS IN :--"))

economicsth = int(input("ECONOMICS TH :--"))
economicsin = int(input("ECONOMICS IN :--"))

accountth = int(input("ACCOUNT TH :--"))
accountin = int(input("ACCOUNT IN :--"))


def grede(marks):
    if (marks >= 91):
        return 4
    
    if (marks >= 81 and marks <= 90):
        return 3.6
    elif (marks >= 81 and marks <= 90):
        return 3.6
    elif (marks >= 71 and marks <= 80):
        return 3.2
    elif (marks >= 61 and marks <= 70):
        return 2.8
    elif (marks >= 51 and marks <= 60):
        return 2.4
    elif (marks >= 41 and marks <= 50):
        return 2
    elif (marks >= 35 and marks <= 40):
        return 1.6
    else:
        return NG

num_nepali = nepalith + nepaliin
nepali = grede(num_nepali)

num_english = englishth + englishin
english = grede(num_english)

num_social = socialth + socialin
social = grede(num_social)

num_business = businessin + businessth
business = grede(num_business)

num_economics = economicsin + economicsth
economics = grede(num_economics)

num_account = accountin + accountth
account = grede(num_account)

def GPA():
    gpa = (nepali + english + social + economics + business + account) / 6
    print("Mr.",name, "YOU GPA IS :-- ",gpa)

GPA()