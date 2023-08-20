# SGU 151 - Construct a triangle


## Description

Find coordinates of any $\triangle ABC$ if it is know that $|AB|=c$, $|AC|=b$, $|AM|=m$, $AM$ is a median of triangle.

## Input

There are three real numbers in input: $c$, $b$, $m$ ($0<c, b, m\leq 10^3$) separated by a space. Length of the fractional part of each number is not greater than 2 digits.

## Output

If solution exists, write three lines. Write coordinates of point $A$ to first line, coordinates of $B$ to second line and coordinates of $C$ to third line. Separate numbers by a space; absolute value of each coordinate must not exceed $10^4$. Write numbers with 5 digits after decimal point. If there is no solution, write "Mission impossible". 

## Sample Input

```
5 5 3
```

## Sample Output

```
0.00000 3.00000
-4.00000 0.00000
4.00000 0.00000
```

## Analysis

解析几何的题目，因为是任意输出一个 $\triangle ABC$，为了简化计算，我们不妨令点 $A$ 为坐标原点，即 $A(0, 0)$。同时，我们可以令点 $B$ 在 $x$ 轴上，即 $B(c, 0)$。这样，问题就转化成了求解点 $C$ 的坐标了。根据中学有关解析几何的知识，我们可以得出下面的求解过程：

设 $C(x, y)$，则 $M\left(\frac{x + c}{2}, \frac{y}{2}\right)$。得方程组：$$\begin{align}x^2 + y^2 &= b^2 \\\ (\frac{x + c}{2})^2 + (\frac{y}{2})^2 &= m^2 \end{align}$$ 将上面两个式子联立，化简即可得到：$$\begin{cases}x = \frac{4 m^2 - b^2 - c^2}{2c} \\\ y = \sqrt{b^2 - x^2}\end{cases}$$ 接下来要判断是否有解，一种方法是根据上面两个方程推导有解的条件，另一种方法是直接判断 $y^2$ 是否大于等于 0。这里我们采用第二种方法，因为不需要额外推导公式，利用已有的结果就可以得出我们需要的答案。

要特别注意的是，在这里，很可能出现 "-0.00000" 的情况，对于这种情况，我们需要进行特殊处理。使得它等于 0。

## Solution

```cpp
#include <iostream>
#include <iomanip>
#include <math.h>
 
using namespace std;
 
int Check(double x);
 
int main()
{
    double c, b, m;
    while(cin >> c >> b >> m)
    {
        double x = (4 * m * m - b * b - c * c) / (2 * c), y = b * b - x * x;
        if(Check(y) >= 0)
        {
            if(Check(x) == 0) { x = 0; }
            if(Check(y) == 0) { y = 0; }
            cout << fixed << setprecision(5) << 0.0 << " " << 0.0 << endl;
            cout << fixed << setprecision(5) << c << " " << 0.0 << endl;
            cout << fixed << setprecision(5) << x << " " << sqrt(y) << endl;
        }
        else { cout << "Mission impossible" << endl; }
    }
    return 0;
}
 
int Check(double x)
{
    if(fabs(x) < 1E-9) { return 0; }
    else { return x > 0 ? 1 : -1; }
}
```

本来在刷小白书的课后习题，但是记到简单的链表和堆栈让我 WA 了很久，所以就去 SGU 上找了几道题目刷刷。

做题目的时候一直遇不到 AC 很容易打击积极性。

这道题目主要在于推到公式，以及注意对于浮点数 "-0.00000" 这种情况的处理。
