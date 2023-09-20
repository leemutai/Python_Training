
# print hello world to the terninal
#print('hello world')
#print('hey there can you see me')

# the if statement
#a = True
#b = True
#c = True
#if a:
 #   print('it is true')
  #  print('Also print this')
   # if b:
    #    print('Both are true')
     #   if c:
      #      print('All three are true')
#else:
 #   print('Always print this')
#print('Always print this ')

#the for loops
#a = {1,2,3,4}
#for item in a:
 #   print(item)
   
   #while loop

#a = 0
#while a < 5:
   # print(a) 
    #a = a + 1

    #functtions
def multiplyByThree(val):
    return 3 * val
multiplyByThree(4)

 
def multiply(val1, val2):
    return val1 * val2
multiply(3, 4)

a =[1,2,3]

def appendFour(myList):
    myList.append(4)

appendFour(a)
print(a)

#classes
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4
    def speak(self):
        print(self.name + 'says: Bark!')
        


class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark!')
my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
another_dog.speak()

#challenge 1: the terminal scribe
#challenge goals> run scribe.py> write function that draws a square>pass in the size of the square


import os
import time
from termcolor import colored

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [['' for y in range(self._y)] for x in range(self._x)]

    def hitswall(self, point):
        return point[0] < 0 or point [0] >= self._x or point[1] < 0 or point[1] >= self._y
    
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark
    def Clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.Clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

    class TerminalScribe:
        def __init__(self, canvas):
            self.canvas = canvas
            self.trail = '.'
            self.mark = '*'
            self.framerate = 0.05
            self.pos =[0, 0]

        def up(self):
            pos = [self.pos[0], self.pos[1]-1]
            if not self.canvas.hitswall(pos):
                self.draw(pos)

        def down(self):
            pos = [self.pos[0], self.pos[1]+1]
            if not self.canvas.hitswall(pos):
                self.draw(pos)

        def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

        def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

        def drawSquare(self, size):
        i = 0
        while i < size:
            self.right()
            i = i + 1
        i = 0
        while i < size:
            self.down()
            i = i + 1
        i = 0
        while i < size:
            self.left()
            i = i + 1
        i = 0
        while i < size:
            self.up()
            i = i + 1



        def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

scribe.drawSquare(20)




    
         
 


