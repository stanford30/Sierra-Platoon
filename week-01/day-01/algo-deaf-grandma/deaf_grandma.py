def deaf_grandma():
    print('HEY KID')
    running = True
    goodbye = 0
    while running:
        x = input()
        if x == 'GOODBYE!':
            if goodbye == 1:
                print('LATER, SKATER!')
                running = False
            else:
                print('LEAVING SO SOON?')
                goodbye += 1
        elif x.isupper():
            print('NO, NOT SINCE 1964!')
        elif x == '':
            print('WHAT?!')

        else:
            print('SPEAK UP, KID!')


deaf_grandma()
