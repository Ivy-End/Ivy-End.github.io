# SGU 112 - a^b - b^a


## Description

You are given natural numbers $a$ and $b$. Find $a^b - b^a$.

## Input

Input contains numbers $a$ and $b$ ($1\leq a,b\leq 100$).

## Output

Write answer to output.

## Sample Input

```
2 3
```

## Sample Output

```
-1
```

## Analysis

非常明显的高精度，再观察一下样例，要处理减法，而且有负数，注意一下好了。

## Solution

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 1024;
const int HEX = 10000;
const int BIT = 4;
 
class Huge
{
public:
    Huge();
    Huge(int x);
    ~Huge();
     
public:
    Huge& operator *= (int x);
    Huge& operator - (Huge &x);
    bool operator > (Huge x);
     
public:
    friend ostream& operator << (ostream &out, Huge &x);
     
public:
    int m_pData[MAX];
    int m_nLen;
};
 
Huge::Huge()
{
    memset(m_pData, 0, sizeof(m_pData));
    m_nLen = 1;
}
 
Huge::Huge(int x)
{
    memset(m_pData, 0, sizeof(m_pData));
    m_pData[1] = x;
    m_nLen = 1;
}
 
Huge::~Huge()
{
     
}
 
bool Huge::operator > (Huge x)
{
    if(this->m_nLen != x.m_nLen)
    { return this->m_nLen > x.m_nLen; }
    else
    {
        for(int i = this->m_nLen; i >= 1; i--)
        {
            if(this->m_pData[i] != x.m_pData[i])
            { return this->m_pData[i] > x.m_pData[i]; }
        }
    }
    return true;
}
 
Huge& Huge::operator *= (int x)
{
    for(int i = 1; i <= this->m_nLen; i++)
    { this->m_pData[i] *= x; }
    for(int i = 1; i <= this->m_nLen; i++)
    {
        this->m_pData[i + 1] += this->m_pData[i] / HEX;
        this->m_pData[i] %= HEX;
    }
    while(this->m_pData[this->m_nLen + 1]) { this->m_nLen++; }
    return *this;
}
 
Huge& Huge::operator - (Huge &x)
{
    bool bFlag = (*this > x);
    if(!bFlag) { swap(*this, x); }
    Huge *ans = new Huge();
    ans = this;
    for(int i = 1; i <= ans->m_nLen; i++)
    {
        ans->m_pData[i] -= x.m_pData[i];
        if(ans->m_pData[i] < 0)
        {
            ans->m_pData[i + 1]--;
            ans->m_pData[i] += HEX;
        }
    }
    while(!ans->m_pData[ans->m_nLen] && ans->m_nLen) { ans->m_nLen--; }
    if(!bFlag) { ans->m_pData[ans->m_nLen] = -ans->m_pData[ans->m_nLen]; }
    return *ans;
}
 
ostream& operator << (ostream &out, Huge &x)
{
    out << x.m_pData[x.m_nLen];
    for(int i = x.m_nLen - 1; i >= 1; i--)
    {
        if(x.m_pData[i] < 1000) { out << "0"; }
        if(x.m_pData[i] < 100) { out << "0"; }
        if(x.m_pData[i] < 10) { out << "0"; }
        out << x.m_pData[i];
    }
    return out;
}
 
int main()
{
    int a, b;
    while(cin >> a >> b)
    {
        Huge x(a), y(b);
        for(int i = 1; i < b; i++)
        { x *= a; }
        for(int i = 1; i < a; i++)
        { y *= b; }
        cout << x - y << endl;
    }
    return 0;
}
```

高精度是我最惧写的，因为太麻烦，每次都要写上百行，还要重载运算符，弄不好还需要进行调试。
