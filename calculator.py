a = int(input("Write a number : "))
b = int(input("Write another number : "))

print("Choose an action now \n / is division \n * is multiplication \n + is plus and \n - is substraction")

islem = str(input("what would you like to do? (/, *, -, +) : "))

if islem == "/":
  print(a/b)
 
elif islem == "*":
  print(a*b)
 
elif islem == "+":
  print(a+b)
  
elif islem == "-":
  print(a-b)
