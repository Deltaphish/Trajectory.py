#Made by Joakim from sweden!!!
#importing lib
import matplotlib.pyplot as plt
from pylab import *
from math import sin, cos, radians, floor
#main
def tra(v, a, s, m):
    #declerations
    posix = [0]#posx array
    posiy = [s]#posy array
    #start position
    posx=0
    posy  =  0.001 + s 
    angle = radians(a)
    #velocites
    velx  = v * cos(angle) 
    vely  = v * sin(angle)
    # main loop
    while posy > 0: # while projectile is over ground
          # air resistance
          fdx = (0.5 * float(m) * float((velx**2)) * 0.3 * 0.2)/8 
          fdy = (0.5 * float(m) * float((vely**2)) * 0.3 * 0.2)/8
          # adding velocity
          posx = posx + velx/8 
          posy = posy + vely/8
          # adding gravity and air resistance
          vely = vely - (9.8/8) - fdy
          velx = velx - fdx
          # adding current position to final array
          posix.append(posx)
          posiy.append(posy)
          if posy < 0:
             break
            
    if posy <= 0 :
       num = 0 - posy
       posy = posy + num
       posx = posx - num
    posiy.append(posy)
    posix.append(posx)
    # Creating plot
    plt.plot(posix, posiy)
    plt.axis([0,50,0,50])
    plt.xlabel("Distance in Meters")
    plt.ylabel("Hight in Meters")
    plt.show()
    # Printing result to Console
    print(posix)
    print(posiy)
# Geting input
v_input = int(input('input your start velocity: '))
a_input = int(input('input your launch angle: '))
s_input = float(input('input your start heigth: '))
m_input = float(input('input the mass of the object in kg: '))
#Calling trajectory method    
tra(v_input,a_input,s_input,m_input)
