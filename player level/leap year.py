a=int(raw_input())
if((a%400==0)or(a%4==0)and(a%100!=0)):
    print("yes,it is leap year")
else:
    print("no,it is not leap year")
