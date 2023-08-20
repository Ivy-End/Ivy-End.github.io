# ACM-ICPC 寒假练习 03


今天刷了高精度专题，本来准备写一个高精度类，然后直接套模版，后来发现根据每题的要求分开写高精度反而效率高。

主要涉及了高精度加法、乘法、除法、取余（其中后两项为高精度和低精度进行运算）。

终于打过一遍高精度除以低精度了，高精度专题也算圆满了。

## UVaOJ 424

高精度加法，水题。

```cpp
#include <iostream>
#include <string>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int nLen;
int pData[MAX];
 
int main()
{
    nLen = 1;
    memset(pData, 0, sizeof(pData));
    string x;
    while(cin >> x)
    {
        if(x != "0")
        {
            while(x[0] == '0') { x = x.substr(1, x.length() - 1); }
            nLen = max(nLen, (int)x.length());
            for(int i = 1; i <= x.length(); i++)
            {
                pData[i] += x[x.length() - i] - '0';
                pData[i + 1] += pData[i] / 10;
                pData[i] %= 10;
            }
            while(pData[nLen + 1]) { nLen++; }
        }
        else
        {
            for(int i = nLen; i >= 1; i--)
            { cout << pData[i]; }
            cout << endl;
            nLen = 1;
            memset(pData, 0, sizeof(pData));
        }
    }
    return 0;
}
```

## UVaOJ 10106

高精度乘法，要注意的是某一个乘数为 0 的情况，要特判一下。

```cpp
#include <iostream>
#include <string>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int nLen;
int pData[MAX];
 
int main()
{
     
    string x, y;
    while(cin >> x >> y)
    {
        if(x.length() < y.length()) { swap(x, y); }
        nLen = x.length() + y.length();
        memset(pData, 0, sizeof(pData));
        for(int i = 1; i <= y.length(); i++)
        {
            for(int j = 1; j <= x.length(); j++)
            {
                pData[i + j - 1] += (x[x.length() - j] - '0') * (y[y.length() - i] - '0');
                pData[i + j] += pData[i + j - 1] / 10;
                pData[i + j - 1] %= 10;
            }
        }
        while(nLen && !pData[nLen]) { nLen--; }
        if(nLen == 0) { nLen = 1; }
        for(int i = nLen; i >= 1; i--)
        { cout << pData[i]; }
        cout << endl;
    }
    return 0;
}
```

## UVaOJ 465

判断加数、乘数以及结果是否在 `int` 范围内，一开始把结果都算出来再比较。后来查了资料发现可以直接用 `double` 过，其中使用到了 `atof` 这个命令。

```cpp
#include <iostream>
#include <string>
#include <stdlib.h>
 
using namespace std;
 
const int MAX_INT = 2147483647;
 
int main()
{
    char dwOpt;
    string x, y;
    while(cin >> x >> dwOpt >> y)
    {
        cout << x << " " << dwOpt << " " << y << endl;
        double a, b;
        a = atof(x.c_str());
        b = atof(y.c_str());
        if(a > MAX_INT) { cout << "first number too big" << endl; }
        if(b > MAX_INT) { cout << "second number too big" << endl; }
        if(dwOpt == '+' && a + b > MAX_INT) { cout << "result too big" << endl; }
        if(dwOpt == '*' && a * b > MAX_INT) { cout << "result too big" << endl; }
    }
}
```

## UVaOJ 748

带有小数的乘方问题。

先确定小数点的位数，然后去掉小数点，进行高精度乘方运算，最后加上小数点即可。

```cpp
#include <iostream>
#include <string>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int nLen, nDot;
int pData[MAX];
 
string Solve(string x, string y);
 
int main()
{
    string x;
    int y;
    while(cin >> x >> y)
    {
        while(x[x.length() - 1] == '0') { x = x.substr(0, x.length() - 1); }
        nDot = x.length() - x.find('.') - 1;
        nDot *= y;
        x = x.substr(0, x.find('.')) + x.substr(x.find('.') + 1, x.length() - x.find('.') - 1);
        string z = "1";
        for(int i = 1; i <= y; i++)
        { z = Solve(z, x); }
        if(z.length() <= nDot)
        {
            cout << ".";
            for(int i = z.length(); i < nDot; i++)
            { cout << "0"; }
            cout << z << endl;
        }
        else
        {
            for(int i = 0; i < z.length() - nDot; i++)
            { cout << z[i]; }
            cout << ".";
            for(int i = z.length() - nDot; i < z.length(); i++)
            { cout << z[i]; }
            cout << endl;
        }
    }
    return 0;
}
 
string Solve(string x, string y)
{
    if(x.length() < y.length()) { swap(x, y); }
    nLen = x.length() + y.length();
    memset(pData, 0, sizeof(pData));
    for(int i = 1; i <= y.length(); i++)
    {
        for(int j = 1; j <= x.length(); j++)
        {
            pData[i + j - 1] += (x[x.length() - j] - '0') * (y[y.length() - i] - '0');
            pData[i + j] += pData[i + j - 1] / 10;
            pData[i + j - 1] %= 10;
        }
    }
    while(nLen && !pData[nLen]) { nLen--; }
    if(nLen == 0) { nLen = 1; }
    string z = "";
    for(int i = 1; i <= nLen; i++)
    { z = (char)(pData[i] + '0') + z; }
    return z;
}
```

## UVaOJ 10494
高精度除以低精度以及取模运算。在网上搜了资料，终于学会了。但是要注意 `0 % X` 的情况。

另外想说的是非常喜欢这道题目的标题“If We Were A Child Again”，勾起了多少回忆。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int nLen;
int pData[MAX], pAns[MAX];
 
string Solve(string x, long long y, char dwOpt);
 
int main()
{
    char dwOpt;
    string x;
    long long y;
    while(cin >> x >> dwOpt >> y)
    { cout << Solve(x, y, dwOpt) << endl; }
    return 0;
}
 
string Solve(string x, long long y, char dwOpt)
{
    memset(pData, 0, sizeof(pData));
    memset(pAns, 0, sizeof(pAns));
    nLen = x.length();
    for(int i = 1; i <= x.length(); i++)
    { pData[i] = x[x.length() - i] - '0'; }
    long long d = 0;
    for(int i = nLen; i >= 1; i--)
    {
        d = d * 10 + pData[i];
        pAns[i] = d / y;
        d %= y;
    }
    while(nLen && pAns[nLen] == 0) { nLen--; }
    if(nLen == 0) { nLen = 1; }
    string z = "";
    if(dwOpt == '/')
    {
        for(int i = 1; i <= nLen; i++)
        { z = (char)(pAns[i] + '0') + z; }
    }
    else
    {
        while(d)
        {
            z = (char)(d % 10 + '0') + z;
            d /= 10;
        }
        if(z == "") { z = "0"; }
    }
    return z;
}
```

今天由于题目相对比较少，所以做的比较快。接下来一个专题应该是排序和检索。
