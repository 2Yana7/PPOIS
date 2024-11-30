#ifndef equipment_h
#define equipment_h

#include <string>
using namespace std;

class equipment {
public:
    equipment(const string& type, int id);
    string get_type() const;
    int get_id() const;
    void operate() const;

private:
    string type;
    int id;
};

#endif
