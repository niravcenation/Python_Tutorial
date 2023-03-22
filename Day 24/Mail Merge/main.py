#  Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open('./Input/Names/invited_names.txt') as name_file:
    invited_name = name_file.readlines()

    for i in invited_name:
        names.append(i.strip())

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()

for i in names:
    new_letter = letter_content.replace("[name]", i)
    with open(f'./Output/ReadyToSend/letter_for_{i}', mode='w') as final_letter:
        final_letter.write(new_letter)
