PLACEHOLDER = "[name]"

# Opens the names files
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    
# Opens the letter file
with open("./Input/Letters/starting_letter.txt") as letter:
    # Reads through the entire letter
    letter_content = letter.read()
    for name in name_list:
        # Takes the \n out of the list
        stripped_name = name.strip()  
        # Replaces the placeholder with the name
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)  
        # Writes to each new file 
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as finished_letter:
            finished_letter.write(new_letter)
            


