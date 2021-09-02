# SGU 115 - Calendar


## Description

First year of new millenium is gone away. In commemoration of it write a program that finds the name of the day of the week for any date in 2001.

## Input

Input is a line with two positive integer numbers $N$ and $M$, where $N$ is a day number in month $M$. $N$ and $M$ is not more than 100.

## Output

Write current number of the day of the week for given date (Monday – number 1, … , Sunday – number 7) or phrase "Impossible" if such date does not exist.

## Sample Input

```
21 10
```

## Sample Output

```
7
```

## Analysis

翻看日历，我们可以知道 2001 年 1 月 1 日为星期一。

这样，我们只需要计算输入的日期为该年中的第几天就行了。

当然，要记得判断输入的日期是否合法。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
const int pDay[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
 
int main()
{
    int N, M, ans = 0;
    cin >> N >> M;
    if((M > 12 || N > 31) ||
        (M == 4 || M == 6 || M == 9 || M == 11) && N > 30 ||
        M == 2 && N > 28)
    {
        cout << "Impossible" << endl;
    }
    else
    {
        for(int i = 1; i < M; i++)
        { ans += pDay[i]; }
        ans += N;
        cout << (ans % 7 == 0 ? 7 : ans % 7) << endl;
    }
    return 0;
}
```
