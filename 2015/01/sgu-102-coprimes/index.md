# SGU 102 - Coprimes


## Description

For given integer $N$ ($1\leq N\leq 10^4$) find amount of positive numbers not greater than $N$ that coprime with $N$. Let us call two positive integers (say, $A$ and $B$, for example) coprime if (and only if) their greatest common divisor is 1. (i.e. $A$ and $B$ are coprime iff $\mathrm{gcd}\left(A,B\right) = 1$).

## Input

Input file contains integer $N$.

## Output

Write answer in output file.

## Sample Input

```
9
```

## Sample Output

```
6
```

## Analysis

我首先想到的是欧拉函数 $\varphi\left(N\right)$，后来发现数据量并不是特别的大，所以又用暴力做了一遍，也 AC 了。

这道题目的重点在于欧拉函数 $\varphi\left(N\right)$ 的求法，现总结如下：

欧拉函数 $\varphi\left(N\right)$：小于等于 $N$ 且与 $N$ 互素的正整数的个数。

欧拉函数据有如下性质：

 * $\varphi\left(1\right) = 1$
 * $\varphi\left(N\right) = N\cdot\sum_{p|N}{\left(\frac{p-1}{p}\right)}$，其中 $p$ 为素数
 * $\varphi\left(p^k\right) = p^k - p^{k - 1} = \left(p-1\right)p^{k - 1}$，其中p为素数
 * $\varphi\left(mn\right)=\varphi\left(m\right)\cdot \varphi\left(n\right)$，其中 $\mathrm{gcd}\left(m,n\right)=1$

根据第 2 个式子我们就可以求出欧拉函数。

基本思路：首先置 $\varphi\left(N\right) = N$，然后枚举 $N$ 的素因子 $p$，将 $p$ 的整数倍的欧拉函数 $\varphi\left(k\cdot p\right)$ 置 $\varphi\left(k\cdot p\right) = \varphi\left(k\cdot p\right) \cdot \frac{p - 1}{p}$ 即可。

基本代码如下：

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 1024;
 
int N;
int p[MAX], phi[MAX];
 
int main()
{
    cin >> N;
    for(int i = 1; i <= N; i++)  // 初始化
    { p[i] = 1; phi[i] = i; }
    p[1] = 0;   // 1不是素数
    for(int i = 2; i <= N; i++)  // 筛素数
    {
        if(p[i])
        {
            for(int j = i * i; j <= N; j += i)
            { p[j] = 0; }
        }
    }
    for(int i = 2; i <= N; i++)  // 求欧拉函数
    {
        if(p[i])
        {
            for(int j = i; j <= N; j += i)   // 处理素因子p[i]
            {
                phi[j] = phi[j] / i * (i - 1);  // 先除后乘，防止中间过程超出范围
            }
        }
    }
    cout << "Primes: " << endl;
    for(int i = 1; i <= N; i++)
    { if(p[i]) { cout << i << " "; } }
    cout << endl;
    cout << "Euler Phi Function: " << endl;
    for(int i = 1; i <= N; i++)
    { cout << phi[i] << " "; }
    return 0;
}
```

## Solution

### 欧拉函数

```cpp
#include <iostream>
#include <math.h>
#include <stdio.h>
 
using namespace std;
 
int phi(int x);
 
int main()
{
    int N;
    cin >> N;
    cout << phi(N) << endl;
    cout << endl;
    return 0;
}
 
int phi(int x)
{
    int nRet = x;
    int nTmp = (int)sqrt(x);
    for(int i = 2; i <= nTmp; i++)
    {
        if(x % i == 0)
        {
            nRet = nRet / i * (i - 1);
            while(x % i == 0)
            { x /= i; }
        }
    }
    if(x > 1)
    {
        nRet = nRet / x * (x - 1);
    }
    return nRet;
}
```

### 暴力

```cpp
#include <iostream>
#include <math.h>
#include <stdio.h>
 
using namespace std;
 
int gcd(int x, int y);
 
int main()
{
    int N, nRet = 0;
    cin >> N;
    for(int i = 1; i <= N; i++)
    {
        if(gcd(N, i) == 1)
        { nRet++; }
    }
    cout << nRet << endl;
    return 0;
}
 
int gcd(int x, int y)
{
    if(y == 0) { return x; }
    return gcd(y, x % y);
}
```

SGU 不愧是经典题目的合集，每做一道题都会学到一些新的东西。
