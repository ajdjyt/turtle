pos={"x":0,"y":0,"z":0}
x=1
while x:
  print(pos)
  y=input("Enter dimension to move in: ")
  if y in pos:
    pos[y]+=1
  elif y=="quit":
    break
  else:
    print("Enter valid axis")
print(pos)
