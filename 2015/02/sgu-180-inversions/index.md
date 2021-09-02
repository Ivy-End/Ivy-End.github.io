# SGU 180 - Inversions


## Description

There are $N$ integers ($1\leq N\leq 65537$) $A_1, A_2,\cdots, A_N$ ($0\leq A_i\leq 10^9$). You need to find amount of such pairs $(i, j)$ that $1\leq i < j\leq N$ and $A[i]>A[j]$.

## Input

The first line of the input contains the number $N$. The second line contains $N$ numbers $A_1,\cdots,A_N$.

## Output

Write amount of such pairs.

## Sample Input

```
5
2 3 1 5 4
```

## Sample Output

```
3
```

## Analysis

逆序数。树状数组即可。每次更新 $A[i]$ 为 1，然后所有的逆序数就是 $$A[i] - \sum{\left(A[i] - 1\right)} + 1$$ 更新的同时获取答案。

注意答案可能会超 `int`，所以使用 `long long`。

数据中 $A[i]$ 的值过大，但是 $N$ 最大只有 65537，所以使用离散化即可，离散化只要 `sort` 一下，然后用 `lower_bound` 即可。

## Solution

```cpp
#include <iostream>
#include <algorithm>
#include <memory.h>
 
using namespace std;
 
const int MAX = 102400;
 
int N;
int T[MAX], A[MAX], B[MAX];
 
int LowBit(int x);
void Update(int x, int y);
long long Sum(int x);
 
int main()
{
    while(cin >> N)
    {
        long long ans = 0;
        memset(T, 0, sizeof(T));
        for(int i = 1; i <= N; i++)
        {
            cin >> A[i];
            B[i] = A[i];
        }
        sort(B + 1, B + N + 1);
        for(int i = 1; i <= N; i++)
        { A[i] = lower_bound(B + 1, B + N + 1, A[i]) - B; }
        for(int i = 1; i <= N; i++)
        {
            Update(A[i], 1);
            ans += A[i] - Sum(A[i] - 1) - 1;
        }
        cout << ans << endl;
    }
    return 0;
}
 
int LowBit(int x)
{ return x & (-x); }
 
void Update(int x, int y)
{
    while(x <= N)
    {
        T[x] += y;
        x += LowBit(x);
    }
}
 
long long Sum(int x)
{
    long long ans = 0;
    while(x)
    {
        ans += T[x];
        x -= LowBit(x);
    }
    return ans;
}
```

最近整理了一下树状数组，准备刷一下树状数组专题，这道题目是非常基础的应用。
