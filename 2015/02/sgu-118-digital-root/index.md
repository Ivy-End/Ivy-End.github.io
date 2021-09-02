# SGU 118 - Digital Root


## Description

Let $f(n)$ be a sum of digits for positive integer $n$. If $f(n)$ is one-digit number then it is a digital root for $n$ and otherwise digital root of $n$ is equal to digital root of $f(n)$. For example, digital root of 987 is 6. Your task is to find digital root for expression $$ A_1\cdot A_2\cdots A_N + A_1\cdot A_2\cdots A_{N-1} + \cdots + A_1\cdot A_2 + A_1$$

## Input

Input file consists of few test cases. There is $K$ ($1\leq K\leq 5$) in the first line of input.

Each test case is a line. Positive integer number $N$ is written on the first place of test case ($N\leq 1000$). After it there are $N$ positive integer numbers (sequence $A$). Each of this numbers is non-negative and not more than $10^9$.

## Output

Write one line for every test case. On each line write digital root for given expression.

## Sample Input

```
1
3 2 3 4
```

## Sample Output

```
5
```

## Analysis

结论题：$f(n) \equiv n \mod 9$。

证明如下：

令 $$n = a_0 \cdot 10^{p_0} + a_1 \cdot 10_{p_1} + \cdots + a_{m-1} \cdot 10^1 + a_m \cdot 10^0$$ 其中 $n$ 为 $m$ 位数。则 $$n \mod 9 = a_0 + a_1 + \cdots + a_{m-1} + a_m = f(n)$$ 即 $$f(n) \equiv n\mod 9$$ 证毕。

需要注意的是，当 `n mod 9 == 0` 的时候，`f(n) = 9`。

读入的时候要先把数据 mod 9，否则中间计算过程会超 `int`。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 1024;
 
int pData[MAX];
 
int main()
{
    int T, N;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        int ans = 0;
        cin >> N;
        for(int j = 1; j <= N; j++)
        { cin >> pData[j]; pData[j] %= 9; }
        for(int j = 1; j <= N; j++)
        {
            int nTmp = 1;
            for(int k = 1; k <= j; k++)
            {
                nTmp *= pData[k];
                if(nTmp >= 9) { nTmp %= 9; }
            }
            ans += nTmp;
            if(ans >= 9) { ans %= 9; }
        }
        cout << (ans == 0 ? 9 : ans) << endl;
    }
}
```

又是一个数论结论，结论题有时候还是挺难想到的。
