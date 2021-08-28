# 线段树 – 有改动求解区间最值 – 忠诚 2


忠诚 2 是忠诚的一个提升版本。我们在之前的一篇文章[线段树 – 无改动求解区间最值 – 忠诚](/2013/08/线段树-无改动求解区间最值-忠诚/)简单的谈了一下关于无改动求解区间最值的问题。现在我们来研究一下有改动求解区间最值。

首先，我们考虑改动某个值以后，对整棵树重新进行维护。但是很快我们发现，这样的复杂度太大。因为每次只更改一个值，所以只涉及到一条路径，因此我们考虑在递归修改数值的时候，可以标记一下经过的结点，修改完成以后，只对标记过的结点进行维护。这样我们的代码就出来了：

```cpp
int Update(Node *pNode)
{
    if(pNode->nLeft == pNode->nRight || pNode->nMoney != 2147483647)
    { return pNode->nMoney; }
    else
    {
        return pNode->nMoney = min(Update(pNode->pLeft), Update(pNode->pRight));
    }
}

void Change(Node *pNode, int x, int nValue)
{
    pNode->nMoney = 2147483647;
    if(pNode->nLeft == x && x == pNode->nRight) { pNode->nMoney = nValue; }
    else
    {
        if(x <= (pNode->nLeft + pNode->nRight) / 2)
        { Change(pNode->pLeft, x, nValue); }
        else
        { Change(pNode->pRight, x, nValue); }
    }
}
```

这样，除了第一次维护外，每次我们只需要维护一条路径，复杂度也大大降低低了。

附上忠诚 2 代码：

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
int N, M, nTmp, T, L, R, ans;
vector<int> pMoney;

Node* Build(int l, int r);
int Update(Node *pNode);
void Change(Node *pNode, int x, int nValue);
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
        cin >> T >> L >> R; 
        if(T == 1)
        {
            ans = 2147483647;
            cout << Query(pRoot, L, R) << " ";
        }
        else
        {
            Change(pRoot, L, R);
            Update(pRoot);
        }
    }
    cout << endl;
    return 0;
}

Node* Build(int l, int r)
{
    Node *pNode = new Node();
    if(l == r) { pNode->nMoney = pMoney[l - 1]; }
    else { pNode->nMoney = 2147483647; }
    pNode->nLeft = l; pNode->nRight = r;
    if(l == r) { return pNode; }
    int nMid = (l + r) / 2;
    pNode->pLeft = Build(l, nMid);
    pNode->pRight = Build(nMid + 1, r);
    return pNode;
}

int Update(Node *pNode)
{
    if(pNode->nLeft == pNode->nRight || pNode->nMoney != 2147483647)
    { return pNode->nMoney; }
    else
    {
        return pNode->nMoney = min(Update(pNode->pLeft), Update(pNode->pRight));
    }
}

void Change(Node *pNode, int x, int nValue)
{
    pNode->nMoney = 2147483647;
    if(pNode->nLeft == x && x == pNode->nRight) { pNode->nMoney = nValue; }
    else
    {
        if(x <= (pNode->nLeft + pNode->nRight) / 2)
        { Change(pNode->pLeft, x, nValue); }
        else
        { Change(pNode->pRight, x, nValue); }
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
