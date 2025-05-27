from typing import List, Dict, Any
import xml.dom.minidom as minidom
import xml.sax
from .subject import Subject
from .patient_record import PatientRecord
from .xml_handler import XMLHandler
from interfaces.patient_storage import IPatientStorage

class PatientModel(Subject, IPatientStorage):
    #менеджер пац
    def __init__(self):
        super().__init__()
        self.records: List[PatientRecord] = []
    
    def add_record(self, record: PatientRecord) -> None:
        self.records.append(record)
        self.notify_observers()
        
    def get_records(self) -> List[PatientRecord]:
        return self.records
    
    def get_record_count(self) -> int:
        return len(self.records)
    
    def delete_records(self, **conditions) -> int:
        if not conditions:
            return 0
            
        initial_count = len(self.records)
        filtered_records = self.records.copy()
        
        if conditions.get('patient_name') or conditions.get('address'):
            filtered_records = [
                rec for rec in filtered_records 
                if not ((conditions.get('patient_name') and conditions['patient_name'].lower() in rec.patient_name.lower()) or
                       (conditions.get('address') and conditions['address'].lower() in rec.address.lower()))
            ]
            
        if conditions.get('birth_date'):
            filtered_records = [
                rec for rec in filtered_records 
                if rec.birth_date != conditions['birth_date']
            ]
            
        if conditions.get('doctor_name') or conditions.get('appointment_date'):
            filtered_records = [
                rec for rec in filtered_records 
                if not ((conditions.get('doctor_name') and conditions['doctor_name'].lower() in rec.doctor_name.lower()) or
                       (conditions.get('appointment_date') and rec.appointment_date == conditions['appointment_date']))
            ]
        

        self.records = filtered_records
        deleted_count = initial_count - len(self.records)
        
        if deleted_count > 0:
            self.notify_observers()
            
        return deleted_count
    
    def search_records(self, **conditions) -> List[PatientRecord]:
        if not conditions:
            return self.records.copy()
            
        results = self.records.copy()
        
        if conditions.get('patient_name'):
            results = [
                rec for rec in results 
                if conditions['patient_name'].lower() in rec.patient_name.lower()
            ]

        if conditions.get('address'):
            results = [
                rec for rec in results 
                if conditions['address'].lower() in rec.address.lower()
            ]
            
        if conditions.get('birth_date'):
            results = [
                rec for rec in results 
                if rec.birth_date == conditions['birth_date']
            ]
            
        if conditions.get('doctor_name'):
            results = [
                rec for rec in results 
                if conditions['doctor_name'].lower() in rec.doctor_name.lower()
            ]
            
        if conditions.get('appointment_date'):
            results = [
                rec for rec in results 
                if rec.appointment_date == conditions['appointment_date']
            ]
            
        return results
    
    def save_to_file(self, filename: str) -> None:
        dom = minidom.getDOMImplementation().createDocument(None, "patients", None)
        root = dom.documentElement
        
        for record in self.records:
            record_element = dom.createElement("record")
            
            for key, value in record.to_dict().items():
                element = dom.createElement(key)
                text = dom.createTextNode(str(value))
                element.appendChild(text)
                record_element.appendChild(element)
                
            root.appendChild(record_element)
        
        with open(filename, 'w', encoding='utf-8') as f:
            dom.writexml(f, encoding='utf-8', addindent="  ", newl="\n")
            
    def load_from_file(self, filename: str) -> None:
        handler = XMLHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        
        try:
            parser.parse(filename)
            self.records = handler.records
            self.notify_observers()
        except Exception as e:
            print(f"Ошибка загрузки: {e}")