def main():
    n = hent_antall_katter()
    print_mjau(n)


def hent_antall_katter():
    while True:
        antall = int(input("Hvor mange katter har du? "))
        if antall > 0:
            return antall
        
def print_mjau(antall):
    # print("Mjau\n" * antall, end="")
    
    for _ in range(antall):
        print("Mjau")


main()
        