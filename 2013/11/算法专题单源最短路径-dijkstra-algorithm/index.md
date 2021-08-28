# 算法专题：单源最短路径 – Dijkstra Algorithm


这个星期开始复习最短路的一些算法。

单源最短路径（Single Source Shortest Paths），简称 SSSP。这是图论中非常重要的一类算法。解决这一问题有多种算法，今天先来介绍一下 Dijkstra Algorithm。

首先介绍一下单源最短路径的概念，通俗的讲，就是给定一个源点 $ s $ （即起点），求这个源点到其他各个顶点的最短路径。最短路径，通俗的来讲，我们称使得顶点 $ V_{i} $ 到顶点 $ V_{j} $ 所经过的路径的权值之和最小的一条路径，称为从顶点 $ V_{i} $ 到顶点 $ V_{j} $ 的最短路径。

{{< image src="/images/2013/算法专题：单源最短路径 – Dijkstra Algorithm/SSSP.png" caption="单源最短路径" >}}

上面这幅图标出了从源点 $ s $ 到各个顶点的最短路径，大家可以根据图片自己体会一下最短路径的含义。其中 $ -\infty $ 表示到该点的最短路径是负无穷，因为我们发现存在负环，所以我们利用负环，使得最短路径达到负无穷，但是这个一般不在我们一般的算法的讨论范围内。

下面来介绍一下 Dijkstra Algorithm。

首先将所有的顶点分成两个集合 $ A $ 、 $ B $ ，其中集合 $ A $ 表示已经求得最短路径的顶点集合，集合 $ B $ 为待求解的顶点集合。初始时有 $ A=\left \{ V_{0} \right \} $ 。
将集合 $ A $ 与集合 $ B $ 相连的边按照递增次序排序，取最短的边，将该条边在集合 $ B $ 中所对应的顶点加入到集合 $ A $ 中。
重复第二步，直至集合 $ B $ 为空集。

我们通过下面一幅图来理解一下 Dijkstra Algorithm：

{{< image src="/images/2013/算法专题：单源最短路径 – Dijkstra Algorithm/Dijkstra.png" caption="Dijkstra 算法" >}}

下面我们来考虑算法的实现方式，显然，我们需要每次在集合 $ A $ 中发出的所有边中找到最小的一条边，而每次这样找的话，复杂度很高，我们可以考虑用优先队列来优化这个步骤。这样的话复杂度就下降到了 $ O\left ( \left ( V+E \right )\cdot \log{E} \right ) $ 。

代码如下：

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int MAX = 10240;

typedef pair<int,int> pii;

int N, M;
int pDist[MAX];
vector<pair<int, int> > pMap[MAX];
priority_queue<pii, vector<pii>, greater<pii> > Q;	// 优先队列

void Dijkstra(int s);

int main()
{
	cin >> N >> M;
	for(int i = 1; i <= M; i++)
	{
		int s, e, v;
		cin >> s >> e >> v;	// 无向图
		pMap[s].push_back(make_pair(e, v));
		pMap[e].push_back(make_pair(s, v));
	}
	Dijkstra(1);
	return 0;
}

void Dijkstra(int s)
{
	for(int i = 1; i <= N; i++)	// 初始化
	{ pDist[i] = 2147483647; }
	pDist[s] = 0；
	Q.push(make_pair(pDist[s], s));		// 将源点加入队列
	while(!Q.empty())
	{
		pii x = Q.top(); Q.pop();	// 取最短的边
		if(x.first != pDist[x.second]) { continue; }	// 防止重复计算
		for(int i = 0; i < pMap[x.second].size(); i++)
		{
			int v = pMap[x.second][i].first;	// 待松弛的顶点
			int w = pMap[x.second][i].second;	// 从顶点x.second到顶点i的距离
			if(pDist[v] > pDist[x.second] + w)
			{
				pDist[v] = pDist[x.second] + w;		// 松弛
				Q.push(make_pair(pDist[v], v));
			}
		}
	}

	for(int i = 1; i <= N; i++)
	{
		cout << pDist[i] << " ";
	}
	cout << endl;
}
```
