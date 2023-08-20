# SGU 114 - Telecasting station


## Description

Every city in Berland is situated on $Ox$ axis. The government of the country decided to build new telecasting station. After many experiments Berland scientists came to a conclusion that in any city citizens displeasure is equal to product of citizens amount in it by distance between city and TV-station. Find such point on $Ox$ axis for station so that sum of displeasures of all cities is minimal.

## Input

Input begins from line with integer positive number $N$ ($0<N<15000$) – amount of cities in Berland. Following $N$ pairs $(X, P)$ describes cities ($0<X, P<50000$), where $X$ is a coordinate of city and $P$ is an amount of citizens. All numbers separated by whitespace(s).

## Output

Write the best position for TV-station with accuracy $10^{-5}$.

## Sample Input

```
4
1 3
2 1
5 2
6 2
```

## Sample Output

```
3.00000
```

## Analysis

这道题目有几个地方需要注意：

* 最后精确到 $10^{-5}$ 的要求基本是多余的，只要在结果后面再输出“.00000”；
* 本题使用了 Special Judge，因此答案可能不唯一。

有了上面两点的认识，我们来考虑一般的解决方案。我们不妨考虑电视台建在城市中，很容易证明，这也是这个问题的一个解。

我们不妨把所有的城市列出来，比如样例输入中，一共有 8 个城市，我们把它们认为是不同的，并且列成一排：

$$(1, 1)\quad (1, 2)\quad (1, 3)\quad (2, 4)\quad (5, 5)\quad (5, 6)\quad (6, 7)\quad (6, 8)$$

其中第一个数字表示城市的位置，第二个数字表示第几个城市。很容易发现，我们需要求的是最中间的那个城市。

* 如果城市数目为奇数，那么我们所需要求的就是第 `S / 2 + 1` 个城市，其中 $S$ 表示城市总数；
* 如果城市数目为偶数，那么我们可以输出第 `S / 2` 个城市或第 `S / 2 + 1` 个城市。

为了方便起见，我们都取第 `S / 2 + 1` 个城市，这并不会对答案的这正确性产生影响。

## Solution

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
 
using namespace std;
 
struct City
{
    City(int _P = 0, int _M = 0)
    { P = _P; M = _M; }
 
    int P, M;
};
 
int cmp(City x, City y)
{ return x.P < y.P; }
 
vector<City> pCity;
 
int main()
{
    int N, P, M;
    while(cin >> N)
    {
        int nCnt = 0;
        pCity.clear();
        for(int i = 1; i <= N; i++)
        {
            cin >> P >> M;
            pCity.push_back(City(P, M));
            nCnt += M;
        }
        sort(pCity.begin(), pCity.end(), cmp);
        int nTmp = nCnt / 2 + 1;
        int nPos = 0;
        for(; nTmp > 0; nPos++)
        {
            if(nTmp - pCity[nPos].M > 0) { nTmp -= pCity[nPos].M; }
            else { break; }
        }
        cout << pCity[nPos].P << ".00000" << endl;
    }
    return 0;
}
```

这道题目主要是一开始说明的两点要注意一下，否则会 WA 很多次。
