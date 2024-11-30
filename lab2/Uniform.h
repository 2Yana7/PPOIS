#ifndef Uniform_h
#define Uniform_h

#include <string>
using namespace std;

class Uniform {
public:
    Uniform(const string& type = "standart Uniform ", int quantity = 0);

    void set_type(const string& type);
    string get_type() const;

    void set_quantity(int quantity);
    int get_quantity() const;

private:
    string type;
    int quantity;
};

#endif
