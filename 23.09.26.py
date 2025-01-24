#4장 조건문 
#4-1

print("tell me your age?")
myage = int(input())           #int가 실수로 만드는거던가 
if myage< 30:
    print("welcome to the club.")
else :
    print("oh no you are not accepted")
    
#조건의 판단 
a=100
b=100
a is b

a==b

a=300
b=300
a==b



#4-2

score = int(input("enter your score: ")) 

if score >= 90:
    grade = "A"
if score >= 80:
    grade = "b"
if score >=70 :
    grade ='c'
if score >= 60:
    grade = 'd'
if score < 60:
    grade = 'f'
    
print(grade)
    

#4-3
score = int(input("enter your score: "))

if score >=90: grade='A'
elif score >= 80: grade='b'
elif score >= 70: grade= 'C'
elif score >= 60: grade= 'd'
else: grade ='f'

print(grade)

exit()