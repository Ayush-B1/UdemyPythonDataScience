alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and
# print the encrypted text.

def encrypt(text, shifts):
    ciphertext = ""
    for letter in text:
        position = alphabet.index(letter)

        new_position = position + shifts

        # print(new_position)

        new_word = alphabet[new_position]

        ciphertext += new_word
    print(f"the encoded text is {ciphertext}")

encrypt("the", 3)