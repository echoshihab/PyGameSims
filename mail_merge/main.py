
# mail merge challenge from Day 24 of 100 days of Code (Dr. Angela)

with open("Input/Letters/starting_letter.txt", "r") as file:
    current_letter = file.readlines()

with open("Input/Names/invited_names.txt", "r") as file:
    invited_names = file.readlines()

for name in invited_names:
    cleaned_name = name.rstrip()
    with open(f"Output/ReadyToSend/{cleaned_name}-invite-letter.txt", "w") as output:
        current_letter[0] = current_letter[0].replace("[name]", cleaned_name)
        output.writelines(current_letter)
        current_letter[0] = current_letter[0].replace(cleaned_name, "[name]")


