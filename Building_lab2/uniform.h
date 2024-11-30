#ifndef uniform_h
#define uniform_h

#include <string>
using namespace std;

class uniform {
public:
    uniform(const string& type = "standart uniform ", int quantity = 0);

    void set_type(const string& type);
    string get_type() const;

    void set_quantity(int quantity);
    int get_quantity() const;

private:
    string type;
    int quantity;
};

#endif
