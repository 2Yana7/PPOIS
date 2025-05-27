import datetime
from dataclasses import dataclass
from typing import Dict

@dataclass
class PatientRecord:
    patient_name: str
    address: str
    birth_date: datetime.date
    appointment_date: datetime.date
    doctor_name: str
    conclusion: str
    
    def to_dict(self) -> Dict[str, str]:
        return {
            'patient_name': self.patient_name,
            'address': self.address,
            'birth_date': self.birth_date.strftime('%Y-%m-%d'),
            'appointment_date': self.appointment_date.strftime('%Y-%m-%d'),
            'doctor_name': self.doctor_name,
            'conclusion': self.conclusion
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'PatientRecord':
        return cls(
            patient_name=data['patient_name'],
            address=data['address'],
            birth_date=datetime.datetime.strptime(data['birth_date'], '%Y-%m-%d').date(),
            appointment_date=datetime.datetime.strptime(data['appointment_date'], '%Y-%m-%d').date(),
            doctor_name=data['doctor_name'],
            conclusion=data['conclusion']
        ) 