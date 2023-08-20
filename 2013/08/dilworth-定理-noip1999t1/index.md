# Dilworth 定理 - NOIP1999T1


题目是经典的导弹拦截。第一问很有信心的写下了最长非增序列。第二问就懵了。后来看了题解，有一个“Dilworth 定理”，现在将定理的表述和证明整理如下：

这是一个关于偏序集的定理。偏序集即偏序集合。

**偏序的概念**：设 $ \textbf{A} $ 是一个非空集合。 $ P $ 是 $ \textbf{A} $ 上的一个关系，若关系 $ P $ 是自反的、反对称的、传递的，则称 $ P $ 是集合 $ \textbf{A} $ 上的偏序关系。

即 $ P $ 满足下列条件：
1.  $ \forall a\in\textbf{A},\left ( a,a \right )\in P $ ；
2. 若 $ \left ( a,b \right )\in P,\left ( b,a \right )\in P $ ，则 $ a=b $ ；
3. 若 $ \left ( a,b \right )\in P,\left ( b,c \right )\in P $ ，则 $ \left ( a,c \right )\in P $ 。
我们用 $ a\leq b $ 表示 $ \left ( a,b \right )\in P $ 。

注：“ $ \leq $ ”只是符号，不代表不等关系。

例如， $ \left ( \textbf{A},\leq \right ) $ 是一个偏序集，我们定义 $ A=\left \\{ 1,2,3 \right \\} $ ，偏序 $ \leq $ 在 $ \textbf{A} $ 上表现为大于等于关系，则有： $ \leq =\left \\{ \left \langle 3,3 \right \rangle,\left \langle 3,2 \right \rangle,\left \langle 3,1 \right \rangle\left \langle 2,2 \right \rangle,\left \langle 2,1 \right \rangle,\left \langle 1,1 \right \rangle \right \\} $ 。

我们再来通过下面几个例子进一步了解偏序集：

1. 实数集上的小于等于关系是一个偏序关系。
2. 设 $ \textbf{S} $ 是集合， $ P\left(\textbf{A}\right) $ 是 $ \textbf{S} $ 的所有子集构成的集合，定义 $ P\left(\textbf{A}\right) $ 中两个元素 $ \textbf{A}\leq \textbf{B} $ 当且仅当 $ \textbf{A} $ 是 $ \textbf{B} $ 的子集，则 $ P\left(\textbf{A}\right) $ 在这个关系下成为偏序集。
3. 设 $ \textbf{N} $ 是正整数集，定义 $ m\leq n $ 当且仅当 $ m $ 能整除 $ n $ ，不难验证这是一个偏序关系。

在偏序集中，有一个非常著名的定理，叫做“Dilworth 定理”。在介绍这个定理之前，我们需要介绍几个术语：

令 $ \left ( \textbf{A},\leq \right ) $ 是一个偏序集，对于集合中的两个元素 $ a,b $ ，如果有 $ a\leq b $ 或者 $ b\leq a $ ，则称 $ a $ 和 $ b $ 是可比的，否则 $ a $ 和 $ b $ 不可比。

**例**： $ \left ( \textbf{A},\leq \right ) $ 是偏序集，其中 $ \textbf{A}=\left \\{ 1,2,3,4,5 \right \\} $ ，其中 $ \leq $ 是整除关系，那么对任意的 $ x\in P $ 都有 $ 1\leq x $ ,所以 $ 1 $ 和 $ 1,2,3,4,5 $ 都是可比的，但是 $ 2 $ 不能整除 $ 3 $ ，且 $ 3 $ 不能整除 $ 2 $ ，所以 $ 2 $ 和 $ 3 $ 是不可比的。

在X中，对于元素 $ a $ ，如果任意元素 $ b $ ，由 $ b\leq a $ 得出 $ b=a $ ，则称 $ a $ 为极小元。

一个反链 $ \textbf{A} $ 是 $ \textbf{X} $ 的一个子集，它的任意两个元素都不能进行比较。
一个链 $ \textbf{C} $ 是 $ \textbf{X} $ 的一个子集，它的任意两个元素都可比。

**定理1**：令 $ \left ( \textbf{A},\leq \right ) $ 是一个有限偏序集，并令 $ r $ 是其最大链的大小。则 $ \textbf{X} $ 可以被划分成 $ r $ 个但不能再少的反链。

**定理2（Dilworth 定理）**：令 $ \left ( \textbf{A},\leq \right ) $ 是一个有限偏序集，并令 $ m $ 是反链的最大的大小。则 $ \textbf{X} $ 可以被划分成 $ m $ 个但不能再少的链。

**证明**：这里只对定理1进行证明，定理2的证明留给读者自行证明。
设 $ p $ 为最少反链个数；
1. 先证明 $ \textbf{X} $ 不能划分成小于 $ r $ 个反链。由于 $ r $ 是最大链 $ \textbf{C} $ 的大小， $ \textbf{C} $ 中任两个元素都可比，因此 $ \textbf{C} $ 中任两个元素都不能属于同一反链。所以 $ p\geq r $ 。
2. 设 $ \mathbf{X_{1}}=\mathbf{X} $ ， $ \mathbf{A_{1}} $ 是 $ \mathbf{X_{1}} $ 中的极小元的集合。从 $ \mathbf{X_{1}} $ 中删除 $ \mathbf{A_{1}} $ 得到 $ \mathbf{X_{2}} $ 。注意到对于 $ \mathbf{X_{2}} $ 中任意元素 $ a_{2} $ ，必存在 $ \mathbf{X_{1}} $ 中的元素 $ a_{2} $ ，使得 $ a_{1}\leq a_{1} $ 。令 $ \mathbf{A_{2}} $ 是 $ \mathbf{X_{2}} $ 中极小元的集合，从 $ \mathbf{X_{2}} $ 中删除 $ \mathbf{A_{2}} $ 得到 $ \mathbf{X_{3}} $ ……最终，会有一个 $ \mathbf{X_{k}} $ 非空而 $ \mathbf{X_{k+1}} $ 为空。于是 $ \mathbf{A_{1}},\mathbf{A_{2}},\cdots ,\mathbf{A_{k}} $ 就是 $ \mathbf{x} $ 的反链的划分，同时存在链 $ a_{1}\leq a_{2}\leq\cdots\leq a_{k} $ ，其中 $ a_{i} $ 在 $ \mathbf{A_{i}} $ 内。由于 $ r $ 是最长链大小，因此 $ r\geq k $ 。由于 $ \mathbf{x} $ 被划分成了 $ k $ 个反链，因此 $ r=k\geq p $ 。因此 $ r=p $ ，得证。

那么这道题目就化简为求一遍最长非增序列和最长上升序列，DP 即可。

```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 128;

int N, f1[MAX], f2[MAX], ans1, ans2;
vector<int> pVec;

int main()
{
    cin >> N;
    int nTmp;
    for(int i = 0; i < N; i++)
    {
        cin >> nTmp;
        pVec.push_back(nTmp);
    }
    for(int i = 0; i < pVec.size(); i++)
    { f1[i] = f2[i] = 1; }
    for(int i = 1; i < pVec.size(); i++)
    {
        for(int j = 0; j < i; j++)
        {
            if(pVec[j] >= pVec[i] && f1[j] + 1 > f1[i])
            { f1[i] = f1[j] + 1; }
            if(pVec[j] < pVec[i] && f2[j] + 1 > f2[i])
            { f2[i] = f2[j] + 1; }
        }
    }
    ans1 = 0; ans2 = 0;
    for(int i = 0; i < pVec.size(); i++)
    {
        if(f1[i] > ans1) { ans1 = f1[i]; }
        if(f2[i] > ans2) { ans2 = f2[i]; }
    }
    cout << ans1 << " " << ans2 << endl;
    return 0;
}
```
