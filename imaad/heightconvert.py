name = input("enter your name:")
height =float(input("please enter your height in centimetres:"))
heightm = height/100
heightin = height/2.54
print("hi", name)
print("your height is", heightm,"m")
print("that is",heightin,"inches")
if height<= 180:
   print("taller than 180cm:false")
else:
   print("taller than 180cm:true")