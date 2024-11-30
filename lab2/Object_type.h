#ifndef Object_type_h
#define Object_type_h

#include <string>
using namespace std;

class Object_type {
public:
    Object_type(const string& type_name = "generic object");
    void set_type_name(const string& type_name);
    string get_type_name() const;

private:
    string type_name;
};

#endif
