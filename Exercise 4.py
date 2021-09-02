from math import pi

for i in range(2, 12):
    p = "Pi = {:." + str(i) + "f}"
    print(p.format(pi))
