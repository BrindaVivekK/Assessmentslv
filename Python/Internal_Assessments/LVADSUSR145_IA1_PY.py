# -*- coding: utf-8 -*-
"""IA_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-vZ0ynCRmbKN3j1aguzvIM2rIOVTcLWK

**KOTHA BRINDA VIVEK**
"""

#1
print("Enter length of propery in meters")
l=float(input())
print("Enter width of propery in meters")
w=float(input())
area=l*w
if(area>25000):
  print("area of property is",area)
  print("property is having large area")
elif(area>10000):
  print("area of property is",area)
  print("property is having medium area")
else:
  print("area of property is",area)
  print("propert is having small area")

#2bmi
print("Enter weight in kgs")
w=float(input())
print("Enter height in meters")
h=float(input())
bmi=w/(h*h)
if(bmi<18):
  print("you are underweight,eat nutritious food")
elif(bmi<25):
  print("you are normal weight,maintain healthy lifestyle")
elif(bmi<30):
  print("you are overweight,reduce your calories intake and workout ")
elif(bmi>30):
  print("you are extremely overweight,immediately start workout and consult a doctor for a checkup")

#3

#4
children=["Sofia the first","Little princess","Frozen","Aladin and the magic lamp"]
teen=["Friends","RUN BTS","In the soop"]
adult=["Life a misery","Money heist","Squid game","Vincenzo"]
senior=["Retro life","Finding happiness while being happy","Queen of tears"]
print("Enter your age:")
a=int(input())
print("These are recommendations:")
if (a<13):
  print(children)
elif(a<19):
  print(teen)
elif(a<60):
  print(adult)
elif(a>=60):
  print(senior)

#5
subscribers_id=[12,23,34,45,56,67,78,89,90]
promo_subs_list=[]
for i in subscribers_id:
  if(i%2==0):
    promo_subs_list.append(i)

print("These are the ids of targeted list of subscribers:")
print(promo_subs_list)

#6
while(True):
  print("Enter correct password for user id")
  password=input()
  if(password=="BrindaVivekk"):
    print("Welcome to your account")
    break

#7 customer feedback satisfaction
print("No.of customers:")
n=int(input())
satis_scores=[]
c=0
for i in range(n):
  print("Score of customer in the scale of 10:",i+1)
  s=int(input())
  satis_scores.append(s)
  c=c+s
avg=c/n
print(avg,":5average score")
if(avg>8):
  print("customer service is in satisfactory range")
elif(avg>6):
  print("customer service is not in satisfactory range and needs little improvement to satisfy customer")
else:
  print("Customer service is very poor")

#8
cmt1="This is very bad content without good direction"
cmt2="hmm bad"
def cmt_qua(n):
  c=0
  for i in range(len(n)):
    n[i].lower()
    if(n[i]=='a'or n[i]=='e'or n[i]=='i' or n[i]=='o' or n[i]=='u'):
      c=c+1
  if(c<5):
    print("comment quality is very low")
  else:
    print("comment to be considered")
cmt_qua(cmt1)
cmt_qua(cmt2)

#9
import datetime

#11online polling
print("no.of cust for polling")
n=int(input())
for i in range(n):
  try:
    poll=input()
    id=int(input())
  except ValueError|TypeError:
    print("Enter correct type and value ")

#12 Scientific calculation
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Divivsion")
n=int(input())
print("Enter two numbers:")
a=int(input())
b=int(input())
if(n==1):
  print("Sum",a+b)
elif(n==2):
  print("Diff",a-b)
elif(n==3):
  print("Product",a*b)
elif(n==4):
  try:
    print("Division",a/b)
  except ZeroDivisionError:
    print("Denominatoer should not be 0")

#10:
#robust financial calucaltor
'''1)value error
2)type error
3)zerodivision error'''
try:
  savings=int(input())
  loan=int(input())
  savings_intrerest=float(input())
  t=loan/savings_intrerest
except ValueError|TypeError|ZeroDivivsionError:
  print("Enter valid")

#14
'''1)log file upload in folder
2)r for read only '''

file1=open('/content/sample_data/mnist_test.csv','r')
print("Reading the file")
file1.readlines()