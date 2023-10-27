# lab 6 Kyle Schipf 10_25_23

def encoder():
    user_input = input("Enter a string of 8 numbers to encode: ")
    if len(user_input) == 8:
        encode_pass = ''
        for num in user_input:
            if (int(num) + 3) >= 10:
                convert = str(int(num) + 3)
                encode_pass = encode_pass + convert[-1]
            else:
                encode_pass = encode_pass + str(int(num) + 3)
        print(encode_pass)
        return encode_pass


def decoder(encode_pass):
    decode_pass = ''
    for num in encode_pass:
        if int(num) <= 2:
            convert = str(int(num) + 7)
            decode_pass = decode_pass + convert
        else:
            decode_pass = decode_pass + str(int(num) -3)
    print(decode_pass)


if __name__ == '__main__':
    menu = True
    while menu:
        menu = input(f'{"Menu":^25}\n{"-"*25}\n1 to encode your password\n2 to decode your password\nq to quit program ')
        if menu == '1':
            encode_pass = encoder()
        elif menu == '2':
            decoder(encode_pass)
        elif menu == 'q':
            menu = False
