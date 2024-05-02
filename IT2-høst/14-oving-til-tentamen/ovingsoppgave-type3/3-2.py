
def pris_inkl_frakt(varepris):
    if varepris > 1000:
        return varepris
    elif 500 <= varepris <= 1000:
        return varepris + 50
    elif varepris < 500:
        return varepris + 80
    
a = pris_inkl_frakt(300)
print(a)
b = pris_inkl_frakt(600)
print(b)
c = pris_inkl_frakt(1300)
print(c)