# 算法专题：欧拉回路


欧拉回路（Euler Circuit）是指：在一个无向图中，一条包含所有边，且其中每一条边只经过一次的路径。欧拉回路最常见的应用是一笔画。

下面介绍几个用于判断给定的图 $ G=\left(V,E\right) $ 中是否欧拉通路或欧拉回路：

* 一个图有欧拉回路当且仅当它是连通的且每个顶点都有偶数度。
* 一个图有欧拉通路当且经当它是连通的且除两个顶点外，其他顶点都有偶数度。
* 在第二个定理下，含奇数度的两个节点中，一个必为欧拉通路起点，另一个必为欧拉通路的终点。

这样，我们就可以很容易想出程序的思路：

* 计算各个顶点的度，如果存在 1 个奇数度，或者奇数度个数大于 2，则不存在欧拉回路。
* 选择奇数度的一个顶点作为欧拉回路的起点，如果不存在奇数度的顶点，则任意选取一个，在这里我们选取第一个顶点。
* 每次遍历与该点相连的边，删去该条边，则原图就转化成了一个更小的图，求它的欧拉通路，这样递归即可求解。

代码如下：

```cpp
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int MAX = 10240;

int N, M, pCnt[MAX];
int pMap[MAX][MAX];
vector<int> pVec;

void Search(int x);
void Euler_Circuit();

int main()
{
    cin >> N >> M;
    memset(pMap, 0, sizeof(pMap));
    for(int i = 1; i <= M; i++)
    {
        int s, e;
        cin >> s >> e;
        pMap[s][e] = pMap[e][s] = 1;    // 无向图
    }
    Euler_Circuit();
    return 0;
}

void Euler_Circuit()
{
    int nStart = 1, nOddNum = 0;    // nStart保存起点，nOddNum保存有几个顶点有奇数度
    memset(pCnt, 0, sizeof(pCnt));
    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= N; j++)
        {
            pCnt[i] += pMap[i][j];        // 计算各个顶点的度
        }
    }

    for(int i = 1; i <= N; i++)    // 统计奇数度顶点的个数
    {
        if(pCnt[i] & 1)
        {
            nStart = i;
            nOddNum++;
        }
    }
    if(nOddNum > 2 || nOddNum == 1)        // 不存在欧拉回路
    {
        cout << "Not Exsit Euler Circuit" << endl;
    }
    else
    {
        Search(nStart);
        for(int i = 0; i < pVec.size(); i++)
        { cout << pVec[i] << " "; }
        cout << endl;
    }
}

void Search(int x)
{
    for(int i = 1; i <= N; i++)
    {
        if(pMap[x][i] == 1)
        {
            pMap[x][i] = pMap[i][x] = 0;    // 删边
            Search(i);    
        }
    }
    pVec.push_back(x);
}
```


欧拉回路我至今也没有在做题目的时候用到过，不知道是不是这类题目比较少见。
