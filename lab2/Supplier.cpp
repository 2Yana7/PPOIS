#include "Supplier.h"
#include "Material.h"
#include <iostream>

Supplier::Supplier(const string& name) : name(name) {}

void Supplier::add_material(const Material& material) {
    materials.push_back(material);
}

void Supplier::list_materials() const {
    cout << "Materials from Supplier " << name << ":\n";
    for (const auto& material : materials) {
        cout << "- " << material.get_name() << ": $" << material.get_cost() << "\n";
    }

}
