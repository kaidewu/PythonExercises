# Import the module path and extract the absolute path of the txt file containing the name and surname
from path import Path
txt_path = Path('PythonExercises\\Own Exercises\\Email Generator\\content').abspath()

# Write here the company name or any name. By default, it's python.
address = '@python.com'

# Need to read the txt file and separate the name and surname
with open(f'{txt_path}\\name and last name.txt', 'r') as txt:
    with open(f'{txt_path}\\emailGenerate.txt', 'w') as txt_email:
        for person in txt:
            name, surname = person.strip().split(' ')
            # Need to write a new txt file to insert the email we will generating
            email = f'{str.lower(name)}.{str.lower(surname)}{address}\n'
            txt_email.write(email)
