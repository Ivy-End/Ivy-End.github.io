# SGU 116 - Index of super-prime


## Description

Let $P_1, P_2,\cdots ,P_N,\cdots$ be a sequence of prime numbers. Super-prime number is such a prime number that its current number in prime numbers sequence is a prime number too. For example, 3 is a super-prime number, but 7 is not. Index of super-prime for number is 0 iff it is impossible to present it as a sum of few (maybe one) super-prime numbers, and if such presentation exists, index is equal to minimal number of items in such presentation. Your task is to find index of super-prime for given numbers and find optimal presentation as a sum of super-primes.

## Input

There is a positive integer number in input. Number is not more than 10000.

## Output

Write index $I$ for given number as the first number in line. Write I super-primes numbers that are items in optimal presentation for given number. Write these I numbers in order of non-increasing.

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

首先，我们可以根据筛法求出 10000 以内的素数，接下来我们继续利用筛法，求出这些素数中，下标为素数的超级素数，这样我们就得到了题目中所需要的超级素数。

对于寻找一个最优的组合，我们可以使用 0/1 背包来解决这个问题，同时记录路径，最后输出最优解即可。

## Solution

```cpp
#include <iostream>
#include <memory.h>
#include <vector>
#include <algorithm>
 
using namespace std;
 
const int MAX = 10240;
 
vector<int> P, SP;
 
int pP[MAX], pSP[MAX], nCnt;
int f[MAX], pPath[MAX];
 
int main()
{
    int N;
    P.push_back(0); SP.push_back(0);
    memset(pP, 0, sizeof(pP));
    memset(pSP, 0, sizeof(pSP));
    for(int i = 2; i < MAX; i++)
    {
        if(pP[i] == 0)
        {
            P.push_back(i);
            for(int j = i + i; j < MAX; j += i)
            { pP[j] = 1; }
        }
    }
    for(int i = 2; i < P.size(); i++)
    {
        if(pSP[i] == 0)
        {
            SP.push_back(P[i]);
            for(int j = i + i; j < P.size(); j += i)
            { pSP[j] = 1; }
        }
    }
    while(cin >> N)
    {
        memset(f, 0, sizeof(f));
        memset(pPath, 0, sizeof(pPath));
        f[0] = 0;
        for(int i = 1; i <= N; i++)
        { f[i] = 214748364; }
        for(int i = 1; i < SP.size(); i++)
        {
            for(int j = SP[i]; j <= N; j++)
            {
                if(f[j - SP[i]] + 1 < f[j])
                {
                    f[j] = f[j - SP[i]] + 1;
                    pPath[j] = j - SP[i];
                }
            }
        }
        if(f[N] == 214748364) { cout << 0 << endl; }
        else
        {
            cout << f[N] << endl << N - pPath[N];
            for(int i = pPath[N]; i; i = pPath[i])
            { cout << " " << i - pPath[i]; }
            cout << endl;
        }
    }
    return 0;
```

这道题目主要考察最为基本的动态规划以及记录路径。
