# SGU 104 - Little shop of flowers


## Description

You want to arrange the window of your flower shop in a most pleasant way. You have $F$ bunches of flowers, each being of a different kind, and at least as many vases ordered in a row. The vases are glued onto the shelf and are numbered consecutively 1 through $V$, where $V$ is the number of vases, from left to right so that the vase 1 is the leftmost, and the vase $V$ is the rightmost vase. The bunches are moveable and are uniquely identified by integers between 1 and $F$. These id-numbers have a significance: They determine the required order of appearance of the flower bunches in the row of vases so that the bunch i must be in a vase to the left of the vase containing bunch $j$ whenever $i < j$.

Suppose, for example, you have bunch of azaleas (id-number=1), a bunch of begonias (id-number=2) and a bunch of carnations (id-number=3). Now, all the bunches must be put into the vases keeping their id-numbers in order. The bunch of azaleas must be in a vase to the left of begonias, and the bunch of begonias must be in a vase to the left of carnations. If there are more vases than bunches of flowers then the excess will be left empty. A vase can hold only one bunch of flowers.

Each vase has a distinct characteristic (just like flowers do). Hence, putting a bunch of flowers in a vase results in a certain aesthetic value, expressed by an integer. The aesthetic values are presented in a table as shown below. Leaving a vase empty has an aesthetic value of 0.

|   |   | VASES | | | | |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| | | 1 | 2 | 3 | 4 | 5 | 6 |
| Bunches | 1 (azaleas) | 7 | 23 | -5 | -24 | 16 |
| | 2 (begonias) | 5 | 21 | -4 | 10 | 23 |
| | 3 (carnations) | -21 | 5 | -4 | -20 | 20 |

According to the table, azaleas, for example, would look great in vase 2, but they would look awful in vase 4.

To achieve the most pleasant effect you have to maximize the sum of aesthetic values for the arrangement while keeping the required ordering of the flowers. If more than one arrangement has the maximal sum value, any one of them will be acceptable. You have to produce exactly one arrangement.

$1\leq F\leq 100$ where $F$ is the number of the bunches of flowers. The bunches are numbered 1 through $F$.

$F\leq V\leq 100$ where $V$ is the number of vases.

$-50\leq A_{i,j}\leq 50$ where $A_{i,j}$ is the aesthetic value obtained by putting the flower bunch $i$ into the vase $j$.

## Input

The first line contains two numbers: $F$, $V$.

The following $F$ lines: Each of these lines contains $V$ integers, so that $A_{i,j}$ is given as the $j$'th number on the $(i+1)$'st line of the input file.

## Output

The first line will contain the sum of aesthetic values for your arrangement.

The second line must present the arrangement as a list of $F$ numbers, so that the $k$'th number on this line identifies the vase in which the bunch $k$ is put.

## Sample Input

```
3 5
7 23 -5 -24 16
5 21 -4 10 23
-21 5 -4 -20 20
```

## Sample Output

```
53
2 4 5
```

## Analysis

经典的动态规划题。我们令 $f[i][j]$ 表示前 $i$ 束花放到前 $j$ 个花瓶中获得的最大的魅力值。

由于花束必须按编号递增安排，所以我们可以得到状态转移方程：$$ f[i][j] = \max{\left(f[i][j - 1], f[i - 1][j - 1] + \mathrm{pData}[i][j]\right)}$$ 即 $f[i][j]$ 这个状态可以由 $f[i][j - 1]$（第 $i$ 束花不放在第 $j$ 个花瓶里）以及 $f[i - 1][j - 1]$（第 $i$ 束花放在第 $j$ 个花瓶里）转移过来。

这道题目还需要输出方案，我们需要记录转移过程。我的方法是令一个结构体，保存它是由那个状态转移过来的，并且是否放置了花束。输出方案的时候递归输出即可。

还有一个注意点，题目中的魅力值可能为负数。这为我们初始化 $f$ 数组的时候带来了问题。

我选择的解决方案是把魅力值加上一个偏移量 100，保证了魅力值为正数，然后把 $f$ 数组全部置为 0，输出的时候把魅力值减去 $100\times F$ 即可。

## Solution

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 128;
 
struct State
{
    State(int _x = 0, int _y = 0, int _k = 0)
    { x = _x; y = _y; k = _k; }
 
    int x, y, k;
};
 
int f[MAX][MAX], pData[MAX][MAX];
State pAns[MAX][MAX];
 
void Print(int x, int y);
 
int main()
{
    ios::sync_with_stdio(false);
    int F, V;
    while(cin >> F >> V)
    {
        memset(f, 0, sizeof(f));
        for(int i = 1; i <= F; i++)
        {
            for(int j = 1; j <= V; j++)
            {
                cin >> pData[i][j];
                pData[i][j] += 100;
            }
        }
        for(int i = 1; i <= F; i++)
        {
            for(int j = 1; j <= V; j++)
            {
                if(f[i][j - 1] < f[i - 1][j - 1] + pData[i][j])
                {
                    f[i][j] = f[i - 1][j - 1] + pData[i][j];
                    pAns[i][j] = State(i - 1, j - 1, 1);
                }
                else
                {
                    f[i][j] = f[i][j - 1];
                    pAns[i][j] = State(i, j - 1, 0);
                }
            }
        }
        cout << f[F][V] - 100 * F << endl;
        Print(F, V);
        cout << endl;
    }
    return 0;
}
 
void Print(int x, int y)
{
    if(x == 0 && y == 0) { return; }
    State tmp = pAns[x][y];
    Print(tmp.x, tmp.y);
    if(tmp.k == 1) { cout << tmp.y + 1 << " "; }
}
```

这道题目一开始 WA 了好几次，后来发现是没有发现魅力值为负数的时候，把 $f$ 数组初始化为 0 会导致错误答案。
