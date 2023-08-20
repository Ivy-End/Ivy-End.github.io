# SGU 154 - Factorial


## Description

You task is to find minimal natural number $N$, so that $N!$ contains exactly $Q$ zeroes on the trail in decimal notation. As you know $N! = 1\cdot2\cdots N$. For example, $5! = 120$, 120 contains one zero on the trail.

## Input

One number $Q$ written in the input ($0\leq Q\leq 10^8$).

## Output

Write "No solution", if there is no such number $N$, and $N$ otherwise.

## Sample Input

```
2
```

## Sample Output

```
10
```

## Analysis

统计 $N!$ 末尾 0 的个数，其实只要看因数 2 和 5 个数的最小值，因为只有 $2\times 5$ 会产生 0。然而实际上因数 2 的个数远大于因数 5 的个数，所以只要看因数 5 的个数。

由于题目给出的空间限制只有 4096KB，所以不能打表，会 MLE。百度题解以后发现可以用二分。

二分的时候统计 1 到 $N$ 这 $N$ 个数中因数 5 的个数，我们采用这样的方法：$$\mathrm{ans} = \left\lfloor\frac{N}{5}\right\rfloor + \left\lfloor\frac{N}{5^2}\right\rfloor + \left\lfloor\frac{N}{5^3}\right\rfloor + \cdots $$

处理这个过程有两种方法，一个是打表，把 5 的幂次打表出来，还有一种利用类似秦九邵算法的思想，每次 `ans += N / 5`，同时 `N /= 5`。

需要注意的是，当输入 0 的时候，要输出 1，因为 0 不是自然数。还有二分的上下界应为 $[1, 2147483647]$。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 2147483647;
 
int main()
{
    int N;
    while(cin >> N)
    {
        if(N == 0) { cout << 1 << endl; continue; }
        int l = 1, r = MAX, ans = -1;
        while(l <= r)
        {
            int nMid = (l + r) >> 1;
            int nTmp = nMid, nCnt = 0;
            while(nTmp) { nCnt += nTmp / 5; nTmp /= 5; }
            if(nCnt == N) { ans = nMid; r = nMid - 1; }
            else if(nCnt < N) { l = nMid + 1; }
            else { r = nMid - 1; }
        }
        if(ans == -1) { cout << "No solution" << endl; }
        else { cout << ans << endl; }
    }
    return 0;
}
```

这道题目一开始 WA 了好几次，后来发现是二分的上界设置的太小了。
