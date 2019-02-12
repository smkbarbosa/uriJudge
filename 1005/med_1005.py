def med(x, y):
    peso_a = 3.5
    peso_b = 7.5

    MEDIA = (x*peso_a + y*peso_b) / (peso_a + peso_b)

    return float(format(MEDIA, '.5f'))

def main():
    A = float(input())
    B = float(input())

    MEDIA = med(A, B)

    print("MEDIA = " + format(MEDIA, '.5f'))

if __name__ == '__main__':
    main()