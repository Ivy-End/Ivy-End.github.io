# SGU 144 - Meeting


## Description

Two of the three members of the winning team of one of the ACM regional contests are going to meet in order to train for the upcoming World Finals. They decided that they will meet sometime between $X$ o'clock and $Y$ o'clock. Because they never get anywhere on time (they were late even on the day of the regional contest), they did not set an exact time when they will meet. However, they decided that the one who gets first at the meeting point will not wait more than $Z$ minutes for the other one (they calculated that, if the other one will not come within $Z$ minutes from the arrival of the first of them, then it is very probable that he will not show up at all).

Knowing that, in the end, both of them will show up at some time between $X$ o'clock and $Y$ o'clock (not necessarily after an integer number of minutes), compute which is the probability that they will actually meet.

## Input

The input will contain 2 integer numbers $X$ and $Y$ ($0\leq X < Y\leq 24$) and one real number $Z$ ($0 < Z\leq 60(Y-X)$).

## Output

You should output the required probability with 7 decimal digits (rounded according to the 8th decimal digit).

## Sample Input

```
11 12 20.0
```

## Sample Output

```
0.5555556
```

## Analysis

这是一道纯粹的数学概率题，我们可以进行公式推导。首先我们需要统一单位，将 $X$ 和 $Y$ 均以分钟为单位；其次，我们以 $X$ 点钟为计时零点；接下来做出这样一张图：

{{< image src="/images/2015/SGU 144 - Meeting/Answer.png" caption="概率分布图" >}}

根据上图，我们可以知道相遇的概率为中间六边形的面积，即 $P = S_A / S$，由于 $S_A$ 求解起来比较困难，我们可以转换为计算总面积减去两个三角形的面积。因此，答案为 $$ P = 1 - \frac{(Y - X - Z) ^ 2}{(Y - X) ^ 2}$$


## Solution

```cpp
#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main()
{
    ios::sync_with_stdio(false);
    double X, Y, Z;
    while(cin >> X >> Y >> Z)
    {
        X *= 60; Y *= 60; Y -= X;
        cout << fixed << setprecision(7) << 1 - (Y - Z) * (Y - Z) / (Y * Y) << endl;
    }
    return 0;
}
```

这道题目主要考察数学中的概率知识。
