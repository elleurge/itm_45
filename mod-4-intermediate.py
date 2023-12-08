'''Module 3: Individual Programming Assignment 1'''

def shift_letter(letter, shift):
    letter = letter.upper()
    shift %= 26

    if(ord(letter) + shift <= ord('Z')):
        shift_letter = chr(ord(letter) + shift)

    elif(ord(letter) + shift > ord('Z')):
        shift -= ord('Z') - ord(letter) + 1
        shift_letter = chr(ord('A') + shift)

    return shift_letter

def caesar_cipher(message, shift):
    message = message.upper()
    message_list = [*message]
    for i, char in enumerate(message_list):
        if not(char == ' '):
            letter_shift = shift_letter(char, shift)
            message_list[i] = letter_shift
    return ''.join(message_list)

def shift_by_letter(letter, letter_shift):
    letter = letter.upper()
    letter_shift = letter_shift.upper()
    letter_shift = ord(letter_shift) - ord('A')
    shift_by_letter = shift_letter(letter, letter_shift)
    return shift_by_letter

def vigenere_cipher(message, key):
    message = message.upper()
    message_list = [*message]
    key = key.upper()
    key_list = [*key]
    key_char = 0
    for i, msg_char in enumerate(message_list):
            if not(msg_char == ' '):
                if(key_char + 1 > len(key_list)):
                    key_char = 0
                message_list[i] = shift_by_letter(msg_char, key[key_char])
                key_char += 1
    return ''.join(message_list)

while(True):
    print("\nSelect a Function")
    print("[1] Shift Letter")
    print("[2] Caeser Cipher")
    print("[3] Shift By Letter")
    print("[4] Vigenere Cipher")

    select = None

    while(True):
        select = int(input(">> "))
        if not(select <= 4 and select >= 1):
            print("\n[SYSTEM]: Please input a number from the available options.")
        else:
            break

    if select == 1:
        print("\nYou've selected SHIFT LETTER.")
        print("Input a Letter")
        while(True):
            letter = str(input(">> "))
            if not(letter.isalnum()):
                print("\n[SYSTEM]: Please input an alphabet character.")
            else:
                break
        print("Input a Number")
        while(True):
            number = int(input(">> "))
            if not(number >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("Letter Shift: " + shift_letter(letter, number))
    
    elif select == 2:
        print("\nYou've selected CAESER CIPHER.")
        print("Input a Message")
        while(True):
            message = str(input(">> "))
            if not(type(message) == str):
                print("\n[SYSTEM]: Please input an string.")
            else:
                break
        print("Input a Number")
        while(True):
            number = int(input(">> "))
            if not(number >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("Caeser Cipher: " + str(caesar_cipher(message, number)))
    
    elif select == 3:
        print("\nYou've selected SHIFT BY LETTER.")
        print("Input a Letter")
        while(True):
            letter = str(input(">> "))
            if not(letter.isalnum()):
                print("\n[SYSTEM]: Please input an alphabet character.")
            else:
                break
        print("\nYou've selected SHIFT LETTER.")
        print("Input a Shift Letter")
        while(True):
            shiftletter = str(input(">> "))
            if not(letter.isalnum()):
                print("\n[SYSTEM]: Please input an alphabet character.")
            else:
                break
        print("Shift by letter: " + str(shift_by_letter(letter, shiftletter)))
    
    elif select == 4:
        print("\nYou've selected VIGENERE CIPHER.")
        print("Input a Message")
        while(True):
            message = str(input(">> "))
            if not(type(message) == str):
                print("\n[SYSTEM]: Please input a string.")
            else:
                break
        print("Input a Key")
        while(True):
            key = str(input(">> "))
            if not(type(key) == str and len(key) <= len(message)):
                print("\n[SYSTEM]: Please ensure that input is a string and longer than the message.")
            else:
                break
        
        print("Vigenere Cipher: " + str(vigenere_cipher(message, key)))


    print("\nInitiate program execution once more?")
    print("[1] Yes")
    print("[2] No")
        
    while(True):
        select = int(input(">> "))
        if not(select <= 2 and select >= 1):
                print("\nPlease input a number from the available options.")
        else:
            break

    if(select == 1):
        continue
    elif(select == 2):
        break