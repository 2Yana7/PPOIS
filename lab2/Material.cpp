#include "Material.h"

Material::Material(const string& name, double cost) : name(name), cost(cost) {}

string Material::get_name() const { return name; }
double Material::get_cost() const { return cost; }
