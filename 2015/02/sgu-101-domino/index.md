# SGU 101 - Domino


## Description

> Dominoes – game played with small, rectangular blocks of wood or other material, each identified by a number of dots, or pips, on its face. The blocks usually are called bones, dominoes, or pieces and sometimes men, stones, or even cards.
> 
> The face of each piece is divided, by a line or ridge, into two squares, each of which is marked as would be a pair of dice...
> 
> The principle in nearly all modern dominoes games is to match one end of a piece to another that is identically or reciprocally numbered.
> 
> ENCYCLOPÆDIA BRITANNICA

Given a set of domino pieces where each side is marked with two digits from 0 to 6. Your task is to arrange pieces in a line such way, that they touch through equal marked sides. It is possible to rotate pieces changing left and right side.

## Input

The first line of the input contains a single integer $N$ ($1\leq N\leq 100$) representing the total number of pieces in the domino set. The following $N$ lines describe pieces. Each piece is represented on a separate line in a form of two digits from 0 to 6 separated by a space.

## Output

Write "No solution"”" if it is impossible to arrange them described way. If it is possible, write any of way. Pieces must be written in left-to-right order. Every of $N$ lines must contains number of current domino piece and sign "+" or "-" (first means that you not rotate that piece, and second if you rotate it).

## Sample Input

```
5
1 2
2 4
2 4
6 4
2 1
```

## Sample Output

```
2 -
5 +
1 +
3 +
4 -
```

## Analysis

这道题目做了好久好久，终于 AC 了。

我第一次看到这道题目完全不知道怎么做，第二次觉得可以 dfs。后来看了题解，发现是欧拉通路。

我们将 0~6 这 7 个数字看成点，每个多米诺骨牌看成一条无向边，构建一张图。

这边用到一个 trick，我们设置 `pVisited` 数组的时候，不一定要判断点是否访问过，我们也可以用来判断边是否访问过，这样我们就可以使用边集数组来保存这张图。

欧拉通路也就是一笔画问题，它区别于欧拉回路（欧拉回路要求回到起始点）。

思路很简单，首先确定起点：

* 度为奇数的点的总数为 0，任选一个点为起点；
* 度为奇数的点的总数为 2，任选两个点中的某个点为起点；
* 其他情况下无解。

接下来就是写欧拉通路了，之前在一个 NOIP 的参考资料上看到一个 dfs 的版本，按着它写了一遍，一直 WA，后来发现，他的方法好像有问题。

除此之外，还需要判断自环，也就是如果这张图不连通，那么显然是无解的。

还有，选择起点的时候，任意返回一个点，需要注意这个点必须是出现过的点，否则就会 WA。

经过这么多的思考，重新写了不知道多少遍代码，终于 AC 了。

最后还在“No solution”中“s”的大小写问题上 PE 了一次。

## Solution

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 128;
const int SIZE = 8;
 
struct Node
{
    int s, e;
};
 
struct Path
{
    int x;
    char y;
};
 
int N;
bool bFlag;
bool pVisited[MAX];
int pDegree[SIZE], pMap[SIZE][SIZE];
Node pNode[MAX];
Path pPath[MAX];
 
int Check();
void dfs(int nStart, int nFlag, int nStep);
 
int main()
{
    int x, y;
    while(cin >> N)
    {
        bFlag = false;
        memset(pMap, 0, sizeof(pMap));
        memset(pVisited, false, sizeof(pVisited));
        for(int i = 1; i <= N; i++)
        {
            cin >> x >> y;
            pMap[x][y]++; pMap[y][x]++;
            pNode[i].s = x; pNode[i].e = y;
        }
        int nStart = Check();
        if(nStart == -1) {  cout << "No solution" << endl; }
        else
        {
            for(int i = 1; i <= N; i++)
            {
                if(pNode[i].s == nStart)
                { dfs(i, 1, 1); break; }
                else if(pNode[i].e == nStart)
                { dfs(i, 2, 1); break; }
            }
        }
        if(!bFlag) { cout << "No solution" << endl; }
    }
}
 
int Check()
{
    memset(pDegree, 0, sizeof(pDegree));
    int nCnt = 0, nPos = pNode[1].s;
    for(int i = 0; i < SIZE; i++)
    {
        for(int j = 0; j < SIZE; j++)
        { pDegree[i] += pMap[i][j]; }
    }
    for(int i = 0; i < SIZE; i++)
    {
        if(pDegree[i] % 2) { nCnt++; nPos = i; }
    }
    if(nCnt == 0 || nCnt == 2) { return nPos; }
    else { return -1; }
}
 
void dfs(int nStart, int nFlag, int nStep)
{
    if(bFlag) { return; }
    pVisited[nStart] = true;
    pPath[nStep].x = nStart;
    pPath[nStep].y = (nFlag == 1) ? '+' : '-';
    if(nStep == N)
    {
        for(int i = 1; i <= N; i++)
        { cout << pPath[i].x << " " << pPath[i].y << endl; }
        bFlag = true;
    }
    int nNext = (nFlag == 1) ? pNode[nStart].e : pNode[nStart].s;
    for(int i = 1; i <= N; i++)
    {
        if(!pVisited[i])
        {
            if(pNode[i].s == nNext) { dfs(i, 1, nStep + 1); }
            else if(pNode[i].e == nNext) { dfs(i, 2, nStep + 1); }
            pVisited[i] = false;
        }
    }
}
```

终于 AC 了这道题目，写了好久好久了。
