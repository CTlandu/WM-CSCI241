n=input()
e=input()
powerof2=2**int(e)
numofresult=0
for i in range(powerof2,int(n)):
  var=str(i)
  if var.find(str(powerof2))!= -1:
    numofresult += 1
print(numofresult)

