import turtle
import memory_turtle

MemoryTurtle = memory_turtle.MemoryTurtle

Turtle = turtle.Turtle


"""Preliminary implementation, but helpful to see. One example of a DynaTurtle,
a Turtle class that exhibits some particular characteristic. This code is probably
not a representation of Python best practices, but the mental model is what's important.

See Chapter 5 of Mindstorms: Children, Computers, and Powerful Ideas, by Seymour Papert, for more.
(Especially the discussion of students studying Newton's Laws of Motion. The book is free online as PDF, and worth buying.)
"""
class GasTurtle(MemoryTurtle):
    def __init__(self, gas=5000):
        super().__init__()
        self.gas = gas
        self.coast_to_stop = True

    def coast(self):
        speed = 0
        tail = self.speak_memory()[-5:]
        for item in tail:
            dir, num = item
            if dir == 'forward' or dir == 'back':
                speed = speed + num

        for x in range(speed, -1, -1):
            self.forward(turtle.math.sqrt(x))

    def gas_forward(self, distance):
        if self.gas > 0:
            print('gas is ', self.gas, 'moving forward')
            super()._fd(distance)
            self.gas = self.gas - distance
        else:
            self.coast()

    def _fd(self, distance):
        if self.gas > 0:
            print('gas is ', self.gas, 'moving forward')
            super()._fd(distance)
            self.gas = self.gas - distance
        else:
            self.coast()

    def gas_back(self, distance):
        if self.gas > 0:
            super()._bk(distance)
            self.gas = self.gas - distance
        else:
            self.coast()

    def _bk(self, distance):
        if self.gas > 0:
            super()._bk(distance)
            self.gas = self.gas - distance
        else:
            self.coast()

    def gas_right(self, angle):
        if self.gas > 0:
            super()._rt(angle)

    def _rt(self, angle):
        if self.gas > 0:
            super()._rt(angle)

    def gas_left(self, angle):
        if self.gas > 0 :
            super()._lt(angle)

    def _lt(self, angle):
        if self.gas > 0:
            super()._lt(angle)

    def fill(self, amount):
        self.gas = self.gas + amount

    def check_gas(self):
        return self.gas
    
tad = GasTurtle(50)

for x in range(35):
    tad._fd(2)

turtle.done()
