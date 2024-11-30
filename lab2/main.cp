// #include <iostream>
// #include "employee.h"
// #include "project.h"
// #include "equipment.h"
// #include "material.h"
// #include "supplier.h"
// #include "task.h"
// #include "client.h"
// #include "construction_time.h"
// #include "safety_report.h"
// #include "shift.h"
// #include "days_off.h"
// #include "salary.h"
// #include "object_type.h"
// #include "uniform.h"
// #include "city.h"
#include "building_test.h"
#include "city_test.h"
#include "client_test.h"
#include "construction_time_test.h"
#include "days_off_test.h"
#include "employee_test.h"
#include "equipment_test.h"
#include "material_test.h"
#include "object_type_test.h"
#include "safety_report_test.h"
#include "salary_test.h"
#include "shift_test.h"
#include "supplier_test.h"
#include "task_test.h"
#include "uniform_test.h"
using namespace std;

int main() {

//     Показать данные
//     cout << "\nProject details:\n";
//
//     Создаем клиента
//      client client("Kto-to", "+375(44)432-432-8");
//
//     Создаем сотрудников
//      employee emp1("John Doe", 1, "Engineer");
//     employee emp2("Jane Smith", 2, "Architect");
//
//     Создаем проект и добавляем сотрудников
//     project project("Skyscraper", 5000000.0, client);
//     project.add_employee(emp1);
//     project.add_employee(emp2);
//
//     Показать сотрудников проекта
//    project.show_employees();
//
//     Устанавливаем тип объекта
//     object_type object_type("house");
//     project.set_object_type(object_type);
//
//     Добавляем материалы
//     material material_1("cement", 10000);
//     material material_2("bricks", 5000);
//     project.add_material(material_1);
//     project.add_material(material_2);
//
//     Поставщик
//     supplier supplier("BuildCo Supplies");
//     supplier.add_material(material_1);
//     supplier.add_material(material_2);
//
//     Устанавливаем время строительства
//     construction_time construction_time ("2024-01-01", "2024-12-31");
//     project.set_construction_time(construction_time);
//
//     добавляем отчёты по технике безопасности
//     safety_report safety_report_1("Safety Report - January", "Done");
//     safety_report safety_report_2("Safety Report - February", "Wating");
//     project.add_safety_report(safety_report_1);
//     project.add_safety_report(safety_report_2);
//
//
//
//     Добавляем задачи
//     task task_1("laying the foundation", &emp1);
//     task task_2("wall installation", &emp2);
//     project.add_task(task_1);
//     project.add_task(task_2);
//
//
//     Добавляем оборудование
//     equipment equipment_1("Excavator",101);
//     equipment equipment_2("overhead crane", 890);
//     project.add_equipment(equipment_1);
//     project.add_equipment(equipment_2);
//
//
//
//     shift shift_1("08:00", "16:00");
//     shift shift_2("16:00", "00:00");
//     project.assign_shift(shift_1);
//     project.assign_shift(shift_2);
//
//
//     days_off days_off(10);
//     project.set_days_off(days_off);
//
//
//
//     salary salary(75000.0);
//     project.set_salary(salary);
//
//         supplier.list_materials();
//
//
//
//     uniform uniform("Construction jacket", 150);
//     project.set_uniform(uniform);
//
//
//     city city("Minsk");
//     project.set_city(city);
//
//     project.show_project_details();
//
//
//     return 0;
::testing::InitGoogleTest();
return RUN_ALL_TESTS();
return 0;
}
