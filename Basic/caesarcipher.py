alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and
# print the encrypted text.
def caesercipher(text, shifts, direction):
    if direction == "encode":
        cipher_Text = ""
        for letter in text:
            position = alphabet.index(letter)

            new_position = position + shifts
            new_letter = alphabet[new_position]

            cipher_Text += new_letter
        print(f"the encoded text is {cipher_Text}")
    elif direction == "decode":
        normal_text = ""
        for letters in text:
            position = alphabet.index(letters)

            new_position = position - shift
            new_letter = alphabet[new_position]

            normal_text += new_letter
        print(f"the decoded text is {normal_text}")
    else:
        print("TF you typing type encode or decode")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesercipher(text=text, shifts=shift, direction=direction)