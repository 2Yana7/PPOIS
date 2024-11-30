#include "safety_report.h"

safety_report::safety_report(const string& report_name, const string& status)
    : report_name(report_name), status(status) {}



string safety_report::get_report_name() const {
    return report_name;
}

string safety_report::get_status() const {
    return status;
}
