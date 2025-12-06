summa = int(input('summani kiriting: '))

if summa < 100_000:
    print('5%')
elif summa < 500_000:
    print('7%')
elif summa > 500_000:
    print('10%')        