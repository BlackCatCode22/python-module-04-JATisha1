import datetime
import random
from utils import gen_birth_date, gen_unique_id, process_animals, write_report

# Main execution of the program
def main():
    # Specify input files
    arrival_file = "arrivingAnimals.txt"
    name_file = "animalNames.txt"
    output_file = "zooPopulation.txt"
    
    # Process the animals and write the report
    process_animals(arrival_file, name_file)
    write_report(output_file)
    print("Zoo population report generated successfully.")

if __name__ == "__main__":
    main()
