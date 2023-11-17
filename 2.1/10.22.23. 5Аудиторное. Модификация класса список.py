class My_list(list):
  
  def __str__(a):

    с = super().__str__()  
    return f"My_list: {с}" 

  def __sub__(a, b):

    return My_list(map(lambda x, y: x - y, a, b))

  def __truediv__(a, num):
    try:
       isinstance(num, int)
       return My_list(map(lambda x: x / num, a))
    
    except:
      return "Ошибка деления на ноль"

l1 = My_list([1, 2, 3])
l2 = My_list([3, 4, 5])
l3 = l2 - l1
l4 = l1 - l2
print(l1 / 5)
print(l3)
print(l4)
