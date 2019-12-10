import turtle
import time
from PIL import Image
  
def langton(color, rotation, x, maximum): 
   
    window = turtle.Screen() 
    window.bgcolor('white') 
    window.screensize(10000,10000) 
 
    maps = {} 
 
    ant = turtle.Turtle() 
    ant.shape('square') 
    ant.shapesize(0.2) 
    ant.speed(10000)
                 
    pos = coordinate(ant)                              

    time.sleep(3)
    
    total = 0
    parcial = 0.1
    while (total != maximum): 
         
        step = 4
        for i in range (1, x, 1):
            if pos not in maps or maps[pos] == str(color[0]):
                ant.fillcolor(str(color[1]))         
                invert(maps, ant, color[1])
            
                ant.stamp()
                if (rotation[0] == 'L'):
                    ant.left(90)
                else:
                    ant.right(90)    
                ant.forward(step)                          
                pos = coordinate(ant)
                break
            else:
                if (maps[pos] == str(color[i])):
                    if i == x-1:
                        ant.fillcolor(str(color[0]))         
                        invert(maps, ant, color[0])
            
                        ant.stamp()
                        if (rotation[i] == 'L'):
                            ant.left(90)
                        else:
                            ant.right(90)    
                        ant.forward(step)                          
                        pos = coordinate(ant)
                        break

                    else:
                        ant.fillcolor(str(color[i+1]))         
                        invert(maps, ant, color[i+1])
            
                        ant.stamp()
                        if (rotation[i] == 'L'):
                            ant.left(90)
                        else:
                            ant.right(90)    
                        ant.forward(step)                          
                        pos = coordinate(ant)
                        break  
        total = total + 1
        if (total == (int (maximum * parcial))):
            print (parcial)
            parcial = parcial + 0.1

    ant.getscreen().getcanvas().postscript(file="ant.eps")
  
def invert(graph, ant, color): 
    graph[coordinate(ant)] = color 
  
def coordinate(ant): 
    return (round(ant.xcor()), round(ant.ycor()))


color = []
rotation = []

x = int (input('Interactions: '))
for i in range (x):
    a = input('Color: ')
    color.append(a)
       
    b = str(input('Rotation(L/R): '))
    rotation.append(b)

maximum = int(input("Number of Ant steps (a negative number will make the ant run forever): "))
print("Langton's Ant Rules: \n")
print("When the ant steps on " + str(color[0]) + " square (or an empty space), the square turns " + str(color[1]) + " and the ant turns " + str(rotation[0]))
for i in range (1, x, 1):
    if (i == x-1):
        print ("When the ant steps on " + str(color[i]) + " square, the square turns " + str(color[0]) + " and the ant turns " + str(rotation[i]))
    else:
        print ("When the ant steps on " + str(color[i]) + " square, the square turns " + str(color[i+1]) + " and the ant turns " + str(rotation[i]))

langton(color, rotation, x, maximum)
