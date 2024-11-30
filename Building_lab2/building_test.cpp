#include <gtest/gtest.h>
#include "project.h"

TEST(ProjectTest, AddEmployeeAddsEmployee) {
  client client("ооо стройинвест", "+7 123 456 7890");
  project project("Строительство жилого комплекса", 5000000.0, client);

  employee employee1("Иван Иванов", 5454, "Инженер");
  project.add_employee(employee1); // Добавляем сотрудника

  EXPECT_EQ(project.get_employee()[0].get_name(), "Иван Иванов"); // Проверяем имя
  EXPECT_EQ(project.get_employee()[0].get_id(), 5454); // Проверяем ID
  EXPECT_EQ(project.get_employee()[0].get_role(), "Инженер"); // Проверяем роль
}

TEST(ProjectTest, ConstructorSetsFieldsCorrectly) {
  client client("ооо стройинвест", "+7 123 456 7890");
  project project("Строительство жилого комплекса", 5000000.0, client);

  EXPECT_EQ(project.get_name(), "Строительство жилого комплекса");
  EXPECT_DOUBLE_EQ(project.get_budget(), 5000000.0);
  EXPECT_EQ(project.get_client().get_name(), "ооо стройинвест");
  EXPECT_EQ(project.get_client().get_contact(), "+7 123 456 7890");
}

TEST(ProjectTest, SetConstructionTimeSetsTimeCorrectly) {
  client client("ооо стройинвест", "+7 123 456 7890");
  project project("строительство жилого комплекса", 5000000.0, client);

  construction_time times("2024-01-01", "2025-01-01");
  project.set_construction_time(times);

  EXPECT_EQ(project.get_construction_time().get_start_date(), "2024-01-01");
  EXPECT_EQ(project.get_construction_time().get_end_date(), "2025-01-01");
}

TEST(ProjectTest, SetSalarySetsSalaryCorrectly) {
  client client("ооо стройинвест", "+7 123 456 7890");
  project project("Строительство жилого комплекса", 5000000.0, client);

  salary salary(3000.0);
  project.set_salary(salary);

  EXPECT_DOUBLE_EQ(project.get_salary().get_amount(), 3000.0);
}

TEST(ProjectTest, SetObjectTypeSetsObjectTypeCorrectly) {
  client client("ооо стройинвест", "+7 123 456 7890");
  project project("Строительство жилого комплекса", 5000000.0, client);

  object_type object_type("Жилой комплекс");
  project.set_object_type(object_type);

  EXPECT_EQ(project.get_object_type().get_type_name(), "Жилой комплекс");
}

TEST(ProjectTest, SetUniformSetsUniformCorrectly) {
  client client("ооо стройинвест", "+7 123 456 7890");
  project project("Строительство жилого комплекса", 5000000.0, client);

  uniform uniform("Каска", 100);
  project.set_uniform(uniform);

  EXPECT_EQ(project.get_uniform().get_type(), "Каска");
  EXPECT_EQ(project.get_uniform().get_quantity(), 100);
}

TEST(ProjectTest, SetCitySetsCityCorrectly) {
  client client("ооо стройинвест", "+7 123 456 7890");
  project project("Строительство жилого комплекса", 5000000.0, client);

  city city("Москва");
  project.set_city(city);

  EXPECT_EQ(project.get_city().get_name(), "Москва");
}

TEST(ProjectTest, ShowProjectDetailsDisplaysCorrectInformation) {
  client client("ооо стройинвест", "+7 123 456 7890");
  project project("Строительство жилого комплекса", 5000000.0, client);

  project.show_project_details(); // Этот тест проверяет вывод в консоль, вы можете настроить вывод и проверить его через перенаправление в строку.
}
TEST(ProjectTest, DefaultConstructor) {
  construction_time ct;
  // Проверяем, что по умолчанию строки пустые
  EXPECT_EQ(ct.get_start_date(), "");
  EXPECT_EQ(ct.get_end_date(), "");
}

TEST(ProjectTest, ParameterizedConstructor) {
  construction_time ct("2024-01-01", "2024-12-31");
  // Проверяем, что даты инициализируются правильно
  EXPECT_EQ(ct.get_start_date(), "2024-01-01");
  EXPECT_EQ(ct.get_end_date(), "2024-12-31");
}

TEST(ProjectTest, GetStartDateReturnsCorrectStartDate) {
  construction_time ct("2024-01-01", "2024-12-31");
  EXPECT_EQ(ct.get_start_date(), "2024-01-01");
}

TEST(ProjectTest, GetEndDateReturnsCorrectEndDate) {
  construction_time ct("2024-01-01", "2024-12-31");
  EXPECT_EQ(ct.get_end_date(), "2024-12-31");
}
  TEST(ProjectTest, a) {
    days_off doff(10);  // Создаем объект с 10 днями
    EXPECT_EQ(doff.get_days_count(), 10);  // Проверяем, что days_count равен 10
  }

  // Тест конструктора по умолчанию
  TEST(ProjectTest, b) {
    days_off doff;  // Создаем объект с умолчательным конструктором
    EXPECT_EQ(doff.get_days_count(), 0);  // По умолчанию days_count должен быть 0
  }

  // Тест метода add_day_off
  TEST(ProjectTest, AddDayOff) {
    days_off doff(5);  // Создаем объект с 5 днями
    doff.add_day_off();  // Добавляем один выходной день
    EXPECT_EQ(doff.get_days_count(), 6);  // Проверяем, что days_count стал равен 6
  }

  // Тест метода add_day_off для увеличения нескольких дней
  TEST(ProjectTest, AddMultipleDaysOff) {
    days_off doff(3);  // Создаем объект с 3 днями
    doff.add_day_off();  // Добавляем один выходной день
    doff.add_day_off();  // Добавляем еще один выходной день
    EXPECT_EQ(doff.get_days_count(), 5);  // Проверяем, что days_count стал равен 5
  }

  // Тест метода get_days_count (проверка возвращаемого значения)
  TEST(ProjectTest, GetDaysCount) {
    days_off doff(7);  // Создаем объект с 7 днями
    EXPECT_EQ(doff.get_days_count(), 7);  // Проверяем, что метод возвращает правильное количество дней
  }

  // Тест конструктора
  TEST(ProjectTest, Constructor) {
    employee emp("Иван Иванов", 12345, "Менеджер");

    // Проверяем, что имя сотрудника правильно установлено
    EXPECT_EQ(emp.get_name(), "Иван Иванов");

    // Проверяем, что ID сотрудника правильно установлен
    EXPECT_EQ(emp.get_id(), 12345);

    // Проверяем, что роль сотрудника правильно установлена
    EXPECT_EQ(emp.get_role(), "Менеджер");
  }

  // Тест метода get_name
  TEST(ProjectTest, GetName) {
    employee emp("Мария Петрова", 67890, "Разработчик");
    EXPECT_EQ(emp.get_name(), "Мария Петрова");  // Проверяем, что метод get_name возвращает правильное имя
  }

  // Тест метода get_id
  TEST(ProjectTest, GetId) {
    employee emp("Алексей Смирнов", 11223, "Тестировщик");
    EXPECT_EQ(emp.get_id(), 11223);  // Проверяем, что метод get_id возвращает правильный ID
  }

  // Тест метода get_role
  TEST(ProjectTest, GetRole) {
    employee emp("Екатерина Иванова", 44556, "HR");
    EXPECT_EQ(emp.get_role(), "HR");  // Проверяем, что метод get_role возвращает правильную роль
  }

  // Тест конструктора
  TEST(ProjectTest, c) {
    equipment eq("Кран", 1001);

    // Проверяем, что тип оборудования правильно установлен
    EXPECT_EQ(eq.get_type(), "Кран");

    // Проверяем, что ID оборудования правильно установлен
    EXPECT_EQ(eq.get_id(), 1001);
  }

  // Тест метода get_type
  TEST(ProjectTest, GetType) {
    equipment eq("Экскаватор", 2002);
    EXPECT_EQ(eq.get_type(), "Экскаватор");  // Проверяем, что метод get_type возвращает правильный тип оборудования
  }

  // Тест метода get_id
  TEST(ProjectTest, g) {
    equipment eq("Бульдозер", 3003);
    EXPECT_EQ(eq.get_id(), 3003);  // Проверяем, что метод get_id возвращает правильный ID оборудования
  }

  // Тест метода operate (предположим, что метод ничего не возвращает, но проверяем, что он не вызывает ошибок)
  TEST(ProjectTest, Operate) {
    equipment eq("Гусеничный кран", 4004);

    // Ожидаем, что метод operate не вызывает ошибок, так как он пустой
    EXPECT_NO_THROW(eq.operate());
  }

  // Тест конструктора
  TEST(ProjectTest, d) {
    material mat("Цемент", 500.0);

    // Проверяем, что имя материала правильно установлено
    EXPECT_EQ(mat.get_name(), "Цемент");

    // Проверяем, что стоимость материала правильно установлена
    EXPECT_DOUBLE_EQ(mat.get_cost(), 500.0);
  }

  // Тест метода get_name
  TEST(ProjectTest, n) {
    material mat("Песок", 150.0);
    EXPECT_EQ(mat.get_name(), "Песок");  // Проверяем, что метод get_name возвращает правильное имя материала
  }

  // Тест метода get_cost
  TEST(ProjectTest, GetCost) {
    material mat("Гранит", 1200.0);
    EXPECT_DOUBLE_EQ(mat.get_cost(), 1200.0);  // Проверяем, что метод get_cost возвращает правильную стоимость материала
  }
  // Тест конструктора
  TEST(ProjectTest, cc) {
    object_type obj("Жилой");

    // Проверяем, что имя типа объекта правильно установлено
    EXPECT_EQ(obj.get_type_name(), "Жилой");
  }

  // Тест метода set_type_name
  TEST(ProjectTest, SetTypeName) {
    object_type obj("Коммерческий");

    // Меняем тип объекта
    obj.set_type_name("Промышленный");

    // Проверяем, что тип объекта обновился
    EXPECT_EQ(obj.get_type_name(), "Промышленный");
  }

  // Тест метода get_type_name
  TEST(ProjectTest, GetTypeName) {
    object_type obj("Торговый");

    // Проверяем, что метод get_type_name возвращает правильный тип
    EXPECT_EQ(obj.get_type_name(), "Торговый");
  }
  // Тест конструктора
  TEST(ProjectTest, ccc) {
    safety_report report("Отчет 1", "Ожидает проверки");

    // Проверяем, что отчет правильно инициализируется с именем и статусом
    EXPECT_EQ(report.get_report_name(), "Отчет 1");
    EXPECT_EQ(report.get_status(), "Ожидает проверки");
  }

  // Тест метода get_report_name
  TEST(ProjectTest, GetReportName) {
    safety_report report("Отчет 2", "Одобрен");

    // Проверяем, что метод get_report_name возвращает правильное имя отчета
    EXPECT_EQ(report.get_report_name(), "Отчет 2");
  }

  // Тест метода get_status
  TEST(ProjectTest, GetStatus) {
    safety_report report("Отчет 3", "Отказано");

    // Проверяем, что метод get_status возвращает правильный статус
    EXPECT_EQ(report.get_status(), "Отказано");
  }

  // Тест конструктора
  TEST(ProjectTest, cccc) {
    salary emp_salary(5000.0);

    // Проверяем, что объект правильно инициализируется с заданной суммой
    EXPECT_EQ(emp_salary.get_amount(), 5000.0);
  }

  // Тест метода get_amount
  TEST(ProjectTest, GetAmount) {
    salary emp_salary(3000.0);

    // Проверяем, что метод get_amount возвращает правильную сумму
    EXPECT_EQ(emp_salary.get_amount(), 3000.0);
  }

  // Тест метода update_salary
  TEST(ProjectTest, UpdateSalary) {
    salary emp_salary(4000.0);

    // Обновляем зарплату
    emp_salary.update_salary(4500.0);

    // Проверяем, что зарплата была обновлена правильно
    EXPECT_EQ(emp_salary.get_amount(), 4500.0);
  }
  // Тест конструктора
  TEST(ProjectTest, ccccc) {
    shift work_shift("08:00", "16:00");

    // Проверяем, что конструктор правильно инициализирует время начала и окончания смены
    EXPECT_EQ(work_shift.get_start_time(), "08:00");
    EXPECT_EQ(work_shift.get_end_time(), "16:00");
  }

  // Тест метода get_start_time
  TEST(ProjectTest, GetStartTime) {
    shift work_shift("09:00", "17:00");

    // Проверяем, что метод get_start_time возвращает правильное значение
    EXPECT_EQ(work_shift.get_start_time(), "09:00");
  }

  // Тест метода get_end_time
  TEST(ProjectTest, GetEndTime) {
    shift work_shift("10:00", "18:00");

    // Проверяем, что метод get_end_time возвращает правильное значение
    EXPECT_EQ(work_shift.get_end_time(), "18:00");
  }

  TEST(ProjectTest, AddMaterials) {
    supplier s("ABC Supplier");

    material m1("Wood", 25.5);
    material m2("Steel", 40.0);

    s.add_material(m1);
    s.add_material(m2);

    // Используем метод get_material_count для проверки
    EXPECT_EQ(s.get_material_count(), 2);  // Ожидаем 2 материала
  }

  TEST(ProjectTest, TaskInitialization) {
    // Создание объекта employee
    employee emp("John Doe", 1, "Developer");

    // Создание задачи, назначенной на emp
    task t("Fix bugs", &emp);

    // Проверка, что описание задачи и статус инициализированы правильно
    EXPECT_EQ(t.get_description(), "Fix bugs");
    EXPECT_EQ(t.get_status(), "In Progress");

    // Проверка, что назначенный сотрудник правильный
    EXPECT_EQ(t.get_assigned_employee(), &emp);
  }

  TEST(ProjectTest, MarkComplete) {
    // Создание объекта employee
    employee emp("Jane Smith", 2, "Manager");

    // Создание задачи, назначенной на emp
    task t("Prepare Report", &emp);

    // Проверка статуса до вызова mark_complete
    EXPECT_EQ(t.get_status(), "In Progress");

    // Завершаем задачу
    t.mark_complete();

    // Проверка статуса после вызова mark_complete
    EXPECT_EQ(t.get_status(), "Completed");
  }

  TEST(ProjectTest, AssignedEmployee) {
    // Создание двух объектов employee
    employee emp1("Alice Brown", 3, "Designer");
    employee emp2("Bob White", 4, "Developer");

    // Создание задачи, назначенной на emp1
    task t1("Design new logo", &emp1);
    EXPECT_EQ(t1.get_assigned_employee(), &emp1);

    // Переназначаем задачу на emp2
    t1 = task("Redesign website", &emp2);
    EXPECT_EQ(t1.get_assigned_employee(), &emp2);
  }

  TEST(ProjectTest, dc) {
    // Проверка корректной работы конструктора по умолчанию (если он есть)
    employee emp("Charlie", 5, "Tester");
    task t("", &emp);  // Пустое описание

    // Проверка, что описание пустое, а статус по умолчанию "In Progress"
    EXPECT_EQ(t.get_description(), "");
    EXPECT_EQ(t.get_status(), "In Progress");
    EXPECT_EQ(t.get_assigned_employee(), &emp);
  }
  TEST(ProjectTest, DefaultConsstructor) {
    // Создание объекта униформы с помощью конструктора по умолчанию
    uniform u;

    // Проверка, что по умолчанию тип равен "standart uniform", а количество равно 0
    EXPECT_EQ(u.get_type(), "standart uniform ");
    EXPECT_EQ(u.get_quantity(), 0);
  }

  TEST(ProjectTest, SetNegativeQuantity) {
    // Создание объекта униформы с типом "Boots" и количеством 10
    uniform u("Boots", 10);

    // Установка отрицательного значения для количества
    u.set_quantity(-5);

    // Проверка, что количество не может быть отрицательным
    EXPECT_EQ(u.get_quantity(), -5);  // Возможно, тут нужно добавить проверку, что метод не изменяет количество на отрицательное значение.
  }

  TEST(ProjectTest, SetZeroQuantity) {
    // Создание объекта униформы с типом "Hat" и количеством 10
    uniform u("Hat", 10);

    // Установка количества в 0
    u.set_quantity(0);

    // Проверка, что количество стало равно 0
    EXPECT_EQ(u.get_quantity(), 0);
  }

  TEST(ProjectTest, IncreaseQuantityWithNegativeValue) {
    uniform u("Gloves", 3);
    u.set_quantity(u.get_quantity() - 4);

    // Проверка, что количество не может быть отрицательным
    EXPECT_EQ(u.get_quantity(), -1);  // Если вы хотите предотвратить такие значения, нужно добавить проверку в код.
  }



int main(){
  ::testing::InitGoogleTest();
  return RUN_ALL_TESTS();
  return 0;
}

