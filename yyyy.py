n=input()
def num (n):
  return (f"hello {n}")
num (n)
y1=int(input("enter the  first number"))
y2=int(input("enter the  first number"))
y3=int(input("enter the  first number"))
y4=int(input("enter the  first number"))
def  fun(y1,y2,y3,y4):
      if y1>y2 and y1>y3 and y1>y4:
          print(y1)
      elif y2>y1 and y2>y3 and y2> y4:
          print(y2)
      elif y3>y2 and y3>y1 and y3> y4:
          print(y3)
      elif y4>y1 and y4>y2 and y4>y3:
          print(y4)
      else:
          print("error")
fun(y1,y2,y3,y4)

