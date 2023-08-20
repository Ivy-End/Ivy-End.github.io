# ACM-ICPC 寒假练习 02


今天刷了小白书的字符串专题，各种 WA 以及 PE。UVaOJ 中有时候会把 PE 判成 WA，这样会导致很难查错。

## UVa 401

这道题目有个坑，只有表格中列出的才是镜像字母，没有列出了的表示没有镜像字母，在这上 WA 了一次。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
const char pAlphabet[] = {
    'A', '*', '*', '*', '3', '*', '*', 'H', 'I',
    'L', '*', 'J', 'M', '*', 'O', '*', '*', '*',
    '2', 'T', 'U', 'V', 'W', 'X', 'Y', '5', '1',
    'S', 'E', '*', 'Z', '*', '*', '8', '*' };
 
bool Palindrome(string x);
bool Mirrored(string x);
 
int main()
{
    string x;
    while(cin >> x)
    {
        if(!Palindrome(x))
        {
            if(Mirrored(x)) { cout << x << " -- is a mirrored string." << endl; }
            else { cout << x << " -- is not a palindrome." << endl; }
        }
        else
        {
            if(Mirrored(x)) { cout << x << " -- is a mirrored palindrome." << endl; }
            else { cout << x << " -- is a regular palindrome." << endl; }
        }
        cout << endl;
    }
    return 0;
}
 
bool Palindrome(string x)
{
    for(int i = 0; i < x.length() / 2; i++)
    {
        if(x[i] != x[x.length() - i - 1]) { return false; }
    }
    return true;
}
 
bool Mirrored(string x)
{
    if(x.length() == 1)
    {
        if(x[0] >= 'A' && x[0] <= 'Z')
        {
            if(pAlphabet[x[0] - 'A'] != x[0]) { return false; }
        }
        else
        {
            if(pAlphabet[x[0] - '0' + 25] != x[0]) { return false; }
        }
    }
    for(int i = 0; i < x.length() / 2; i++)
    {
        if(x[i] >= 'A' && x[i] <= 'Z')
        {
            if(pAlphabet[x[i] - 'A'] != x[x.length() - i - 1]) { return false; }
        }
        else
        {
            if(pAlphabet[x[i] - '0' + 25] != x[x.length() - i - 1]) { return false; }
        }
    }
    return true;
}
```

## UVa 10010

这道题目要求八个方向都要搜一遍，一开始准备写八个函数，后来发现用 `dx[]` 和 `dy[]` 数组就搞定了。

```cpp
#include <iostream>
#include <string>
#include <memory.h>
 
using namespace std;
 
const int MAX = 128;
 
const int dx[] = { 0, 0, 1, -1, -1, 1, -1, 1 };
const int dy[] = { 1, -1, 0, 0, 1, 1, -1, -1 };
 
int T, N, M, Q;
char pMap[MAX][MAX];
 
char ToLower(char x);
void Find(string x);
bool Search(string s, int x, int y);
 
 
int main()
{
    string x;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        memset(pMap, 0, sizeof(pMap));
        cin >> N >> M;
        for(int j = 1; j <= N; j++)
        {
            for(int k = 1; k <= M; k++)
            {
                cin >> pMap[j][k];
                pMap[j][k] = ToLower(pMap[j][k]);
            }
        }
        cin >> Q;
        for(int j = 1; j <= Q; j++)
        {
            cin >> x;
            Find(x);
        }
        if(i != T) { cout << endl; }
    }
    return 0;
}
 
char ToLower(char x)
{
    if(x >= 'a' && x <= 'z') { return x; }
    else { return x + 32; }
}
 
void Find(string x)
{
    bool bFlag = false;
    for(int i = 0; i < x.length(); i++)
    { x[i] = ToLower(x[i]); }
    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= M; j++)
        {
            if(Search(x, i, j))
            { cout << i << " " << j << endl; bFlag = true; break; }
        }
        if(bFlag) { break; }
    }
}
 
bool Search(string s, int x, int y)
{
    for(int i = 0; i < 8; i++)
    {
        bool bFlag = true;
        for(int j = 0; j < s.length(); j++)
        {
            int nx = x + dx[i] * j;
            int ny = y + dy[i] * j;
            if(pMap[nx][ny] != s[j]) { bFlag = false; break; }
        }
        if(bFlag) { return true; }
    }
    return false;
}
```

## UVa 10361

这道题目卡了好久，一直不知道为什么我的代码会各种 WA 以及 PE。最后还是采用了网上一种 C 语言的写法才 AC 了。但还是不知道为什么我的错了。

```cpp
#include <stdio.h>
#include <string.h>
 
const int MAX = 128;
 
char s1[MAX], s2[MAX], s3[MAX], s4[MAX], s5[MAX], line[MAX];
 
void getss(char s[]);
 
int main()
{
    int N;
    scanf("%d", &N);
    getchar();
    for(int i = 1; i <= N; i++)
    {
        getss(s1);
        getss(s2);
        getss(s3);
        getss(s4);
        getss(s5);
        gets(line);
        line[strlen(line) - 3] = '\0';
        printf("%s%s%s%s%s\n", s1, s2, s3, s4, s5);
        printf("%s%s%s%s%s\n", line, s4, s3, s2, s5);
    }
    return 0;
}
 
void getss(char s[])
{
    for(int i = 0; i < MAX; i++)
    {
        if((s[i] = getchar()) =='<' || s[i] == '>' || s[i] == '\n')
        { s[i] = '\0'; break; }
    }
}
```

## UVa 537

这道题目一下就 AC 了，处理的时候注意一下坑数据。

这里还有一个知识点，除了 `atoi` 可以实现 `string` 到 `int` 的转换，还有 `atof`，可以实现 `string` 到 `double` 的转换。

```cpp
#include <iostream>
#include <iomanip>
#include <string>
#include <stdlib.h>
 
using namespace std;
 
int main()
{
    int T;
    cin >> T;
    cin.ignore();
    for(int j = 1; j <= T; j++)
    {
        cout << "Problem #" << j << endl;
        double u = 0, i = 0, p = 0;
        string x, U = "", I = "", P = "";
        getline(cin, x);
        if(x.find("U=") != string::npos) { U = x.substr(x.find("U=") + 2, x.find('V', x.find("U=")) - x.find("U=") - 2); }
        if(x.find("I=") != string::npos) { I = x.substr(x.find("I=") + 2, x.find('A', x.find("I=")) - x.find("I=") - 2); }
        if(x.find("P=") != string::npos) { P = x.substr(x.find("P=") + 2, x.find('W', x.find("P=")) - x.find("P=") - 2); }
        if(U != "")
        {
            if(U[U.length() - 1] >= '0' && U[U.length() - 1] <= '9') { u = atof(U.c_str()); }
            else
            {
                u = atof(U.substr(0, U.length() - 1).c_str());
                if(U[U.length() - 1] == 'm') { u /= 1000.0; }
                if(U[U.length() - 1] == 'k') { u *= 1000.0; }
                if(U[U.length() - 1] == 'M') { u *= 1000000.0; }
            }
        }
        if(I != "")
        {
            if(I[I.length() - 1] >= '0' && I[I.length() - 1] <= '9') { i = atof(I.c_str()); }
            else
            {
                i = atof(I.substr(0, I.length() - 1).c_str());
                if(I[I.length() - 1] == 'm') { i /= 1000.0; }
                if(I[I.length() - 1] == 'k') { i *= 1000.0; }
                if(I[I.length() - 1] == 'M') { i *= 1000000.0; }
            }
        }
        if(P != "")
        {
            if(P[P.length() - 1] >= '0' && P[P.length() - 1] <= '9') { p = atof(P.c_str()); }
            else
            {
                p = atof(P.substr(0, P.length() - 1).c_str());
                if(P[P.length() - 1] == 'm') { p /= 1000.0; }
                if(P[P.length() - 1] == 'k') { p *= 1000.0; }
                if(P[P.length() - 1] == 'M') { p *= 1000000.0; }
            }
        }
        if(U != "" && I != "")
        { cout << "P=" << fixed << setprecision(2) << u * i << "W" << endl; }
        if(U != "" && P != "")
        { cout << "I=" << fixed << setprecision(2) << p / u << "A" << endl; }
        if(I != "" && P != "")
        { cout << "U=" << fixed << setprecision(2) << p / i << "V" << endl; }
        cout << endl;
    }
    return 0;
}
```

## UVa 409

只用运用 `string` 的 `find` 函数就可以解决了。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 32;
 
int pCnt[MAX];
string pKeyword[MAX], pExcuse[MAX], pTmp[MAX];
 
int main()
{
    int N, K, nCase = 0;
    while(cin >> N >> K)
    {
        cout << "Excuse Set #" << ++nCase << endl;
        memset(pCnt, 0, sizeof(pCnt));
        for(int i = 1; i <= N; i++)
        {
            cin >> pKeyword[i];
            pKeyword[i] += ' ';
        }
        cin.ignore();
        for(int i = 1; i <= K; i++)
        {
            getline(cin, pTmp[i]);
            pExcuse[i] = pTmp[i];
            for(int j = 0; j < pExcuse[i].length(); j++)
            {
                if(pExcuse[i][j] >= 'A' && pExcuse[i][j] <= 'Z')
                { pExcuse[i][j] += 32; }
                if(!(pExcuse[i][j] >= 'a' && pExcuse[i][j] <= 'z'))
                { pExcuse[i][j] = ' '; }
            }
            pExcuse[i] += ' ';
        }
        for(int i = 1; i <= K; i++)
        {
            for(int j = 1; j <= N; j++)
            {
                int nPos = 0;
                while((nPos = pExcuse[i].find(pKeyword[j], nPos)) && nPos != string::npos)
                { pCnt[i]++; nPos += pKeyword[j].length() + 1; }
            }
        }
        int nMax = 0;
        for(int i = 1; i <= K; i++)
        { nMax = max(nMax, pCnt[i]); }
        for(int i = 1; i <= K;i ++)
        {
            if(pCnt[i] == nMax) { cout << pTmp[i] << endl; }
        }
        cout << endl;
    }
    return 0;
}
```

## UVa 10878

一看就知道和二进制有关系，翻译过来果然如此（忽略字符 `.`）。解法中用了秦九韶算法来进制转换。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
    int nCnt = 0;
    string x;
    while(getline(cin, x))
    {
        int nTmp = 0;
        if(x == "___________") { nCnt++; }
        if(nCnt == 2) { break; }
        if(x != "___________")
        {
            x = x.substr(1, x.length() - 2);
            for(int i = 0; i < x.length(); i++)
            {
                if(x[i] != '.') { nTmp *= 2; }
                if(x[i] == 'o') { nTmp += 1; }
            }
            cout << (char)(nTmp);
        }
    }
    return 0;
}
```

## UVa 10815

C++ 的 STL 中的 `set` 可以水过。

```cpp
#include <iostream>
#include <string>
#include <set>
 
using namespace std;
 
const int MAX = 5120;
 
set<string> pSet;
 
bool IsAlpha(char x);
char ToLower(char x);
 
int main()
{
    string x;
    while(getline(cin, x))
    {
        for(int i = 0; i < x.length(); i++)
        {
            if(!IsAlpha(x[i]))
            { continue; }
            string strTmp;
            while(i < x.length() && IsAlpha(x[i]))
            { strTmp += ToLower(x[i++]); }
            pSet.insert(strTmp);
        }
    }
    for(set<string>::iterator it = pSet.begin(); it != pSet.end(); it++)
    { cout << *it << endl; }
    return 0;
}
 
bool IsAlpha(char x)
{ return x >= 'A' && x <= 'Z' || x >= 'a' && x <= 'z'; }
 
char ToLower(char x)
{
    if(x >= 'A' && x <= 'Z') { x += 32; }
    return x;
}
```

## UVa 644

一开始 TLE，还以为算法不行，后来发现是读入出了问题。

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 10240;
 
string x[MAX];
 
int main()
{
    int nCase = 0, nPos = 0;
    while(cin >> x[++nPos])
    {
        if(x[nPos] != "9") { continue; }
        else
        {
            nPos--;
            bool bFlag = true;
            for(int i = 1; i <= nPos; i++)
            {
                for(int j = 1; j <= nPos; j++)
                {
                    if(x[i].length() < x[j].length())
                    { if(x[i] == x[j].substr(0, x[i].length())) { bFlag = false; break; } }
                }
                if(!bFlag) { break; }
            }
            if(bFlag) { cout << "Set " << ++nCase << " is immediately decodable" << endl; }
            else { cout << "Set " << ++nCase << " is not immediately decodable" << endl; }
            nPos = 0;
        }
    }
}
```

## UVa 10115

自己写一个 `replace` 函数就可以 AC 了。

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 16;
 
string strRules[MAX], strReplace[MAX];
 
string& ReplaceAll(string& str, const string& strOld, const string& strNew);
 
int main()
{
    int N;
    while(cin >> N)
    {
        string x;
        if(N == 0) { break; }
        cin.ignore();
        for(int i = 1; i <= N; i++)
        {
            getline(cin, strRules[i]);
            getline(cin, strReplace[i]);
        }
        getline(cin, x);
        for(int i = 1; i <= N; i++)
        { x = ReplaceAll(x, strRules[i], strReplace[i]); }
        cout << x << endl;
    }
    return 0;
}
 
string& ReplaceAll(string& str, const string& strOld, const string& strNew)
{
    while(true)
    {
        string::size_type pos(0);
        if((pos = str.find(strOld)) != string::npos)
        { str.replace(pos, strOld.length(), strNew); }
        else { break; }
    }
    return str;
}
```

最后总结一个知识点，如何在 C++ 中自己写基于 `string` 的 `relpace` 函数。

在这里，`replace` 分为两种，一种是 `repalce_all`，一种是 `replace_all_distinct`。

```cpp
/* replace 12 with 21
    12212 -> 22211 */
string&   replace_all(string&   str,const   string&   old_value,const   string&   new_value)  
{  
    while(true)   {  
        string::size_type   pos(0);  
        if(   (pos=str.find(old_value))!=string::npos   )  
            str.replace(pos,old_value.length(),new_value);  
        else   break;  
    }  
    return   str;  
}  
 
/* replace 12 with 21
    12212 -> 21221 */
string&   replace_all_distinct(string&   str,const   string&   old_value,const   string&   new_value)  
{  
    for(string::size_type   pos(0);   pos!=string::npos;   pos+=new_value.length())   {  
        if(   (pos=str.find(old_value,pos))!=string::npos   )  
            str.replace(pos,old_value.length(),new_value);  
        else   break;  
    }  
    return   str;  
}
```

还有很深的感触就是 UVaOJ 上面关于 WA 和 PE 分的不是很清楚。多了空行算 WA，行内少了或多了空格算 PE。

一套字符串题目刷下来，感到非常吃力，被各种 WA 以及 PE。
