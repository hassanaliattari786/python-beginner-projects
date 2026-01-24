score=0
print ("Q1.Python kis type ki language hai ?")
print("A.High level")
print ("B.Low level")
print ("C.Machine ")
print ("D.Assembly")


answer1=input ("Enter your answer A/ B/ C/ D :")
answer1=answer1.upper()

if answer1=="A":
    print ("Correct Answer ")
    score=score+1
else :
    print ("Wrong Answer")


print("Q2. Python mein variable kis cheez ko store karta hai?")
print("A. Program")
print("B. Data")
print("C. Function")
print("D. Loop")
answer2=input ("Enter Your answer A/B/C/D/ :")
answer2=answer2.upper()
if answer2=="B":
    print(" Correct Answer" )
    score=score+1
else:
    print("Wrong Answer")


print("Q3. Python mein number input lene ke liye kaunsa function use hota hai?")
print("A. print()")
print("B. input()")
print("C. type()")
print("D. len()")

answer3=input ("Enter your answer A/B/C/D/ :")
answer3=answer3.upper()
if answer3=="B":
    print ("Correct Answer ")
    score=score+1
else:
    print ("Wrong Answer ")

print("-------------------")
print("Quiz Finished")
print("Your Total Score is:", score, "/ 3")

percentage= (score/3)*100
print("Percentage ", round (percentage ,2 ))

if score>=2:
    print ("Result : Pass")
else:
    print ("Result : Fail")
print ("----------------------") 
