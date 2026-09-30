total=0
count=1
Highest=0
Lowest=0
marks=int(input("enter a mark"))
while marks!=-1: 
    if marks>=0 and marks<=100:
      count=count+1
    if marks>Highest:
            Highest=marks
    if marks<Lowest:
            Lowest=marks
        total=total+marks
    marks=int(input("enter a mark or -1 to finish:"))
    else:
            print("invalid")
            marks=int(input("enter a mark or -1 to finish:"))
print(count)
print(Highest)
print(Lowest)
print("average",total/count)