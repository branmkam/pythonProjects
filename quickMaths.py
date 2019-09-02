def addNums(num1, num2):
  sum = num1 + num2
  if num2 < 0:
    print(str(num1) + " - " + (str(int(num2/-1))) + " = " + str(sum))
  else:
    print(str(num1) + " + " + str(num2) + " = " + str(sum))

addNums(2, 2)
addNums(4,-1)
print("Quick maffs")
