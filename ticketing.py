seats = [
    {'A1' : 1, 'A2' : 1, 'A3' : 1, 'A4' : 1},
    {'B1' : 1, 'B2' : 1, 'B3' : 1, 'B4' : 1},
    {'C1' : 1, 'C2' : 1, 'C3' : 1, 'C4' : 1},
    {'D1' : 1, 'D2' : 1, 'D3' : 1, 'D4' : 1},
    {'E1' : 1, 'E2' : 1, 'E3' : 1, 'E4' : 1},
    {'F1' : 1, 'F2' : 1, 'F3' : 1, 'F4' : 1},
    {'G1' : 1, 'G2' : 1, 'G3' : 1, 'G4' : 1},
    {'H1' : 1, 'H2' : 1, 'H3' : 1, 'H4' : 1},
    {'I1' : 1, 'I2' : 1, 'I3' : 1, 'I4' : 1},
    {'J1' : 1, 'J2' : 1, 'J3' : 1, 'J4' : 1, 'J5' : 1}
]

rseats = [4, 4, 4, 4, 4, 4, 4, 4, 4, 5]

pseat = []

def aseats() :
    print('\nAvailable seats:')
    for dict in seats :
        tmp = [k for (k, v) in dict.items() if v == 1]
        if tmp :
            print(*tmp)
        tmp.clear()

def cseats() :
    aseats()
    q = input('\nWhich seat would you like to buy? ')
    i = 0

    for dicts in seats :
        if rseats[i] > 0 :
            if q.upper() in dicts :
                print('\nSuccessfully purchased seat', q.upper())
                pseat.append(q.upper())
                seats[i][q.upper()] = 0
                rseats[i] -= 1
                i += 1
                return
            elif q.upper() not in dicts :
                print('Invalid seat.')
                i += 1
                return
        else :
            i += 1

while True :
    cseats()

    quitter = input('\nWould you like to buy another seat? Y/N ')

    if quitter.upper() == 'Y':
        continue
    elif quitter.upper() == 'N':
        print('\nPurchased seat/s', *pseat)
        print('Thank you for choosing us!')
        quit()
