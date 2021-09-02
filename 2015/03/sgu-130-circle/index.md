# SGU 130 - Circle


## Description

On a circle border there are $2k$ different points $A_1, A_2, \cdots , A_{2k}$, located contiguously. These points connect $k$ chords so that each of points $A_1, A_2, \cdots, A_{2k}$ is the end point of one chord. Chords divide the circle into parts. You have to find $N$ - the number of different ways to connect the points so that the circle is broken into minimal possible amount of parts $P$.

## Input

The first line contains the integer $k$ ($1\leq k\leq 30$).

## Output

The first line should contain two numbers $N$ and $P$ delimited by space.

## Sample Input

```
2
```

## Sample Output

```
23
```

## Analysis

我们可以采用分治的方法，固定某个点，从其上引一条弦，将圆分成左右两部分。我们可以将这两部分看成新的圆，那么方案数就是这两个圆的方案数相乘。即：$$f[N] = \sum{\left(f[i - 1] \cdot f[N - i]\right)}$$ 其中 $1\leq i\leq N$。$f[i-1]$ 表示左边的圆，为 $k = i - 1$ 时的情况，$f[N - i]$ 为右边的圆，表示 $k = N - i$ 时的情况。这样，我们只要递推一下就可以了。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 32;
 
long long f[MAX];
 
int main()
{
    int N;
    f[0] = 1; f[1] = 1; f[2] = 2;
    for(int i = 3; i < MAX; i++)
    {
        for(int j = 1; j <= i; j++)
        { f[i] += f[j - 1] * f[i - j]; }
    }
    while(cin >> N)
    { cout << f[N] << " " << N + 1 << endl; }
    return 0;
}
```

这也算是一道数学题，然而想到分治这一点还是有些难度的。
