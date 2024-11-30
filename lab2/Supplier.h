#ifndef Supplier_h
#define Supplier_h

#include <string>
#include <vector>
#include "Material.h"
using namespace std;

class Supplier {
public:
    Supplier(const string& name);

    void add_material(const Material& material);
    void list_materials() const;
    string get_name()const { return name; };
     size_t get_material_count() const { return materials.size(); }
private:
    string name;
    vector<Material> materials;
};

#endif
