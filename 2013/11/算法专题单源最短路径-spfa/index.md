# 算法专题：单源最短路径 - SPFA


SPFA 是 Shortest Path Fast Algorithm 的缩写，它是之前介绍的 Bellman-Ford Algorithm 的一种队列实现，减少了不必要的冗余计算。

算法的基本步骤如下：

1. 初始化队列和标记数组，将源点入队。
2. 每次取队首元素，对其发出的所有边进行松弛。并将松弛过的且不在队列中的顶点加入到队列中。
3. 重复第二步直至队列为空。

若要判断负环，则当某个顶点松弛超过V次，即存在负环。

对于SPFA还是比较容易理解的，它的复杂度为 $O\left(kE\right)$。

代码如下：

```cpp
#include <iostream>
#include <memory.h>
#include <vector>
#include <queue>

using namespace std;

const int MAX = 10240;

bool pQueue[MAX];
int N, M, pDist[MAX], pCnt[MAX];	// pCnt[]记录顶点i松弛的次数
vector<pair<int, int> > pMap[MAX];
queue<int> Q;

void SPFA(int s);

int main()
{
    cin >> N >> M;
    for(int i = 1; i <= M; i++)
    {
        int s, e, v;
        cin >> s >> e >> v;
        pMap[s].push_back(make_pair(e, v));	// 无向图
        pMap[e].push_back(make_pair(s, v));
    }
    SPFA(1);
    return 0;
}

void SPFA(int s)
{
    bool bNativeLoop = false;	// 判断负环的变量
    for(int i = 1; i <= N; i++)	// 初始化
    { pDist[i] = 2147483647; }
    memset(pQueue, false, sizeof(pQueue));
    pDist[s] = 0;
    Q.push(s);	// 源点入队
    pQueue[s] = true;
    while(!Q.empty())
    {
        int x = Q.front(); Q.pop();	// 取出队首元素
        pQueue[x] = false;	// 出队
        for(int i = 0; i < pMap[x].size(); i++)
        {
            if(pDist[pMap[x][i].first] > pDist[x] + pMap[x][i].second)	// 松弛
            {
                pDist[pMap[x][i].first] = pDist[x] + pMap[x][i].second;
                if(!pQueue[pMap[x][i].first])	// 如果未入队
                {
                    Q.push(pMap[x][i].first);
                    pQueue[pMap[x][i].first] = true;	// 入队

                    if(++pCnt[pMap[x][i].first] > N)
		    {
			bNativeLoop = true;	// 存在负环
			while(!Q.empty()) { Q.pop(); }	// 立即退出循环
		    }
                }
            }
        }
    }

    if(bNativeLoop) { cout << "Exist Negative Loop" << endl; }
    else
    {
    	for(int i = 1; i <= N; i++)
    	{ cout << pDist[i] << " "; }
    	cout << endl;
    }
}
```

至此，单源最短路的算法基本复习结束。细究这三种算法，个人觉得 SPFA 的编程复杂度较低。而 Dijkstra Algorithm 也挺实用的。不过在一般情况下我比较倾向于 SPFA。
