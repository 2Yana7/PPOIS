import random
import datetime
import xml.dom.minidom as minidom
import os
from faker import Faker

# Initialize faker with a fixed seed for reproducibility
fake = Faker()
Faker.seed(12345)

# Define number of records to generate per file
RECORDS_PER_FILE = 50
NUMBER_OF_FILES = 3

# Generate realistic patient data
def generate_patient_record():
    # Generate random dates
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
    appointment_date = fake.date_between(start_date='-1y', end_date='today')
    
    # Generate a random patient record
    record = {
        'patient_name': fake.name(),
        'address': fake.address().replace('\n', ', '),
        'birth_date': birth_date.strftime('%Y-%m-%d'),
        'appointment_date': appointment_date.strftime('%Y-%m-%d'),
        'doctor_name': f"Dr. {fake.last_name()}",
        'conclusion': fake.paragraph(nb_sentences=3)
    }
    
    return record

# Save records to XML file
def save_to_xml(records, filename):
    dom = minidom.getDOMImplementation().createDocument(None, "patients", None)
    root = dom.documentElement
    
    for record in records:
        record_element = dom.createElement("record")
        
        for key, value in record.items():
            element = dom.createElement(key)
            text = dom.createTextNode(str(value))
            element.appendChild(text)
            record_element.appendChild(element)
            
        root.appendChild(record_element)
    
    # Create samples directory if it doesn't exist
    os.makedirs('samples', exist_ok=True)
    
    # Save XML file
    with open(os.path.join('samples', filename), 'w', encoding='utf-8') as f:
        dom.writexml(f, encoding='utf-8', addindent="  ", newl="\n")

def main():
    # Generate sample files
    for i in range(1, NUMBER_OF_FILES + 1):
        records = [generate_patient_record() for _ in range(RECORDS_PER_FILE)]
        save_to_xml(records, f'sample_data_{i}.xml')
        print(f"Generated {RECORDS_PER_FILE} records in samples/sample_data_{i}.xml")

if __name__ == "__main__":
    main() 