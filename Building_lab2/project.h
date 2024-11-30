#ifndef project_h
#define project_h

#include "client.h"
#include <string>
#include <vector>
#include "employee.h"
#include "equipment.h"
#include "material.h"
#include "task.h"
#include "construction_time.h"
#include "safety_report.h"
#include "shift.h"
#include "days_off.h"
#include "salary.h"
#include "object_type.h"
#include "uniform.h"
#include "city.h"
#include "supplier.h"

using namespace std;

class project {
public:
    project(const string& name, double budget, const client& client  );


    void add_employee(const employee& employee);
    void add_equipment(const equipment& equipment);
    void add_material(const material& material);
    void add_task(const task& task);
    void set_construction_time(const construction_time& time);
    void add_safety_report(const safety_report& report);
    void assign_shift(const shift& shift);
    void set_days_off(const days_off& days_off);
    void set_salary(const salary& salary);
    void set_object_type(const object_type& type);
    void set_uniform(const uniform& uniform);
    void set_city(const city& city);

    void show_employees() const;
    void show_equipment() const;
    void show_tasks() const;
    void show_project_details() const;
    vector<employee>  get_employee( )const { return employees; };
    construction_time get_construction_time ()const { return construction_time_1; };
    salary get_salary ()const { return salary_1; };
    object_type get_object_type ()const { return object_type_1; };
    city get_city ()const { return city_1; };
    uniform get_uniform ()const { return uniform_1; };
    string get_name ()const { return name; };
    double get_budget()const { return budget; };
    double get_total_material_cost() const { return total_material_cost; };
    client get_client ()const { return client_1; };
private:
    string name;
    double budget;
    double total_material_cost;

    ::client client_1;
    ::construction_time construction_time_1;
    ::days_off days_off;
    ::salary salary_1;
    ::object_type object_type_1;
    ::uniform uniform_1;
    ::city city_1;

    vector<employee> employees;
    vector<equipment> equipmentList;
    vector<material> materials;
    vector<task> tasks;
    vector<safety_report> safety_reports;
    vector<shift> shifts;
};

#endif
