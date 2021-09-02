# SGU 113 - Nearly prime numbers


## Description

Nearly prime number is an integer positive number for which it is possible to find such primes $P_1$ and $P_2$ that given number is equal to $P_1\cdot P_2$. There is given a sequence on $N$ integer positive numbers, you are to write a program that prints "Yes" if given number is nearly prime and "No" otherwise.

## Input

Input file consists of $N + 1$ numbers. First is positive integer $N$ ($1\leq N\leq 10$). Next $N$ numbers followed by $N$. Each number is not greater than $10^9$. All numbers separated by whitespace(s).

## Output

Write a line in output file for each number of given sequence. Write "Yes" in it if given number is nearly prime and "No" in other case.

## Sample Input

```
1
6
```

## Sample Output

```
Yes
```

## Analysis

考虑到数据范围不是很大，$10^9$ 以内仅有五千多万个质数，可以通过打表来解决。打表自然是筛法求素数。

每次读入数据以后，只要比较到 $\sqrt{X}$ 就可以了，这样我们就可以在 $O\left(\sqrt{n}\right)$ 的时间内求出结果。

这里有个小小的注意点，我们在循环的时候，最好使用 `i * i <= X` 来代替 `i <= sqrt(X) + 1`，因为后者容易产生浮点数误差。

## Solution

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory.h>
#include <math.h>
 
using namespace std;
 
const int MAX = 32000;
 
bool pPrimes[MAX];
vector<int> pVec;
 
int main()
{
    unsigned long long N, x, y;
    memset(pPrimes, true, sizeof(pPrimes));
    for(int i = 2; i < MAX; i++)
    {
        if(pPrimes[i])
        {
            pVec.push_back(i);
            for(int j = i + i; j < MAX; j += i)
            { pPrimes[j] = false; }
        }
    }
    cin >> N;
    for(int i = 1; i <= N; i++)
    {
        cin >> x;
        bool bFlag = false;
        for(int j = 0; j < pVec.size(); j++)
        {
            if(x % pVec[j] == 0)
            {
                y = x / pVec[j];
                bool bTmp = true;
                for(int k = 2; k * k <= y; k++)
                {
                    if(y % k == 0)
                    { bTmp = false; break; }
                }
                if(y <= 1) { bTmp = false; }
                if(y == 2) { bTmp = true; }
                if(bTmp) { bFlag = true; break; }
            }
        }
        if(bFlag) { cout << "Yes" << endl; }
        else { cout << "No" << endl; }
    }
    return 0;
}
```

这道题目可以用来练习使用筛法求素数，题目本身并不具有很强的思考性。
