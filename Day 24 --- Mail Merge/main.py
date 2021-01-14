#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

NAMES = open("Input/Names/invited_names.txt", "r").readlines()
FORMAT = open("Input/Letters/starting_letter.docx", "r").read()
OUTPUT = "Output/ReadyToSend"

for NAME in NAMES:

    name = NAME.strip("\n")

    letter = FORMAT.replace("[name]", name)

    file = open(f"{OUTPUT}/{name}.docx", "w")
    file.write(letter)