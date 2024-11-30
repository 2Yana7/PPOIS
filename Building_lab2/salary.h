#ifndef salary_h
#define salary_h

class salary {
public:
    salary(double amount);
    salary();

    double get_amount() const;
    void update_salary(double new_amount);

private:
    double amount;
};

#endif
