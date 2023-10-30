# lab 6 Kyle Schipf 10_25_23

def encoder():
    user_input = input("Please enter your password to encode: ")
    if len(user_input) == 8:
        encode_pass = ''
        for num in user_input:
            if (int(num) + 3) >= 10:
                convert = str(int(num) + 3)
                encode_pass = encode_pass + convert
            else:
                encode_pass = encode_pass + str(int(num) + 3)
        print('Your password has been encoded and stored!')
        return encode_pass


def decoder(encode_password):
    #Jack Worth
    new_password = ''
    a = 0
    for i in range(0, len(encode_password)):
        if(a==len(encode_password)):
            break
        if encode_password[a] == '1' and encode_password[a+1] == '0':
            new_password = new_password + '7'
            a += 2
        elif encode_password[a] == '1' and encode_password[a+1] == '1':
            new_password = new_password + '8'
            a += 2
        elif encode_password[a] == '1' and encode_password[a+1] == '2':
            new_password = new_password + '9'
            a += 2
        else:
            new_password = new_password + str(int(encode_password[a]) - 3)
            a+=1
    return new_password

if __name__ == '__main__':
    menu = True
    encode_pass = ''
    while menu:
        print(f'{"Menu"}\n{"-"*13}\n1. Encode\n2. Decode\n3. Quit ')
        menu = input('\nPlease enter an option: ')
        if menu == '1':
            encode_pass = encoder()
            print(f'')
        elif menu == '2':
            decode_pass = decoder(encode_pass)
            print(f'The encoded password is {encode_pass}, and the original password is {decode_pass}')
        elif menu == '3':
            menu = False
