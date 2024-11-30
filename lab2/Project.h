#ifndef Project_h
#define Project_h

#include "Client.h"
#include <string>
#include <vector>
#include "Employee.h"
#include "Equipment.h"
#include "Material.h"
#include "Task.h"
#include "Construction_time.h"
#include "Safety_report.h"
#include "Shift.h"
#include "Days_off.h"
#include "Salary.h"
#include "Object_type.h"
#include "Uniform.h"
#include "City.h"
#include "Supplier.h"

using namespace std;

class Project {
public:
    Project(const string& name, double budget, const Client& client  );


    void add_employee(const Employee& employee);
    void add_equipment(const Equipment& equipment);
    void add_material(const Material& material);
    void add_task(const Task& task);
    void set_construction_time(const Construction_time& time);
    void add_safety_report(const Safety_report& report);
    void assign_shift(const Shift& shift);
    void set_days_off(const Days_off& days_off);
    void set_salary(const Salary& salary);
    void set_object_type(const Object_type& type);
    void set_uniform(const Uniform& uniform);
    void set_city(const City& city);

    void show_employees() const;
    void show_equipment() const;
    void show_tasks() const;
    void show_Project_details() const;
    vector<Employee>  get_employee( )const { return employees; };
    Construction_time get_construction_time ()const { return construction_time_1; };
    Salary get_salary ()const { return salary_1; };
    Object_type get_object_type ()const { return object_type_1; };
    City get_city ()const { return city_1; };
    Uniform get_uniform ()const { return uniform_1; };
    string get_name ()const { return name; };
    double get_budget()const { return budget; };
    double get_total_material_cost() const { return total_material_cost; };
    Client get_client ()const { return client_1; };
private:
    string name;
    double budget;
    double total_material_cost;

    ::Client client_1;
    ::Construction_time construction_time_1;
    ::Days_off days_off;
    ::Salary salary_1;
    ::Object_type object_type_1;
    ::Uniform uniform_1;
    ::City city_1;

    vector<Employee> employees;
    vector<Equipment> equipmentList;
    vector<Material> materials;
    vector<Task> tasks;
    vector<Safety_report> safety_reports;
    vector<Shift> shifts;
};

#endif
