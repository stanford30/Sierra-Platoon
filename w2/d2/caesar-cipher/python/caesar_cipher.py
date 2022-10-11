def caesar_cipher(string, shift_amount):
    abc = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for x in string:
        try:
            shift = abc.index(x.lower()) + shift_amount
            if shift > 25:
                shift -= 26
            substr = abc[shift]
            if x.isupper():
                substr = substr.upper()
            ans += substr
        except ValueError:
            ans += x
    return ans


caesar_cipher("Abcdefghijklmnopqrstuvwxyz", 5)
