def med(x, y, z):
    peso_a = 2
    peso_b = 3
    peso_c = 5

    MEDIA = (x*peso_a + y*peso_b + z*peso_c) / (peso_a + peso_b + peso_c)

    return float(format(MEDIA, '.1f'))

def main():
    A = float(input())
    B = float(input())
    C = float(input())

    MEDIA = med(A, B, C)

    print("MEDIA = " + format(MEDIA, '.1f'))

if __name__ == '__main__':
    main()
