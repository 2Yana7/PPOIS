#ifndef Equipment_h
#define Equipment_h

#include <string>
using namespace std;

class Equipment {
public:
    Equipment(const string& type, int id);
    string get_type() const;
    int get_id() const;
    void operate() const;

private:
    string type;
    int id;
};

#endif
