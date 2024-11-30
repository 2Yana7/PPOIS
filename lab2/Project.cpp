#include "Project.h"
#include <iostream>

Project::Project(const string& name, double budget, const class Client& Client)
: name(name), budget(budget), total_material_cost(0.0), client_1(Client) {}


void Project::add_employee(const Employee& employee) {
    employees.push_back(employee);
}

void Project::add_equipment(const Equipment& equipment) {
    equipmentList.push_back(equipment);
}

void Project::add_material(const Material& material) {
    materials.push_back(material);
    total_material_cost += material.get_cost();
}

void Project::add_task(const Task& task) {
    tasks.push_back(task);
}

void Project::show_employees() const {
    cout << "Employees in Project " << name << ":\n";
    for (const auto& employee : employees) {
        cout << "- " << employee.get_name() << " (" << employee.get_role() << ")\n";
    }
}

void Project::show_equipment() const {
    cout << "Equipment used in Project " << name << ":\n";
    for (const auto& equipment : equipmentList) {
        cout << "- " << equipment.get_type() << " with ID: " << equipment.get_id() << "\n";
    }
}

void Project::show_tasks() const {
    cout << "Tasks in Project " << name << ":\n";
    for (const auto& task : tasks) {
        cout << "- " << task.get_description()
        << " (Status: " << task.get_status()
        << ", Assigned to: " << task.get_assigned_employee()->get_name() << ")\n";
    }
}

void Project::set_construction_time(const class Construction_time& time) {
    construction_time_1 = time;
}


void Project::add_safety_report(const class Safety_report& report) {
    safety_reports.push_back(report);
}

void Project::assign_shift(const Shift& shift) {
    shifts.push_back(shift);

}

void Project::set_days_off(const class Days_off& days_off) {
    this->days_off = days_off; }

    void Project::set_salary(const class Salary& salary) {
        this->salary_1 = salary;

}

void Project::set_object_type(const class Object_type& type) {
    object_type_1 = type;}

    void Project::set_uniform(const class Uniform& uniform) {
        this->uniform_1 = uniform;
    }

    void Project::set_city(const class City& city_name) {
        city_1 = city_name;
    }

void Project::show_Project_details() const {
    cout << "\nProject: " << name << "\n";

    cout << "Client: " << client_1.get_name() << endl;

    cout << "Contact: " << client_1.get_contact() << endl;

    cout << "Object Type: " << object_type_1.get_type_name() << endl;

    cout << "City: " << city_1.get_name() << endl;

    cout << "Budget: $" << budget << "\n";

    cout << "Total Material Cost: $" << total_material_cost << "\n";

    cout << "Construction Time: "<< construction_time_1.get_start_date() <<" to "<< construction_time_1.get_end_date()<< endl;

    show_equipment();

     cout << "Uniform: " << uniform_1.get_type() << " (quantity: " << uniform_1.get_quantity() << ")" << endl;


    if (!safety_reports.empty()) {
        cout << "safety reports:" << endl;
        for (const auto& report : safety_reports) {
            cout << "- " << report.get_report_name() << " - status: " << report.get_status() << endl;
        }
    }

    if (!shifts.empty()) {
        cout << "Shifts:" << endl;
        for (const auto& shift : shifts) {
            cout << "- Start: " << shift.get_start_time() << ", end: " << shift.get_end_time() << endl;
        }
    }

    cout << "Days Off: " << days_off.get_days_count() << endl;

    cout << "Salary: " << salary_1.get_amount() << endl;


}
