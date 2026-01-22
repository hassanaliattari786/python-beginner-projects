name = input("Enter your name :")
print ("Name",name)
math = int (input ("Enter Math Marks :"))
english = int(input ("Enter English Marks :"))
physics= int(input ("Enter Physics Marks :"))


if math > 100 or english > 100 or physics > 100 or math < 0 or english < 0 or physics < 0:
    print("Error, Marks must be between 0 and 100")
else:
    total = math+english+physics
    percentage= (total/300) *100
    print ("Total Marks :",total)
    print ("Total Percentage:", round( percentage,2))
    if percentage>=95:
         print ("Grade A+") 
    elif percentage>=90:
         print ( "Grade A")
    elif percentage>=80:
         print ("Grade B+")
    elif percentage>=70:
        print ("Grade B")
    elif percentage>=60:
        print ("Grade C+")
    elif percentage>=50:
       print ("Grade D ")
    else:
       print ("Fail")
