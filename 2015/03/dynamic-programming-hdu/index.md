# Dynamic Programming - HDU


## HDU 2955

这是一道概率 DP，我第一次的想法是把概率 $P$ 乘以 100，变成一个背包然后做 0/1 背包，后来发现这样做是错误的。

原因：概率应该是相乘，而不是相加。

后来看了题解想到了另外一种方法，使用逃脱概率来计算，用 $f[j]$ 表示偷走 $j$ 价值后逃脱的概率。易知，多次逃脱概率为每次逃脱概率相乘。这里不使用被逮捕的概率是因为被逮捕的情况比较复杂（例如偷第一件物品不被逮捕，偷第二件物品被逮捕，被逮捕的概率应该为头第一件物品不被逮捕的概率乘以偷第二件物品不被逮捕的概率。），而当我们转而考虑它的对立事件——逃脱时，问题就会变得容易了，因为逃脱的概率永远是相乘的。

更为严格的说法是这样的：设被第 $i$ 个银行逮捕的事件为 $P_i$，那么 $1-\sum{P_i}$ 就是至少被一个银行逮捕的概率，也就是我们所需要求的被逮捕的概率。通过这样的数学上的说理，我们可以证明这一算法是正确的。

由于要计算逃脱概率，我们可以在读入的时候就把可能被逮捕的概率 $P$ 变成可能逃脱的概率 $1 - P$。这样，状态转移方程为：$$ f[j] = \max{\left\\{f[j - \mathrm{pValue}[i]] \times \mathrm{pCost}[i], f[j]\right\\}}$$  其中 $\mathrm{pValue}[i]$ 表示第 $i$ 个银行的价值，$\mathrm{pCost}[i]$ 表示偷第 $i$ 个银行逃脱的概率。

这时候，我们还需要考虑一个转移条件，如果 $f[j - \mathrm{pValue}[i]]$ 没有被更新过，那么是不能转移过来的。因为暂时没有一个状态可以偷到 $j - \mathrm{pValue}[i]$ 价值的物品。

接下来，我们要考虑一下初始条件，很显然 $f[0] = 1$，因为不偷任何东西，就不会被逮捕，逃脱的概率就为 1。其余 $f[j] = -1$，其中 $j \neq 0$，表示暂时没有一个状态可以偷到 $j$ 价值的物品。

最后扫一遍 $f[j]$，满足 $1 - f[j] \leq P$ 的最大下标 $j$ 为满足题设条件的答案。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int pValue[MAX];
double pCost[MAX], f[MAX];
 
int main()
{
    int T, M, V;
    double P;
    cin >> T;
    for(int k = 1; k <= T; k++)
    {
        f[0] = 1; V = 0;
        for(int i = 1; i < MAX; i++)
        { f[i] = -1; }
        cin >> P >> M;
        for(int i = 1; i <= M; i++)
        {
            cin >> pValue[i] >> pCost[i];
            pCost[i] = 1 - pCost[i];
            V += pValue[i];
        }
        for(int i = 1; i <= M; i++)
        {
            for(int j = V; j >= pValue[i]; j--)
            {
                if(f[j - pValue[i]] != -1)
                { f[j] = max(f[j - pValue[i]] * pCost[i], f[j]); }
            }
        }
        int ans = 0;
        for(int i = 0; i <= V; i++)
        {
            if(1 - f[i] <= P)
            { ans = i; }
        }
        cout << ans << endl;
    }
    return 0;
}
```

接触的第一道概率DP，发现DP非常的灵活，自己还有很多东西要学。 @ **2015年3月14日**

## HDU 1864

这是一道较为典型的 0/1 背包，但是物品的价值和费用都需要自己处理出来。需要注意一下只能报销 A、B、C 类的发票。只要有一个条件不成立，就不报销该发票。

输入两位小数的时候，把它乘以 100，做 0/1 背包就可以了，状态转移方程为：$$f[j] = \max{\left\\{f[j - \mathrm{pValue}[i]] + \mathrm{pCost}[i], f[j]\right\\}}$$ 数据方面可能输入的时候没有给出小数部分，比如直接输入 100，而不是 100.00。但是题目中没有给出报销限额的数据范围，开到 3000000 就可以了。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
 
using namespace std;
 
const int MAX = 3840000;
 
int pHash[32];
int f[MAX], pValue[MAX], pCost[MAX];
 
int main()
{
    int N, M, V, nCnt;
    string strTmp;
    double Q;
    while(cin >> Q >> N && N)
    {
        V = Q * 100; nCnt = 0;
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= N; i++)
        {
            int nSum = 0;
            bool bFlag = true;
            cin >> M;
            memset(pHash, 0, sizeof(pHash));
            for(int j = 1; j <= M; j++)
            {
                cin >> strTmp;
                pHash[strTmp[0] - 'A'] += atof(strTmp.substr(2, strTmp.length() - 2).c_str()) * 100;
            }
            for(int j = 0; j < 32; j++)
            {
                if(j >= 3 && pHash[j]) { bFlag = false; }
                nSum += pHash[j];
                if(pHash[j] > 60000) { bFlag = false;}
            }
            if(nSum > 100000) { bFlag = false; }
            if(bFlag)
            {
                nCnt++;
                pValue[nCnt] = pCost[nCnt] = nSum; 
            }
        }
        for(int i = 1; i <= nCnt; i++)
        {
            for(int j = V; j >= pCost[i]; j--)
            { f[j] = max(f[j - pCost[i]] + pValue[i], f[j]); }
        }
        int ans = 0;
        for(int i = 0; i <= V; i++)
        { ans = max(ans, f[i]); }
        cout << ans / 100 << ".";
        if(ans % 100 < 10 ) { cout << "0"; }
        cout << ans % 100 << endl;
    }
    return 0;
}
```

这道题目第一次 Hash 表的范围为 32，访问到了 MAX，所以导致了 Runtime Error。 @ **2015年3月14日**

## HDU 1231

这道题目有一种贪心的做法，扫一遍 $\mathrm{pData[i]}$ 求和（`Sum += pData[i]`），如果遇到当前和 $\mathrm{Sum}$ 小于 0 的时候，就更新答案，并且把当前累加的和置为当前遍历到的数字 $\mathrm{pData}[i]$。

还会有一种动态规划的方法：$$f[i] = \max{\left\\{f[i - 1] + \mathrm{pData}[i], \mathrm{pData}[i]\right\\}}$$ 每次更新以后都要更新答案。需要注意，如果最后最大的和还是负数的话，则输出 0 以及数据的首尾两个元素。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int l, r, ans, al, ar;
int pData[MAX], f[MAX];
 
int main()
{
    ios::sync_with_stdio(false);
    int K;
    while(cin >> K)
    {
        if(K == 0) { break; }
        for(int i = 1; i <= K; i++)
        { cin >> pData[i]; }
        l = r = al = ar = 1; ans = pData[1];
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= K; i++)
        {
            if(f[i - 1] + pData[i] > pData[i])
            { f[i] = f[i - 1] + pData[i]; r = i; }
            else
            { f[i] = pData[i]; l = r = i; }
            if(f[i] > ans) { ans = f[i]; al = l; ar = r; }
        }
        if(ans >= 0)
        { cout << ans << " " << pData[al] << " " << pData[ar] << endl; }
        else { cout << 0 << " " << pData[1] << " " << pData[K] << endl; }
    }
    return 0;
}
```

以前处理这类题目的时候都是使用贪心的方法，今天看到动态规划的方法，使得对于以前贪心的方法有了更深刻的理解。这两种方法的本质思想是相同的。 @ **2015年3月14日**

## HDU 1003

这道题目上面一道题目是差不多的。状态转移方程为：$$f[i] = \max{\left\\{f[i - 1] + \mathrm{pData}[i], \mathrm{pData}[i]\right\\}}$$ 唯一的一个区别是状态转移的时候并不能严格大于，因为它要找到第一个，因此左端点一定是越小越好。

如果使用严格大于的话，假设前面有 $X$ 个数加起来等于 0，它并不影响最终和的答案，但是却使得求出的答案不是第一个了。

其余的代码和上面一道题目没有太大的区别，注意一下输出格式。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 102400;
 
int l, r, ans, al, ar;
int pData[MAX], f[MAX];
 
int main()
{
    ios::sync_with_stdio(false);
    int K, N;
    while(cin >> K)
    {
        for(int i = 1; i <= K; i++)
        {
            cin >> N;
            for(int j = 1; j <= N; j++)
            { cin >> pData[j]; }
            l = r = al = ar = 1; ans = pData[1];
            memset(f, 0, sizeof(f));
            for(int j = 1; j <= N; j++)
            {
                if(f[j - 1] + pData[j] >= pData[j])    // 此处为非严格大于
                { f[j] = f[j - 1] + pData[j]; r = j; }
                else
                { f[j] = pData[j]; l = r = j; }
                if(f[j] > ans) { ans = f[j]; al = l; ar = r; }
            }
            cout << "Case " << i << ":" << endl;
            cout << ans << " " << al << " " << ar << endl;
            if(i != K) { cout << endl; }
        }
    }
    return 0;
}
```

这到题目一开始是用贪心做的，今天重新用动态规划做了一下。 @ **2015年3月14日**

## HDU 1506

这道题目以前用单调栈做过，单调栈的思路如下：不断的将矩形入栈，当当前要加入的矩形的高度大于栈顶的矩形高度时，将栈顶的矩形出栈，与当前的矩形合成一个大的矩形，高度为较短的矩形的高度。然后把和合成的新的矩形加入栈顶，并且更新答案。这样扫一遍就好了。

下面介绍DP的思想：我们首先考虑这样一件事情，一段矩形的面积取决于矩形的个数以及最矮的矩形的高度。我们可以枚举每一个矩形，然后往左右两边枚举连续比它高的矩形的总个数 $N$，那么就更新答案。

下面就要考虑如何快速的求出左右两边连续比它高的矩形的总个数。

我们不妨考虑左边的情况，用 $\mathrm{pLeft}[i]$ 表示第 $i$ 个矩形左边连续比它高的矩形最左边的矩形的编号。那么如果我们有另外一个矩形 $j$，存在 $\mathrm{pData}[j] < \mathrm{pData}[i]$，我们就可以将 $\mathrm{pLeft}[j]$ 置为 $\mathrm{pLeft}[i]$，然后再往左迭代。需要注意的是，左右两边需要分开进行。因为从左往右只能保证 $\mathrm{pLeft}$ 数组被更新了，可以进行迭代，而 $\mathrm{pRight}$ 则还是类似之前的暴搜一样，复杂度很高，因此我们需要将左右两边分开迭代。

```cpp
#include <stdio.h>
 
const int MAX = 102400;
 
long long pData[MAX], pLeft[MAX], pRight[MAX];
 
long long max(long long x, long long y);
 
int main()
{
    int N;
    long long ans;
    while(scanf("%I64d", &N) != EOF && N)
    {
        ans = 0;
        for(int i = 1; i <= N; i++)
        {
            scanf("%I64d", &pData[i]);
            pLeft[i] = pRight[i] = i;
        }
        for(int i = 1; i <= N; i++)
        {
            int nCur = i - 1;
            while(nCur >= 1 && pData[i] <= pData[nCur])
            {
                pLeft[i] = pLeft[nCur];
                nCur = pLeft[nCur] - 1;
            }
        }
        for(int i = N; i >= 1; i--)
        {
            int nCur = i + 1;
            while(nCur <= N && pData[i] <= pData[nCur])
            {
                pRight[i] = pRight[nCur];
                nCur = pRight[nCur] + 1;
            }
        }
        for(int i = 1; i <= N; i++)
        { ans = max(ans, pData[i] * (pRight[i] - pLeft[i] + 1)); }
        printf("%I64d\n", ans);
    }
    return 0;
}
 
long long max(long long x, long long y)
{ return x > y ? x : y; }
```

这道题目没有严格的状态转移方程，只有一个状态转移的思想。 @ **2015年3月15日**

## HDU 1505

这道题目是上面一道题目的加强版，变成了一个二维的问题。我们可以这样转化。

枚举每一行，每一行中的每个点向上搜有 $X$ 个连续的 'F'，就表示这个点所表示的的矩形的高度为 $X$，然后每一行使用一次上一道题目的动态规划思想即可，复杂度$O\left(N^2 * \log{N}\right)$。

关键问题在于如何在最短的时间内构造出这样的一个数组 $\mathrm{pData}$，使得 $\mathrm{pData}[i][j]$ 表示从第 $i$ 行第 $j$ 个向上搜索有几个连续的 'F'。

我们可以考虑一个类似前缀和的思想，如果当前读入的地形为 'F'，那么 $\mathrm{pData}[i][j] = \mathrm{pData}[i - 1][j] + 1$，表示和上面组成一个更大的矩形；否则，$\mathrm{pData}[i][j] = 0$，表示不能和上面的组成更大的矩形。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 1024;
 
int pLeft[MAX], pRight[MAX];
int pMap[MAX][MAX], pData[MAX][MAX];
 
int main()
{
    char dwTmp;
    int T, M, N;
    cin >> T;
    while(T)
    {
        T--;
        int ans = 0;
        memset(pData, 0, sizeof(pData));
        cin >> M >> N;
        for(int i = 1; i <= M; i++)
        {
            for(int j = 1; j <= N; j++)
            {
                cin >> dwTmp;
                pMap[i][j] = (dwTmp == 'R' ? 1 : 0);
                if(!pMap[i][j]) { pData[i][j] = pData[i - 1][j] + 1; }
                else { pData[i][j] = 0; }
            }
        }
        for(int i = 1; i <= M; i++)
        {
            memset(pLeft, 0, sizeof(pLeft));
            memset(pRight, 0, sizeof(pRight));
            for(int j = 1; j <= N; j++)
            { pLeft[j] = pRight[j] = j; }
            for(int j = 1; j <= N; j++)
            {
                int nCur = j - 1;
                while(nCur >= 1 && pData[i][j] <= pData[i][nCur])
                {
                    pLeft[j] = pLeft[nCur];
                    nCur = pLeft[nCur] - 1;
                }
            }
            for(int j = N; j >= 1; j--)
            {
                int nCur = j + 1;
                while(nCur <= N && pData[i][j] <= pData[i][nCur])
                {
                    pRight[j] = pRight[nCur];
                    nCur = pRight[nCur] + 1;
                }
            }
            int nTmp = 0;
            for(int j = 1; j <= N; j++)
            { nTmp = max(nTmp, pData[i][j] * (pRight[j] - pLeft[j] + 1)); }
            ans = max(ans, nTmp);
        }
        cout << ans  * 3 << endl;
    }
    return 0;
}
```

这道题目需要一个转化的思想，把二维的地图转化为一维的情况，然后调用N遍处理一维问题的算法，就可以解决问题了。 @ **2015年3月15日**

## HDU 2602

简单的 0/1 背包问题，状态转移方程：$$f[j] = \max{\left\\{f[j - \mathrm{pCost}[i]] + \mathrm{pValue}[i], f[j]\right\\}}$$

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 1024;
 
int pCost[MAX], pValue[MAX], f[MAX];
 
int main()
{
    int T, N, V;
    cin >> T;
    while(T)
    {
        T--;
        memset(f, 0, sizeof(f));
        cin >> N >> V;
        for(int i = 1; i <= N; i++)
        { cin >> pValue[i]; }
        for(int i = 1; i <= N; i++)
        { cin >> pCost[i]; }
        for(int i = 1; i <= N; i++)
        {
            for(int j = V; j >= pCost[i]; j--)
            { f[j] = max(f[j - pCost[i]] + pValue[i], f[j]); }
        }
        int ans = 0;
        for(int i = 1; i <= V; i++)
        { ans = max(ans, f[i]); }
        cout << ans << endl;
    }
    return 0;
}
```

这道题目比较简单。 @ **2015年3月15日**

## HDU 1087

这道题目是求上升序列的最大和。用 $f[i]$ 表示以第 $i$ 个节点结尾可以达到的最大和，那讲最长上升序列改造一下即可，状态转移方程基本不变：$$f[i] = \max{\left\\{f[j]\right\\}} + \mathrm{pData}[i]$$ 其中 $1\leq j < i$。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 1024;
 
int pData[MAX], f[MAX], pSum[MAX];
 
int main()
{
    int N;
    while(cin >> N && N)
    {
        for(int i = 1; i <= N; i++)
        { cin >> pData[i]; }
        memset(f, 0, sizeof(f));
        f[1] = pData[1];
        for(int i = 2; i <= N; i++)
        {
            int nTmp = 0;
            for(int j = 1; j < i; j++)
            {
                if(pData[j] < pData[i])
                { nTmp = max(nTmp, f[j]); }
            }
            f[i] = nTmp + pData[i];
        }
        int ans = 0;
        for(int i = 1; i <= N; i++)
        { ans = max(ans, f[i]); }
        cout << ans << endl;
    }
    return 0;
}
```

这道题目也不难。 @ **2015年3月15日**

## HDU 2571

这是一道动态规划的题目，只不过转移的时候需要考虑的情况变多了。不但要考虑从点 $(i - 1, j)$，$(i, j - 1)$ 以及 $(i, j / k)$ 转移过来，其中 $k$ 为 $j$ 的约数。

需要注意的是，数据可能为负数，因此需要将初值置为 -2147483647，更新的时候需要注意初值是否改变，如果没有改变，说明没有状态能够转移过来，因此不需要操作（也就是加 0），否则就把该数值加上去，并且在加上原来地图上的数值。

还需要注意的时，转移的时候应该使用动态规划使用的数组，而不是地图上的数据。

最后，状态转移方程为：$$ f[i][j] = \max{\left\\{f[i - 1][j], f[i][j - 1], f[i][\frac{j}{k}]\right\\}} + \mathrm{pData}[i][j]$$ 其中 $f[i][j]$ 表示走到点 $(i, j)$ 能够获得的最大幸运值，同时 $k$ 是 $j$ 的约数。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 1024;
 
int pMap[MAX][MAX], f[MAX][MAX];
 
int main()
{
    int C, N, M;
    cin >> C;
    while(C)
    {
        C--;
        memset(f, 0, sizeof(f));
        cin >> N >> M;
        for(int i = 1; i <= N; i++)
        {
            for(int j = 1; j <= M; j++)
            { cin >> pMap[i][j]; }
        }
        for(int i = 1; i <= N; i++)
        {
            for(int j = 1; j <= M; j++)
            {
                int nTmp = -2147483647;
                if(i != 1) { nTmp = max(nTmp, f[i - 1][j]); }
                if(j != 1) { nTmp = max(nTmp, f[i][j - 1]); }
                for(int k = 2; k <= j; k++)
                {
                    if(j % k == 0) { nTmp = max(nTmp, f[i][j / k]); }
                }
                f[i][j] = (nTmp == -2147483647 ? 0 : nTmp) + pMap[i][j];
            }
        }
        cout << f[N][M] << endl;
    }
    return 0;
}
```

这道题目和典型的走迷宫差不多，只是状态转移的时候需要考虑更多的情况。还需要注意的是输入的数据有负数的情况。 @ **2015年3月15日**

## HDU 1069

这道题目也可以运用动态规划来求解，在此之前，我们需要处理几个小问题。

首先是对于题目中所讲的每个矩形有无穷个的处理方法。根据题目条件，每类方块可以转化成3类方块考虑以哪条边为高度），再考虑底面的边长可以互换，因此无数个一类方块可以转化为有限的 6 个方块来求解。

为了保证动态规划的正确性，我们需要对数据进行排序，可选的两种排序方法如下：

* 按照 $x$ 递增，然后按照 $y$ 递增，最后按照 $z$ 递增；
* 按照 $xy$ 递增。

我们用 $f[i]$ 表示以第 $i$ 个方块为最后一个方块所能到达的最大高度。那么状态转移方程为：$$f[i] = \max{\left\\{f[j]\right\\}} + \mathrm{pData}[i].z$$ 其中 $pData[i].z$ 表示第 $i$ 个方块的高度，且满足 $1\leq j < i$。

此外转移的条件为可以将第 $i$ 个方块放到第 $j$ 个方块上面，或者第 $i$ 个方块可以放到第 $j$ 个方块的下面，即 $$\begin{cases} \mathrm{pData}[i].x < \mathrm{pData}[j].x \\\ \mathrm{pData}[i].y < \mathrm{pData}[j].y\end{cases}\quad\mathrm{or}\quad\begin{cases}\mathrm{pData}[i].x > \mathrm{pData}[i].x\\\ \mathrm{pData}[i].y > \mathrm{pData}[i].y\end{cases}$$

最后的答案就是 $\max{\left\\{\mathrm{pData}[i].z\right\\}}$。

```cpp
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <vector>
 
using namespace std;
 
const int MAX = 512;
 
struct Block
{
    Block(int _x = 0, int _y = 0, int _z = 0)
    { x = _x; y = _y; z = _z; }
 
    int x, y, z;
};
 
int cmp(Block a, Block b)
{
    if(a.x != b.x) { return a.x < b.x; }
    else if(a.y != b.y) { return a.y < b.y; }
    else { return a.z < b.z; }
}
 
bool operator < (Block a, Block b)
{ return a.x < b.x && a.y < b.y; }
 
bool operator > (Block a, Block b)
{ return a.x > b.x && a.y > b.y; }
 
int f[MAX], ans;
vector<Block> pVec;
 
int main()
{
    int N, nCase = 0, x, y, z;
    while(cin >> N && N)
    {
        cout << "Case " << ++nCase << ": maximum height = ";
        ans = 0;
        pVec.clear();
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= N; i++)
        {
            cin >> x >> y >> z;
            pVec.push_back(Block(x, y, z));
            pVec.push_back(Block(x, z, y));
            pVec.push_back(Block(y, x, z));
            pVec.push_back(Block(y, z, x));
            pVec.push_back(Block(z, x, y));
            pVec.push_back(Block(z, y, x));
        }
        sort(pVec.begin(), pVec.end(), cmp);
        for(int i = 0; i < pVec.size(); i++)
        {
            int nTmp = 0;
            for(int j = 0; j < i; j++)
            {
                if(pVec[i] < pVec[j] || pVec[i] > pVec[j])
                { nTmp = max(nTmp, pVec[j].z); }
            }
            pVec[i].z += nTmp;
        }
        for(int i = 0; i < pVec.size(); i++)
        { ans = max(ans, pVec[i].z); }
        cout << ans << endl;
    }
    return 0;
}
```

这道题目也是用了一个动态规划的思想，把数据排序以后就可以是用动态规划了。只是要注意可以放在上面也可以放在下面。还有就是把无穷个方块转化为 6 个方块，使得问题得到简化。 @ **2015年3月15日**

## HDU 1171

将每种物品都变成 $M$ 个体积为 $V$ 的物品，然后进行一遍 0/1 背包。

我们用 $f[j]$ 表示装体积为 $V$ 的物品是否可行（可行为 1，不可行为 0）。初始化时，对于每种物品均有 $f[V] = 0$;

状态转移方程为：$$f[j] = 1 \quad\mathrm{iff.}~~ f[j - \mathrm{pCost}[i]] = 1$$

最后我们只要计算小于等于 $V / 2$ 的情况下最多能够装多少体积的物品，记作 $\mathrm{ans}$。那么答案就是 $V - \mathrm{ans}$ 以及 $\mathrm{ans}$。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 1024000;
 
int V, C;
int pCost[MAX], f[MAX];
 
int main()
{
    int N, x, y;
    while(cin >> N)
    {
        if(N < 0) { break; }
        V = 0; C = 0;
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= N; i++)
        {
            cin >> x >> y;
            for(int j = 1; j <= y; j++)
            { pCost[++C] = x; V += x; f[x] = 1; }
        }
        for(int i = 1; i <= C; i++)
        {
            for(int j = V; j >= pCost[i]; j--)
            {
                if(f[j - pCost[i]] == 1) { f[j] = 1; }
            }
        }
        int ans = 0;
        for(int i = 1; i <= V / 2; i++)
        {
            if(f[i]) { ans = i; }
        }
        cout << V - ans << " " << ans << endl;
    }
    return 0;
}
```

这道题目主要考察一个动态规划的思想，通过状态的转移来求解一共能够装多少体积的物品。 @ **2015年3月23日**

## HDU 2084

数字三角形。状态转移方程为：$$f[i][j] += \max{\left\\{f[i + 1][j], f[i + 1][j + 1]\right\\}}$$

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 1024000;
 
int V, C;
int pCost[MAX], f[MAX];
 
int main()
{
    int N, x, y;
    while(cin >> N)
    {
        if(N < 0) { break; }
        V = 0; C = 0;
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= N; i++)
        {
            cin >> x >> y;
            for(int j = 1; j <= y; j++)
            { pCost[++C] = x; V += x; f[x] = 1; }
        }
        for(int i = 1; i <= C; i++)
        {
            for(int j = V; j >= pCost[i]; j--)
            {
                if(f[j - pCost[i]] == 1) { f[j] = 1; }
            }
        }
        int ans = 0;
        for(int i = 1; i <= V / 2; i++)
        {
            if(f[i]) { ans = i; }
        }
        cout << V - ans << " " << ans << endl;
    }
    return 0;
}
```

最为经典的动态规划题目。 @ **2015年3月23日**

## HDU 1176

我们用 $f[i][j]$ 来表示第 $i$ 时间在第 $j$ 个位置上能够接到的馅饼总数。

那么状态转移方程为：$$f[i][j] += \max{\left\\{f[i + 1][j - 1], f[i + 1][j], f[i + 1][j + 1]\right\\}}$$

这里采用倒推法，因为最后我们一开始的起始位置在 5。因此只需要输出 $f[0][5]$ 即可。

当然，这里还需要处理一下边界 0 和 10 的情况，具体表现为：$$\begin{cases} f[i][0] = f[i][0] + \max{\left\\{f[i + 1][0], f[i + 1][1]\right\\}}\\\ f[i][10] = f[i][10] + \max{\left\\{f[i + 1][9], f[i + 1][10]\right\\}}\end{cases}$$

读入数据的时候，我们可以直接置 `f[T][X]++`，其中 $T$ 为时间点，$X$ 为坐标。

最后，最大的时间点 $T$，我们从 $T-1$ 遍历到0。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 102400;
 
int f[MAX][16];
 
int max(int x, int y);
int max(int x, int y, int z);
 
int main()
{
    ios::sync_with_stdio(false);
    int N, X, T, nCnt = 0;
    while(cin >> N && N)
    {
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= N; i++)
        {
            cin >> X >> T;
            f[T][X]++;
            nCnt = max(nCnt, T);
        }
        for(int i = nCnt - 1; i >= 0; i--)
        {
            f[i][0] += max(f[i + 1][0], f[i + 1][1]);
            for(int j = 1; j < 10; j++)
            { f[i][j] += max(f[i + 1][j - 1], f[i + 1][j], f[i + 1][j + 1]); }
            f[i][10] += max(f[i + 1][9], f[i + 1][10]);
        }
        cout << f[0][5] << endl;
    }
    return 0;
}
 
int max(int x, int y)
{ return x > y ? x : y; }
 
int max(int x, int y, int z)
{ return max(x, max(y, z)); }
```

这道题目也是考虑状态的转移。 @ **2015年3月23日**

## HDU 1203

这道题目和一开始做到的 HDU 2955 是差不多的题目，也是一道概率 DP。同样我们考虑它的反面，用 $f[j]$ 表示花费 $j$ 万元被所有 offer 拒绝的最小概率，也就对应着至少被一个 offer 接受的最大概率。

与之不同的是，我们在这里不需要考虑转移的条件，直接置所有的 $f[j] = 1$。而状态转移方程则为：$$f[j] = \min{\left\\{f[j - \mathrm{pCost}[i]] \times \mathrm{pValue}[i], f[j]\right\\}}$$ 最后输出的时候注意一下格式即可。

```cpp
#include <iostream>
#include <iomanip>
 
using namespace std;
 
const int MAX = 10240;
 
int pCost[MAX];
double pValue[MAX], f[MAX];
 
int main()
{
    int N, M;
    while(cin >> N >> M)
    {
        if(N == 0 && M == 0) { break; }
        for(int i = 1; i <= M; i++)
        {
            cin >> pCost[i] >> pValue[i];
            pValue[i] = 1 - pValue[i];
        }
        for(int i = 0; i <= N; i++)
        { f[i] = 1; }
        for(int i = 1; i <= M; i++)
        {
            for(int j = N; j >= pCost[i]; j--)
            {
                f[j] = min(f[j - pCost[i]] * pValue[i], f[j]);
            }
        }
        cout << fixed << setprecision(1) << (1 - f[N]) * 100 << "%" << endl;
    }
    return 0;
}
```

又是一道概率 DP。 @ **2015年3月23日**

## HDU 2159

这是一个二维完全背包，一个装杀怪数目，一个装忍耐值。

我们使用 $f[j][k]$ 表示杀了 $j$ 个怪兽，使用了 $k$ 个忍耐值，能够获得的最大经验。

那么状态转移方程为：$$f[j][k] = \max{\left\\{f[j - 1][k - \mathrm{pBare}[i]] + \mathrm{pExp}[i], f[j][k]\right\\}}$$

最后，若 $f[S][M] < N$，则无解。否则我们需要求解能够升级的情况下所使用的最少的忍耐值 `nTmp`，输出 `M - nTmp` 即可。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 128;
 
int pExp[MAX], pBare[MAX];
int f[MAX][MAX];
 
int main()
{
    int N, M, K, S;
    while(cin >> N >> M >> K >> S)
    {
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= K; i++)
        { cin >> pExp[i] >> pBare[i]; }
        for(int i = 1; i <= K; i++)
        {
            for(int j = 1; j <= S; j++)
            {
                for(int k = pBare[i]; k <= M; k++)
                { f[j][k] = max(f[j - 1][k - pBare[i]] + pExp[i], f[j][k]); }
            }
        }
        if(f[S][M] < N) { cout << -1 << endl; }
        else
        {
            int nTmp = M;
            for(int i = 0; i <= S; i++)
            {
                 for(int j = M; j >= 0; j--)
                 {
                     if(f[i][j] >= N) { nTmp = min(nTmp, j); }
                 }
            }
            cout << M - nTmp << endl;
        }
    }
    return 0;
}
```

第一次做二维背包的问题，感觉理解透了，也不怎么难。 @ **2015年3月23日**

## HDU 2577

我们令 $f[i]$、$g[i]$ 分别表示输入完 $i$ 个字符后，Caps Lock 灯关与开的状态下所需要的按键次数，易得状态转移方程：

* 第 $i$ 个字母小写：$$f[i] = \min{\left\\{f[i - 1] + 1, g[i - 1] + 2\right\\}},\quad g[i] = \min{\left\\{f[i - 1] + 2, g[i - 1] + 2\right\\}}$$
* 第 $i$ 个字母大写：$$f[i] = \min{\left\\{f[i - 1] + 2, g[i - 1] + 2\right\\}},\quad g[i] = \min{\left\\{f[i - 1] + 2, g[i - 1] + 2\right\\}}$$

下面我们来分析一下上面的状态转移方程：第 $i$ 个字母小写，要保持最后 Caps Lock 灯关，那么在灯关的状态下直接输入字母，因此为 `f[i - 1] + 1`；在灯开的状态下关灯，输入字母，因此为 `g[i - 1] + 2`。如果要保持最后 Caps Lock 灯开，在灯关的状态下输入字母，开灯，因此为 `f[i - 1] + 2`；在灯开的状态下 Shift + 字母，因此为 `g[i - 1] + 2`。当第 $i$ 个字母大写的情况类似。

初始条件如下：

* 第 1 个字母小写：$f[0] = 1,\quad g[0] = 2$
* 第 1 个字母大写：$f[0] = 2,\quad g[0] = 2$

最后答案为 `min(f[x.length() - 1], g[x.length() - 1] + 1)`，因为最后 Caps Lock 灯要保持关闭状态。

```cpp
#include <iostream>
#include <string>
#include <memory.h>
 
using namespace std;
 
const int MAX = 128;
 
int f[MAX], g[MAX];
 
bool IsUpper(char x);
bool IsLower(char x);
 
int main()
{
    int N;
    string x;
    while(cin >> N)
    {
        for(int i = 1; i <= N; i++)
        {  
            cin >> x;
            memset(f, 0, sizeof(f));
            memset(g, 0, sizeof(g));
            if(IsLower(x[0])) { f[0] = 1; g[0] = 2; }
            else { f[0] = 2; g[0] = 2; }
            for(int j = 1; j < x.length(); j++)
            {
                if(IsLower(x[j]))
                {
                    f[j] = min(f[j - 1] + 1, g[j - 1] + 2);
                    g[j] = min(f[j - 1] + 2, g[j - 1] + 2);
                }
                else
                {
                    f[j] = min(f[j - 1] + 2, g[j - 1] + 2);
                    g[j] = min(f[j - 1] + 2, g[j - 1] + 1);
                }
            }
            cout << min(f[x.length() - 1], g[x.length() - 1] + 1) << endl;
        }
    }
    return 0;
}
 
bool IsUpper(char x)
{ return x >= 'A' && x <= 'Z'; }
 
bool IsLower(char x)
{ return x >= 'a' && x <= 'z'; }
```

这道题目需要用两个数组来维护不同的两种状态，使得问题得到简化。 @ **2015年4月5日**

## HDU 2844

一个很明显的思路是构造 $C_i$ 个物品 $A_i$，然后做一遍 0/1 背包即可。但是会 TLE，因此需要寻求优化的方法。

在这里我们采用二进制拆分的方法。对于 $C_i$ 个物品 $A_i$，将它拆分成 $A_i \times (1 + 2 + 4 + 8 + 16 + ... + \mathrm{left})$，根据二进制的知识，我们知道通过这样的方法可以获得 $1 \times A_i, 2 \times Ai, \cdots C_i \times Ai$ 的各个数值。证明如下：

这就等效于证明可以从 $1, 2, 4, 8, 16, \cdots , \mathrm{left}$ 中选取任意个数字组成 $1, 2, 3,\cdots , C_i$。我们将这些数字写成二进制的形式，会发现这与前面的拆分是一一对应的。因此这样拆分物品不影响结果的正确性，接下来做一遍 0/1 背包即可出解。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 102400;
 
int f[MAX];
int pValue[MAX], pData[MAX];
 
int main()
{
    int N, M, nTmp;
    ios::sync_with_stdio(false);
    while(cin >> N >> M)
    {
        int nCnt = 0;
        if(N == 0 && M == 0) { break; }
        memset(f, 0, sizeof(f)); f[0] = 1;
        for(int i = 1; i <= N; i++)
        { cin >> pValue[i]; }
        for(int i = 1; i <= N; i++)
        {
            cin >> nTmp;
            for(int j = 1; j <= nTmp; j <<= 1)
            {
                pData[++nCnt] = pValue[i] * j;
                nTmp -= j;
            }
            if(nTmp) { pData[++nCnt] = pValue[i] * nTmp; }
        }
        for(int i = 1; i <= nCnt; i++)
        {
            for(int v = M; v >= pData[i]; v--)
            {
                if(f[v - pData[i]]) { f[v] = 1; }
            }
        }
        int ans = 0;
        for(int i = 1; i <= M; i++)
        { ans += f[i]; }
        cout << ans << endl;
    }
    return 0;
}
```

第一次接触到二进制拆分的思路，感觉很巧妙，值得学习。 @ **2015年4月5日**

*未完待续...*
