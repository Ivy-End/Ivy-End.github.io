# ACM-ICPC 寒假练习 06


这一次主要是数论专题，感到思维量比上一次的数学题要多多了。同样的问题也是英文题看起来有些吃力。

## UVaOJ 575

这应该算不上是一个数论题，它重新定义了一种进制转换的公式，然后根据公式计算即可。

```cpp
#include <iostream>
 
using namespace std;
 
int Pow(int x, int y);
 
int main()
{
    string x;
    while(cin >> x)
    {
        if(x == "0") { break; }
        int ans = 0;
        for(int i = 0; i < x.length(); i++)
        { ans += (x[i] - '0') * (Pow(2, x.length() - i) - 1); }
        cout << ans << endl;
    }
    return 0;
}
 
int Pow(int x, int y)
{
    int ret = 1;
    for(int i = 1; i <= y; i++)
    { ret *= x; }
    return ret;
}
```

## UVaOJ 10110

这是一道典型的数论题，最后亮着的灯，它的开关一定被拨动了奇数次。所以，我们只要看它的因数个数的奇偶性。

记得高中数学竞赛的时候遇到过类似的题目，有一个结论——完全平方数的因数有奇数个，非完全平方数的因数有偶数个。

这个命题的证明有些繁琐，读者自己思考一下就会发现，这个结论是正确的。

```cpp
#include <iostream>
#include <math.h>
 
using namespace std;
 
int main()
{
    long long N;
    while(cin >> N)
    {
        if(N == 0) { break; }
        long long x = (long long)floor(sqrt(N * 1.0) + 0.5);
        if(x * x == N) { cout << "yes" << endl; }
        else { cout << "no" << endl; }
    }
    return 0;
}
```

## UVaOJ 550

类似倒推的思想。

首先，我们有$B$、$D$、$M$ ——分别代表进制、最后一位数字、乘数。我们不妨记满足条件的数字为 $N$，且 $N \cdot M = S$。

有了上述假设，我们就可以进行如下操作：

$N$ 的最后一位数字为 $D$，那么 $S$ 的最后一位数字记为 $T = D \cdot M \mod B$（这里为 $B$ 进制）。

这时候需要注意的是，$S$ 的最后一位数字，恰好是 $N$ 的倒数第二位数字，那么也就是说 $N$ 的倒数第二位数字为 $T$。

有了 $N$ 的倒数第二位数字，我们就可以求出 $S$ 的倒数第二位数字为 $T\cdot M \mod B + T / B$（其中 $T / B$ 为进位），以此类推。

直到我们计算出来的数字与一开始给定的数字 $D$ 相当，这时候的 $N$ 的位数即为答案。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int B, D, M;
    while(cin >> B >> D >> M)
    {
        int nCnt = 1;
        int nD = D;
        while((nD = M * (nD % B) + (nD / B)) && nD != D)
        { nCnt++; }
        cout << nCnt << endl;
    }
    return 0;
}
```

## UVaOJ 568

由于数据范围比较小，我们可以直接算出来，记得在每次计算的时候把末尾的 0 去掉，同时为了防止溢出，我们可以对 10 的一个幂次取模。

这里选择了 10000，因为最大的 $N$ 为 10000。但是这个选取并不是任意的，比如我们取 10，计算出来的结果就会出错。

```cpp
#include <iostream>
#include <iomanip>
 
using namespace std;
 
const int MAX = 100000;
 
int main()
{
    int N;
    while(cin >> N)
    {
        int ans = 1;
        for(int i = 1; i <= N; i++)
        {
            ans *= i;
            while(ans % 10 == 0) { ans /= 10; }
            ans %= MAX;
        }
        cout << setw(5) << N << " -> " << ans % 10 << endl;
    }
}
```

## UVaOJ 408

这道题目就是求满足 $$\mathrm{seed}(x + 1) = [\mathrm{seed}(x) + \mathrm{STEP}] \mod \mathrm{MOD}$$ 的 $\mathrm{seed}(x)$ 能否组成模 $\mathrm{MOD}$ 的剩余系。

有一个结论，若 $\mathrm{gcd}(\mathrm{STEP}, \mathrm{MOD}) = 1$，则可以组成一个模 $\mathrm{MOD}$ 的剩余系。

我们可以这样来证明：

$$\begin{align*}\mathrm{seed}(x + 1) &= [\mathrm{seed}(x) + \mathrm{STEP}] \mod \mathrm{MOD} \\\ &= [\mathrm{seed}(x - 1) + 2 \cdot \mathrm{STEP}] \mod \mathrm{MOD} \\\ &= [\mathrm{seed}(x - 2) + 3 \cdot \mathrm{STEP}] \mod \mathrm{MOD} \\\ &= \cdots \\\ &= [\mathrm{seed}(0) + (x + 1) \cdot \mathrm{STEP}] \mod \mathrm{MOD}\end{align*}$$

若不能满足条件，则必定存在 $0 \leq i \neq j < \mathrm{MOD}$ 的整数 $i$ 和 $j$ 满足：$\mathrm{seed}(i) = \mathrm{seed}(j)$，即 $$[\mathrm{seed}(0) + i \cdot \mathrm{STEP}] \mod \mathrm{MOD} = [\mathrm{seed}(0) +j \cdot \mathrm{STEP}] \mod \mathrm{MOD}$$ 即 $$((j - i) \cdot \mathrm{STEP}) \mod \mathrm{MOD} = 0$$ 又 $j - i < \mathrm{MOD}$，所以 $\mathrm{gcd}(\mathrm{STEP}, \mathrm{MOD}) \neq 1$，即 $ \mathrm{STEP} $ 中含有 $\mathrm{MOD}$ 的因子——若 $\mathrm{MOD}$ 整除 $j - i$，那么 $\mathrm{STEP}$ 中含有 $\mathrm{MOD}$ 的因子 $\mathrm{MOD} / (j - i)$，反之，$\mathrm{STEP}$ 含有因子 $\mathrm{MOD}$。

故需满足题设条件，必有 $$\mathrm{gcd}(\mathrm{STEP}, \mathrm{MOD}) = 1$$

证毕。

```cpp
#include <iostream>
#include <iomanip>
 
using namespace std;
 
int gcd(int x, int y);
 
int main()
{
    int x, y;
    while(cin >> x >> y)
    {
        if(gcd(x, y) == 1) { cout << setw(10) << x << setw(10) << y << "    Good Choice" << endl; }
        else { cout << setw(10) << x << setw(10) << y << "    Bad Choice" << endl; }
        cout << endl;
    }
    return 0;
}
 
int gcd(int x, int y)
{
    if(y == 0) { return x; }
    else { return gcd(y, x % y); }
}
```

## UVaOJ 350

简单模拟，没有想到数论的做法。不断的计算 $L$，直到发现重复。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 10240;
 
int f[MAX];
 
int main()
{
    int nCase = 0;
    int Z, I, M, L;
    while(cin >> Z >> I >> M >> L)
    {
        if(Z == 0 && I == 0 && M == 0 && L == 0) { break; }
        int nCnt = -1;
        memset(f, 0, sizeof(f));
        do
        {
            L = ((Z % M) * (L % M) + (I % M)) % M;
            f[L]++;
            nCnt++;
        }
        while(f[L] == 1);
        cout << "Case " << ++nCase << ": " << nCnt << endl;
    }
    return 0;
}
```

## UVaOJ 10061

要求 $N!$ 转化为 $B$ 进制后的位数以及末尾 0 的个数。

为了简化问题，我们首先来看 10 进制的情况。

我们知道，在 10 进制情况下，我们有 $$f(N) = f(N / 5) + N / 5$$

证明：令 $k = N / 5$，则 $$N! = 5k \cdot 5(k - 1) \cdot \cdots \cdot 10 \cdot 5 \cdot a = 5^k \cdot k! \cdot a$$ 其中 $a$ 为不能被 5 整除的部分。因此， $$f(N) = f(k) + k = f(N / 5) + N / 5$$ 证毕。

有了上面的结论，我们可以大胆猜测，对于 $B$ 进制数，我们有 $$f(N, B) = f(N / X, B) + N / X$$ 其中 $X$ 为 $B$ 的最大因数，证略。

这样，我们就解决了第一个问题，对于第二个问题，我们可以直接取对数，计算 $\log{\left(N!\right)}$，即 $$\log{1} + \log{2} + \log{3} + \cdots + \log{N}$$

```cpp
#include <iostream>
#include <math.h>
 
using namespace std;
 
const int MAX = 1 << 20;
 
double pLog[MAX];
 
int main()
{
    for(int i = 1; i < MAX; i++)
    { pLog[i] = pLog[i - 1] + log(i); }
    int N, B;
    while(cin >> N >> B)
    {
        int nLen = (int)floor(pLog[N] / log(B) + 1E-9) + 1;
        int nMaxFactor, nFactorCnt = 0, nCnt = 0;
        for(int i = 2; i <= B; i++)
        {
            nFactorCnt = 0;
            while(B % i == 0)
            {
                nMaxFactor = i;
                nFactorCnt++;
                B /= i;
            }
        }
        while(N)
        {
            N /= nMaxFactor;
            nCnt += N;
        }
        cout << nCnt / nFactorCnt << " " << nLen << endl;
    }
    return 0;
}
```

## UVaOJ 10392

质因数分解即可，要注意题目中说只有一个大于 1,000,000 的因子，但是还是需要处理本身就是素数以及除到最后不等于 1 的情况。

```cpp
#include <iostream>
#include <memory.h>
#include <vector>
 
using namespace std;
 
const int MAX = 1000020;
 
vector<int> pVec;
bool pVisited[MAX];
 
int main()
{
    memset(pVisited, false, sizeof(pVisited));
    for(int i = 2; i < MAX; i++)
    {
        if(!pVisited[i]) { pVec.push_back(i); }
        for(int j = i + i; j < MAX; j += i)
        { pVisited[j] = true; }
    }
     
    long long N;
    while(cin >> N)
    {
        if(N < 0) { break; }
        int nCnt = 0;
        for(int i = 0; i < pVec.size(); i++)
        {
            if(N < pVec[i]) { break; }
            while(N % pVec[i] == 0)
            {
                cout << "    " << pVec[i] << endl;
                N /= pVec[i];
                nCnt++;
            }
        }
        if(nCnt == 0 || N != 1) { cout << "    " << N << endl; }
        cout << endl;
    }
    return 0;
}
```

## UVaOJ 10879

这道题目的样例好像有点吓唬人，其实里面应该有 spj 的。

数据量不大，直接分解因式即可。

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int T, N;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> N;
        cout << "Case #" << i << ": " << N;
        int nCnt = 0;
        for(int j = 2; j * j <= N; j++)
        {
            if(N % j == 0)
            {
                cout << " = " << j << " * " << N / j;
                nCnt++;
            }
            if(nCnt == 2) { break; }
        }
        cout << endl;
    }
    return 0;
}
```

数论专题很多都是看着题解做的，因为很多都不知道，学到了很多新的东西。
