import os
import json
import unittest
from io import StringIO
from unittest.mock import patch

# Импортируем классы и функции из проекта
from government.models import Laws, Citizen, Infrastructure, Economy, Foreign_relations
from government.managers import LawManager, CitizenManager, InfrastructureManager
from government.government import Government
from utils.persistence import save_data, load_data, DATA_FILE

class TestLawManager(unittest.TestCase):
    def setUp(self):
        self.law_manager = LawManager([])

    @patch('builtins.input', return_value='Test Law')
    def test_new_law(self, mock_input):
        self.law_manager.new_law()
        self.assertEqual(len(self.law_manager.laws), 1)
        self.assertEqual(self.law_manager.laws[0].title, 'Test Law')
        self.assertEqual(self.law_manager.laws[0].status, 'неактивен')

    @patch('builtins.input', return_value='Nonexistent Law')
    def test_change_status_of_law_not_found(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.law_manager.change_status_of_law()
            output = fake_out.getvalue()
            self.assertIn("не найден", output)

    def test_change_status_of_law(self):
        # Добавляем закон и затем изменяем его статус
        self.law_manager.laws.append(Laws("Test Law", "неактивен"))
        with patch('builtins.input', return_value='Test Law'):
            self.law_manager.change_status_of_law()
        self.assertEqual(self.law_manager.laws[0].status, "активен")

class TestCitizenManager(unittest.TestCase):
    def setUp(self):
        self.citizens = []
        self.manager = CitizenManager(self.citizens)

    @patch('builtins.input', side_effect=['1', 'John Doe', '1000'])
    def test_add_citizen(self, mock_input):
        self.manager.add_citizen("USD")
        self.assertEqual(len(self.citizens), 1)
        self.assertEqual(self.citizens[0].name, "John Doe")
        self.assertEqual(self.citizens[0].id, 1)
        self.assertEqual(self.citizens[0].incom, 1000)

    @patch('builtins.input', side_effect=['1'])
    def test_del_citizen_not_found(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.manager.del_citizen("USD")
            output = fake_out.getvalue()
            self.assertIn("не найден", output)

    @patch('builtins.input', side_effect=['1', 'John Doe', '1000'])
    def test_del_citizen(self, mock_input):
        self.manager.add_citizen("USD")
        with patch('builtins.input', side_effect=['1']):
            self.manager.del_citizen("USD")
        self.assertEqual(len(self.citizens), 0)

    @patch('builtins.input', side_effect=['1'])
    def test_pay_tax(self, mock_input):
        self.citizens.append(Citizen("John Doe", 1, 1000, "неуплачено", "не запрошено"))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.manager.pay_tax()
            output = fake_out.getvalue()
            self.assertIn("оплатил налог", output)
        self.assertEqual(self.citizens[0].tax_paid, "уплочено")

    @patch('builtins.input', side_effect=['1'])
    def test_ask_help(self, mock_input):
        self.citizens.append(Citizen("John Doe", 1, 1000, "неуплачено", "не запрошено"))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.manager.ask_help()
            output = fake_out.getvalue()
            self.assertIn("запросил помощь", output)
        self.assertEqual(self.citizens[0].social_status, "запрошено")

class TestInfrastructureManager(unittest.TestCase):
    def setUp(self):
        self.infrastructures = []
        self.manager = InfrastructureManager(self.infrastructures)

    @patch('builtins.input', side_effect=['1', 'School', 'Main Street', 'хорошее'])
    def test_add_object(self, mock_input):
        self.manager.add_object()
        self.assertEqual(len(self.infrastructures), 1)
        self.assertEqual(self.infrastructures[0].id, 1)
        self.assertEqual(self.infrastructures[0].type, "School")
        self.assertEqual(self.infrastructures[0].location, "Main Street")
        self.assertEqual(self.infrastructures[0].condition, "хорошее")

    @patch('builtins.input', side_effect=['1'])
    def test_del_infrastructure_not_found(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.manager.del_infrastructure()
            output = fake_out.getvalue()
            self.assertIn("не найден", output)

    @patch('builtins.input', side_effect=['1', 'School', 'Main Street', 'хорошее'])
    def test_del_infrastructure(self, mock_input):
        self.manager.add_object()
        with patch('builtins.input', side_effect=['1']):
            self.manager.del_infrastructure()
        self.assertEqual(len(self.infrastructures), 0)

    @patch('builtins.input', side_effect=['1', 'School', 'Main Street', 'плохое'])
    def test_change_condition(self, mock_input):
        self.manager.add_object()
        # Если объект имеет состояние "плохое", изменение должно установить "среднее"
        with patch('builtins.input', side_effect=['1']):
            self.manager.change_condition()
        self.assertEqual(self.infrastructures[0].condition, "среднее")

class TestEconomy(unittest.TestCase):
    def setUp(self):
        # Создаем тестового гражданина
        from government.models import Citizen
        self.citizens = [Citizen("John", 1, 1000, "неуплачено", "не запрошено")]
        self.economy = Economy(salary=0, currency="USD")

    @patch('builtins.input', return_value='200')
    def test_salary_up(self, mock_input):
        self.economy.salary_up(self.citizens)
        self.assertEqual(self.citizens[0].incom, 1200)

    @patch('builtins.input', return_value='100')
    def test_salary_down(self, mock_input):
        self.economy.salary_down(self.citizens)
        self.assertEqual(self.citizens[0].incom, 900)

    @patch('builtins.input', return_value='EUR')
    def test_currency_change(self, mock_input):
        self.economy.currency_change()
        self.assertEqual(self.economy.currency, "EUR")

class TestForeignRelations(unittest.TestCase):
    def setUp(self):
        self.foreign = Foreign_relations(["Alliance1"])

    @patch('builtins.input', return_value='Narnia')
    def test_change_bording_status_not_found(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.foreign.change_bording_status()
            output = fake_out.getvalue()
            self.assertIn("не является соседом", output)

    @patch('builtins.input', return_value='Нарния')
    def test_change_bording_status(self, mock_input):
        # По умолчанию статус для "Нарния" равен "открыта", после переключения должен стать "закрыта"
        self.foreign.change_bording_status()
        self.assertEqual(self.foreign.bording_status[0], "закрыта")

    @patch('builtins.input', return_value='Alliance2')
    def test_add_alliances(self, mock_input):
        self.foreign.add_alliances()
        self.assertIn("Alliance2", self.foreign.list_of_alliances)

    @patch('builtins.input', return_value='Alliance1')
    def test_del_alliances(self, mock_input):
        self.foreign.del_alliances()
        self.assertNotIn("Alliance1", self.foreign.list_of_alliances)

class TestGovernmentPersistence(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый объект Government
        self.gov = Government(
            name="TestGov",
            laws=[Laws("Law1", "неактивен")],
            currency="USD",
            tax_rate=10,
            my_object=[Infrastructure(1, "School", "Street", "хорошее")],
            foreign_relations=["Alliance"],
            citizen=[Citizen("John", 1, 1000, "неуплачено", "не запрошено")]
        )
        # Удаляем тестовый файл, если он существует
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)

    def test_save_and_load(self):
        save_data(self.gov)
        data = load_data()
        self.assertIn("laws", data)
        self.assertEqual(data["laws"][0]["title"], "Law1")
        self.assertEqual(data["currency"], "USD")

    def tearDown(self):
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)

if __name__ == "__main__":
    unittest.main()
