h = 0.2
g = 9.81
l = 0.63
d = 0.6

delta_l = 0.001
delta_t = 0.2

rel_l = delta_l/l

t = float(input())
rel_t = delta_t/t

a = round((2*l) / (t**2), 3)
mi = round(((h*g)-(a*l))/(g*d), 3)

delta_a = round(a*((delta_l/l) + (2*delta_t/t)), 3)
rel_a = round(rel_l + 2*rel_t, 3)

print("a: ", a)
print("Mi: ", mi)
print(r"/\a: ", delta_a)
print("Ba: ", rel_a)