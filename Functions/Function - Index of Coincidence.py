#IoC - Index of Coincidence 



def ic(self):
  num = 0.0
  den = 0.0
  for val in self.count.values():
    i = val
    num += i * (i - 1)
    den += i
  if (den == 0.0):
    return 0.0
  else:
    return num / ( den * (den - 1))


user = input("text: ")

ic(list(user))