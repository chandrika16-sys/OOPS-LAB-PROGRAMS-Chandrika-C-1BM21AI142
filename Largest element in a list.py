def largest(n):
  large=n[0]
  for i in n:
    if i>large:
      large=i
  return large;

n=[3,5,6,7,2,3,410,26,21,4]
print("Largest number in the list=",largest(n))
