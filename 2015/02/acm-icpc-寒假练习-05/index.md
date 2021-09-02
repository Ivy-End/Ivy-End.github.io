# ACM-ICPC 寒假练习 05


刷完了数学专题，感觉思维量有些大，同时也对浮点数的运算有些接触。最重要的还是感觉有时候题目读起来有些吃力，需要借助中文翻译。

## UVaOJ 113

这道题目是集训的时候第一天晚上的题目，据说可以 `double` 解决，当时没有 AC。

现在重新做了一遍，需要注意的是最后输出的结果一定要转换成int，否则会 WA。

同时，`double` 转换为 `int` 的时候可以采取这样的方式：`(int)floor(x + 0.5)`。

```cpp
#include <iostream>
#include <math.h>
 
using namespace std;
 
int main()
{
    double x, y;
    while(cin >> x >> y)
    { cout << (int)floor(pow(y, 1 / x) + 0.5) << endl; }
    return 0;
}
```

## UVaOJ 10161

这道题目是通常的找规律题目，和一道《Cantor 的数表》是差不多的，需要注意奇偶不同的处理。

```cpp
#include <iostream>
#include <math.h>
 
using namespace std;
 
int main()
{
    int N;
    while(cin >> N)
    {
        if(N == 0) { break; }
        int k = ceil(sqrt(N));
        int s = (k - 1) * (k - 1);
        int d = N - s;
        int x, y;
        if(d <= k) { x = d; y = k; }
        else { x = k; y = 2 * k - d; }
        if(k & 1) { swap(x, y); }
        cout << x << " " << y << endl;
    }
    return 0;
}
```

## UVaOJ 253

这道题目如果直接考虑会非常的麻烦，我们可以考虑“颜色对”这样一个概念。

即，将互为对面的两种颜色看为一个颜色对，那么一个立方体一共有 3 个颜色对，只要匹配这三个颜色对就可以了。

```cpp
#include <iostream>
#include <string>
#include <memory.h>
 
using namespace std;
 
const int MAX = 4;
 
bool pVisited[MAX];
 
int main()
{
    string x;
    while(cin >> x)
    {
        int nCnt = 0;
        memset(pVisited, false, sizeof(pVisited));
        for(int i = 1; i <= 3; i++)
        {
            for(int j = 1; j <= 3; j++)
            {
                if((x[i - 1] == x[5 + j] && x[6 - i] == x[12 - j] ||
                    x[i - 1] == x[12 - j] && x[6 - i] == x[5 + j]) && !pVisited[j])
                {
                    nCnt++;
                    pVisited[j] = true;
                    break;
                }
            }
        }
        cout << (nCnt == 3 ? "TRUE" : "FALSE") << endl;
    }
    return 0;
}
```

## UVaOJ 621

这道题目感觉不是数学题，应该算字符串处理。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
    int N;
    string x;
    while(cin >> N)
    {
        cin.ignore();
        for(int i = 1; i <= N; i++)
        {
            getline(cin, x);
            if(x == "1" || x == "4" || x == "78") { cout << "+" << endl; }
            else if(x.substr(x.length() - 2, 2) == "35") { cout << "-" << endl; }
            else if(x[0] == '9' && x[x.length() - 1] == '4') { cout << "*" << endl; }
            else if(x.substr(0, 3) == "190") { cout << "?" << endl; }
        }
    }
    return 0;
}
```

## UVaOJ 10025

这道题目当时没有想出来怎么做，后来看了题解恍然大悟。

首先，根据对称性，我们可以只考虑 $k > 0$ 的情况。

然后，我们令 $S = \bigoplus 1\bigoplus 2\bigoplus 3\bigoplus\cdots\bigoplus N$，其中 $\bigoplus$ 为正负号。

如果将 $S$ 中任意一个 $\bigoplus$ 变换符号，那么 $S$ 的减少量或者增加量必定为偶数。

我们考虑 $\bigoplus$ 都为 $+$ 的情况，因为当 $S > k$ 的时候，我们可以改变其中的 $\bigoplus$ 来达到要求的 $k$。

因此，只要求最小的 $N$，使得 $S > k$，并且满足 $S - k$ 为偶数，因为每次变换 $\bigoplus$ 的符号对 $S$ 的改变量为偶数。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int T, K;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> K;
        if(K < 0) { K = -K; }
        int nSum = 0;
        for(int j = 1; ; j++)
        {
            nSum += j;
            if(nSum >= K && (nSum - K)  % 2 == 0)
            { cout << j << endl; break; }
        }
        if(i != T) { cout << endl; }
    }
    return 0;
}
```

## UVaOJ 591

贪心，计算变换后每列的末高度。将高于末高度的搬到低于末高度的地方即可。

```cpp
#include <iostream>
 
using namespace std;
 
const int MAX = 64;
 
int pData[MAX];
 
int main()
{
    int N, nCase = 0;
    while(cin >> N)
    {
        if(N == 0) { break; }
        int nSum = 0, ans = 0;
        cout << "Set #" << ++nCase << endl;
        for(int i = 1; i <= N; i++)
        {
            cin >> pData[i];
            nSum += pData[i];
        }
        nSum /= N;
        for(int i = 1; i <= N; i++)
        {
            if(pData[i] > nSum)
            { ans += pData[i] - nSum; }
        }
        cout << "The minimum number of moves is " << ans << "." << endl;
        cout << endl;
    }
}
```

## UVaOJ 107

这道题目需要推导公式，我们令要输出的答案分别为 $x$ 和 $y$。

假设 $k$ 代小猫（包括第一代），每个小猫帽子里有 $N$ 个小猫。

那么我们可以得到公式 $$(N + 1)^k = H,\quad N^k = C$$

两边去对数即可得到 $$k \cdot \log{\left(N + 1\right)} = \log{H},\quad k \cdot \log{N} = \log{C}$$

将 $k$ 约去，得到 $$\log{H}\cdot\log{N} = \log{\left(N + 1\right)}\cdot\log{C}$$

根据上式，我们额可以求出 $N$，即每个小猫帽子里有几个小猫。之所以约去 $k$，是为了多次运算导致浮点数误差。

求得 $N$ 以后，我们就可以进一步的求出一共有多少只小猫不在工作。这是一个等比数列 $$x = 1 + N + N^2 + N^3 + ... + N^k$$

当 $N = 1$ 时 $$x = k = \log{H} / \log{2}$$ 由 $(N + 1)^K = H$，代入 $N = 1$ 得 $2^k = H$

当 $N \neq 1$ 时 $$x = \frac{1 - N^k}{1 - N} = \frac{1 - C}{1 - N} = \frac{C - 1}{N - 1}$$

为了计算所有小猫的身高，我们可以得到另一个等比数列 $$y = H + N \cdot\left(\frac{N}{N + 1}\right)\cdot H + N^2 \cdot\left(\frac{N}{N + 1}\right)^2\cdot H + \cdots + N^k \cdot\left(\frac{N}{N + 1}\right)^k\cdot H$$

当 $N = 1$ 时 $$ y = H \cdot \left(1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots + \frac{1}{2^k}\right) = H \cdot \left(2 - \frac{1}{2^k}\right) = 2\cdot H - H \cdot\frac{1}{2^k} = 2 \cdot H - 1$$ 由 $(N + 1)^K = H$，代入 $N = 1$ 得 $2^k = H$

当 $N \neq 1$ 时 $$ y = H \cdot \frac{1 - \left(\frac{N^2}{N + 1}\right)^k}{1 - \frac{N^2}{N + 1}} = (N + 1) \cdot H - C \cdot N$$

又，当 $N = 1$ 时，必有 $C = 1$，因此我们对输入数据进行分类讨论即可。

```cpp
#include <iostream>
#include <math.h>
 
using namespace std;
 
int main()
{
    double H, C;
    while(cin >> H >> C)
    {
        if(H == 0 && C == 0) { break; }
        int x, y;
        if(C == 1)
        {
            x = ceil(log(H) / log(2));
            y = 2 * H - 1;
        }
        else
        {
            int N;
            for(N = 1; N < H; N++)
            {
                if(fabs(log(H) * log(N) - log(C) * log(N + 1)) < 1E-8)
                { break; }
            }
            x = (C - 1) / (N - 1);
            y = (N + 1) * H - C * N;
        }
        cout << x << " " << y << endl;
    }
    return 0;
}
```

##  UVaOJ 573

蜗牛爬墙，很经典的题目，要注意两点：

* 上爬的衰减因子只与第一次上爬的距离有关；
* 当上爬的距离小于0时，蜗牛不再上爬。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    double H, U, D, F;
    while(cin >> H >> U >> D >> F)
    {
        if(H == 0) { break; }
        F /= 100.0;
        int nDay = 0;
        double dNow = 0, dUp = U;
        while(1)
        {
            nDay++;
            dNow += dUp;
            dUp -= F * U;
            if(dNow > H) { cout << "success on day " << nDay << endl; break; }
            if(dUp < 0) { dUp = F = 0; }
            dNow -= D;
            if(dNow < 0) { cout << "failure on day " << nDay << endl; break; }
        }
    }
    return 0;
}
```

## UVaOJ 846

这道题目一开始完全不知道怎么做，后来百度以后才发现有规律：

| 距离 | 步长 | 距离 | 步长 |
|:-:|:-:|:-:|:-:|
| 1 | 1 | 9 | 5 |
| 2 | 2 | 10 | 6 |
| 3 | 3 | 11 | 6 |
| 4 | 3 | 12 | 6 |
| 5 | 4 | 13 | 7 |
| 6 | 4 | 14 | 7 |
| 7 | 5 | 15 | 7 |
| 8 | 5 | 16 | 7 |

我们令 $d = y - x$（其中 $x$ 和 $y$ 为输入数据），`s = floor(sqrt(d))`，规律如下：$$s = \begin{cases} 2s - 1, & s^2 = d \\\ 2s + 1, & s(s+1) < d \\\ 2s, & \mathrm{otherwise}\end{cases}$$ 当然，要注意特判相距为 0 的情况。

```
#include <iostream>
#include <math.h>
 
using namespace std;
 
int main()
{
    int T, x, y;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> x >> y;
        int d = y - x;
        if(d == 0) { cout << "0" << endl; }
        else
        {
            int s = (int)(sqrt(d * 1.0));
            if(s * s == d) { s = 2 * s - 1; }
            else if(s * (s + 1) < d) { s = 2 * s + 1; }
            else { s *= 2; }
            cout << s << endl;
        }
    }
    return 0;
}
```

## UVaOJ 10499

一开始没看懂题意。感觉在考英语。

我们假设一开始小球的半径 $R = 1$，那么表面积 $S = 4\pi$。分割成 $N$ 部分，表面积增加 $N\cdot \pi$。那么答案即为 $N / 4 \times 100 = 25N$。

注意，需要特判 1 的情况。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    long long N;
    while(cin >> N)
    {
        if(N < 0) { break; }
        long long nPercent = N * 25;
        if(N == 1) { nPercent = 0; }
        cout << nPercent << "%" << endl;
    }
    return 0;
}
```

## UVaOJ 10790

映射法：每个四边形对应一条对角线——每条对角线对应一个交点。

题目转化为求四边形的个数，即为 $$\mathrm{C}_N^2 \cdot \mathrm{C}_M^2$$

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int nCase = 0;
    long long x, y;
    while(cin >> x >> y)
    {
        if(x == 0 && y == 0) { break; }
        long long ans = x * (x - 1) * y * (y - 1) / 4;
        cout << "Case " << ++nCase << ": " << ans << endl;   
    }
    return 0;
}
```

## UVaOJ 11044

由于边缘不需要计算，那么答案就是 $$\left\lceil\frac{W-2}{3}\right\rceil \cdot \left\lceil\frac{H-2}{3}\right\rceil$$

```cpp
#include <iostream>
#include <math.h>
 
using namespace std;
 
int main()
{
    int T, W, H;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> W >> H;
        int x = (W - 2) / 3 + ((W - 2) % 3 != 0);
        int y = (H - 2) / 3 + ((H - 2) % 3 != 0);
        cout << x * y << endl;
    }
    return 0;
}
```

## UVaOJ 10719

模拟多项式除法，只要会多项式除法，写起来就非常的轻松。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
#include <sstream>
 
using namespace std;
 
const int MAX = 10240;
 
int pData[MAX], pAns[MAX];
 
int main()
{
    int k;
    string x;
    while(cin >> k)
    {
        memset(pData, 0, sizeof(pData));
        memset(pAns, 0, sizeof(pAns));
        int nCnt = 0, nPos = 1, r = 0;
        cin.ignore();
        getline(cin, x);
        istringstream iss(x);
        while(iss >> pData[++nCnt]);
        nCnt--;
        while(nPos < nCnt)
        {
            if(pData[nPos] != 0)
            {
                pAns[nPos] = pData[nPos];
                pData[nPos] = 0;
                pData[nPos + 1] += k * pAns[nPos];
            }
            nPos++;
        }
        if(pData[nPos]) { r = pData[nPos]; }
        cout << "q(x):";
        for(int i = 1; i < nPos; i++)
        { cout << " " << pAns[i]; }
        cout << endl;
        cout <<"r = " << r << endl;
         
    }
    return 0;
}
```

## UVaOJ 10177
结论题。对于 $w$ 维正方体，边长为 $N$，其中包含的正方体（$S$）、长方体（$R$）的个数为：$$ S(w) = 1^w + 2^w + 3^w + ... + N^w$$ $$R(w) = \left(\frac{N \cdot (N + 1)}{2}\right)^w - S(w)$$

这里补充一下幂级数求和公式：$$S(4) = \frac{N \cdot (N + 1) \cdot \left(3 N^2 + 3 N - 1\right)}{30}$$

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    long long N;
    while(cin >> N)
    {
        long long s2 = (N * (N + 1) * (2 * N + 1)) / 6;
        long long s3 = (N * (N + 1) / 2) * (N * (N + 1) / 2);
        long long s4 = (N * (N + 1) * (2 * N + 1) * (3 * N * N + 3 * N - 1)) / 30;
        long long r2 = (N * (N + 1) / 2) * (N * (N + 1) / 2) - s2;
        long long r3 = (N * (N + 1) / 2) * (N * (N + 1) / 2) * (N * (N + 1) / 2) - s3;
        long long r4 = (N * (N + 1) / 2) * (N * (N + 1) / 2) * (N * (N + 1) / 2) * (N * (N + 1) / 2) - s4;
        cout << s2 << " " << r2 << " " << s3 << " " << r3 << " " << s4 << " " << r4 << endl;
    }
    return 0;
}
```

## UVaOJ 10916
我们知道 $2^N < N! < 2^{(N + 1)}$，以 2 为底取对数得 $$N < \log{1} + \log{2} + \log{3} + \cdots + \log{N} < N + 1$$

这样，模拟一下就可以得到答案。

```cpp
#include <iostream>
#include <math.h>
 
using namespace std;
 
int main()
{
    int N;
    while(cin >> N)
    {
        if(N == 0) { break; }
        int k = (N - 1960) / 10 + 2;
        double dSum = 0.0;
        for(int i = 1; ; i++)
        {
            dSum += log(i) / log(2);
            if(dSum > (1 << k)) { cout << i - 1 << endl; break; }
        }
    }
    return 0;
}
```

##  UVaOJ 10970
记得在 Codeforces 上做过，当时被 hack 了。这里数据范围比较小，所以可以直接用 `int`。

$$ ans = xy - 1$$

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int x, y;
    while(cin >> x >> y)
    { cout << x * y - 1 << endl; }
    return 0;
}
```

## UVaOJ 10014

这道题目也需要推导公式。根据题目条件，我们有：$$\begin{cases}2 \cdot a_1 = a_0 + a_2 - 2 \cdot c_1\\\ 2 \cdot a_2 = a_1 + a_3 - 2 \cdot c_2\\\ 2 \cdot a_3 = a_2 + a_4 - 2 \cdot c_3\\\ \cdots \\\ 2 \cdot a_N = a_{N-1} + a_{N+1} - 2 \cdot c_N \end{cases}$$ 将第一个式子分别加到下面 $N - 1$ 个式子上，得到：$$\begin{cases}2 \cdot a_1 = a_0 + a_2 - 2 \cdot c_1\\\ a_1 + a_2 = a_0 + a_3 - 2 \cdot \left(c_1 + c_2\right)\\\ a_1 + a_3 = a_0 + a_4 - 2 \cdot \left(c_1 + c_2 + c_3\right)\\\ \cdots \\\ a_1 + a_N = a_0 + a_{N+1} - 2 \cdot \left(c_1 + c_2 + c_3 + \cdots + c_N\right) \end{cases}$$ 将上面 $N$ 个式子累加，得到：$$ (N + 1) \cdot a_1 = N \cdot a_0 + a_N + 1 - 2 \cdot \left(N \cdot c_1 + (N - 1) \cdot c_2 + (N - 2) \cdot c_3 + \cdots + c_N\right)$$ 由此，便可得到 $a_1$。

```cpp
#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main()
{
    int T, N;
    double s, e;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        double ans = 0, dTmp;
        cin >> N;
        cin >> s >> e;
        ans = N * s + e;
        for(int j = 1; j <= N; j++)
        {
            cin >> dTmp;
            ans -= 2.0 * (N - j + 1) * dTmp;
        }
        cout << fixed << setprecision(2) << ans / (N + 1) << endl;
        if(i != T) { cout << endl; }
    }
    return 0;
}
```

刷完数学专题，感觉数学题目的思维量还是很大的，同时也要注意浮点数对结果造成的误差。
