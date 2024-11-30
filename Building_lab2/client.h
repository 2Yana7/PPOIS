#ifndef client_h
#define client_h

#include <string>
using namespace std;

class client {
public:
    client(const string& name, const string& contact);

    string get_name() const;
    string get_contact() const;


private:
    string name;
    string contact;
};

#endif
