#ifndef material_h
#define material_h

#include <string>
using namespace std;

class material {
public:
    material(const string& name, double cost);

    string get_name() const;
    double get_cost() const;

private:
    string name;
    double cost;
};

#endif
