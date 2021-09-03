# SGU 222 - Little Rooks


## Description

Inspired by a "Little Bishops" problem, Petya now wants to solve problem for rooks.

A rook is a piece used in the game of chess which is played on a board of square grids. A rook can only move horizontally and vertically from its current position and two rooks attack each other if one is on the path of the other.

Given two numbers $n$ and $k$, your job is to determine the number of ways one can put $k$ rooks on an $n\times n$ chessboard so that no two of them are in attacking positions.

## Input

The input file contains two integers $n$ ($1\leq n\leq 10$) and $k$ ($0\leq k\leq n^2$). 

## Output

Write index $I$ for given number as the first number in line. Write $I$ super-primes numbers that are items in optimal presentation for given number. Write these $I$ numbers in order of non-increasing.

## Sample Input

```
6
```

## Sample Output

```
2
3 3
```

## Analysis

由于 $K$ 个车每行只能放一个，所以一共有 $K!$ 种情况，一共有 $N\times N$ 的棋盘，行列选择共 $\binom{N}{k}\cdot \binom{N}{k}$ 种情况。因此，通过排列组合，我们有 $$\mathrm{ans} = \binom{N}{k}\cdot \binom{N}{k}\cdot K!$$ 化简可得 $$\mathrm{ans} = \frac{N!}{K!\cdot (N - K)!}\cdot\frac{N!}{(N - K)!}$$

## Solution

```cpp
#include <iostream>
#include <algorithm>
 
using namespace std;
 
const int MAX = 16;
 
unsigned long long f[MAX];
 
int main()
{
    f[0] = 1;
    for(int i = 1; i < MAX; i++)
    { f[i] = f[i - 1] * i; }
    int N, K;
    while(cin >> N >> K)
    {
        if(K > N) { cout << 0 << endl; }
        else { cout << f[N] / f[K] / f[N - K] * f[N] / f[N - K] << endl; }
    }
    return 0;
}
```

还以为类似八皇后，准备写 `Check` 函数，后来发现只是简单的排列组合而已。
