#A code that calculate the number of days between two dates

from datetime import date
f_date=[]
f_date.append(input("Enter the date"))

l_date=[]
l_date.append(input("Enter the date"))

delta=l_date - f_date

print(delta.days)



