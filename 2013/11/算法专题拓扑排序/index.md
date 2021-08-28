# 算法专题：拓扑排序


拓扑排序（Topological Sorting）是图论中一个比较重要的概念。它主要用来解决下面这类问题：

给定一个 AOV 网（Activity On Vertex Network）， $ A\rightarrow B $ 表示活动 $ A $ 必须在活动 $ B $ 之前完成。请给出一个合理的活动顺序。

当然，AOV 网中不可能出现环，因为出现了环就无法拓扑排序。因此可以用拓扑排序来判断图中是否存在环。

关于拓扑排序，我们来看一下下面这张图片：


{{< image src="/images/2013/算法专题：拓扑排序/Toplogical-Sorting.png" caption="Toplogical Sorting" >}}

我们可以用队列来实现这个算法，具体改进的过程如下：

1. 记录每个点的入度；
2. 将入度为 0 的顶点加入队列；
3. 依次对入度为 0 的点进行删边操作，同时将新得到的入度为零的点加入队列；
4. 重复上述操作，直至队列为空。

代码如下：

```cpp
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

const int MAX = 10240;

int N, M, pDegree[MAX];
queue<int> Q;
vector<int> pMap[MAX], pVec;

void TopSort();

int main()
{
    cin >> N >> M;
    memset(pDegree, 0, sizeof(pDegree));
    for(int i = 1; i <= M; i++)
    {
        int s, e;
        cin >> s >> e;
        pMap[s].push_back(e);    // 有向图
        pDegree[e]++;    // 计算入度
    }
    TopSort();
    return 0;
}

void TopSort()
{
    for(int i = 1; i <= N; i++)
    {
        if(pDegree[i] == 0)    // 入度为0的点入队
        { Q.push(i); }
    }

    while(!Q.empty())
    {
        int x = Q.front(); Q.pop();
        pVec.push_back(x);    // 出队顺序即为拓扑序列
        for(int i = 0; i < pMap[x].size(); i++)
        {
            pDegree[pMap[x][i]]--;    // 删边
            if(pDegree[pMap[x][i]] == 0)    // 新的入度为0的点
            { Q.push(pMap[x][i]); }
        }
    }

    for(int i = 1; i <= N; i++)
    {
        if(pDegree[i] != 0)    // 若存在入度不为0的点，则存在环
        {
            cout << "Exsit Loop" << endl;
            return;
        }
    }

    for(int i = 0; i < pVec.size(); i++)    // 顺序输出即为拓扑序列
    { cout << pVec[i] << " "; }
    cout << endl;    
}
{% endhighlight %}

对于这一问题，我们也可以用DFS来解决它，代码如下：

{% highlight cpp linenos %}
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int MAX = 10240;

int N, M, pVisited[MAX];    // 0-未访问  1-正在访问  2-已访问
vector<int> pMap[MAX], pVec;

void TopSort();
bool DFS(int v);

int main()
{
    cin >> N >> M;
    for(int i = 1; i <= M; i++)
    {
        int s, e;
        cin >> s >> e;
        pMap[s].push_back(e);    // 有向图
    }
    TopSort();
    return 0;
}

void TopSort()
{
    memset(pVisited, 0, sizeof(pVisited));
    for(int i = 1; i <= N; i++)    // 所有顶点都访问一遍
    {
        if(!pVisited[i])
        {
            if(!DFS(i))
            {
                cout << "Exsit Loop" << endl;
            }
        }
    }

    for(int i = pVec.size() - 1; i >= 0; i--)    // 倒序输出拓扑序列
    { cout << pVec[i] << " "; }
    cout << endl;
}

bool DFS(int v)        // false-有环  true-无环
{
    pVisited[v] = 1;    // 正在访问
    for(int i = 0; i < pMap[v].size(); i++)        // 搜索它的前驱
    {
        if(pVisited[pMap[v][i]] == 1) { return false; }        // 该点进入两次则有环
        else if(pVisited[pMap[v][i]] == 0)
        {
            if(!DFS(pMap[v][i])) { return false; }
        }
    }
    pVisited[v] = 2;    // 访问完毕
    pVec.push_back(v);    // 加入拓扑序列
    return true;
}
```

相较这两种算法，我更倾向于用队列来实现，毕竟这种方法符合求解拓扑排序的一般思路。至于这两种算法的复杂度，在这里就不再分析了。
