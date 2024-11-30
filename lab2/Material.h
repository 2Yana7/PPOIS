#ifndef Material_h
#define Material_h

#include <string>
using namespace std;

class Material {
public:
    Material(const string& name, double cost);

    string get_name() const;
    double get_cost() const;

private:
    string name;
    double cost;
};

#endif
