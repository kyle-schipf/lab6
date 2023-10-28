# lab 6 Kyle Schipf 10_25_23

def encoder():
    user_input = input("Please enter your password to encode: ")
    if len(user_input) == 8:
        encode_pass = ''
        for num in user_input:
            if (int(num) + 3) >= 10:
                convert = str(int(num) + 3)
                encode_pass = encode_pass + convert[-1]
            else:
                encode_pass = encode_pass + str(int(num) + 3)
        print('Your password has been encoded and stored!')
        return encode_pass


def decoder(encode_pass):
    pass

if __name__ == '__main__':
    menu = True
    while menu:
        print(f'{"Menu"}\n{"-"*13}\n1. Encode\n2. Decode\n3. Quit ')
        menu = input('\nPlease enter an option: ')
        if menu == '1':
            encode_pass = encoder()
            print(f'')
        elif menu == '2':
            decode_pass = decoder(encode_pass)
            print(f'The encoded password is {decode_pass}, and the original password is {encode_pass}')
        elif menu == '3':
            menu = False
