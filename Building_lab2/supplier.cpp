#include "supplier.h"
#include <iostream>

supplier::supplier(const string& name) : name(name) {}

void supplier::add_material(const material& material) {
    materials.push_back(material);
}

void supplier::list_materials() const {
    cout << "Materials from supplier " << name << ":\n";
    for (const auto& material : materials) {
        cout << "- " << material.get_name() << ": $" << material.get_cost() << "\n";
    }

}
