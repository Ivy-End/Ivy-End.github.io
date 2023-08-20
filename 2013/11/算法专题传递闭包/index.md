# 算法专题：传递闭包


传递闭包（Transitive Closure）主要是研究图上两点之间的连通性。对于这个问题，我们只需要改进一下 Floyd-Warshall Algorithm 就可以很方便的求出它的解。

我们这里主要研究的是有向图的传递闭包问题。

代码如下：

```cpp
#include <iostream>

using namespace std;

const int MAX = 10240;
const int INF = 65536;

int N, M;
bool f[MAX][MAX], pMap[MAX][MAX];

void Floyd();

int main()
{
    cin >> N >> M;
    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= N; j++)
        {
            pMap[i][j] = f[i][j] = (i == j) ? 1 : 0;    // 初始化
        }
    }
    for(int i = 1; i <= M; i++)
    {
        int s, e;
        cin >> s >> e;
        pMap[s][e] = pMap[e][s] = true;        // 无向图
        f[s][e] = f[e][s] = true;
    }
    Floyd();
    return 0;
}

void Floyd()
{
    for(int k = 1; k <= N; k++)    // 最外层必须是k
    {
        for(int i = 1; i <= N; i++)    
        {
            for(int j = 1; j <= N; j++)
            {
                f[i][j] = f[i][j] || (f[i][k] && f[k][j]);    // 判断连通性 
            }
        }
    }

    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= N; j++)
        { cout << f[i][j] << " "; } 
        cout << endl;
    }
}
```

这个算法还是比较简单的，只要在 Floyd-Warshall Algorithm 的基础上修改一下就行了。
