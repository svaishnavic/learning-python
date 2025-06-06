name = input ("Give name:")
age = input ("Give age:")
age = int(age)
if name == "xyz" :
    if age < 40:
        print( "suitable")
    elif age > 50:
        print ("old")
    else :
        print( "OK")
else:
    print ( "not known")