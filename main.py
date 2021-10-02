'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


'''
.Returneaza produsul numerelor din lista lst
'''


def get_product(lst):
    prod = 1
    for i in lst:
        prod = prod * i
    return prod


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    t = x
    while t != 0:
        if x % t == 0 and y % t == 0:
            return t
        else:
            t -= 1


def main():
    assert is_prime(5) is True
    assert is_prime(4) is False
    assert is_prime(10) is False
    assert get_cmmdc_v1(9, 6) is 3
    assert get_cmmdc_v1(12, 12) is 12
    assert get_cmmdc_v2(9, 6) is 3
    assert get_cmmdc_v2(12, 12) is 12
    ok = '0'
    while ok != 'x':
        print('''
1.Returneaza true daca n este prim si false daca nu.
2.Returneaza produsul numerelor din lista lst
3.Returneaza CMMDC a doua numere x si y folosind primul algoritm.
4.Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
x.Iesire
    ''')
        ok = input('NR: ')
        if ok == '1':
            n = int(input('Nr:'))
            if is_prime(n):
                print('Nr prim')
            else:
                print('Nr nu este prim')

        elif ok == '2':
            lst = []
            lung = int(input('Lungime lista: '))
            for i in range(lung):
                x = int(input())
                lst.append(x)
            print('Produs:', get_product(lst))

        elif ok == '3':
            x = int(input('Nr 1: '))
            y = int(input('Nr 2: '))
            cmmdc = get_cmmdc_v1(x, y)
            print('CMMDC = ', cmmdc)

        elif ok == '4':
            x = int(input('Nr 1: '))
            y = int(input('Nr 2: '))
            cmmdc = get_cmmdc_v2(x, y)
            print('CMMDC = ', cmmdc)


if __name__ == '__main__':
    main()
