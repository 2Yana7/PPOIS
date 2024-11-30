#ifndef object_type_h
#define object_type_h

#include <string>
using namespace std;

class object_type {
public:
    object_type(const string& type_name = "generic object");
    void set_type_name(const string& type_name);
    string get_type_name() const;

private:
    string type_name;
};

#endif
