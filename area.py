class rectangle:
    def gets_values(self):
        rectangle.l=int(input("Enter length"))
        rectangle.b=int(input("Enter breadth"))
        print(rectangle.l)
        print(rectangle.b)
    def area(self):
        a=self.l*self.b
        print(a)
a1=rectangle()
a1.gets_values()
a1.area()
