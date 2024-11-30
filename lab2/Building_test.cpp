#include <gtest/gtest.h>
#include "Project.h"

TEST(ProjectTest, AddEmployeeAddsEmployee) {
Client client("ооо стройинвест", "+7 123 456 7890");
  Project Project("Строительство жилого комплекса", 5000000.0, client);

  Employee employee1("Иван Иванов", 5454, "Инженер");
  Project.add_employee(employee1); // Добавляем сотрудника

  EXPECT_EQ(Project.get_employee()[0].get_name(), "Иван Иванов"); // Проверяем имя
  EXPECT_EQ(Project.get_employee()[0].get_id(), 5454); // Проверяем ID
  EXPECT_EQ(Project.get_employee()[0].get_role(), "Инженер"); // Проверяем роль
}

TEST(ProjectTest, ConstructorSetsFieldsCorrectly) {
  Client client("ооо стройинвест", "+7 123 456 7890");
  Project Project("Строительство жилого комплекса", 5000000.0, client);

  EXPECT_EQ(Project.get_name(), "Строительство жилого комплекса");
  EXPECT_DOUBLE_EQ(Project.get_budget(), 5000000.0);
  EXPECT_EQ(Project.get_client().get_name(), "ооо стройинвест");
  EXPECT_EQ(Project.get_client().get_contact(), "+7 123 456 7890");
}

TEST(ProjectTest, SetConstructionTimeSetsTimeCorrectly) {
  Client client("ооо стройинвест", "+7 123 456 7890");
  Project Project("строительство жилого комплекса", 5000000.0, client);

  Construction_time times("2024-01-01", "2025-01-01");
  Project.set_construction_time(times);

  EXPECT_EQ(Project.get_construction_time().get_start_date(), "2024-01-01");
  EXPECT_EQ(Project.get_construction_time().get_end_date(), "2025-01-01");
}

TEST(ProjectTest, SetSalarySetsSalaryCorrectly) {
  Client client("ооо стройинвест", "+7 123 456 7890");
  Project Project("Строительство жилого комплекса", 5000000.0, client);

  Salary salary(3000.0);
  Project.set_salary(salary);

  EXPECT_DOUBLE_EQ(Project.get_salary().get_amount(), 3000.0);
}

TEST(ProjectTest, SetObjectTypeSetsObjectTypeCorrectly) {
  Client client("ооо стройинвест", "+7 123 456 7890");
  Project Project("Строительство жилого комплекса", 5000000.0, client);

  Object_type object_type("Жилой комплекс");
  Project.set_object_type(object_type);

  EXPECT_EQ(Project.get_object_type().get_type_name(), "Жилой комплекс");
}

TEST(ProjectTest, SetUniformSetsUniformCorrectly) {
  Client client("ооо стройинвест", "+7 123 456 7890");
  Project Project("Строительство жилого комплекса", 5000000.0, client);

  Uniform uniform("Каска", 100);
  Project.set_uniform(uniform);

  EXPECT_EQ(Project.get_uniform().get_type(), "Каска");
  EXPECT_EQ(Project.get_uniform().get_quantity(), 100);
}

TEST(ProjectTest, SetCitySetsCityCorrectly) {
  Client client("ооо стройинвест", "+7 123 456 7890");
  Project Project("Строительство жилого комплекса", 5000000.0, client);

  City city("Москва");
  Project.set_city(city);

  EXPECT_EQ(Project.get_city().get_name(), "Москва");
}

TEST(ProjectTest, ShowProjectDetailsDisplaysCorrectInformation) {
  Client client("ооо стройинвест", "+7 123 456 7890");
  Project Project("Строительство жилого комплекса", 5000000.0, client);

  Project.show_Project_details();
}
TEST(ProjectTest, DefaultConstructor) {
  Construction_time ct;
  EXPECT_EQ(ct.get_start_date(), "");
  EXPECT_EQ(ct.get_end_date(), "");
}

TEST(ProjectTest, ParameterizedConstructor) {
  Construction_time ct("2024-01-01", "2024-12-31");
  EXPECT_EQ(ct.get_start_date(), "2024-01-01");
  EXPECT_EQ(ct.get_end_date(), "2024-12-31");
}

TEST(ProjectTest, GetStartDateReturnsCorrectStartDate) {
  Construction_time ct("2024-01-01", "2024-12-31");
  EXPECT_EQ(ct.get_start_date(), "2024-01-01");
}

TEST(ProjectTest, GetEndDateReturnsCorrectEndDate) {
  Construction_time ct("2024-01-01", "2024-12-31");
  EXPECT_EQ(ct.get_end_date(), "2024-12-31");
}
  TEST(ProjectTest, a) {
    Days_off doff(10);
    EXPECT_EQ(doff.get_days_count(), 10);
  }


  TEST(ProjectTest, b) {
    Days_off doff;  // Создаем объект с умолчательным конструктором
    EXPECT_EQ(doff.get_days_count(), 0);  // По умолчанию days_count должен быть 0
  }

  // Тест метода add_day_off
  TEST(ProjectTest, AddDayOff) {
    Days_off doff(5);  // Создаем объект с 5 днями
    doff.add_day_off();  // Добавляем один выходной день
    EXPECT_EQ(doff.get_days_count(), 6);  // Проверяем, что days_count стал равен 6
  }

  // Тест метода add_day_off для увеличения нескольких дней
  TEST(ProjectTest, AddMultipleDaysOff) {
    Days_off doff(3);  // Создаем объект с 3 днями
    doff.add_day_off();  // Добавляем один выходной день
    doff.add_day_off();  // Добавляем еще один выходной день
    EXPECT_EQ(doff.get_days_count(), 5);  // Проверяем, что days_count стал равен 5
  }

  // Тест метода get_days_count (проверка возвращаемого значения)
  TEST(ProjectTest, GetDaysCount) {
    Days_off doff(7);  // Создаем объект с 7 днями
    EXPECT_EQ(doff.get_days_count(), 7);  // Проверяем, что метод возвращает правильное количество дней
  }

  // Тест конструктора
  TEST(ProjectTest, Constructor) {
    Employee emp("Иван Иванов", 12345, "Менеджер");

    // Проверяем, что имя сотрудника правильно установлено
    EXPECT_EQ(emp.get_name(), "Иван Иванов");

    // Проверяем, что ID сотрудника правильно установлен
    EXPECT_EQ(emp.get_id(), 12345);

    // Проверяем, что роль сотрудника правильно установлена
    EXPECT_EQ(emp.get_role(), "Менеджер");
  }

  // Тест метода get_name
  TEST(ProjectTest, GetName) {
    Employee emp("Мария Петрова", 67890, "Разработчик");
    EXPECT_EQ(emp.get_name(), "Мария Петрова");  // Проверяем, что метод get_name возвращает правильное имя
  }

  // Тест метода get_id
  TEST(ProjectTest, GetId) {
    Employee emp("Алексей Смирнов", 11223, "Тестировщик");
    EXPECT_EQ(emp.get_id(), 11223);  // Проверяем, что метод get_id возвращает правильный ID
  }

  TEST(ProjectTest, GetRole) {
    Employee emp("Екатерина Иванова", 44556, "HR");
    EXPECT_EQ(emp.get_role(), "HR");  // Проверяем, что метод get_role возвращает правильную роль
  }

  TEST(ProjectTest, c) {
    Equipment eq("Кран", 1001);

    EXPECT_EQ(eq.get_type(), "Кран");

    EXPECT_EQ(eq.get_id(), 1001);
  }

  TEST(ProjectTest, GetType) {
    Equipment eq("Экскаватор", 2002);
    EXPECT_EQ(eq.get_type(), "Экскаватор");  // Проверяем, что метод get_type возвращает правильный тип оборудования
  }

  TEST(ProjectTest, g) {
    Equipment eq("Бульдозер", 3003);
    EXPECT_EQ(eq.get_id(), 3003);  // Проверяем, что метод get_id возвращает правильный ID оборудования
  }

  TEST(ProjectTest, Operate) {
    Equipment eq("Гусеничный кран", 4004);

    EXPECT_NO_THROW(eq.operate());
  }

  TEST(ProjectTest, d) {
    Material mat("Цемент", 500.0);

    EXPECT_EQ(mat.get_name(), "Цемент");

    EXPECT_DOUBLE_EQ(mat.get_cost(), 500.0);
  }

  TEST(ProjectTest, n) {
    Material mat("Песок", 150.0);
    EXPECT_EQ(mat.get_name(), "Песок");  // Проверяем, что метод get_name возвращает правильное имя материала
  }


  TEST(ProjectTest, GetCost) {
    Material mat("Гранит", 1200.0);
    EXPECT_DOUBLE_EQ(mat.get_cost(), 1200.0);  // Проверяем, что метод get_cost возвращает правильную стоимость материала
  }
  TEST(ProjectTest, cc) {
    Object_type obj("Жилой");

    EXPECT_EQ(obj.get_type_name(), "Жилой");
  }

  TEST(ProjectTest, SetTypeName) {
    Object_type obj("Коммерческий");

    obj.set_type_name("Промышленный");

    EXPECT_EQ(obj.get_type_name(), "Промышленный");
  }

  TEST(ProjectTest, GetTypeName) {
    Object_type obj("Торговый");

    EXPECT_EQ(obj.get_type_name(), "Торговый");
  }
  TEST(ProjectTest, ccc) {
    Safety_report report("Отчет 1", "Ожидает проверки");

    EXPECT_EQ(report.get_report_name(), "Отчет 1");
    EXPECT_EQ(report.get_status(), "Ожидает проверки");
  }

  TEST(ProjectTest, GetReportName) {
    Safety_report report("Отчет 2", "Одобрен");

    // Проверяем, что метод get_report_name возвращает правильное имя отчета
    EXPECT_EQ(report.get_report_name(), "Отчет 2");
  }

  TEST(ProjectTest, GetStatus) {
    Safety_report report("Отчет 3", "Отказано");

    EXPECT_EQ(report.get_status(), "Отказано");
  }

  TEST(ProjectTest, cccc) {
    Salary emp_salary(5000.0);

    EXPECT_EQ(emp_salary.get_amount(), 5000.0);
  }

  TEST(ProjectTest, GetAmount) {
    Salary emp_salary(3000.0);

    // Проверяем, что метод get_amount возвращает правильную сумму
    EXPECT_EQ(emp_salary.get_amount(), 3000.0);
  }



  TEST(ProjectTest, ccccc) {
    Shift work_shift("08:00", "16:00");

    EXPECT_EQ(work_shift.get_start_time(), "08:00");
    EXPECT_EQ(work_shift.get_end_time(), "16:00");
  }

  TEST(ProjectTest, GetStartTime) {
    Shift work_shift("09:00", "17:00");

    EXPECT_EQ(work_shift.get_start_time(), "09:00");
  }


  TEST(ProjectTest, GetEndTime) {
    Shift work_shift("10:00", "18:00");

    // Проверяем, что метод get_end_time возвращает правильное значение
    EXPECT_EQ(work_shift.get_end_time(), "18:00");
  }

  TEST(ProjectTest, AddMaterials) {
    Supplier s("ABC Supplier");

    Material m1("Wood", 25.5);
    Material m2("Steel", 40.0);

    s.add_material(m1);
    s.add_material(m2);

    EXPECT_EQ(s.get_material_count(), 2);
  }

  TEST(ProjectTest, TaskInitialization) {
    Employee emp("John Doe", 1, "Developer");

    Task t("Fix bugs", &emp);

    EXPECT_EQ(t.get_description(), "Fix bugs");
    EXPECT_EQ(t.get_status(), "In Progress");

    EXPECT_EQ(t.get_assigned_employee(), &emp);
  }

  TEST(ProjectTest, MarkComplete) {
    Employee emp("Jane Smith", 2, "Manager");

    Task t("Prepare Report", &emp);

    EXPECT_EQ(t.get_status(), "In Progress");

    t.mark_complete();

    EXPECT_EQ(t.get_status(), "Completed");
  }

  TEST(ProjectTest, AssignedEmployee) {
    // Создание двух объектов employee
    Employee emp1("Alice Brown", 3, "Designer");
    Employee emp2("Bob White", 4, "Developer");

    // Создание задачи, назначенной на emp1
    Task t1("Design new logo", &emp1);
    EXPECT_EQ(t1.get_assigned_employee(), &emp1);

    // Переназначаем задачу на emp2
    t1 = Task("Redesign website", &emp2);
    EXPECT_EQ(t1.get_assigned_employee(), &emp2);
  }

  TEST(ProjectTest, dc) {
    Employee emp("Charlie", 5, "Tester");
    Task t("", &emp);  // Пустое описание

    EXPECT_EQ(t.get_description(), "");
    EXPECT_EQ(t.get_status(), "In Progress");
    EXPECT_EQ(t.get_assigned_employee(), &emp);
  }
  TEST(ProjectTest, DefaultConsstructor) {

    Uniform u;

    EXPECT_EQ(u.get_type(), "standart uniform ");
    EXPECT_EQ(u.get_quantity(), 0);
  }

  TEST(ProjectTest, SetNegativeQuantity) {

    Uniform u("Boots", 10);


    u.set_quantity(-5);


    EXPECT_EQ(u.get_quantity(), -5);    }

  TEST(ProjectTest, SetZeroQuantity) {

    Uniform u("Hat", 10);


    u.set_quantity(0);

    EXPECT_EQ(u.get_quantity(), 0);
  }

  TEST(ProjectTest, IncreaseQuantityWithNegativeValue) {
    Uniform u("Gloves", 3);
    u.set_quantity(u.get_quantity() - 4);


    EXPECT_EQ(u.get_quantity(), -1);
  }



int main(){
  ::testing::InitGoogleTest();
  return RUN_ALL_TESTS();
  return 0;
}

