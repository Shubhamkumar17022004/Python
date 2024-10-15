def year(yr):
    if((yr%4 and yr%100!=0)or(yr%400==0)):
        print("It's leap year")
    else:
        print("Not a leap year")

year(2000)
    