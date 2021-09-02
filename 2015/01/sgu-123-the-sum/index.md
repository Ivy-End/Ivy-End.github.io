# SGU 123 - The Sum


## Description

The Fibonacci sequence of numbers is known: $F_1 = 1$; $F_2 = 1$; $F_{n+1} = F_n + F_{n-1}$, for $n>1$. You have to find $S$ - the sum of the first $K$ Fibonacci numbers.

## Input

First line contains natural number $K$ ($0<K<41$).

## Output

First line should contain number $S$.

## Sample Input

```
5
```

## Sample Output

```
12
```

## Analysis

考虑到数据范围，这道题目只要模拟一下就行了。但是我还是比较喜欢使用数学方法来求解。

令 $S_n$ 表示斐波那契数列的前 $N$ 项和，那么我们很容易求得 $S_n = F_{n+2} - 1$。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 64;
 
int f[MAX];
 
int main()
{
    int N;
    cin >> N;
    f[1] = f[2] = 1;
    for(int i = 3; i <= N + 2; i++)
    { f[i] = f[i - 1] + f[i - 2]; }
    cout << f[N + 2] - 1 << endl;
    return 0;
}
```

这道题目应该是非常简单的。当然，如果你不知道斐波那契数列可以在$O(n)$时间内求得，那么这道题目对于你来说还是有一定难度的。
