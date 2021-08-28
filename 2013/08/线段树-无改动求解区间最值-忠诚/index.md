# 线段树 – 无改动求解区间最值 – 忠诚


昨天研究了一下线段树，发现原来线段树有这么多实现方式。当然，对于非递归自底向上线段树，俗称 ZKW 线段树还是不太理解。而且我的实现方式还是用的指针，所以效率不是特别高。首先记录一下自己对于线段树的理解吧。我们用忠诚这道题目来做例子。

线段树可以直观的表示为下面这张图：


{{< image src="/images/2013/线段树 – 无改动求解区间最值 – 忠诚/线段树.jpg" caption="线段树示意图" >}}

对于一个给定的区间，不断的二分，直到区间变为一个点为止。当然，平时我们所需要的线段树不是这么简陋的，我们需要一些数据域：

```cpp
struct Node
{
    int nLeft, nRight;
    unsigned long long nMoney;
    Node *pLeft, *pRight;
};
```

有了节点的数据结构，我们需要构建这棵树，我们使用递归的方式生成这棵树，当然，在生成的过程中也可以进行一些初始化操作：

```cpp
Node* Build(int l, int r)
{
    Node *pNode = new Node();
    // Init data
    if(l == r) { pNode->nMoney = pMoney[l - 1]; }
    else { pNode->nMoney = 0; }

    pNode->nLeft = l; pNode->nRight = r;
    if(l == r) { return pNode; }
    int nMid = (l + r) / 2;
    pNode->pLeft = Build(l, nMid);
    pNode->pRight = Build(nMid + 1, r);
    return pNode;
}
```

接下来就是线段树最核心的部分了，查找。查找的时候可能有三种情况：

* 所需要查询的区间全部落在左儿子的区间中，递归左儿子。
* 所需要查询的区间全部落在右儿子的区间中，递归右儿子。
* 所需要查询的区间一部分在左儿子的区间中，另一部分在右儿子的区间中，递归左儿子，右儿子，根据需要进行一些操作，例如相加，取最大最小等。

实现部分如下：

```cpp
int Query(Node *pNode, int l, int r)
{
    if(pNode->nLeft == l && r == pNode->nRight) { return pNode->nMoney; }
    else
    {
        if(r <= (pNode->nLeft + pNode->nRight) / 2)
        { return Query(pNode->pLeft, l, r); }
        else if(l > (pNode->nLeft + pNode->nRight) / 2)
        { return Query(pNode->pRight, l, r); }
        else
        {
            int nMid = (pNode->nLeft + pNode->nRight) / 2;
            return min(Query(pNode->pLeft, l, nMid), Query(pNode->pRight, nMid + 1, r));
        }
    }
}
```

但是上面的代码要递归很久才返回数据，有很多的重复运算，这样在数据量很大的情况下非常不理想，所以我们需要进行一些优化。我们可以考虑提前把每个区间的最值求出来，因为原来只有点区间才有数据：

```cpp
int Update(Node *pNode)
{
    if(pNode->nLeft == pNode->nRight)
    { return pNode->nMoney; }
    else
    {
        return pNode->nMoney = min(Update(pNode->pLeft), Update(pNode->pRight));
    }
}
```

这样，这棵线段树的效率就得到了很大的提高。

附上忠诚代码：

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Node
{
    int nLeft, nRight;
    unsigned long long nMoney;
    Node *pLeft, *pRight;
};

Node *pRoot;
int N, M, nTmp, L, R, ans;
vector<int> pMoney;

Node* Build(int l, int r);
int Update(Node *pNode);
int Query(Node *pNode, int l, int r);

int main()
{
    ios::sync_with_stdio(false);
    cin >> N >> M;
    for(int i = 1; i <= N; i++)
    {
        cin >> nTmp;
        pMoney.push_back(nTmp);
    }
    pRoot = Build(1, N);
    Update(pRoot);
    for(int i = 1; i <= M; i++)
    {
        cin >> L >> R; 
        ans = 2147483647;
        cout << Query(pRoot, L, R) << " ";
    }
    cout << endl;
    return 0;
}

Node* Build(int l, int r)
{
    Node *pNode = new Node();
    if(l == r) { pNode->nMoney = pMoney[l - 1]; }
    else { pNode->nMoney = 0; }
    pNode->nLeft = l; pNode->nRight = r;
    if(l == r) { return pNode; }
    int nMid = (l + r) / 2;
    pNode->pLeft = Build(l, nMid);
    pNode->pRight = Build(nMid + 1, r);
    return pNode;
}

int Update(Node *pNode)
{
    if(pNode->nLeft == pNode->nRight)
    { return pNode->nMoney; }
    else
    {
        return pNode->nMoney = min(Update(pNode->pLeft), Update(pNode->pRight));
    }
}

int Query(Node *pNode, int l, int r)
{
    if(pNode->nLeft == l && r == pNode->nRight) { return pNode->nMoney; }
    else
    {
        if(r <= (pNode->nLeft + pNode->nRight) / 2)
        { return Query(pNode->pLeft, l, r); }
        else if(l > (pNode->nLeft + pNode->nRight) / 2)
        { return Query(pNode->pRight, l, r); }
        else
        {
            int nMid = (pNode->nLeft + pNode->nRight) / 2;
            return min(Query(pNode->pLeft, l, nMid), Query(pNode->pRight, nMid + 1, r));
        }
    }
}
```
