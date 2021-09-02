# ACM-ICPC 寒假练习 04


断断续续的把排序和检索专题刷完了，感觉英语还是不够，题目太长以后看起来就会很吃力。

还有一点感触就是 STL 的广泛应用。学到了很多新东西。

当然，不能忍受的就是答案最后多输出一行空行，UVaOJ 会判 WA。

## UVaOJ 340

简单模拟题，一开始没有看懂题目。百度以后才明白的题意。朴素模拟以后即可得到答案。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 1024;
 
int pCode[MAX], pGuess[MAX], pVisited[MAX];
 
int main()
{
    int N, nCase = 0;
    while(cin >> N)
    {
        if(N == 0) { break; }
        memset(pCode, 0, sizeof(pCode));
        for(int i = 1; i <= N; i++)
        { cin >> pCode[i]; }
        cout << "Game " << ++nCase << ":" << endl;
        while(1)
        {
            int x = 0, y = 0, nCnt = 0;
            memset(pGuess, 0, sizeof(pGuess));
            memset(pVisited, 0, sizeof(pVisited));
            for(int i = 1; i <= N; i++)
            {
                cin >> pGuess[i];
                if(pGuess[i] == 0) { nCnt++; }
            }
            if(nCnt == N) { break; }
            for(int i = 1; i <= N; i++)
            {
                if(pCode[i] == pGuess[i])
                {
                    x++;
                    pVisited[i] = 2;
                }
            }
            for(int i = 1; i <= N; i++)
            {
                if(pVisited[i] == 2) { continue; }
                for(int j = 1; j <= N; j++)
                {
                    if(pVisited[j] != 0) { continue; }
                    if(pCode[i] == pGuess[j])
                    {
                        y++;
                        pVisited[j] = 1;
                        break;
                    }
                }
            }
            cout << "    (" << x << "," << y << ")" << endl;
        }
    }
    return 0;
}
```

## UVaOJ 10420

STL 中的 `set` 水过。

```cpp
#include <iostream>
#include <string>
#include <map>
 
using namespace std;
 
map<string, int> pMap;
 
int main()
{
    int N;
    while(cin >> N)
    {
        pMap.clear();
        string x, y;
        for(int i = 1; i <= N; i++)
        {
            cin >> x;
            getline(cin, y);
            pMap[x]++;
        }
        map<string, int>::iterator it;
        for(it = pMap.begin(); it != pMap.end(); it++)
        { cout << (*it).first << " " << (*it).second << endl; }
    }
    return 0;
}
```

## UVaOJ 10474

水题，一开始没看见“CASE”是大写的，WA 了好几次。

```cpp
#include <iostream>
#include <algorithm>
 
using namespace std;
 
const int MAX = 10240;
 
int pData[MAX];
 
int main()
{
    int nCase = 0;
    int N, Q, x;
    while(cin >> N >> Q)
    {
        if(N == 0 && Q == 0) { break; }
        for(int i = 1; i <= N; i++)
        { cin >> pData[i]; }
        cout << "CASE# " << ++nCase << ":" << endl;
        sort(pData + 1, pData + N + 1);
        for(int i = 1; i <= Q; i++)
        {
            cin >> x;
            bool bFlag = false;
            for(int j = 1; j <= N; j++)
            {
                if(pData[j] == x)
                { cout << x << " found at " << j << endl; bFlag = true; break; }
            }
            if(!bFlag) { cout << x << " not found" << endl; }
        }
    }
    return 0;
}
```

## UVaOJ 152

这道题目一开始也没有看懂题意，百度以后才明白的题意。

为了避免 `sqrt` 的误差，可以直接判断平方的大小关系。

```cpp
#include <iostream>
#include <iomanip>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
const int pTable[] = { 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 };
 
struct Point
{
    int x, y, z;
};
 
int pOut[MAX];
Point pData[MAX];
 
int Calc(int i, int j);
 
int main()
{
    int x, y, z, nCnt = 0;
    memset(pOut, 0, sizeof(pOut));
    while(cin >> x >> y >> z)
    {
        if(x == 0 && y == 0 && z == 0) { break; }
        pData[++nCnt] = {x, y, z};
    }
    for(int i = 1; i <= nCnt; i++)
    {
        int nMin = 2147483647;
        for(int j = 1; j <= nCnt; j++)
        {
            if(i == j) { continue; }
            int nTmp = Calc(i, j);
            if(nMin > nTmp) { nMin = nTmp; }
        }
        pOut[nMin]++;
    }
    for(int i = 1; i <= 10; i++)
    { cout << setw(4) << pOut[i]; }
    cout << endl;
    return 0;
}
 
int Calc(int i, int j)
{
    int x = pData[i].x - pData[j].x;
    int y = pData[i].y - pData[j].y;
    int z = pData[i].z - pData[j].z;
    int nTmp = x * x + y * y + z * z;
    for(int k = 1; k <= 10; k++)
    {
        if(nTmp < pTable[k]) { return k; }
    }
}
```

## UVaOJ 299

学过线性代数以后直接想到了逆序数。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int pData[MAX];
 
int main()
{
    int T, N;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> N;
        int nCnt = 0;
        memset(pData, 0, sizeof(pData));
        for(int j = 1; j <= N; j++)
        { cin >> pData[j]; }
        for(int j = 1; j <= N; j++)
        {
            for(int k = j + 1; k <= N; k++)
            {
                if(pData[j] > pData[k]) { nCnt++; }
            }
        }
        cout << "Optimal train swapping takes " << nCnt << " swaps." << endl;
    }
    return 0;
}
```

## UVaOJ 120

简单模拟题，也是百度以后才知道的题意。

如果当前区间最大的不是第一个，那么先将它翻转到第一个，然后在翻转到当前区间的最后一个。

如果它恰好是第一个，直接翻转到最后一个。

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <deque>
#include <algorithm>
 
using namespace std;
 
deque<int> Q;
 
int main()
{
    int nTmp;
    string x;
    while(getline(cin, x))
    {
        cout << x << endl;
        istringstream iss(x);
        Q.clear();
        while(iss >> nTmp) { Q.push_front(nTmp); }
        for(deque<int>::iterator it = Q.begin(); it != Q.end(); it++)
        {
            deque<int>::iterator iMax = max_element(it, Q.end());
            if(iMax != it)
            {
                if(iMax != Q.end() - 1)
                {
                    reverse(iMax, Q.end());
                    cout << iMax - Q.begin() + 1 << " ";
                }
                reverse(it, Q.end());
                cout << it - Q.begin() + 1 << " ";
            }
        }
        cout << "0" << endl;
    }
    return 0;
}
```

## UVaOJ 156

STL 中的 `map` 水过。但是对于 `map` 内部的自动排序还不是非常的理解。

```cpp
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
 
using namespace std;
 
const int MAX = 10240;
 
map<string, int> pMap;
vector<string> pVec;
string pData[MAX], pSorted[MAX];
 
string ToLower(string x);
 
int main()
{
    int nCnt = 0;
    string x;
    while(cin >> x)
    {
        if(x == "#") { break; }
        nCnt++;
        pData[nCnt] = x;
        pSorted[nCnt] = ToLower(x);
        sort(pSorted[nCnt].begin(), pSorted[nCnt].end());
        pMap[pSorted[nCnt]]++;
    }
    for(map<string, int>::iterator it = pMap.begin(); it != pMap.end(); it++)
    {
        if((*it).second != 1) { continue; }
        int nPos;
        for(nPos = 1; nPos <= nCnt; nPos++)
        {
            if(pSorted[nPos] == (*it).first) { break; }
        }
        pVec.push_back(pData[nPos]);
    }
    sort(pVec.begin(), pVec.end());
    for(int i = 0; i < pVec.size(); i++)
    { cout << pVec[i] << endl; }
}
 
string ToLower(string x)
{
    for(int i = 0; i < x.length(); i++)
    {
        if(x[i] >= 'A' && x[i] <= 'Z') { x[i] += 32; }
    }
    return x;
}
```

## UVaOJ 400

一开始没有注意到除数为 0 的情况，导致 RE 了好多次。

```cpp
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;
 
const int MAX = 60;
 
vector<string> pVec;
 
int main()
{
    int N;
    string x;
    while(cin >> N)
    {
        int nMax = 0;
        pVec.clear();
        for(int i = 1; i <= N; i++)
        {
            cin >> x;
            pVec.push_back(x);
            nMax = max(nMax, (int)x.length());
        }
        int nCnt = MAX / (nMax + 2);
        if(nCnt == 0) { nCnt = 1; }
        int nRow = N / nCnt + (N % nCnt != 0);
        sort(pVec.begin(), pVec.end());
        cout << "------------------------------------------------------------" << endl;
        for(int i = 1; i <= nRow; i++)
        {
            for(int j = 1; j <= nCnt; j++)
            {
                int nPos = (j - 1) * nRow + i - 1;
                if(nPos >= N) { continue; }
                cout.setf(ios::left);
                if(nPos >= (nCnt - 1) * nRow)   
                { cout << setw(nMax) << pVec[nPos]; }
                else { cout << setw(nMax + 2) << pVec[nPos]; }
                 
            }
            cout << endl;
        }
    }
    return 0;
}
```

## UVaOJ 123

这道题目要求按照原来的顺序，而 `sort` 是非稳定排序，在这上面 WA 了好几次。

```cpp
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <sstream>
 
using namespace std;
 
const int MAX = 10240;
 
int cmp(pair<string, pair<string, int> > x, pair<string, pair<string, int> > y)
{
    if(x.first != y.first) { return x.first < y.first; }
    else { return x.second.second < y.second.second; }
}
 
string pData[MAX];
set<string> pSet;
vector<pair<string, pair<string, int> > > pVec;
 
string ToLower(string x);
string ToUpper(string x);
 
int main()
{
    int nPos = 0;
    string x;
    while(cin >> x)
    {
        if(x == "::") { break; }
        pSet.insert(x);
    }
    cin.ignore();
    while(getline(cin, x))
    {
        string strLow = ToLower(x);
        istringstream iss(strLow);
        int nCnt = 0;
        while(iss >> x)
        {
            if(x != "") { pData[++nCnt] = x; }
        }
        for(int i = 1; i <= nCnt; i++)
        {
            if(!pSet.count(pData[i]))
            {
                string strTmp = "";
                for(int j = 1; j <= nCnt; j++)
                {
                    if(j != i) { strTmp += pData[j] + " "; }
                    else { strTmp += ToUpper(pData[j]) + " "; }
                }
                strTmp = strTmp.substr(0, strTmp.length() - 1);
                pVec.push_back(make_pair(ToUpper(pData[i]), make_pair(strTmp, ++nPos)));
            }
        }
    }
    sort(pVec.begin(), pVec.end(), cmp);
    for(int i = 0; i < pVec.size(); i++)
    { cout << pVec[i].second.first << endl; }
    return 0;
}
 
string ToLower(string x)
{
    for(int i = 0; i < x.length(); i++)
    {
        if(x[i] >= 'A' && x[i] <= 'Z')
        { x[i] += 32; }
    }
    return x;
}
 
string ToUpper(string x)
{
    for(int i = 0; i < x.length(); i++)
    {
        if(x[i] >= 'a' && x[i] <= 'z')
        { x[i] -= 32; }
    }
    return x;
}
```

## UVaOJ 10194

水题，直接模拟即可。注意写好排序的 `cmp` 函数即可。

```cpp
#include <iostream>
#include <string>
#include <algorithm>
 
using namespace std;
 
const int MAX = 1024;
 
struct Player
{
    Player()
    { Clear(); }
     
    void Clear()
    {
        strName = "";
        nPoint = nGame = 0;
        nWin = nTie = nLose = 0;
        nDiff = nScored = nAgainst = 0;
    }
     
    string strName;
    string strTmp;
    int nPoint, nGame;
    int nWin, nTie, nLose;
    int nDiff, nScored, nAgainst;
};
 
Player pData[MAX];
 
int GetPos(string x);
int Trans(string x);
string ToLower(string x);
 
int cmp(Player x, Player y)
{
    if(x.nPoint != y.nPoint) { return x.nPoint > y.nPoint; }
    if(x.nWin != y.nWin) { return x.nWin > y.nWin; }
    if(x.nDiff != y.nDiff) { return x.nDiff > y.nDiff; }
    if(x.nScored != y.nScored) { return x.nScored > y.nScored; }
    if(x.nGame != y.nGame) { return x.nGame < y.nGame; }
    return ToLower(x.strName) < ToLower(y.strName);
}
 
int main()
{
    int N, nPlayer, nGame;
    string x;
    cin >> N;
    cin.ignore();
    for(int i = 1; i <= N; i++)
    {
        getline(cin, x);
        cout << x << endl;
        int nCnt = 0;
        cin >> nPlayer;
        cin.ignore();
        for(int j = 1; j <= nPlayer; j++)
        {
            getline(cin, x);
            pData[++nCnt].Clear();
            pData[nCnt].strName = x;
            pData[nCnt].strTmp = ToLower(x);
        }
        cin >> nGame;
        cin.ignore();
        for(int j = 1; j <= nGame; j++)
        {
            getline(cin, x);
            int nLeft = x.find_first_of('#'), nRight = x.find_last_of('#'), nMid = x.find('@');
            string strLeft = x.substr(0, nLeft);
            string strRight = x.substr(nRight + 1, x.length() - nRight - 1);
            string strLeftPoint = x.substr(nLeft + 1, nMid - nLeft - 1);
            string strRightPoint = x.substr(nMid + 1, nRight - nMid - 1);
            int nLeftPos = GetPos(strLeft), nRightPos = GetPos(strRight);
            int nLeftPoint = Trans(strLeftPoint), nRightPoint = Trans(strRightPoint);
            pData[nLeftPos].nGame++; pData[nRightPos].nGame++;
            pData[nLeftPos].nScored += nLeftPoint; pData[nRightPos].nScored += nRightPoint;
            pData[nLeftPos].nAgainst += nRightPoint; pData[nRightPos].nAgainst += nLeftPoint;
            if(nLeftPoint > nRightPoint) { pData[nLeftPos].nWin++; pData[nRightPos].nLose++; }
            else if(nLeftPoint < nRightPoint) { pData[nLeftPos].nLose++; pData[nRightPos].nWin++; }
            else { pData[nLeftPos].nTie++; pData[nRightPos].nTie++; }
        }
        for(int i = 1; i <= nPlayer; i++)
        {
            pData[i].nPoint = pData[i].nWin * 3 + pData[i].nTie;
            pData[i].nDiff = pData[i].nScored - pData[i].nAgainst;
        }
        sort(pData + 1, pData + nPlayer + 1, cmp);
        for(int i = 1; i <= nPlayer; i++)
        {
            cout << i << ") " << pData[i].strName
                << " " << pData[i].nPoint << "p, "
                << pData[i].nGame << "g ("
                << pData[i].nWin << "-"
                << pData[i].nTie << "-"
                << pData[i].nLose << "), "
                << pData[i].nDiff << "gd ("
                << pData[i].nScored << "-"
                << pData[i].nAgainst << ")"
                << endl;
        }
        if(i != N) { cout << endl; }
    }
    return 0;
}
 
int GetPos(string x)
{
    for(int nPos = 1; nPos < MAX; nPos++)
    {
        if(pData[nPos].strTmp == ToLower(x))
        { return nPos; }
    }
}
 
int Trans(string x)
{
    int nRet = 0;
    for(int i = 0; i < x.length(); i++)
    {
        nRet *= 10;
        nRet += x[i] - '0';
    }
    return nRet;
}
 
string ToLower(string x)
{
    for(int i = 0; i <x.length(); i++)
    {
        if(x[i] >= 'A' && x[i] <= 'Z')
        { x[i] += 32; }
    }
    return x;
}
```

## UVaOJ 755
直接 `map` 水过。多输出了一行空行，导致 WA 了一次。

```cpp
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
 
using namespace std;
 
const char pTable[] = {
    '2', '2', '2', '3', '3', '3',
    '4', '4', '4', '5', '5', '5',
    '6', '6', '6', '7', '*', '7',
    '7', '8', '8', '8', '9', '9',
    '9', '*' };
     
int cmp(pair<string, int> x, pair<string, int> y)
{ return x.first < y.first; }
 
vector<pair<string, int> > pVec;
map<string, int> pMap;
 
int main()
{
    int T, N;
    string x;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        pVec.clear();
        pMap.clear();
        cin >> N;
        cin.ignore();
        for(int j = 1; j <= N; j++)
        {
            getline(cin, x);
            string strTmp = "";
            for(int k = 0; k < x.length(); k++)
            {
                if(x[k] >= '0' && x[k] <= '9') { strTmp += x[k]; }
                if(x[k] >= 'A' && x[k] <= 'Z') { strTmp += pTable[x[k] - 'A']; }
            }
            while(strTmp.length() != 7) { strTmp = '0' + strTmp; }
            pMap[strTmp]++;
        }
        for(map<string, int>::iterator it = pMap.begin(); it != pMap.end(); it++)
        {
            if((*it).second > 1) { pVec.push_back(*it); }
        }
        if(pVec.size() == 0) { cout << "No duplicates." << endl; }
        else
        {
            sort(pVec.begin(), pVec.end(), cmp);
            for(int j = 0; j < pVec.size(); j++)
            {
                cout << pVec[j].first.substr(0, 3) << "-"
                    << pVec[j].first.substr(3, 4) << " "
                    << pVec[j].second << endl;
            }
        }
        if(i != T) { cout << endl; }
    }
    return 0;
}
```

## UVaOJ 10785

类似归并的思想。一开始打错表了，WA 了一次。

```cpp
#include <iostream>
#include <string>
#include <algorithm>
 
using namespace std;
 
const char pOdd[] = { 'A', 'U', 'E', 'O', 'I' };
const char pEven[] = {
    'J', 'S', 'B', 'K', 'T',
    'C', 'L', 'D', 'M', 'V',
    'N', 'W', 'F', 'X', 'G',
    'P', 'Y', 'H', 'Q', 'Z',
    'R' };
 
string Solve(int x);
 
int main()
{
    int T, N;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> N;
        cout << "Case " << i << ": "
             << Solve(N) << endl;
    }
    return 0;
}
 
string Solve(int x)
{
    string strRet = "";
    string strOdd = "";
    string strEven = "";
    int nOdd = (x + 1) / 2;
    int nEven = x / 2;
    int nOddCnt = nOdd / 21 + (nOdd % 21 != 0);
    int nEvenCnt = nEven / 5 + (nEven % 5 != 0);
    for(int i = 1; i <= nOddCnt; i++)
    {
        for(int j = 1; j <= 21; j++)
        { strOdd += pOdd[i - 1]; }
    }
    for(int i = 1; i <= nEvenCnt; i++)
    {
        for(int j = 1; j <= 5; j++)
        { strEven += pEven[i - 1]; }
    }
    strOdd = strOdd.substr(0, nOdd);
    strEven = strEven.substr(0, nEven);
    sort(strOdd.begin(), strOdd.end());
    sort(strEven.begin(), strEven.end());
    int nOddPos = 0, nEvenPos = 0;
    for(int i = 1; i <= x; i++)
    {
        if(i & 1) { strRet += strOdd[nOddPos++]; }
        else { strRet += strEven[nEvenPos++]; }
    }
    return strRet;
     
}
```

这一组题目做下来，感觉英语还是要提升，有时候题目一长，干扰信息一多，读起来就感觉很有难度了。
