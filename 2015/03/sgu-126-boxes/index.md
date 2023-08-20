# SGU 126 - Boxes


## Description

There are two boxes. There are $A$ balls in the first box, and $B$ balls in the second box ($0 < A + B < 2147483648$). It is possible to move balls from one box to another. From one box into another one should move as many balls as the other box already contains. You have to determine, whether it is possible to move all balls into one box.

## Input

The first line contains two integers $A$ and $B$, delimited by space.

## Output

First line should contain the number $N$ - the number of moves which are required to move all balls into one box, or -1 if it is impossible.

## Sample Input

```
2 6
```

## Sample Output

```
2
```

## Analysis

### 模拟法

设定一个规定步数（经过反复测试，在给定的数据范围内32步即可满足要求），如果在规定步数内完成任务，则输出步数，否则输出-1。

### 数学法

首先我们有一个结论 $(x, y)$ 与 $\left(\frac{x}{\mathrm{gcd}(x, y)}, \frac{y}{\mathrm{gcd}(x, y)}\right)$ 具有相同的答案。

证明：我们可以运用整体的思想，将 $\mathrm{gcd}(x, y)$ 个球看成一个球。例如 5 5，我们可以看成 1 1，其中后面的 1 代表了 5 个小球。

有了上面的结论，我们只需要处理 $(X, Y)$ 即可，其中 $$ X = \frac{x}{\mathrm{gcd}(x, y)},\quad Y = \frac{y}{\mathrm{gcd}(x, y)}$$ 很明显，当 $X + Y$ 为奇数时无解，因为要完成任务，必定有状态 $(A, A)$ 出现，其中 $A = \frac{X + Y}{2}$。

接下来，我们来推到一般解的情况，令 $N = X + Y$，并设 $K$步完成任务：

| 步骤数目 | 解空间状态 |
|:-:|:-:|
| $K$ | $(N, 0)$ |
| $K - 1$ | $(N / 2, N / 2)$ |
| $K - 2$ | $(N / 4, 3N / 4)$ |
| $K - 3$ | $(N / 8, 7N / 8), (5N / 8, 3N / 8)$ |
| $K - 4$ | $(N / 16, 15N / 16), (9N / 16, 7N / 16), (5N / 16, 11N / 16), (13N / 16, 3N / 16)$ |
| $\cdots$ | $\cdots$ |

我们可以看到，当 $N$ 为 2 的幂次时有解，其中 2 的指数则为所需要的步骤数（这也就验证了模拟时只需要 32 步即可），这样我们就可以很轻松的解决这个问题了。

## Solution

### 模拟法

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 32;
 
int main()
{
    int x, y;
    while(cin >> x >> y)
    {
        int nCnt = 0;
        while(x != 0 && y != 0 && nCnt <= MAX)
        {
            if(x <= y) { y -= x; x += x; }
            else { x -= y; y += y; }
            nCnt++;
        }
        if(x != 0 && y != 0) { cout << -1 << endl; }
        else { cout << nCnt << endl; }
    }
    return 0;
}
```

### 数学法

```cpp
#include <iostream>
 
using namespace std;
 
int gcd(int x, int y);
 
int main()
{
    int x, y;
    while(cin >> x >> y)
    {
        int nCnt = 0;
        int nTmp = gcd(x, y);
        x /= nTmp; y /= nTmp;
        int nSum = x + y;
        while(nSum > 1)
        {
            if(nSum & 1) { nCnt = -1; break; }
            else { nCnt++; nSum >>= 1; }
        }
        if(x == 0 || y == 0) { nCnt = 0; }
        cout << nCnt << endl;
    }
}
 
int gcd(int x, int y)
{
    if(y == 0) { return x; }
    else { return gcd(y, x % y); }
}
```

这道数学题想了好久，终于AC了，主要在于一个逆推的过程以及看出 $(x, y)$ 与 $\left(\frac{x}{\mathrm{gcd}(x, y)}, \frac{y}{\mathrm{gcd}(x, y)}\right)$ 同解。
