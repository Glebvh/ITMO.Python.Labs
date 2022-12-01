# -*- coding: utf-8 -*-

import math

YARDS_IN_MILE = 1760
FEETS_IN_MILE = 5280


def input_param():
    dist1 = input('Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) =>')
    dist2 = input('Введите кратчайшее расстояние от утопающего до берега, d2 (футы) =>')
    h_dist = input('Введите боковое смещение между спасателем и утопающим, h (ярды) =>')
    v_sand = input('Введите скорость движения спасателя по песку, v_sand (мили в час) =>')
    n_kf = input('Введите коэффициент замедления спасателя при движении в воде, n =>')
    theta1 = input('Введите направление движения спасателя по песку, theta1 (градусы) =>')
    return dist1, dist2, h_dist, v_sand, n_kf, theta1


def time_calc(dist1, dist2, h_dist, theta1, n_kf, v_sand):
    dist1_mile = float(dist1) / YARDS_IN_MILE
    dist2_mile = float(dist2) / FEETS_IN_MILE
    h_dist_mile = float(h_dist) / YARDS_IN_MILE
    theta1_rad = float(theta1) * math.pi / 180
    x_dist = dist1_mile * math.tan(theta1_rad)

    line1 = math.sqrt(x_dist ** 2 + dist1_mile ** 2)
    line2 = math.sqrt((h_dist_mile - x_dist) ** 2 + dist2_mile ** 2)

    t_hours = (line1 + float(n_kf) * line2) / float(v_sand)
    t_sec = t_hours * 3600
    return t_sec


def print_result(t_sec, theta1):
    print(f'Если спасатель начнёт движение под углом theta1, равным {round(float(theta1))} градусам, он достигнет '
          f'утопащего через {round(t_sec, 1)} секунды')
