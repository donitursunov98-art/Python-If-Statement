telefon = input('raqam kiriting: ')

kod = telefon[:2]

if kod in ['90', '91']:
    print('ucell')
elif kod in ['93', '94']:
    print('belline')  
elif kod in ['95', '97']:
    print('uzmobile')    
elif kod in ['88', '99']:
    print('mobiuz')
else:
    print('Noma\'lum operator')