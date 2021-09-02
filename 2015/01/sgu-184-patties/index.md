# SGU 184 - Patties


## Description

Petya is well-known with his famous cabbage patties. Petya's birthday will come very soon, and he wants to invite as many guests as possible. But the boy wants everybody to try his specialty of the house. That's why he needs to know the number of the patties he can cook using the stocked ingredients. Petya has $P$ grams of flour, $M$ milliliters of milk and $C$ grams of cabbage. He has plenty of other ingredients. Petya knows that he needs $K$ grams of flour, $R$ milliliters of milk and $V$ grams of cabbage to cook one patty. Please, help Petya calculate the maximum number of patties he can cook.

## Input

The input file contains integer numbers $P$, $M$, $C$, $K$, $R$ and $V$, separated by spaces and/or line breaks ($1 \leq P, M, C, K, R, V \leq 10000$).

## Output

Output the maximum number of patties Petya can cook.

## Sample Input

```
3000 1000 500
30 15 60
```

## Sample Output

```
8
```

## Analysis

简单的数学分析就知道，所求答案为 $P / K$，$M / R$，$C / V$ 的最小值。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
int min(int x, int y, int z);
 
int main()
{
    int P, M, C, K, R, V;
    cin >> P >> M >> C;
    cin >> K >> R >> V;
    cout << min(P / K, M / R, C / V) << endl;
    return 0;
}
 
int min(int x, int y, int z)
{
    return min(x, min(y, z));
}
```

这道题目涉及到的一个数学思想是——短板理论。

也就是决定能够制作多少个馅饼的数目是由各个原料能够制作的馅饼数的最小值来决定的。

短板理论在我们的日常生活中也很常见。我们也要经常发现自己的短板所在，并对其进行提升，进一步的完善自我，提升自我。
