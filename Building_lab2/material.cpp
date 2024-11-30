#include "material.h"

material::material(const string& name, double cost) : name(name), cost(cost) {}

string material::get_name() const { return name; }
double material::get_cost() const { return cost; }
