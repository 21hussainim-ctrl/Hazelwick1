number = int(input("enter a three digit number:"))
hundreds = numbers//100
remainder = number%100
tens = remainder//10
remainderten = remainder%10
units = remainderten//1
sum = hundreds + tens + units
reversed = "units" + "tens" + "hundreds"
 print("hundreds:" hundreds)
 print("tens:"tens)
 print("units:"units)
 print("sum of digits:"sum)
 print("reversed":reversed)
if number%2==0:
  print("even number:true")
else:
  print("even number:false")