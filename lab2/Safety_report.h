#ifndef Safety_report_h
#define Safety_report_h

#include <string>
using namespace std;

class Safety_report {
public:
    Safety_report(const string& report_name, const string& status);



    string get_report_name() const;
    string get_status() const;

private:
    string report_name;
    string status;
};

#endif
