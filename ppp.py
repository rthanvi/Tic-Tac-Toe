from datetime import datetime,timedelta
year=int(input("Enter the year"))
month=int(input("Enter the month"))
dt1=datetime(year,month,6,4,59,50)
add_dt1=dt1+timedelta(days=6)
sub_dt1=dt1-timedelta(days=4)


  





if add_dt1>sub_dt1:
    print("add_dt1 is greater")


elif add_dt1<sub_dt1:
      print("sub_dt1 is greater")

    

else:
  print("They are equal")  


print(add_dt1-sub_dt1)    

