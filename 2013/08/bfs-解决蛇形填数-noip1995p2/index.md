# BFS 解决蛇形填数 - NOIP1995P2


题目描述是经典的蛇形填数问题。

以前解决这类问题，通常是通过控制 $ i,j $ 的值来定位数组元素的位置，然后进行赋值。但是这种方法非常的繁琐，且难于理解。容易出错。

今天在做这道题目的时候，通过搜索资料，思索出了一种新解法，相较于原来的解法更以理解，且时间复杂度更低。解法的基本思想是 BFS。下面我们仔细来探讨一下。

首先我们定义一组偏移量数组：

```cpp
const int dx[] = { 1, 0, -1, 0 };
const int dy[] = { 0, -1, 0, 1 };
```

 这个数组的顺序必须和填数的顺序一致。在这里，它被定义为逆时针填数。

然后我们需要设置 BFS 的起点：

```cpp
x = 1; y = N; i = 0;
f[x][y] = nNum++;
```

其中， $ x,y $ 用来保存当前坐标， $ i $ 则是保存当前偏移量的数组下标。 $ f\left [ x \right ]\left [ y \right ] $ 表示需要填充的矩阵， $ nNum $ 则是所需要填的数。

我们来简单的模拟以下，假设现在坐标为 $ \left ( 1,n \right ) $ ，偏移量下标 $ i=0 $ 。首先尝试向右扩展标 $ \left ( 1,n+1 \right ) $ ，不合法，于是返回到坐标 $ \left ( 1,n \right ) $ 再先下扩展，检测合法后，进行填充，当填充到最下端时，又不合法，这样，返回到坐标 $ \left ( n,n \right ) $ 后向左扩展，同理，填充到最左端后又会向上扩展，这里还需要检测当前扩展结点是否已经填数。如果已经填数，则不合法，需要返回上一个坐标。

这样我们模拟一遍 BFS 就可以知道，这种解法是正确的，所以这里略过证明。

基本代码如下：

```cpp
#include <iostream>
#include <memory.h>

using namespace std;

const int MAX = 16;
const int dx[] = { 1, 0, -1, 0 };
const int dy[] = { 0, -1, 0, 1 };

int x, y, i, nNum = 1;
int N, f[MAX][MAX];

int main()
{
    memset(f, 0, sizeof(f));
    cin >> N;
    x = 1; y = N; i = 0;
    f[x][y] = nNum++;
    while(nNum <= N * N)
    {
        x += dx[i]; y += dy[i];
        if(x >= 1 && x <= N && y >= 1 && y <= N && f[x][y] == 0)
        { f[x][y] = nNum++; }
        else
        {
            x -= dx[i]; y -= dy[i];
            i = (i + 1) % 4;
        }
    }
    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= N; j++)
        {
            if(N * N > 99 && f[i][j] < 100) { cout << " "; }
            if(N * N > 9 && f[i][j] < 10) { cout << " "; }
            cout << f[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```
