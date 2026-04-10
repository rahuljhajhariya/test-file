pas="reg123"

if(len(pas)>0):
    for i in range(len(pas)):
        if(pas[i] in "qwertyuiopasdfghjklzxcvbnm" ):
            if(pas[i] in "123456789"):
                print("valid password")
                break
        else:
            print("not a valid password")
else:
    print("not a valid password")