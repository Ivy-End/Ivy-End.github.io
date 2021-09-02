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
