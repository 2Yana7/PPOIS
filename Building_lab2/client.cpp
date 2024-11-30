#include "client.h"

client::client(const string& name, const string& contact)
    : name(name), contact(contact) {}

string client::get_name() const {
    return name;
}

string client::get_contact() const {
    return contact;
}
