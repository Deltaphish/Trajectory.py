
import matplotlib.pyplot as plt
from pylab import *
from math import sin, cos, radians, floor

def tra(v, a, s, m):
    posix = [0]
    posiy = [s]
    posx=0
    posy  =  0.1 + s
    angle = radians(a)
    velx  = v * cos(angle) 
    vely  = v * sin(angle)
    while posy > 0:
          fd = (0.5 * float(m) * float((velx**2)) * 0.3 * 0.2)/8
          posx = posx + velx/8 
          posy = posy + vely/8
          vely = vely - (9.8/8)
          velx = velx - fd
          """posx = math.floor(posx)
          posy = math.floor(posy)"""
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
    plt.plot(posix, posiy)
    plt.axis([0,15,0,15])
    plt.xlabel("Distance in Meters")
    plt.ylabel("Hight in Meters")
    plt.show()
    print(posix)
    print(posiy)
v_input = int(input('input your start velocity: '))
a_input = int(input('input your launch angle: '))
s_input = float(input('input your start heigth: '))
m_input = float(input('input the mass of the object in kg: '))    
tra(v_input,a_input,s_input,m_input)
