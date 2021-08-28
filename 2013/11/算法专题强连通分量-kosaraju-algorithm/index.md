# 算法专题：强连通分量 - Kosaraju Algorithm


强连通分量（Strongly Connected Components），简称 SCC。是指在给定的一张图 $ G=\left(V,E\right) $ 的一个子图 $ G{}'=\left(V,E\right) $ 这个子图满足对于其中的任意一对点 $ \left \langle V_{i},V_{j} \right \rangle $ 均存在这样两条路径 $ \left \langle V_{i},\cdots,V_{j} \right \rangle,\left \langle V_{j},\cdots,V_{i} \right \rangle $ 。

如果我们把强连通分量缩成一个点，这时候，原图 $ G $ 则会变成有向无环图。

图 $ G=\left(V,E\right) $ 是有向无环图当且仅当该图中没有点集合元素个数大于1的强连通分量。且任意一个强连通分量都至少包含一个有向环。下面我们通过一张图片来理解一下强连通分量以及缩点：

{{< image src="/images/2013/算法专题：强连通分量 - Kosaraju Algorithm/SCC.png" caption="强连通分量" >}}

对于统计给定的图 $ G=\left(V,E\right) $ 中强连通分量的个数，我们可以应用并查集在 $ O\left ( \alpha \left ( V \right )\cdot V \right ) $ 时间内得到求解。

如果不仅需要统计强连通分量的个数，还要将强连通分量缩点，则需要用到今天介绍的Kosaraju Algorithm。它的具体步骤如下：

* 对原图 $ G $ 进行DFS并将出栈顺序进行逆序，得到的顺序就是拓扑序列。
* 将原图的每一条边反向，得到反图 $ G{}' $ 。
* 按照第一步生成的拓扑序列的顺序再对反图 $ G{}' $ 进行DFS染色，染成同色的就是一个强连通分量。

这个算法比较容易理解，也是最通用的算法。它主要是同时运用了原图 $ G $ 和反图 $ G{}' $ 。

该算法具有一个性质：如果我们把求出来的每个强连通分量缩成一个点，并且用求出每个强连通分量的顺序来标记收缩后的结点，那么这个顺序就是强连通分量缩点后所形成的有向无环图的拓扑序列。

代码如下：

```cpp
#include <iostream>
#include <cstring>
#include <stack>

using namespace std;

const int MAX = 10240;

int N, M, nCnt = 0;
int pMap[MAX][MAX], pColor[MAX];
stack<int> S;    // 储存拓扑序列

void dfs1(int x);    // 原图DFS
void dfs2(int x);    // 反图DFS
void Kosaraju();

int main()
{
    cin >> N >> M;
    memset(pMap, 0, sizeof(pMap));
    for(int i = 1; i <= M; i++)
    {
        int s, e;
        cin >> s >> e;
        pMap[s][e] = 1;        // 有向图
    }
    Kosaraju();
    return 0;
}

void Kosaraju()
{
    memset(pColor, 0, sizeof(pColor));
    for(int i = 1; i <= N; i++)    // DFS原图求出拓扑序列
    {
        if(!pColor[i])
        { dfs1(i); }
    }

    memset(pColor, 0, sizeof(pColor));
    while(!S.empty())    // 按照拓扑序列DFS反图
    {
        int x = S.top(); S.pop();
        if(!pColor[x])
        {
            nCnt++;        // 找到一个强连通分量
            dfs2(x);
        }
    }
    cout << "The number of SCC is " << nCnt << endl;
}

void dfs1(int x)
{
    pColor[x] = 1;    // 染色
    for(int i = 1; i <= N; i++)
    {
        if(pMap[x][i] == 1 && !pColor[i])
        { dfs1(i); }
    }
    S.push(x);    // 加入拓扑序列
}

void dfs2(int x)
{
    pColor[x] = nCnt;    // 属于第几个强连通分量
    for(int i = 1; i <= N; i++)
    {
        if(pMap[i][x] == 1 && !pColor[i])    // 原邻接矩阵的对称矩阵为反图
        { dfs2(i); }
    }
}
```
