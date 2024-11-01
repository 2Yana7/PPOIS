#pragma once
#include <string>
#include <unordered_map>
#include <vector>
#include <functional>
#include <iostream>


class multiset {
public:
    multiset(std::unordered_map<int, int> data, std::unordered_map<std::string, int> hashes);
    multiset();
    multiset(const std::string& str);

    void operator=(std::string str);
    bool operator==(multiset another);
    bool operator!=(multiset another);
    multiset operator+(multiset another);
    void operator+=(multiset another);
    multiset operator-(multiset another);
    void operator-=(multiset another);
    multiset operator*(multiset another);
    void operator*=(multiset another);

    int size();
    bool operator[](std::string str);
    bool operator[](char elm);

    void add(std::pair<char, int> element);
    void add(std::pair<std::string, int> element);
    void remove(std::pair<char, int> element);
    void remove(std::pair<std::string, int> element);
    std::string print();
    bool empty();
    std::vector<std::vector<std::unordered_map<int, int>>> boolean();

    std::unordered_map<std::string, int> hashes;
    std::unordered_map<int, int> data;
    int hashf(std::string str);
    int hash(std::string str, int& pos, int& level);;
};
