#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


# Create a list of names using invited_names.txt file
with open(r".\Input\Names\invited_names.txt") as names_file:
    name_list = names_file.readlines()

# Create name list without trailing newline
for i, name in enumerate(name_list):
    name_list[i] = name.rstrip("\n")

# Read sample letter_text:
with open(r".\Input\Letters\starting_letter.txt") as letter_file:
    sample_letter_text = letter_file.readlines()

for name in name_list:
    letter_text = sample_letter_text.copy()
    letter_text[0] = letter_text[0].replace("[name]", name)
    with open(fr".\Output\ReadyToSend\letter_to_{name}.txt", "w") as letter_file:
        letter_file.writelines(letter_text)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp