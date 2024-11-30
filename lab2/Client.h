#ifndef Client_h
#define Client_h

#include <string>
using namespace std;

class Client {
public:
    Client(const string& name, const string& contact);

    string get_name() const;
    string get_contact() const;


private:
    string name;
    string contact;
};

#endif
