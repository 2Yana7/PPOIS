#include "Safety_report.h"

Safety_report::Safety_report(const string& report_name, const string& status)
    : report_name(report_name), status(status) {}



string Safety_report::get_report_name() const {
    return report_name;
}

string Safety_report::get_status() const {
    return status;
}
