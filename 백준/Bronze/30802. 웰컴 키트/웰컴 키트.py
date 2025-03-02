import sys

n = int(sys.stdin.readline())
quantity_of_sizes = map(int, sys.stdin.readline().split())
t, p = map(int, sys.stdin.readline().split())

shirts_quantities = 0
for count in quantity_of_sizes:
    if count % t == 0:
        shirts_quantities += count // t
    else:
        shirts_quantities += (count // t) + 1 

bundle_of_pen_quantities = n // p
pen_quantities = n % p

print(shirts_quantities)
print(bundle_of_pen_quantities, pen_quantities)