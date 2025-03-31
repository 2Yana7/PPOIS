import json
import os
from government.government import Government
from government.models import Laws, Citizen, Infrastructure

DATA_FILE = "data/data.json"

def save_data(government: Government) -> None:
    data = {
        "laws": [{"title": law.title, "status": law.status} for law in government.law_manager.laws],
        "citizens": [
            {
                "name": citizen.name,
                "id": citizen.id,
                "incom": citizen.incom,
                "tax_paid": citizen.tax_paid,
                "social_status": citizen.social_status
            } for citizen in government.citizen_manager.citizens
        ],
        "infrastructures": [
            {
                "id": obj.id,
                "type": obj.type,
                "location": obj.location,
                "condition": obj.condition
            } for obj in government.infrastructure_manager.infrastructures
        ],
        "foreign_alliances": government.foreign_relations.list_of_alliances,
        "currency": government.currency,
        "tax_rate": government.tax_rate
    }
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Данные сохранены.\n")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def load_data() -> dict:
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return {}
