#!/usr/bin/env python3
B=print
L=float
V=str
__author__='Nathaniel Lyttle'
import requests
A=requests.get
import turtle
P=turtle.Turtle
S=turtle.Screen
from PIL import Image
r=Image.open
import pprint as pp
g=pp.pprint
import time
G=time.ctime
n='http://api.open-notify.org/'
b=(90,-90)
R=(-180,180)
c=(-86.1,39.7)
def k():
 r=A(n+"astros.json")
 return r.json()
def Q():
 r=A(n+"iss-now.json")
 return r.json()
def K(lat,lon):
 B(lat,lon)
 r=A(f'{n}iss-pass.json?lat={lat}&lon={lon}')
 return r.json()
def x(iss_location,indy_location,next_indy_time):
 F,d=r("map.gif").size
 s=S()
 s.setup(F,d)
 s.screensize(F,d,"yellow")
 s.setworldcoordinates(R[0],b[1],R[1],b[0])
 s.addshape('iss.gif')
 s.bgpic('map.gif')
 Y=P()
 t=P()
 Y.color("yellow")
 Y.up()
 t.shape('iss.gif')
 Y.shape("circle")
 t.up()
 Y.goto(indy_location)
 t.goto(L(iss_location["longitude"]),L(iss_location["latitude"]))
 O=P()
 O.color("green")
 O.ht()
 O.up()
 O.goto(indy_location)
 O.down()
 O.write(V(G(next_indy_time)))
 s.exitonclick()
def f():
 g(k())
 r=Q()
 l=K(c[1],c[0])
 B()
 g(r)
 B()
 g(l)
 x(r["iss_position"],c,l['response'][0]['risetime'])
if __name__=='__main__':
 f()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
