# Вычислить число Pi c заданной точностью d, не используя ф. round()
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

PI = math.pi
user_d = float(input('Input accuracy (for example 0.001):\n'))

round_pi = int((PI / user_d) * 10)

if (round_pi % 10) > 4:
    round_pi = int((round_pi + 10) / 10)
else:
    round_pi = int(round_pi / 10)

print(f'Rounded pi={PI} => {round_pi * user_d}')