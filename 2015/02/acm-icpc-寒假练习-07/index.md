# ACM-ICPC 寒假练习 07


断断续续终于刷完了计算几何专题，感觉太麻烦，小错误不断，尤其是精度问题。还有输出问题，有时候 `printf` 比 `cout` 要方便。

## UVaOJ 10250

给出正方形的一组对角坐标，求另外两个坐标，用三角函数推到公式。

不妨设两点为 $A(x_1, y_1)$ 和 $C(x_2, y_2)$，则中点为 $G\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$，对角线长度为 $L = \sqrt{(x_1 - x_2)^2 - (y_1 - y_2)^2}$。

设直线 $AC$ 与 $x$ 轴的夹角为 $\alpha$，则 $$\sin\alpha = \frac{y_2 - y_1}{L},\quad \cos\alpha = \frac{x_2 - x_1}{L}$$

则另外两个坐标分别为 $$B\left(G_x - \frac{1}{2}\cdot L \cdot \sin, G_y + \frac{1}{2}\cdot L \cdot \cos\alpha\right),\quad D\left(G_x + \frac{1}{2}\cdot L \cdot \sin\alpha, G_y - \frac{1}{2}\cdot L \cdot \cos\alpha\right)$$

```cpp
#include <iostream>
#include <iomanip>
#include <math.h>
 
using namespace std;
 
struct Point
{
    double x, y;
};
 
int main()
{
    Point a, b;
    while(cin >> a.x >> a.y >> b.x >> b.y)
    {
        Point c, d;
        double l = hypot(a.x - b.x, a.y - b.y);
        double sin = (a.y - b.y) / l;
        double cos = (a.x - b.x) / l;
        double x = (a.x + b.x) / 2.0;
        double y = (a.y + b.y) / 2.0;
        c.x = x - l * sin * 0.5;
        c.y = y + l * cos * 0.5;
        d.x = x + l * sin * 0.5;
        d.y = y - l * cos * 0.5;
        cout << fixed << setprecision(10) << c.x << " " << c.y << " " << d.x << " " << d.y << endl;
    }  
    return 0;
}
```

## UVaOJ 579

时钟每小时走 $30^\circ$，分钟每分钟走 $6^\circ$，模拟即可。

```cpp
#include <stdio.h>
#include <stdlib.h>
 
using namespace std;
 
int main()
{
    int h, m;
    while(scanf("%d:%d", &h, &m) != EOF)
    {
        if(h == 0 && m == 0) { break; }
        if(h == 12) { h = 0; }
        double dAngle = (h * 30.0 + m / 2.0) - m * 6.0;
        if(dAngle < 0) { dAngle = -dAngle; }
        if(dAngle > 180) { dAngle = 360 - dAngle; }
        printf("%.3f\n", dAngle);
    }
    return 0;
}
```

## UVaOJ 375

等腰三角形内接圆直到半径小于 $10^{-6}$，根据几何关系推得半径 $$r = \tan{\frac{1}{2}\cdot\left[\arctan{\frac{2\cdot \mathrm{Height}}{\mathrm{Width}}}\right]}\cdot \frac{\mathrm{Width}}{2} $$。

```cpp
#include <stdio.h>
#include <math.h>
 
using namespace std;
 
const double PI = 4.0 * atan(1.0);
 
int main()
{
    int T;
    double x, y;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++)
    {
        scanf("%lf%lf", &x, &y);
        double dSum = 0;
        double r = tan(atan(y / x * 2) / 2) * x / 2;
        while(r >= 1E-6)
        {
            dSum += r;
            x = x / y * (y - 2 * r);
            y -= 2 * r;
            r = tan(atan(y / x * 2) / 2) * x / 2;
        }
        printf("%13.6lf\n", 2 * PI * dSum);
        if(i != T) { printf("\n"); }
    }
    return 0;
}
```

## UVaOJ 10387

根据几何关系，速度 $v = L / t$，角度为 $$\arctan{\frac{y}{x}} \times \frac{180}{\pi}$$

```cpp
#include <iostream>
#include <iomanip>
#include <math.h>
 
using namespace std;
 
int main()
{
    double PI = acos(-1.0);
    double a, b, s, m, n;
    while(cin >> a >> b >> s >> m >> n)
    {
        if(a == 0 && b == 0 && s == 0 && m == 0 && n == 0) { break; }
        double x = a * m, y = b * n;
        double l = hypot(x, y);
        cout << fixed << setprecision(2) << atan(y / x) * 180.0 / PI << " " << l / s << endl;
    }
    return 0;
}
```

## UVaOJ 10112

枚举各个点，判断是否满足条件，求三角形面积可以使用三阶行列式，判断点是否在三角形内可以使用 $S_{\triangle ABC} = S_{\triangle ABD} + S_{\triangle ACD} + S_{\triangle BCD}$ 来判断。

```cpp
#include <iostream>
#include <string>
#include <math.h>
 
using namespace std;
 
const int MAX = 128;
 
struct Tri
{
    char dwLabel;
    int x, y;
};
 
Tri pTri[MAX];
 
double fabs(double x);
double Area(int i, int j, int k);
bool Check(int i, int j, int k, int nPos);
string Solve(int N);
 
int main()
{
    int N;
     
    while(1)
    {
        cin >> N;
        if(N == 0) { break; }
        cin.ignore();
        for(int i = 1; i <= N; i++)
        {
            cin >> pTri[i].dwLabel >> pTri[i].x >> pTri[i].y;
            cin.ignore();
        }
        cout << Solve(N) << endl;
    }
    return 0;
}
 
string Solve(int N)
{
    double dMax = 0;
    string strAns = "000";
    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= N; j++)
        {
            if(i == j) { continue; }
            for(int k = 1; k <= N; k++)
            {
                if(k == i || k == j) { continue; }
                int nPos;
                for(nPos = 1; nPos <= N; nPos++)
                {
                    if(nPos == i || nPos == j || nPos == k) { continue; }
                    if(Check(i, j, k, nPos)) { break; }
                }
                if(nPos == N + 1 && Area(i, j, k) > dMax)
                {
                    dMax = Area(i, j, k);
                    strAns[0] = pTri[i].dwLabel;
                    strAns[1] = pTri[j].dwLabel;
                    strAns[2] = pTri[k].dwLabel;
                }
            }
        }
    }
    return strAns;
}
 
double Area(int i, int j, int k)
{ return fabs(0.5 * ((pTri[k].y - pTri[i].y) * (pTri[j].x - pTri[i].x) - (pTri[j].y - pTri[i].y) * (pTri[k].x - pTri[i].x))); }
 
bool Check(int i, int j, int k, int nPos)
{
    double dSum = Area(i, j, nPos) + Area(i, k, nPos) + Area(j, k, nPos);
    double dGap = dSum - Area(i, j, k);
    return (fabs(dGap) < 1E-8);
}
```

终于把小白书第一部分的推荐题目刷完了，总计 65 道。
