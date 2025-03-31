from typing import List
from government.models import Laws, Citizen, Infrastructure, Economy, Foreign_relations
from government.managers import LawManager, CitizenManager, InfrastructureManager

class Government:
    def __init__(self, name: str, laws: List[Laws], currency: str, tax_rate: int,
                 my_object: List[Infrastructure], foreign_relations: List[str], citizen: List[Citizen]) -> None:
        self.name = name
        self.currency = currency
        self.tax_rate = tax_rate
        self.foreign_relations = Foreign_relations(foreign_relations)
        self.law_manager = LawManager(laws)
        self.citizen_manager = CitizenManager(citizen)
        self.infrastructure_manager = InfrastructureManager(my_object)

    # Методы для работы с законами
    def new_law(self) -> None:
        self.law_manager.new_law()

    def change_status_of_law(self) -> None:
        self.law_manager.change_status_of_law()

    def display_laws(self) -> None:
        self.law_manager.display_laws()

    # Методы для работы с гражданами
    def add_citizen(self) -> None:
        self.citizen_manager.add_citizen(self.currency)

    def del_citizen(self) -> None:
        self.citizen_manager.del_citizen(self.currency)

    def display_citizen(self) -> None:
        self.citizen_manager.display_citizen(self.currency)

    def display_debtor(self) -> None:
        self.citizen_manager.display_debtor()

    def help_citizen(self) -> None:
        self.citizen_manager.help_citizen()

    def pay_tax(self) -> None:
        self.citizen_manager.pay_tax()

    def ask_help(self) -> None:
        self.citizen_manager.ask_help()

    # Методы для работы с инфраструктурой
    def add_object(self) -> None:
        self.infrastructure_manager.add_object()

    def change_condition(self) -> None:
        self.infrastructure_manager.change_condition()

    def show_infrastructure(self) -> None:
        self.infrastructure_manager.show_infrastructure()

    def del_infrastructure(self) -> None:
        self.infrastructure_manager.del_infrastructure()

    # Методы для работы с внешними отношениями
    def display_borders(self) -> None:
        self.foreign_relations.display_bording_status()

    def change_bording(self) -> None:
        self.foreign_relations.change_bording_status()

    def add_alliances(self) -> None:
        self.foreign_relations.add_alliances()

    def del_alliance(self) -> None:
        self.foreign_relations.del_alliance()

    def display_alliances(self) -> None:
        self.foreign_relations.display_alliances()

    def display_country_info(self) -> None:
        print(f"\n Государство {self.name}")

        print("\n Законы:")
        self.law_manager.display_laws()

        print("\n Граждане:")
        self.citizen_manager.display_citizen(self.currency)

        print("\n Инфраструктура:")
        self.infrastructure_manager.show_infrastructure()

        print("\n Экономика:")
        print(f"Валюта: {self.currency}")
        print(f"Налоговая ставка: {self.tax_rate}%")

        print("\n Внешние отношения:")
        self.foreign_relations.display_bording_status()
        self.foreign_relations.display_alliances()
