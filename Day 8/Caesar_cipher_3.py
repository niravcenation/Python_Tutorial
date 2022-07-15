alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    user_choice = input("Type 'encode' to encrypt, and 'decode' to decrypt:\n")
    text = input("Enter the message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(user_text, shift_amount, direction):
        global new_position

        word = ''
        for letter in user_text:
            if letter in alphabets:
                position = alphabets.index(letter)
                if direction == 'encode':
                    new_position = position + shift_amount
                elif direction == 'decode':
                    new_position = position - shift_amount
                word_form = alphabets[new_position]
                word = word + word_form
            else:
                word = word + letter
        print(f"Your {direction}d text is {word}")


    shift = shift % 26

    caesar(user_text=text, shift_amount=shift, direction=user_choice)
    user_input = input("Do you want to continue 'yes' or 'no' ?\n")
    if user_input == 'no':
        print("Goodbye")
        break
