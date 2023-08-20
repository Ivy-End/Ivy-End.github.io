# 算法专题：欧拉函数


昨天终于把欧拉函数想通了，现在总结一下。

欧拉函数 $ \varphi \left ( N \right ) $ 表示小于或等于 $ N $ 的正整数中与 $ N $ 互质的数的个数。又称 $ \varphi $ 函数、欧拉商数。

下面介绍欧拉函数的几个性质：

* $ \displaystyle\varphi\left ( 1 \right )=1 $；
* $ \displaystyle\varphi \left( N\right )=N\cdot\prod_{p\mid N}\left ( \frac{p-1}{p} \right ) $；
* $ \displaystyle\varphi \left ( p^{k} \right ) = p^{k}-p^{k-1}=\left(p-1 \right )\cdot p^{k-1} $ ，其中 $ p $ 为质数；
* $ \displaystyle\varphi \left(mn \right )=\varphi \left(m \right )\cdot \varphi \left(n \right ) $ ，其中 $ \gcd \left ( m,n \right )=1 $ 。

我们根据这几个性质就可以求出欧拉函数。

基本思路是首先置 $ \varphi \left ( N \right )=N $ ，然后再枚举素数 $ p $ ，将 $ p $ 的整数倍的欧拉函数 $ \varphi \left ( kp \right ) $ 进行操作 $ \varphi \left ( kp \right )=\varphi \left ( kp \right )\cdot \frac{p-1}{p} $ 即可。

代码如下：

```cpp
#include <iostream>

using namespace std;

const int MAX = 1024;

int N;
int p[MAX], phi[MAX];

int main()
{
    cin >> N;
    for(int i = 1; i <= N; i++)    // 初始化
    { p[i] = 1; phi[i] = i; }
    p[1] = 0;    // 1不是素数
    for(int i = 2; i <= N; i++)    // 筛素数
    {
        if(p[i])
        {
            for(int j = i * i; j <= N; j += i)
            { p[j] = 0; }
        }
    }
    for(int i = 2; i <= N; i++)    // 求欧拉函数
    {
        if(p[i])
        {
            for(int j = i; j <= N; j += i)    // 处理素因子p[i]
            {
                phi[j] = phi[j] / i * (i - 1);    // 先除后乘，防止中间过程超出范围
            }
        }
    }
    cout << "Primes: " << endl;
    for(int i = 1; i <= N; i++)
    { if(p[i]) { cout << i << " "; } }
    cout << endl;
    cout << "Euler Phi Function: " << endl;
    for(int i = 1; i <= N; i++)
    { cout << phi[i] << " "; }
    return 0;
}
```

以上是关于欧拉函数的求法，对于它的应用，这里暂且介绍一个——求解原根的个数。

对于原根的定义，我们可以这样来叙述：

若存在一个实数 $ a $ ，使得 $ a^{i}\mod{N},a\in\left \\{ 1,2,3,\cdots ,N \right \\} $ 的结果各不相同，我们就成实数 $ a $ 为 $ N $ 的一个原根。

原根的个数等于 $ \varphi \left ( \varphi \left ( N \right ) \right ) $ 。这样我们就可以很方便的求出原根的个数。

代码如下：

```cpp
#include <iostream>
#include <math.h>

using namespace std;

typedef unsigned long long ull;

ull N;

ull phi(ull x);

int main()
{
    cin >> N;
    cout << phi(phi(N)) << endl;
    return 0;
}

ull phi(ull x)
{
    ull ans = x;
    ull m = (ull)sqrt(x);
    for(ull i = 2; i <<= m; i++)
    {
        if(x % i == 0)    // 求素因子
        {
            ans = ans / i * (i - 1);    // 运用通项求解欧拉函数
            while(x % i == 0)    // 每个素因子只计算一次
            { x /= i; }
        }
    }
    if(x > 1)    // 防质数
    { ans = ans / x * (x - 1); }
    return ans;
}
```

关于欧拉函数的知识就介绍这么多吧，应付NOIP应该足够了。
