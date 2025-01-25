def enc_dec(text, mode, shift):
    result = '' 

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
                # في حالة التشفير أو فك التشفير يتم تعديل الإزاحة بشكل صحيح
                new_char = chr((ord(char) - start + (shift if mode == 'E' else -shift)) % 26 + start)
                result += new_char
            else:
                start = ord('a')
                new_char = chr((ord(char) - start + (shift if mode == 'E' else -shift)) % 26 + start)
                result += new_char
        else:
            result += char

    return result


print("##########################################################################")
print("Cipher Program")
print("##########################################################################")
print()
print("Do you want to Encrypt or Decrypt?")
uinput = input('E or D: ').upper()
print()

if uinput == 'E': 
    print("Encrypt Mode is ON")
    key = int(input('Please enter Key: '))
    text = input('Enter text to Encrypt: ')
    cipher_text = enc_dec(text, uinput, key)
    print(f'Cipher_Text: {cipher_text}')
elif uinput == 'D':
    print("Decrypt Mode is ON")
    key = int(input('Enter Key: '))
    text = input('Enter text to Decrypt: ')
    plain_text = enc_dec(text, uinput, key)
    print(f'Plain_Text: {plain_text}')
else:
    print('Please input E to Encrypt or D to Decrypt.')
