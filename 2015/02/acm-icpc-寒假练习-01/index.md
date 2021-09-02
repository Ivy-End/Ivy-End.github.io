# ACM-ICPC 寒假练习 01


这一系列的练习主要在 Virtual Judge 上进行，题目为小白书上的题目推荐。

## UVa 10055

求两方军队人数的差值，直接相减即可。

不过要注意两个数的大小关系。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    long long x, y;
    while(cin >> x >> y)
    {
        if(x > y) { swap(x, y); }
        cout << y - x << endl;
    }
    return 0;
}
```

## UVa 10071

简单物理题，求两倍时间内匀速运动的路程。即 $s = 2vt$。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int x, y;
    while(cin >> x >> y)
    { cout << x * y * 2 << endl; }
    return 0;
}
```

## UVa 10300

根据题目描述推导公式，$$ ans = \sum{\left(\frac{x}{y}\cdot y\cdot z\right)} = \sum{xz}$$

题中讲到了首先计算每只动物的占地面积，乘以环境友好常数，再乘以动物数目。这里可以直接将动物数目约去。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int T, N, x, y, z;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        int ans = 0;
        cin >> N;
        for(int j = 1; j <= N; j++)
        {
            cin >> x >> y >> z;
            ans += x * z;
        }
        cout << ans << endl;
    }
}
```

## UVa 458

凯撒密码，加密的时候将 ASCII 右移了 7 位，解密的时候只要反过来左移 7 位即可。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
    string x;
    while(getline(cin, x))
    {
        for(int i = 0; i < x.length(); i++)
        { cout << (char)(x[i] - 7); }
        cout << endl;
    }
    return 0;
}
```

## UVa 494

一开始想通过计算空格数来计算单词个数，后来发现不行，只好使用原始的模拟方法。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
    string x, y;
    while(getline(cin, x))
    {
        y = "";
        int ans = 0;
        for(int i = 0; i < x.length(); i++)
        {
            if(x[i] >= 'A' && x[i] <= 'Z' ||
                x[i] >= 'a' && x[i] <= 'z')
            { y += x[i]; }
            else
            {
                if(y != "") { ans++; y = ""; }
            }
        }
        cout << ans << endl;
    }
    return 0;
}
```

## UVa 414

英语不好，题目看了半天，找了翻译，才看懂题目。

实际上，只有包裹在 $X$ 内部的空格才要统计在内，即得 $ans = Total - Minimum \times Row$。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
    int N;
    string x;
    while(cin >> N)
    {
        cin.get();
        if(!N) { break; }
        int nTotal = 0, nMin = 2147483647;
        for(int i = 1; i <= N; i++)
        {
            int nTmp = 0;
            getline(cin, x);
            for(int j = 0; j < x.length(); j++)
            {
                if(x[j] == ' ') { nTmp++; }
            }
            nTotal += nTmp;
            nMin = min(nMin, nTmp);
        }
        cout << nTotal - nMin * N << endl;
    }
    return 0;
}
```

## UVa 490

这个处理要注意没有字符的时候输出空格，否则会 PE。类似矩阵转置。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
const int MAX = 128;
 
string strTmp[MAX];
 
int main()
{
    int nPos = 0, nLen = 0;
    while(getline(cin, strTmp[++nPos]))
    { nLen = max(nLen, (int)strTmp[nPos].length()); }
    for(int j = 0; j < nLen; j++)
    {
        for(int i = nPos - 1; i >= 1; i--)
        {
            if(j < strTmp[i].length())
            { cout << strTmp[i][j]; }
            else
            { cout << " "; }
        }
        cout << endl;
    }
    return 0;
}
 
int max(int x, int y)
{ return x > y ? x : y; }
```

## UVa 445

朴素的字符串处理题，注意换行的处理。水题。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
string x;
 
int main()
{
    while(getline(cin, x))
    {
        int nPos = 0;
        while(nPos < x.length())
        {
            int nCnt = 0;
            if(x[nPos] == '!') { cout << endl; }
            while(x[nPos] >= '0' && x[nPos] <= '9')
            {
                nCnt += x[nPos] - '0';
                nPos++;
            }
            for(int i = 1; i <= nCnt; i++)
            {
                if(x[nPos] == 'b') { cout << " "; }
                else { cout << x[nPos]; }
            }
            nPos++;
        }
        cout << endl;
    }
    return 0;
}
```

## UVa 488

水题。

```cpp
#include <iostream>
 
using namespace std;
 
void Tri(int x);
 
int main()
{
    int T, N, M;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> N >> M;
        for(int j = 1; j <= M; j++)
        {
            Tri(N);
            if(j != M) { cout << endl; }
        }
        if(i != T) { cout << endl; }
    }
}
 
void Tri(int x)
{
    for(int i = 1; i <= x - 1; i++)
    {
        for(int j = 1; j <= i; j++)
        { cout << i; }
        cout << endl;
    }
    for(int i = 1; i <= x; i++)
    { cout << x; }
    cout << endl;
    for(int i = x - 1; i >= 1; i--)
    {
        for(int j = i; j >= 1; j--)
        { cout << i; }
        cout << endl;
    }
}
```

## UVa 489

还是英语不好，百度了游戏规则才看懂了题目。看懂以后就是水题了。

```cpp
#include <iostream>
#include <string>
#include <memory.h>
 
using namespace std;
 
const int MAX = 32;
 
bool pVisited[MAX];
 
int main()
{
    int N;
    string x, y;
    while(cin >> N)
    {
        if(N == -1) { break; }
        bool bFlag = true;
        int nCnt = 0, nTmp = 0, nWrong = 0;
        memset(pVisited, false, sizeof(pVisited));
        cout << "Round " << N << endl;
        cin >> x >> y;
        for(int i = 0; i < x.length(); i++)
        {
            if(!pVisited[x[i] - 'a'])
            {
                pVisited[x[i] - 'a'] = true;
                nCnt++;
            }
        }
        for(int i = 0; i < y.length(); i++)
        {
            if(pVisited[y[i] - 'a'])
            {
                pVisited[y[i] - 'a'] = false;
                nTmp++;
            }
            else { nWrong++; }
            if(nTmp == nCnt && nWrong < 7) { bFlag = true; break; }
            if(nTmp != nCnt && nWrong >= 7) { bFlag = false; break; }
        }
        if(bFlag)
        {
            if(nTmp == nCnt) { cout << "You win." << endl; }
            else { cout << "You chickened out." << endl; }
        }
        else { cout << "You lose." << endl; }
    }
    return 0;
}
```

## UVa 694

又是 $3n + 1$ 问题，一开始总是 TLE，位运算以后还是 TLE，后来发现用了 `int`，中间值会溢出，所以表面上是 TLE，实际上已经 WA 了。或许这就是 TLE 有可能是 WA 的一个很好的例子吧。 

```cpp
#include <stdio.h>
 
int main()
{
    long long A, L, nCase = 0;
    while(scanf("%lld%lld", &A, &L) != EOF)
    {
        if(A == -1 && L == -1) { break; }
        printf("Case %lld: A = %lld, limit = %lld, number of terms = ", ++nCase, A, L);
        long long nCnt = 0;
        while(A <= L)
        {
            nCnt++;
            if(A == 1) { break; }
            if(A & 1) { A = 3 * A + 1; }
            else { A >>= 1; }
        }
        printf("%lld\n", nCnt);
    }
    return 0;
}
```

## UVa 457

感觉像模拟细胞生命的游戏，模拟即可，水题。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 64;
 
int pData[MAX], pDish[MAX][2];
 
int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        memset(pDish, 0, sizeof(pDish));
        pDish[20][0] = 1;
        for(int j = 0; j < 10; j++)
        { cin >> pData[j]; }
        for(int j = 1; j <= 50; j++)
        {
            for(int k = 1; k <= 40; k++)
            {
                if(pDish[k][0] == 0) { cout << " "; }
                if(pDish[k][0] == 1) { cout << "."; }
                if(pDish[k][0] == 2) { cout << "x"; }
                if(pDish[k][0] == 3) { cout << "W"; }
            }
            for(int k = 1; k <= 40; k++)
            {
                int nCnt = pDish[k - 1][0] + pDish[k][0] + pDish[k + 1][0];
                pDish[k][1] = pData[nCnt];
            }
            for(int k = 1; k <= 40; k++)
            { pDish[k][0] = pDish[k][1]; }
            cout << endl;
        }
        if(i != T) { cout << endl; }
    }
    return 0;
}
```

总结一下，刷了12道水题，发现比sgu简单多了，就这样穿插着刷一刷小白书吧。
