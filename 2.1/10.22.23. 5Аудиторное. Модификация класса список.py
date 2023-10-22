class My_list(list):
  pass

l1 = My_list((1, 2, 3))
l2 = My_list((3, 4, 5))

def __sub__(a, b):
  return My_list(map(lambda x, y: x - y, a, b))

def __truediv__(a, num):
  try:
    return My_list(map(lambda x: x / num, a))
  except ZeroDivisionError:
    print("Ошибка деления на ноль")
    return None

l3 = __sub__(l2, l1)
l4 = __sub__(l1, l2)
res = __truediv__(l1, 5)

print(res)
print(l3)
print(l4)