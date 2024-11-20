import datetime
import random

# Global dictionary to hold habitat data
habitats = {}

# Function to generate a birth date
def gen_birth_date(age, birth_season=None):
    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    # If birth season is provided, calculate month
    if birth_season:
        if birth_season == "spring":
            month = 3
        elif birth_season == "summer":
            month = 6
        elif birth_season == "fall":
            month = 9
        elif birth_season == "winter":
            month = 12
        else:
            month = 1
    else:
        month = random.randint(1, 12)  # If no birth season, random month
    
    # Use random day for simplicity, for the example
    day = random.randint(1, 28)  # To avoid month errors
    birth_date = datetime.date(birth_year, month, day)
    return birth_date.isoformat()

# Function to generate a unique ID
def gen_unique_id(species, count):
    return f"{species[:2].capitalize()}{str(count).zfill(2)}"

# Function to process the arriving animals
def process_animals(arrival_file, name_file):
    with open(arrival_file, 'r') as animals_file:
        animals_data = animals_file.readlines()

    with open(name_file, 'r') as names_file:
        animal_names = names_file.readlines()

    animal_count = 0
    animal_list = []

    for line in animals_data:
        # Parse the data line for animal details
        details = line.strip().split(', ')
        age = int(details[0].split()[0])  # Extract age
        sex = details[1].split()[0]  # Extract sex
        species = details[2].split()[0]  # Extract species
        color = details[3].split()[0]  # Extract color
        weight = details[4].split()[0]  # Extract weight
        origin = details[5].split('from ')[1]  # Extract origin
        
        # Get the animal name
        name = animal_names[animal_count].strip()

        # Generate birth date
        birth_season = details[2].split("born in ")[-1] if 'born in' in details[2] else None
        birth_date = gen_birth_date(age, birth_season)
        
        # Generate unique ID
        animal_id = gen_unique_id(species, animal_count + 1)
        
        # Organize the animal by habitat
        if species not in habitats:
            habitats[species] = []

        # Store animal data
        animal = {
            'id': animal_id,
            'name': name,
            'birth_date': birth_date,
            'color': color,
            'sex': sex,
            'weight': weight,
            'origin': origin,
            'arrival_date': datetime.datetime.now().date().isoformat()
        }

        habitats[species].append(animal)
        animal_count += 1

# Function to write the zoo report
def write_report(output_file):
    with open(output_file, 'w') as report:
        for species, animals in habitats.items():
            report.write(f"{species} Habitat:\n")
            for animal in animals:
                report.write(f"{animal['id']}; {animal['name']}; birth date: {animal['birth_date']}; "
                              f"{animal['color']} color; {animal['sex']}; {animal['weight']} pounds; "
                              f"from {animal['origin']}; arrived {animal['arrival_date']}\n")
            report.write("\n")
