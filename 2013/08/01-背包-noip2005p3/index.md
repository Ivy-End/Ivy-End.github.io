# 0/1 背包 - NOIP2005P3


题目是经典的采药问题。也是最基础的 0/1 背包问题。

我们约定有 $ N $ 件物品和一个容量为 $ C $ 的背包。第 $ i $ 件物品的重量是 $ w\left [ i \right ] $ ，价值是 $ v\left [ i \right ] $ 。这样，我们所需要求解将哪些物品装入背包可使价值总和最大。

## 二维数组表示

**定义状态**： $ f\left [ i \right ]\left [ c \right ] $ 表示前 $ i $ 件物品恰放入一个容量为 $ c $ 的背包可以获得的最大价值。

**状态转移方程**： $ f\left [ i \right ]\left [ c \right ]=\max\left \\{ f\left [ i-1 \right ]\left [ c \right ],f\left [i-1  \right ]\left [ c-w\left [ i \right ] \right ] +v\left [ i \right ]\right \\} $ 

**代码模版**：

```cpp
for(int i = 1; i <= N; i++)
{
	for(int c = 0; c <= C; c++)
	{
		f[i][c] = f[i - 1][c];
		if(c >= w[i])
		{ f[i][c] = max(f[i][c], f[i - 1][c - w[i]] + v[i]); }
	}
}
```

**时间复杂度、空间复杂度**： $ O\left ( NC \right ) $ 

## 一维数组表示

**定义状态**：由于 $ i $ 基本没有什么用处，所以我们把它省略。

**状态转移方程**： $ f\left [ c \right ]=\max\left \\{ f\left [ c \right ],f\left [ c-w\left [ i \right ] \right ] +v\left [ i \right ]\right \\} $ 需要注意的是，这时候，我们需要将 $ c $ 从 $ C $ 开始，倒着推。

**代码模版**：

```cpp
for(int i = 1; i <= N; i++)
{
	for(int c = C; C >= 0; C--)
	{
		if(c >= w[i])
		{ f[c] = max(f[c], f[c - w[i]] + v[i]); }
	}
}
```

**时间复杂度**： $ O\left ( NC \right ) $ 

**空间复杂度**： $ O\left ( C \right ) $ 

### 一维数组表示下的常数优化

内层循环的下限不需要为 0。

**代码模版**：

```cpp
int bound, sumw = 0;
for(int i = 1; i <= N; i++)
{
	sumw += w[i];
	bound = max(C - sumw, w[i]);
	for(int c = C; C >= bound; C--)
	{
		if(c >= w[i])
		{ f[c] = max(f[c], f[c - w[i]] + v[i]); }
	}
}
```

**初始化的细节**：
* 若要求“恰好装满”： $ f\left [ 0 \right ]=0 $ ，其他 $ f\left [ i \right ]=\textrm{-INF} $ 。
* 若不用“恰好装满”： $ f\left [ 0 \right ]=0 $ 。

最后附上 NOIP2005P3 的代码：

```cpp
#include <iostream>
#include <memory.h>
#include <algorithm>

using namespace std;

const int MAX = 1024;

int C, N;
int pC[MAX], pW[MAX], f[MAX];

int main()
{
	cin >> C >> N;
	for(int i = 0; i < N; i++)
	{ cin >> pC[i] >> pW[i]; }
	memset(f, 0, sizeof(f));
	for(int i = 0; i < N; i++)
	{
		for(int j = C; j >= pC[i]; j--)
		{
			f[j] = max(f[j], f[j - pC[i]] + pW[i]);
		} 
	}
	cout << f[C] << endl;
	return 0;
}
```
