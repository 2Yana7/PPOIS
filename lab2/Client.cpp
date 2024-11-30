#include "Client.h"

Client::Client(const string& name, const string& contact)
    : name(name), contact(contact) {}

string Client::get_name() const {
    return name;
}

string Client::get_contact() const {
    return contact;
}
