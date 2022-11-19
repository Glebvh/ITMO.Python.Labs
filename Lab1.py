import math

d1 = input('Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) =>')
d2 = input('Введите кратчайшее расстояние от утопающего до берега, d2 (футы) =>')
h = input('Введите боковое смещение между спасателем и утопающим, h (ярды) =>')
v_sand = input('Введите скорость движения спасателя по песку, v_sand (мили в час) =>')
n = input('Введите коэффициент замедления спасателя при движении в воде, n =>')
theta1 = input('Введите направление движения спасателя по песку, theta1 (градусы) =>')

d1m = float(d1) / 1760
d2m = float(d2) / 5280
hm = float(h) / 1760
theta1rad = float(theta1) * math.pi / 180
x = d1m * math.tan(theta1rad)

L1 = math.sqrt(x ** 2 + d1m ** 2)
L2 = math.sqrt((hm - x) ** 2 + d2m ** 2)

tHours = (L1 + float(n) * L2) / float(v_sand)
tSec = tHours * 3600

print(f'Если спасатель начнёт движение под углом theta1, равным {round(float(theta1))} градусам, он достигнет '
      f'утопащего через {round(tSec, 1)} секунды')
