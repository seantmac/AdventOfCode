#THIS SEEMS TO BE FAIRLY RIDICULOUS HOW THIS WORKS EASY
#AND THE 19A-C DO NOT SEEM TO
lines = open("19.TXT", "r").readlines()
a, b = int(lines[22].split()[2]), int(lines[24].split()[2])
n1 = 836 + 22 * a + b
n2 = n1 + 10550400

for n in (n1, n2):
    sqn = int(n ** .5)
    print(sum(d + n // d for d in range(1, sqn + 1) if n % d == 0) - sqn * (sqn ** 2 == n))
 
#    
#1056
#10915260
#    