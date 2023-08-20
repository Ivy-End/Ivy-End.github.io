# SGU 135 - Drawing Lines


## Description

Little Johnny likes to draw a lot. A few days ago he painted lots of straight lines on his sheet of paper. Then he counted in how many zones the sheet of paper was split by these lines. He noticed that this number is not always the same. For instance, if he draws 2 lines, the sheet of paper could be split into 4, 3 or even 2 (if the lines are identical) zones. Since he is a very curious kid, he would like to know which is the maximum number of zones into which he can split the sheet of paper, if he draws $N$ lines. The sheet of paper is to be considered a very large (=infinite) rectangle.

## Input

The input file will contain an integer number: $N$ ($0\leq N\leq 65535$).

## Output

You should output one integer: the maximum number of zones into which the sheet of paper can be split if Johnny draws $N$ lines.

## Sample Input #1

```
0
```

## Sample Output #1

```
1
```

## Sample Input #2

```
1
```

## Sample Output #2

```
2
```

## Analysis

数学题。直线分平面数，我们也可以通过找规律的方法来求出它的公式：

| 线段数 $N$ | 平面数 $M$ |
|:-:|:-:|
| 0 | 1 |
| 1 | 1 + 1 = 2 |
| 2 | 2 + 2 = 4 |
| 3 | 4 + 3 = 7 |
| 4 | 7 + 4 = 11 |
| 5 | 11 + 5 = 16 |
| 6 | 16 + 6 = 22 |

根据上表，我们可以很容易的求得递推公式：$$M_N = M_{N-1} + N$$

由此得到通项公式：$$M = \frac{N \cdot (N + 1)}{2} + 1$$

当然我们也可以使用数学归纳法证明这个结论。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
typedef unsigned long long ull;
 
int main()
{
    int N;
    cin >> N;
    cout << (ull)N * (N + 1) / 2 + 1;
    return 0;
}
```

本题需要注意的是给出的数据范围如果不使用 `unsigned long long` 会溢出，因此必须使用 `unsigned long long`。
