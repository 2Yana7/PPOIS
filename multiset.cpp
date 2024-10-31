#include "multiset.h"
#include <unordered_map>
using namespace std;

multiset::multiset(unordered_map<int,int> data, unordered_map<string,int> hashes){
        this->data = data;
        this->hashes = hashes;
    }
   multiset::multiset(){}
    multiset::multiset(const string& str){
        int level = -1;
        string sub;
        for(auto& elm : str){
            if(elm=='{') level++;
            if(level>0)sub+=elm;
            if(elm=='}') level--;
            if(elm=='}' && level==0){
                hashes[sub] = hashf(sub);
                data[hashes[sub]] += 1;
                sub.erase();
            }
            if(isalnum(elm) && level==0){
                data[static_cast<int>(elm)] +=1;
            }
        }
        // cout << sub << "-----sub" << endl;
    }
    void multiset::operator =(string str){
        *this = multiset(str);
    }
    bool multiset::operator==(multiset another){
        if(this->data==another.data && this->hashes==another.hashes) return true;
        return false;
    }
    bool multiset::operator!=(multiset another){
        return !(*this==another);
    }
    multiset multiset::operator+(multiset another){
        multiset final(*this);
        for(auto elm : another.data) final.data[elm.first]+= elm.second;
        for(auto elm : another.hashes) final.hashes[elm.first] = elm.second;
        return final;
    }
    void multiset::operator+=(multiset another){
        *this = *this + another;
    }
    multiset multiset::operator-(multiset another){
        multiset final(*this);
        for(auto elm : another.data){
            final.data[elm.first]-= elm.second;
            if(final.data[elm.first]<1){
                for(auto& hash : another.hashes){
                    if(hash.second == elm.first) final.hashes.erase(hash.first);
                }
                final.data.erase(elm.first);
            }
        }

        return final;
    }
    void multiset::operator -=(multiset another){
        *this = *this - another;
    }
    multiset multiset::operator *(multiset another){
        multiset final;
        for(auto& first : this->data){
            for(auto second : another.data){
                if(first.first==second.first){
                    int smallest = first.second < second.second ? first.second : second.second;
                    final.data[first.first] = smallest;
                }
            }
        }
        for(auto& first : this->hashes){
            for(auto& second : another.hashes){
                if(first.second==second.second){
                    final.hashes[first.first] = first.second;
                }
            }
        }
        return final;
    }
    void multiset::operator *=(multiset another){
        *this = *this * another;
    }
    int multiset::size(){
        int size = 0;
        for(auto& elm : this->data) size+=elm.second;
        return size;
    }
    bool multiset::operator [](string str){
        if(this->data[hashf(str)]>0) return true;
        return false;
    }
    bool multiset::operator [](char elm){
        if(this->data[static_cast<int>(elm)]>0) return true;
        return false;
    }
    void multiset::add(pair<char,int> element){
        this->data[static_cast<int>(element.first)] += element.second;
    }
    void multiset::add(pair<string,int> element){
        this->data[hashf(element.first)]+= element.second;
        this->hashes[element.first] = hashf(element.first);
    }
    void multiset::remove(pair<char,int> element){
        this->data[element.first] -= element.second;
        if(this->data[element.first]<1) this->data.erase(element.first);
    }
    void multiset::remove(pair<string, int> element){
        this->data[hashf(element.first)]-=element.second;
        if(this->data[hashf(element.first)] < 1) {
            this->data.erase(hashf(element.first));
            this->hashes.erase(element.first);
        }
    }
    bool multiset::empty(){
        return this->data.size()==0? true : false;
    }
    string multiset::print(){
        string out = "{";
        vector<pair<string,int>> elms;
        for(auto& elm : this->hashes){
            elms.push_back(make_pair(elm.first, this->data[elm.second]));
        }
        for(auto& dep : this->data){
            bool go = true;
            for(auto& elm : this->hashes){
                if(dep.first==elm.second) go = false;
            }
            if(go){
                char c = dep.first;
                string s;
                s+=c;
                elms.push_back(make_pair(s,dep.second));
            }
        }
        for(auto& elm : elms){
            for(int i = 0; i < elm.second ; i++) {out+=elm.first; out+= ',';}
        }
        out+='}';
        return out;
    }
    vector<vector<unordered_map<int, int>>> multiset::boolean() {
        vector<vector<unordered_map<int, int>>> result = {{}};

        for (const auto& [key, count] : data) {
            size_t cs = result.size();

            for (size_t i = 0; i < cs; ++i) {
                for (int k = 1; k <= count; ++k) {
                    auto sub = result[i];
                    sub.push_back({{key, k}});
                    result.push_back(std::move(sub));
                }
            }
        }

        return result;
    }
        int multiset::hashf(string str){
        int hash = 213;
        int i = 0;
        int count = 0;
        int open = 0;
        int close = 0;
        int max_count = 0;
        while(i < str.length()){
            //cout << str[i] << endl;
            if(str[i]=='{' && count == 0){
                count++;
                max_count++;
                open = i;
            } else
                if(str[i]=='{'){
                    count++;
                    max_count++;
                }
                if(str[i]=='}' && count ==1){
                    close = i;
                    count--;
                } else
                    if(str[i]=='}')count--;
                    if(isalnum(str[i]) && count==1) hash += static_cast<int>(str[i]*max_count);
                    i++;
        }
        //cout << str[close] << " --- close" << endl;
        if(max_count==1) return hash;
        if(open==0 && close==0) return hash;
        string next = string(str.begin()+1+open, str.begin()+close);
       //cout << next << endl;
        return hash + hashf(next);
    }

    unordered_map<string, int> hashes = unordered_map<string,int>(100);
    unordered_map<int,int> data = unordered_map<int,int>(100);