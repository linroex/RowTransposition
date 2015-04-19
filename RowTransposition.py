def main():
    key = '4312567'
    # plain_text = 'Hi, I am come from Taiwan. I am the NTUST student.'
    plain_text = 'attackpostponeduntiltwoamxyz'
    encrypt_text = ''

    plain_text = plain_text.replace(' ', '')
    
    key_max = int(max(list(key)))
    key_min = int(min(list(key)))

    for i in range(key_min, key_max + 1):
        column = key.index(str(i))
        encrypt_text += ''.join([plain_text[_] for _ in range(column, len(plain_text), len(key))])

    print(encrypt_text)
    
if __name__ == '__main__':
    main()