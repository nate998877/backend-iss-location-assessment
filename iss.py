#!/usr/bin/env python3

__author__ = 'Nathaniel Lyttle'

import requests
import turtle
from PIL import Image
import pprint as pp
import time

api_base = 'http://api.open-notify.org/'
lat_bounds = (90, -90)
lon_bounds = (-180, 180)
indy_lat_long = (-86.1, 39.7)

def get_astronauts_in_space_now():
    r = requests.get(api_base+"astros.json")
    return r.json()


def get_iss_current_location():
    r = requests.get(api_base+"iss-now.json")
    return r.json()

def get_iss_pass_information(lat, lon):
    print(lat, lon)
    r = requests.get(f'{api_base}iss-pass.json?lat={lat}&lon={lon}')
    return r.json()

def draw_map(iss_location, indy_location, next_indy_time):
    width, height = Image.open("map.gif").size
    s = turtle.Screen()
    s.setup(width, height)
    s.screensize(width, height, "yellow")
    s.setworldcoordinates(lon_bounds[0], lat_bounds[1], lon_bounds[1], lat_bounds[0])
    s.addshape('iss.gif')
    s.bgpic('map.gif')


    indy_dot = turtle.Turtle()
    t = turtle.Turtle()
    indy_dot.color("yellow")
    indy_dot.up()
    t.shape('iss.gif')
    indy_dot.shape("circle")
    t.up()
    indy_dot.goto(indy_location)
    t.goto(float(iss_location["longitude"]), float(iss_location["latitude"]))
    text = turtle.Turtle()
    text.color("green")
    text.ht()
    text.up()
    text.goto(indy_location)
    text.down()
    text.write(str(time.ctime(next_indy_time)))

    s.exitonclick()

def main():
    pp.pprint(get_astronauts_in_space_now())
    r = get_iss_current_location()
    indy = get_iss_pass_information(indy_lat_long[1],indy_lat_long[0])
    print()
    pp.pprint(r)
    print()
    pp.pprint(indy)
    draw_map(r["iss_position"], indy_lat_long, indy['response'][0]['risetime'])



if __name__ == '__main__':
    main()
