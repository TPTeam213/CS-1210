'''
Ben Frederick
CS 1210
'''

EU_EURO = 0.9393    # EU Euro
JP_YEN = 157.8850   # Japan Yen
GB_P = 0.7858       # Great Britain Pound Sterling
BR_REAL = 5.3127    # Brazil Real
CN_YUAN = 7.1829    # China Yuan
IN_RUPEE = 83.0631  # India Rupee
SA_RAND = 17.9418   # South Africa Rand

if __name__ == '__main__':
    usd = float(input('Enter USD: '))
    print(f'US ${usd:,} is equivalent to...\n')
    print('USD equiv. Currency')
    print('---------- ---------------------')
    print(f'{usd * EU_EURO:>10,.2f} EU Euro')
    print(f'{usd * JP_YEN:>10,.2f} Japan Yen')
    print(f'{usd * GB_P:>10,.2f} Great Britain Pound Sterling')
    print(f'{usd * BR_REAL:>10,.2f} Brazil Real')
    print(f'{usd * CN_YUAN:>10,.2f} China Yuan')
    print(f'{usd * IN_RUPEE:>10,.2f} India Rupee')
    print(f'{usd * SA_RAND:>10,.2f} South African Rand')