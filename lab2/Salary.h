#ifndef Salary_h
#define Salary_h

class Salary {
public:
    Salary(double amount);
    Salary();

    double get_amount() const;
    void update_Salary(double new_amount);

private:
    double amount;
};

#endif
