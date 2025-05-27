import xml.sax
from .patient_record import PatientRecord

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.current_tag = ""
        self.current_record = {}
        self.records = []
        self.in_record = False
        
    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "record":
            self.current_record = {}
            self.in_record = True
            
    def endElement(self, tag):
        if tag == "record":
            self.records.append(PatientRecord.from_dict(self.current_record))
            self.in_record = False
        self.current_tag = ""
        
    def characters(self, content):
        if self.in_record and self.current_tag:
            if self.current_tag not in ["record"]:
                if self.current_tag in self.current_record:
                    self.current_record[self.current_tag] += content
                else:
                    self.current_record[self.current_tag] = content 