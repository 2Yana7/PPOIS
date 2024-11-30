#include "project.h"
#include <iostream>

project::project(const string& name, double budget, const class client& client)
: name(name), budget(budget), total_material_cost(0.0), client_1(client) {}


void project::add_employee(const employee& employee) {
    employees.push_back(employee);
}

void project::add_equipment(const equipment& equipment) {
    equipmentList.push_back(equipment);
}

void project::add_material(const material& material) {
    materials.push_back(material);
    total_material_cost += material.get_cost();
}

void project::add_task(const task& task) {
    tasks.push_back(task);
}

void project::show_employees() const {
    cout << "Employees in project " << name << ":\n";
    for (const auto& employee : employees) {
        cout << "- " << employee.get_name() << " (" << employee.get_role() << ")\n";
    }
}

void project::show_equipment() const {
    cout << "Equipment used in project " << name << ":\n";
    for (const auto& equipment : equipmentList) {
        cout << "- " << equipment.get_type() << " with ID: " << equipment.get_id() << "\n";
    }
}

void project::show_tasks() const {
    cout << "Tasks in project " << name << ":\n";
    for (const auto& task : tasks) {
        cout << "- " << task.get_description()
        << " (Status: " << task.get_status()
        << ", Assigned to: " << task.get_assigned_employee()->get_name() << ")\n";
    }
}

void project::set_construction_time(const class construction_time& time) {
    construction_time_1 = time;
}


void project::add_safety_report(const class safety_report& report) {
    safety_reports.push_back(report);
}

void project::assign_shift(const shift& shift) {
    shifts.push_back(shift);

}

void project::set_days_off(const class days_off& days_off) {
    this->days_off = days_off; }

    void project::set_salary(const class salary& salary) {
        this->salary_1 = salary;

}

void project::set_object_type(const class object_type& type) {
    object_type_1 = type;}

    void project::set_uniform(const class uniform& uniform) {
        this->uniform_1 = uniform;
    }

    void project::set_city(const class city& city_name) {
        city_1 = city_name;
    }

void project::show_project_details() const {
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
