import sys
from files import simple, normal, advanced


def usage():
    print('''Usage : python filename.py mode level key1 key2[optional] ( if its command line operation )\n
    Allowed modes : encrypt , decrypt\n
    Allowed Levels : simple, normal, advanced\n
    Key1 : Required - only integer value allowed\n
    Key2: Required if level is normal or advanced, only string value allowed(no special characters or whitespace allowed) ''')


def encrypt(level, text, key1, key2 = None):
    if level == 'simple':
        return simple.encrypt(text, key1)

    elif level == 'normal':
        if key2 == None:
            print('\nError on Encrypt : Key2 Missing ')
            raise TypeError
        return normal.encrypt(text, key1, key2)

    elif level == 'advanced':
        if key2 == None:
            print('\nError on Encrypt : Key2 Missing ')
            raise TypeError
        return advanced.encrypt(text, key1, key2)

    else:
        print('\nError on Encrypt : Invalid Level ')
        raise TypeError


def decrypt(level, text, key1, key2 = None):
    if level == 'simple':
        return simple.decrypt(text, key1)

    elif level == 'normal':
        if key2 == None:
            print('\nError on Decrypt : Key2 Missing')
            raise TypeError
        return normal.decrypt(text, key1, key2)

    elif level == 'advanced':
        #try:
            if key2 == None:
                print('\nError on Decrypt : Key2 Missing')
                raise TypeError
            return advanced.decrypt(text, key1, key2)
        #except ValueError:
            #sys.exit('Something went Wrong , Please Try Below Options\n1) Try again with another level\n2) Try another text that encrypted by advanced level\n3) Change values of key1 to a 2 digit one')

    else:
        print('\nError on Decrypt : Invalid Level')
        raise TypeError


def convert(mode, level, text, key1, key2):
    if mode == 'encrypt':
        return encrypt(level, text, key1, key2)

    elif mode == 'decrypt':
        return decrypt(level, text, key1, key2)

    else:
        print('\nError on Convert : Invalid Mode')
        raise TypeError


def main():
    try:
        arg_len = len(sys.argv)

        key2 = None
        
        if arg_len == 5:
            key2 = sys.argv[4]

        if arg_len > 5 or arg_len < 4:
            print(('Error on Main : Invalid number of Arguments\n'))
            raise TypeError

        mode = sys.argv[1].lower()
        level = sys.argv[2].lower()
        key1 = int(sys.argv[3])
        
        result = f"{convert(mode, level, input('Text : '), key1, key2)}"

        if result == None or result == '':
            print('Something went Wrong\n')
            raise TypeError

        print(f'{mode.capitalize()}ed Text : {result}')

    except (TypeError , ValueError):
        sys.exit(usage())


if __name__ == "__main__":
    main()