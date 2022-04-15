class InputError(Exception):
  pass

class TouchAllWalls:
  def __init__(self, length, width, start, location):
    self.length = length
    self.width = width
    self.start = start
    self.location = location

      
  def starters(self):
    if self.location == "W":
      ratio = self.start/self.width
      self.lengthstart = ratio*self.length
    elif self.location == "L":
      ratio = self.start/self.length
      self.widthstart = ratio*self.width
    else:
        raise InputError("Invalid Input")
    return

  def solve(self):
    if self.location == "W":
      l1 = self.lengthstart**2
      w1 = self.start**2
      total = l1+w1
      side1 = total**0.5
      side1*=2
      l2 = self.length-self.lengthstart
      l2 = l2**2
      w2 = self.width-self.start
      w2 = w2**2
      total1 = w2+l2
      side2 = total1**0.5
      side2*=2
      return side1+side2
    elif self.location == "L":
      l1 = self.start**2
      w1 = self.widthstart**2
      total = l2+w2
      side1 = total**0.5
      l2 = self.length-self.start
      l2 = l2**2
      w2 = self.width-self.widthstart
      w2 = w2**2
      total1 = w2+l2
      side2 = total1**0.5
      side2*=2 
      return side1+side2
      
length = int(input("What is the length? \n"))
width = int(input("What is the width? \n"))
start = int(input("Where are you starting from?\n"))
location = input("Are you starting from W or L?\n")
obj = TouchAllWalls(length, width, start, location)
obj.starters()
print(obj.solve())