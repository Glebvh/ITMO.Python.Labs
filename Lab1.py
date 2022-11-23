# -*- coding: utf-8 -*-

import math

dist1 = input('Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) =>')
dist2 = input('Введите кратчайшее расстояние от утопающего до берега, d2 (футы) =>')
h_dist = input('Введите боковое смещение между спасателем и утопающим, h (ярды) =>')
v_sand = input('Введите скорость движения спасателя по песку, v_sand (мили в час) =>')
n_kf = input('Введите коэффициент замедления спасателя при движении в воде, n =>')
theta1 = input('Введите направление движения спасателя по песку, theta1 (градусы) =>')

dist1_mile = float(dist1) / 1760
dist2_mile = float(dist2) / 5280
h_dist_mile = float(h_dist) / 1760
theta1_rad = float(theta1) * math.pi / 180
x_dist = dist1_mile * math.tan(theta1_rad)

line1 = math.sqrt(x_dist ** 2 + dist1_mile ** 2)
line2 = math.sqrt((h_dist_mile - x_dist) ** 2 + dist2_mile ** 2)

t_hours = (line1 + float(n_kf) * line2) / float(v_sand)
t_sec = t_hours * 3600

print(f'Если спасатель начнёт движение под углом theta1, равным {round(float(theta1))} градусам, он достигнет '
      f'утопащего через {round(t_sec, 1)} секунды')
