# 算法专题：不定方程


关于这个算法，主要是参考 NOIP2012 Day2 T1。即这里所讲的是求解这样一个线性模方程： $$ ax\equiv 1\mod{p} $$ 的最小正整数解。

去年我是暴搜做的，当时什么都不会。今天在这里介绍两种算法，一种是我国古代数学家秦九韶发明的「大衍求一术」，还一种是著名的「扩展欧几里德算法」。

首先来看一下大衍求一术。这里只介绍它的计算方法，至于证明可以参考扩展欧几里德算法。

**例1**：求解方程 $ 23x\equiv 1\mod{97} $ 。

**解**：我们只需要列出下面这张表就可以得到求解 $$ \begin{matrix}23^{1} & 23^{1} & 3^{17} & 3^{17} & 1^{38}\\\ 97^{0} & 5^{4} & 5^{4} & 2^{21} & 2^{21}\end{matrix} $$ 结果就是 38。

接下来我们来理论化的表述一下这个算法的过程：

假设输入 $ a,b $ 满足 $ a>b $ 。那么我们用 $ a_{n},A_{n} $ 分别表示第一行的底数和奇数， $ b_{n},B_{n} $ 分别表示第二行的底数和奇数，如果 $ a_{i}>b_{i} $ ，那么 $ a_{i+1}=a_{i}\mod{b_{i}},A_{i+1}=A_{i}+B_{i}\cdot \left [ \frac{a_{i}}{b_{i}} \right ],b_{i+1}=b_{i},B_{i+1}=B_{i} $ ；如果 $ a_{i}<b_{i} $ 则上面的结论倒过来即可。

算法结束当且仅当 $ a_{i}=1 $ ，此时 $ A_{i} $ 即为所求的最小正整数解。

**例2**：求解方程 $ 97x\equiv 1\mod{23} $ 。

**解**：我们只需要列出下面这张表就可以得到求解 $$ \begin{matrix}97^{1} & 5^{1} & 5^{1} & 2^{5} & 2^{5} & \\\ 23^{0} & 23^{0} & 3^{4} & 3^{4} & 1^{9} & 1^{14}\end{matrix} $$ 结果就是 14。

对于这个结果，如果1最先出现在下面一行，则需要再计算一次，而且这次计算必须使得余数是1。

假设输入 $ a,b $ 满足 $ a<b $ 。中间的步骤和之前一行，在计算过程中必然存在一个 $ i $ 使得 $ b_{i}=1 $ ，此时我们只需计算 $ B_{i+1} $ 即可得到结果。其中 $ B_{i+1}=A_{i}+B_{i}\cdot \left(a_{i} - 1\right) $ 。

代码如下：

```cpp
#include <iostream>

using namespace std;

struct Num
{
    int nBase, nIndex;    // 分别表示底数和奇数
};

Num x, y;

int main()
{
    cin >> x.nBase >> y.nBase;
    x.nIndex = 1; y.nIndex = 0;    // 初始化
    if(x.nBase < y.nBase)
    {
        while(1)
        {
            if(x.nBase == 1 || x.nBase == 0)    // 循环出口
            { cout << x.nIndex << endl; break; }
            if(x.nBase < y.nBase)    // 模拟计算过程
            {
                int nDiv = y.nBase / x.nBase;
                if(y.nBase % x.nBase == 0)
                { nDiv--; }
                y.nBase %= x.nBase;
                y.nIndex += nDiv * x.nIndex;
            }
            else
            {
                int nDiv = x.nBase / y.nBase;
                if(x.nBase % y.nBase == 0)
                { nDiv--; }
                x.nBase %= y.nBase;
                x.nIndex += nDiv * y.nIndex;
            }
        }
    }
    else
    {
        while(1)
        {
            if(y.nBase == 1)    // 出口
            {
                int nDiv = x.nBase - 1;
                cout << nDiv * y.nIndex + x.nIndex << endl;    // 求出结果
                break;
            }
            if(x.nBase < y.nBase)    // 模拟计算过程
            {
                int nDiv = y.nBase / x.nBase;
                if(y.nBase % x.nBase == 0)
                { nDiv--; }
                y.nBase %= x.nBase;
                y.nIndex += nDiv * x.nIndex;
            }
            else
            {
                int nDiv = x.nBase / y.nBase;
                if(x.nBase % y.nBase == 0)
                { nDiv--; }
                x.nBase %= y.nBase;
                x.nIndex += nDiv * y.nIndex;
            }
        }
    }
    return 0;
}
```

可能上面的算法对于某些人来说比较晦涩，我们下面来介绍一下扩展欧几里德算法。首先介绍一个定理：

**方程 $ ax+by=\gcd\left ( a,b \right ) $ 一定有解。**

这样我们的问题就可以转化为求方程 $ ax+b\cdot \left ( -y \right )=1 $ ，在这里，我们先求出方程 $ ax+b\cdot \left ( -y \right )=\gcd\left(a,b\right) $ 的解，然后只要将结果除以 $ \gcd\left(a,b\right) $ 就行了。

下面来推导一下扩展欧几里德算法。

我们已知 $$ ax+by=\gcd\left ( a,b \right ) $$ 且 $$ \gcd\left ( a,b \right )=\gcd\left(b,a\mod b \right ) $$ 不妨设 $$ bx{}'+\left ( a\mod b \right )y{}'=\gcd\left ( b,a\mod b \right ) $$ 此时就有 $$ bx{}'+\left ( a\mod b \right )y{}'=ax+by $$ 展开得到 $$ bx{}'+\left ( a-\left [ \frac{a}{b} \right ]\cdot b \right )y{}'=ax+by $$ 化简得 $$ ay{}'+b\left (x{}'-\left [ \frac{a}{b} \right ]\cdot y{}'  \right )=ax+by $$ 因此可以得到 $$ x=y{}',y=x{}'-\left [ \frac{a}{b} \right ]\cdot y{}' $$ 这样我们就可以用递归来实现扩展欧几里德算法了。

代码如下：

```cpp
#include <iostream>

using namespace std;

typedef long long LL;

LL A, B, C, X = 0, Y = 0;

LL gcd(LL a, LL b);
void exgcd(LL a, LL b, LL &x, LL &y);

int main()
{
    cin >> A >> B;
    C = gcd(A, B);
    exgcd(A, -B, X, Y);
    while(X < 0) { X += B; }    // 找最小正整数
    cout << X << endl;
    return 0;
}

void exgcd(LL a, LL b, LL &x, LL &y)
{
    if(a == 0)
    {
        x = 0; y = C / b;    // 边界
    }
    else
    {
        exgcd(b % a, a, x, y);
        y = x;        // 递推公式
        x = (C - b * y) / a;
    }
}

LL gcd(LL a, LL b)    // 求解最大公倍数
{
    if(b == 0) { return a; }
    else
    {
        return gcd(b, a % b);
    }
}
```

相比之下扩展欧几里德更容易理解一点，并且没有大衍求一术那么多特殊情况要处理，比较方便。
