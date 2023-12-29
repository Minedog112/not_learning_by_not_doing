import os
import random
#create or read device id
def create_or_read_id_file():
    id_file_path = "ids.txt"
    if not os.path.exists(id_file_path):
        with open(id_file_path, "w") as file:
            random_id = random.randint(10000, 99999)
            file.write(str(random_id))
            return random_id
    else:
        with open(id_file_path, "r") as file:
            return int(file.read())
        
#check if the file is in the final folder
def check_location(folder):
    # location of file
    aktuelles_skript_pfad = os.path.abspath(__file__)
    # location off final folder
    ordner_pfad = os.path.abspath(folder)
    if os.path.dirname(aktuelles_skript_pfad) == ordner_pfad:
        print(f"check_location=true")
    else:
        print(f"check_location=false")
