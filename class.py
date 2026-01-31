class bike:
    type="two wheeler"
    def __init__(self,m,y,c):
        self.model=m
        self.year=y
        self.color=c
    def speed(self):
        return"The bike is moving at 20 mph"
    def display(self):
        return f"This is a {self.year} {self.color} {self.model} bike"

bullet=bike("Bullet",2020,"Black")
print(bullet.speed())
print(bullet.display())