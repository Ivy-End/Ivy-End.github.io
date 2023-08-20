# SGU 117 - Counting


## Description

Find amount of numbers for given sequence of integer numbers such that after raising them to the $M$-th power they will be divided by $K$.

## Input

Input consists of two lines. There are three integer numbers $N, M, K$ ($0<N, M, K<10001$) on the first line. There are N positive integer numbers − given sequence (each number is not more than 10001) − on the second line.

## Output

Write answer for given task.

## Sample Input

```
4 2 50
9 10 11 12
```

## Sample Output

```
1
```

## Analysis

快速幂，时间复杂度为 $O(n\log{n})$，应该是可以过的。

要注意用 `int` 的话会溢出，所以我直接用了 `unsigned long long`。

这道题目还有一个方法是质因数分解，求出 $M$ 次方以后的各个因数个数（就是把个因子个数乘以 $M$），然后和 $M$ 的个因子的个数比较即可。

## Solution

### 快速幂

```cpp
#include <iostream>
 
using namespace std;
 
typedef unsigned long long  ull;
 
ull Pow(ull x, ull y, ull z);
 
int main()
{
    ull nTmp;
    int N, M, K;
    while(cin >> N >> M >> K)
    {
        int nCnt = 0;
        for(int i = 1; i <= N; i++)
        {
            cin >> nTmp;
            if(Pow(nTmp, M, K) == 0) { nCnt++; }
        }
        cout << nCnt << endl;
    }
    return 0;
}
 
ull Pow(ull x, ull y, ull z)
{
    if(y == 1) { return x % z; }
    ull nTmp = Pow(x, y / 2, z);
    if(y & 1) { return (ull)nTmp * nTmp * x % z; }
    else { return (ull)nTmp * nTmp % z; }
}
```

### 质因数分解

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int X[MAX], Y[MAX];
 
void Fact(int x, int *p);
 
int main()
{
    int nTmp;
    int N, M, K;
    while(cin >> N >> M >> K)
    {
        int nCnt = 0;
        memset(Y, 0, sizeof(Y));
        Fact(K, Y);
        for(int i = 1; i <= N; i++)
        {
            memset(X, 0, sizeof(X));
            cin >> nTmp;
            Fact(nTmp, X);
            for(int i = 0; i < MAX; i++)
            { X[i] *= M; }
            bool bFlag = true;
            for(int j = 0; j < MAX; j++)
            {
                if(X[j] < Y[j]) { bFlag = false; break; }
            }
            if(bFlag) { nCnt++; }
        }
        cout << nCnt << endl;
    }
    return 0;
}
 
void Fact(int x, int *p)
{
    for(int i = 2; i <= x; i++)
    {
        if(x % i == 0)
        {
            while(x % i == 0)
            {
                (*(p + i))++;
                x /= i;
            }
        }
    }
}
```

这道题目使用快速幂需要将整除转换成 mod 以后余 0。
