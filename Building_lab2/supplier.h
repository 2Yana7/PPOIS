#ifndef supplier_h
#define supplier_h

#include <string>
#include <vector>
#include "material.h"
using namespace std;

class supplier {
public:
    supplier(const string& name);

    void add_material(const material& material);
    void list_materials() const;
    string get_name()const { return name; };
     size_t get_material_count() const { return materials.size(); }
private:
    string name;
    vector<material> materials;
};

#endif
