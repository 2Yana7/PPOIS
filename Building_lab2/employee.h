#ifndef employee_h
#define employee_h

#include <string>
using namespace std;

class employee {
public:
    employee(const string& name, int id, const string& role);

    string get_name() const;
    int get_id() const;
    string get_role() const;

private:
    string name;
    int id;
    string role;
};

#endif
