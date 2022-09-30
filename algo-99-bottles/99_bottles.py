def bottle_song():
    # write your code here!
    bottles = 99
    arr = []

    while (bottles > 1):
        if bottles == 2:
            bottle = 'bottle'
        else:
            bottle = 'bottles'
        string = f'{bottles} bottles of beer on the wall, {bottles} of beer. Take one down and pass it around, {bottles-1} {bottle} of beer on the wall.'
        arr.append(string)
        bottles -= 1

    print('\n'.join(arr))


bottle_song()
