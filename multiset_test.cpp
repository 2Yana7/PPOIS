#include "multiset.h"
#include <gtest/gtest.h>

TEST(multiset_test, default_constructor){
    multiset ms;
    EXPECT_TRUE(ms.empty());
}

TEST(multiset_test, string_constructor){
    multiset ms("{a,b,c,{d,a,{a}, p}, l}");
    EXPECT_EQ(ms.size(), 5);
}

TEST(multiset_test, copy_constructor){
    multiset ms1("{a,b,{c,d},a}");
    multiset ms2(ms1);
    EXPECT_EQ(ms1.size(),ms2.size());
}

TEST(multiset_test, operator_prisvoenie){
    multiset ms1;
    ms1 = "{a,b,{c,d},a}";
    EXPECT_EQ(ms1.size(), 4);
}

TEST(multiset_test, operator_equal){
    multiset ms1("{a,b,{c,d},a}");
    multiset ms2("{a,b,{c,d},a}");
    EXPECT_TRUE(ms1==ms2);
}
TEST(multiset_test, operator_not_equal){
    multiset ms1("{a,b,{c,d},a}");
    multiset ms2("{a,b,{c,d},a}");
    EXPECT_FALSE(ms1!=ms2);
}
TEST(multiset_test, operator_unite){
    multiset ms1("{a,b,{c,d},a}");
    multiset ms2("{c,d,{o,p,a}}");
    multiset final = ms1+ms2;
    EXPECT_EQ(final.size(),7);
}
TEST(multiset_test, operator_minus){
    multiset ms1("{a,b,{c,d},a}");
    multiset ms2("{c,b,{o,p,a}}");
    multiset final = ms1-ms2;
    EXPECT_EQ(final.size(),3);
}
TEST(multiset_test, operator_peresechenie){
    multiset ms1("{a,b,{c,d},a}");
    multiset ms2("{c,b,{o,p,a}}");
    multiset final = ms1*ms2;
    EXPECT_EQ(final.size(),1);
}
TEST(multiset_test, size){
    multiset ms1("{a,b,{c,d},a}");
    EXPECT_EQ(ms1.size(), 4);
}
TEST(multiset_test, exists_simple){
    multiset ms1("{a,b,{c,d},a}");
    EXPECT_TRUE(ms1['a']);
}
TEST(multiset_test, exists_difficult){
    multiset ms1("{a,b,{c,d},a}");
    EXPECT_TRUE(ms1["{c,d}"]);
}
TEST(multiset_test, add_simple){
    multiset ms1("{a,b,{c,d},a}");
    ms1.add(std::make_pair('a',1));
    EXPECT_EQ(ms1.size(), 5);
}
TEST(multiset_test, add_difficult){
    multiset ms1("{a,b,{c,d},a}");
    ms1.add(std::make_pair("{a,b,{c}}", 2));
    EXPECT_EQ(ms1.size(), 6);
}
TEST(multiset_test, remove_simple){
    multiset ms1("{a,b,{c,d},a}");
    ms1.remove(std::make_pair('a',2));
    EXPECT_EQ(ms1.size(), 2);
}
TEST(multiset_test, remove_difficult){
    multiset ms1("{a,b,{c,d},a}");
    ms1.remove(std::make_pair("{c,d}",1));
    EXPECT_EQ(ms1.size(), 3);
}
TEST(multiset_test, print){
    multiset ms1("{a,b,{c,d},a}");
    std::string out = ms1.print();
    EXPECT_EQ(out, "{{c,d},b,a,a,}");
}
TEST(multiset_test, boolean){
    multiset ms1("{a,b,{c,d},a}");
    EXPECT_EQ(ms1.boolean().size(), 12);
}
TEST(multiset_test, hashf){
    multiset test;
    int first = test.hashf("{a,b,c,d,{c,d}}");
    int second = test.hashf("{d,c,b,a,{c,d}}");
    EXPECT_EQ(first,second);}

TEST(multiset_test, hash){
    multiset test;
    int first = test.hashf("{{q,w,{s,{d,w},a}},a,b,c,d,{c,d},{d,d},a}");
    int second = test.hashf("{d,c,b,a,{c,d}, {d,d}, {q,w,{s,{d,w},a}}a}");
    EXPECT_EQ(first,second);
        }

TEST(multiset_test, hashh){
        multiset test;
        int first = test.hashf("{a,{b,c},{d,e},f}");
        int second = test.hashf("{{b,c},a,f,{d,e}}");
        EXPECT_EQ(first,second);
        }


