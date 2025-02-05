#!/usr/bin/env python3
import ev3dev.ev3 as ev3

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.sound import Sound

# Инициализация моторов
left_motor = MoveTank(OUTPUT_B, OUTPUT_C)
right_motor = MoveTank(OUTPUT_B, OUTPUT_C)

# Инициализация сенсоров
color_sensor = ColorSensor()
ultrasonic_sensor = UltrasonicSensor()

# Настройки скорости
SPEED = 30

# Карта маршрута
route_map = []

def follow_line():
    while True:
        color = color_sensor.color
        if color == ColorSensor.COLOR_BLACK:
            route_map.append('black')
            left_motor.on_for_seconds(SPEED, SPEED, 0.1)
        elif color == ColorSensor.COLOR_WHITE:
            route_map.append('white')
            right_motor.on_for_seconds(SPEED, SPEED, 0.1)
        else:
            break

def repeat_route():
    for step in route_map:
        if step == 'black':
            left_motor.on_for_seconds(SPEED, SPEED, 0.1)
        elif step == 'white':
            right_motor.on_for_seconds(SPEED, SPEED, 0.1)

# Основная программа
follow_line()
Sound.speak("Маршрут записан! Повторяю...")
repeat_route()
Sound.speak("Готово!")
