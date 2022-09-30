def bottle_song():
    # write your code here!
    bottles = 99
    arr = []

    while (bottles > 1):
        bottle = 'bottles'
        if bottles == 2:
            bottle = 'bottle'

        string = f'{bottles} bottles of beer on the wall, {bottles} of beer. Take one down and pass it around, {bottles-1} {bottle} of beer on the wall.'
        arr.append(string)
        bottles -= 1
    string = "1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.\n No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall."
    arr.append(string)

    print('\n'.join(arr))


bottle_song()
