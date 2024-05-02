def main():
    time = input("Hva er klokka? ")
    time = convert(time)



    if 7.0 <= time <= 8.00:
        print("Frokost!")
    elif 12.0 <= time <= 13.00:
        print("Lunsj!")
    elif 18.0 <= time <= 19.00:
        print("Middag!")


def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    m = m / 60

    return h + m


if __name__ == "__main__":
    main()