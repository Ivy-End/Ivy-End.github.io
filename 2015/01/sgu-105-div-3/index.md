# SGU 105 - Div 3


## Description

There is sequence 1, 12, 123, 1234, ..., 12345678910, ... . Given first $N$ elements of that sequence. You must determine amount of numbers in it that are divisible by 3.

## Input

Input contains $N$ ($1\leq N\leq 2^{31} - 1$).

## Output

Write answer in output file.

## Sample Input

```
4
```

## Sample Output

```
2
```

## Analysis

由于一个数对 $3$ 取模恒等于这个数各个位上数字之和对 $3$ 取模。因此，非常容易想到的方法是找规律：

| 项数 $N$ | 数列 | 除以 $3$ 的余数 | 答案 $ans$ |
|:-:|:-:|:-:|:-:|
| 1 | 1 | 1 | 0 |
| 2 | 12 | 0 | 1 |
| 3 | 123 | 0 | 2 |
| 4 | 1234 | 1 | 2 |
| 5 | 12345 | 0 | 3 |
| 6 | 123456 | 0 | 4 |
| 7 | 1234567 | 1 | 4 |
| 8 | 12345678 | 0 | 5 |
| 9 | 123456789 | 0 | 6 |

由上述表格，我们可以大致的看出规律，即：$$ans = \begin{cases} ans, & N \mod 3 = 1\\\ ans + 1, & N \mod 3 = 0, 2\end{cases}$$

有了上述的讨论，我们可以很容易的写出一个暴力算法，但是考虑到 $N$ 的数据范围比较大，这并不是一个非常好的选择。

我们可以推导出数学公式来求解这个问题。观察上表（下面的除法为 C++ 意义中的整除）：

 * `if(N % 3 == 0)  ans = 2 * N / 3;`
 * `if(N % 3 == 1)  ans = 2 * N / 3;`
 * `if(N % 3 == 2)  ans = 2 * N / 3 + 1;`

把上述公式归纳成一个公式，即为 `ans = 2 * N / 3 + (N % 3 == 2)`，此处 `N % 3 == 2` 的返回值为真、假，分别对应着 1 和 0。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int N;
    cin >> N;
    cout << N / 3 * 2 + (N % 3 == 2) << endl << endl;
    return 0;
}
```
