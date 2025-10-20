class Base:
    """Common state/behavior for drawable shapes."""
    def __init__(self, x, y, size):  # store position (x, y) and a generic size
        self.x = x
        self.y = y
        self.size = size

    def shape(self): # default description 
        return "This is a shape"

class Circle():
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def shape(self):
        return "This is a circle"

    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """

def main():
    c = Circle(1, 2, 3)
    print(c.shape())   
    print(c.draw())   

if __name__ == "__main__":
    main()