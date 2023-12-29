import os
import random
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