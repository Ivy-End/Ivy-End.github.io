# SGU 107 - 987654321 problem


## Description

For given number $N$ you must output amount of $N$-digit numbers, such, that last digits of their square is equal to 987654321.

## Input

Input contains integer number $N$ ($1\leq N\leq 10^6$).

## Output

Write answer in output file.

## Sample Input

```
8
```

## Sample Output

```
0
```

## Analysis

在一定意义上，这也是一道数学题。

由于一个数平方的后X位，只与这个数字的后X位有关系，所以我们不妨使用下面的程序打一个表来看一下。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    // sqrt(987654321) > 30000
    for(long long i = 30000; i <= 999999999; i++)
    {
        long long x = i * i;
        if(x % 1000000000 == 987654321)
        { cout << i << " "; }
    }
    return 0;
}
```

打完表以后，我们发现只有 8 个数字满足条件，而且分布在 100,000,000 到 999,999,999 之间。

下面我们来推导满足题目条件的答案与输入的位数 $N$ 的关系：$$\mathrm{ans} = \begin{cases}0, & N \leq 8\\\ 8, & N = 9\\\ 72\times 10^{N - 10}, & N \geq 10\end{cases}$$ 最后一种情况我们要稍微考虑一下，由于平方后的后 9 位只与原数的后 9 位有关，因此就变成了给定后 9 位（第二种情况下的 8 个答案作为后九位数字），前面 $N-9$ 位数字的方案数，由排列组合以及 $N$ 位数的要求，不难的出结论：$72 \times 10^{N - 10}$。

有了这个结论，我们就可以在 $O(1)$ 时间内得到答案。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int N;
    cin >> N;
    if(N <= 8)
    { cout << 0 << endl; }
    else if(N == 9)
    { cout << 8 << endl; }
    else
    {
        cout << 72 << endl;
        while(N - 10)
        {
            cout << 0;
            N--;
        }
    }
    return 0;
}
```

这道题目最主要的是通过打表找出规律，然后通过数学方法，巧妙地将题目所要求的答案转换为前面 $N-9$ 位上数字的排列方式，这样问题就得到了简化，也就很容易解决了。
