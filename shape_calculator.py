class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __repr__ (self):
    return "Rectangle(width={}, height={})".format(self.width,self.height)

  def set_width (self, w):
    self.width = w

  def get_width (self):
    return self.width

  def set_height (self,h):
    self.height = h

  def get_height (self):
    return self.height
  
  def get_area (self):
    return self.width * self.height

  def get_perimeter (self):
    return 2 * self.width + 2 * self.height

  def get_diagonal (self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture (self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    rtn = ""
    for i in range (self.height):
      rtn += ('*' * self.width) + '\n'
    return rtn

  def get_amount_inside (self,rect):
    return (self.width // rect.get_width()) * (self.height // rect.get_height())


class Square(Rectangle):
  def __init__ (self,side_len):
    super().__init__(side_len,side_len)

  def __repr__ (self):
    return "Square(side={})".format(self.width)

  def set_side(self,side_len):
    self.width = side_len
    self.height = side_len

  def set_width (self, length):
    self.set_side(length)
  
  def set_height (self, length):
    self.set_side(length)