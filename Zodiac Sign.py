year = eval (input("Enter a year:"))
Zodiacyear = year % 12
if Zodiacyear == 0:
    print("Monkey")     
elif Zodiacyear ==1:
    print("Rooster")
elif Zodiacyear ==2:   
    print("Dog")
elif Zodiacyear==3:
    print ("Pig")
elif Zodiacyear==4:
        print("Rat")
elif Zodiacyear==5:
    print("Ox")
elif Zodiacyear==6:
    print ("Tiger")
elif Zodiacyear==7:
        print ("Rabbit")
elif Zodiacyear==8:
    print ("Dragon")
elif Zodiacyear==9:
        print ("Snake")
elif Zodiacyear==10:
        print ("Horse")
else:
    print ("Sheep")