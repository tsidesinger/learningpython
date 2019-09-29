ageInput = input() 
age = int(ageInput)
ageIn2050 = 31 + age
ageSentance = "in twenty fifty you will be " + str(ageIn2050) + " years old."

if ageIn2050 < 152 :
    print(ageSentance) 
else:
     print ("you are definitly not that age.")