# 专题一、简单搜索 - Virtual Judge


很久以前刷完了 Virtual Judge 上的简单搜索专题，现总结如下：

## POJ 1321

由于题目的数据范围比较小，可以直接 dfs 暴力。读入时记录每个空位的位置，保存在 `pX[]` 以及 `pY[]` 数组中。暴力的时候统计当前处理第几个空格以及当前处理到了第几行即可。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 128;
 
 
long long ans;
int N, K, nCnt;
bool pUsed[MAX];
int pX[MAX], pY[MAX];
int pRow[MAX], pCol[MAX];
 
void dfs(int x, int y);
 
int main()
{
    char dwTmp;
    while(cin >> N >> K)
    {
        if(N == -1 && K == -1) { break; }
        nCnt = 0; ans = 0;
        for(int i = 1; i <= N; i++)
        {
            for(int j = 1; j <= N; j++)
            {
                cin >> dwTmp;
                if(dwTmp == '#')
                { nCnt++; pX[nCnt] = i; pY[nCnt] = j; }
            }
            cin.ignore();
        }
        memset(pRow, 0, sizeof(pRow));
        memset(pCol, 0, sizeof(pCol));
        memset(pUsed, false, sizeof(pUsed));
        dfs(1, 0);
        cout << ans << endl;
    }
    return 0;
}
 
void dfs(int x, int y)
{
    if(y == K)
    { ans++; }
    else
    {
        for(int i = x; i <= nCnt; i++)
        {
            if(!(pUsed[i] || pRow[pX[i]] || pCol[pY[i]]))
            {
                pRow[pX[i]]++; pCol[pY[i]]++;
                pUsed[i] = true;
                dfs(i + 1, y + 1);
                pUsed[i] = false;
                pRow[pX[i]]--; pCol[pY[i]]--;
            }
        }
    }
}
```

## POJ 2251

这是一个三维迷宫，对立体空间的六个方向进行 bfs 即可。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
#include <queue>
 
using namespace std;
 
const int MAX = 32;
 
const int dx[] = { 1, -1, 0, 0, 0, 0 };
const int dy[] = { 0, 0, 1, -1, 0, 0 };
const int dz[] = { 0, 0, 0, 0, 1, -1 };
 
struct Point
{
    Point(int _x = 0, int _y = 0, int _z = 0, int _ans = 0)
    { x = _x; y = _y; z = _z; ans = 0; }
     
    int x, y, z, ans;
};
 
queue<Point> Q;
Point Start, End;
int pMaze[MAX][MAX][MAX];
bool pVisited[MAX][MAX][MAX];
 
int main()
{
    int L, R, C;
    string strTmp;
    while(cin >> L >> R >> C)
    {
        if(L == 0 && R == 0 && C == 0) { break; }
        while(!Q.empty()) { Q.pop(); }
        for(int i = 1; i <= L; i++)
        {
            for(int j = 1; j <= R; j++)
            {
                cin >> strTmp;
                for(int k = 1; k <= C; k++)
                {
                    if(strTmp[k - 1] == 'S') { pMaze[i][j][k] = 0; Start = Point(i, j, k); }
                    else if(strTmp[k - 1] == 'E') { pMaze[i][j][k] = 0; End = Point(i, j, k); }
                    else if(strTmp[k - 1] == '.') { pMaze[i][j][k] = 0; }
                    else if(strTmp[k - 1] == '#') { pMaze[i][j][k] = 1; }
                }
            }
        }
        Q.push(Start);
        bool bFlag = false;
        memset(pVisited, false, sizeof(pVisited));
        pVisited[Start.x][Start.y][Start.z] = true;
        while(!Q.empty())
        {
            Point Now = Q.front(); Q.pop();
            if(Now.x == End.x && Now.y == End.y && Now.z == End.z) { cout << "Escaped in " << Now.ans << " minute(s)." << endl; bFlag = true; break; }
            for(int i = 0; i < 6; i++)
            {
                Point Next;
                Next.x = Now.x + dx[i]; Next.y = Now.y + dy[i]; Next.z = Now.z + dz[i]; Next.ans = Now.ans + 1;
                if(Next.x >= 1 && Next.x <= L && Next.y >= 1 && Next.y <= R && Next.z >= 1 && Next.z <= C &&
                    pMaze[Next.x][Next.y][Next.z] == 0 && !pVisited[Next.x][Next.y][Next.z])
                {
                    pVisited[Next.x][Next.y][Next.z] = true;
                    Q.push(Next);
                }
            }
        }
        if(!bFlag) { cout << "Trapped!" << endl; }
    }
    return 0;
}
```

## POJ 3278

同样是 bfs，一共三种状态进行转移。

```cpp
#include <iostream>
#include <memory.h>
#include <queue>
 
using namespace std;
 
const int MAX = 1024000;
 
struct Pos
{
    Pos(int _x = 0, int _ans = 0)
    { x = _x; ans = _ans; }
     
    int x, ans;
};
 
queue<Pos> Q;
bool pVisited[MAX];
 
int main()
{
    int N, K;
    while(cin >> N >> K)
    {
        memset(pVisited, false, sizeof(pVisited));
        while(!Q.empty()) { Q.pop(); }
        Q.push(Pos(N, 0)); pVisited[N] = true;
        while(!Q.empty())
        {
            Pos Now = Q.front(); Q.pop();
            if(Now.x == K) { cout << Now.ans << endl; break; }
            if(Now.x * 2 >= 0 && Now.x * 2 < MAX && !pVisited[Now.x * 2])
            {
                Q.push(Pos(Now.x * 2, Now.ans + 1));
                pVisited[Now.x * 2] = true;
            }
            if(Now.x - 1 >= 0 && Now.x - 1 < MAX && !pVisited[Now.x - 1])
            {
                Q.push(Pos(Now.x - 1, Now.ans + 1));
                pVisited[Now.x - 1] = true;
            }
            if(Now.x + 1 >= 0 && Now.x + 1 < MAX && !pVisited[Now.x + 1])
            {
                Q.push(Pos(Now.x + 1, Now.ans + 1));
                pVisited[Now.x + 1] = true;
            }
        }
    }
    return 0;
}
```

## POJ 3279

考虑到第一行的状态确定以后，后面的 $N - 1$ 行的状态就确定了，因此只需要枚举第一行，由于数据范围比较小，所以使用二进制状态压缩即可。

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 32;
 
const int dx[] = { 1, -1, 0, 0 };
const int dy[] = { 0, 0, 1, -1 };
 
int M, N;
int pMap[MAX][MAX];
int pAns[MAX][MAX], pTmp[MAX][MAX];
 
int Solve();
int IsFlip(int x, int y);
 
int main()
{
    while(cin >> M >> N)
    {
        int ans = 2147483647;
        for(int i = 1; i <= M; i++)
        {
            for(int j = 1; j <= N; j++)
            { cin >> pMap[i][j]; }
        }
        for(int i = 0; i < (1 << N); i++)
        {
            memset(pTmp, 0, sizeof(pTmp));
            for(int j = 1; j <= N; j++)
            {
                if(i & (1 << j - 1))
                { pTmp[1][j] = 1; }
            }
            int nTmp = Solve();
            if(nTmp == -1) { continue; }
            if(nTmp < ans)
            {
                ans = nTmp;
                memcpy(pAns, pTmp, sizeof(pTmp));
            }
        }
        if(ans != 2147483647)
        {
            for(int i = 1; i <= M; i++)
            {
                for(int j = 1; j <= N; j++)
                {
                    cout << pAns[i][j];
                    if(j != N) { cout << " "; }
                }
                cout << endl;
            }
        }
        else { cout << "IMPOSSIBLE" << endl; }
    }
    return 0;
}
 
int Solve()
{
    int nRet = 0;
    for(int i = 2; i <= M; i++)
    {
        for(int j = 1; j <= N; j++)
        {
            if(IsFlip(i - 1, j)) { pTmp[i][j] = 1; }
        }
    }
    for(int i = 1; i <= N; i++)
    {
        if(IsFlip(M, i)) { return -1; }
    }
    for(int i = 1; i <= M; i++)
    {
        for(int j = 1; j <= N; j++)
        {
            nRet += pTmp[i][j];
        }
    }
    return nRet;
}
 
int IsFlip(int x, int y)
{
    int nRet = pTmp[x][y];
    for(int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 1 && nx <= M && ny >= 1 && ny <= N)
        { nRet += pTmp[nx][ny]; }
    }
    nRet += pMap[x][y];
    return nRet & 1;
}
```

## POJ 1426

这道题目也是一道 bfs，只需要记录每次遍历到的结果 `tmp % N`，同时保存已选取的数字的内容，最后判断已选取的数字的长度是否符合题目的要求。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
#include <queue>
 
using namespace std;
 
const int MAX = 256;
 
const int d[] = { 0, 1 };
 
struct Num
{
    Num(int _nNum = 1, string _ans = "1")
    {
        nNum = _nNum;
        ans = _ans;
    }
 
    int nNum;
    string ans;
};
 
int N;
bool pVisited[MAX];
queue<Num> Q;
 
int main()
{
    while(cin >> N)
    {
        if(N == 0) { break; }
        else
        {
            while(!Q.empty()) { Q.pop(); }
            memset(pVisited, false, sizeof(pVisited));
            Q.push(Num(1)); pVisited[1 % N] = true;
            while(!Q.empty())
            {
                Num Now = Q.front(); Q.pop();
                if(Now.nNum % N == 0) { cout << Now.ans << endl; break; }
                for(int i = 0; i < 2; i++)
                {
                    Num Next = Now;
                    if(!pVisited[(Now.nNum * 10 + d[i]) % N])
                    {
                        pVisited[(Now.nNum * 10 + d[i]) % N] = true;
                        Q.push(Num((Now.nNum * 10 + d[i]) % N, Now.ans + (char)(d[i] + '0')));
                    }
                }
            }
        }
    }
    return 0;
}
```

## POJ 3126

bfs 水题。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
#include <queue>
#include <set>
 
using namespace std;
 
const int MAX = 10240;
 
struct Prime
{
    Prime(int _x = 0, int _ans = 0)
    { x = _x; ans = _ans; }
     
    int x, ans;
};
 
set<int> S;
queue<Prime> Q;
bool pVisited[MAX];
 
int Change(int x, int y, int z);
 
int main()
{
    for(int i = 1000; i <= 9999; i++)
    {
        bool bFlag = true;
        for(int j = 2; j * j <= i; j++)
        {
            if(i % j == 0) { bFlag = false; }
        }
        if(bFlag) { S.insert(i); }
    }
    int N, s, e;
    while(cin >> N)
    {
        for(int i = 1; i <= N; i++)
        {
            while(!Q.empty()) { Q.pop(); }
            memset(pVisited, false, sizeof(pVisited));
            cin >> s >> e;
            Q.push(Prime(s, 0)); pVisited[s] = true;
            while(!Q.empty())
            {
                Prime Now = Q.front(); Q.pop();
                if(Now.x == e) { cout << Now.ans << endl; break; }
                for(int i = 0; i < 4; i++)
                {
                    for(int j = 0; j <= 9; j++)
                    {
                        int nNext = Change(Now.x, i, j);
                        if(S.count(nNext) && !pVisited[nNext])
                        {
                            Q.push(Prime(nNext, Now.ans + 1));
                            pVisited[nNext] = true;
                        }
                    }
                }
            }
        }
    }
    return 0;
}
 
int Change(int x, int y, int z)
{
    int nTmp = 1;
    while(y--) { nTmp *= 10; }
    x -= x / nTmp % 10 * nTmp;
    x += z * nTmp;
    return x;
}
```

## POJ 3087

模拟整个过程即可，如果出现与初始情况相同的情形，就说明无解。

```cpp
#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
    int N, C;
    bool bFlag;
    string SA, SB, S, Init;
    cin >> N;
    for(int i = 1; i <= N; i++)
    {
        cin >> C >> SA >> SB >> S;
        int nCnt = 0; Init = ""; bFlag = false;
        while(1)
        {
            nCnt++;
            string ans = "";
            for(int j = 0; j < SA.size(); j++)
            {
                ans += SB[j];
                ans += SA[j];
            }
            if(Init == "") { Init = ans; }
            SA = ans.substr(0, C);
            SB = ans.substr(C, C);
            if(nCnt != 1 && ans == Init) { break; }
            if(ans == S) { cout << i << " " << nCnt << endl; bFlag = true; break; }
        }
        if(!bFlag) { cout << i << " -1" << endl; }
    }
    return 0;
}
```

## POJ 3414

bfs 水题。处理好倒水的过程即可。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
#include <queue>
 
using namespace std;
 
const int MAX = 128;
 
struct Pots
{
    Pots(int _A = 0, int _B = 0)
    {
        A = _A; B = _B;
        while(!pOpt.empty()) { pOpt.pop(); }
    }
     
    int A, B;
    queue<string> pOpt;
};
 
int A, B, C;
bool pVisited[MAX][MAX];
queue<Pots> Q;
 
Pots Opt(Pots Now, int k);
Pots Fill(Pots Now, int x);
Pots Drop(Pots Now, int x);
Pots Pour(Pots Now, int x);
 
int main()
{
    bool bFlag;
    while(cin >> A >> B >> C)
    {
        bFlag = false;
        while(!Q.empty()) { Q.empty(); }
        memset(pVisited, false, sizeof(pVisited));
        Q.push(Pots(0, 0)); pVisited[0][0] = true;
        while(!Q.empty())
        {
            Pots Now = Q.front(); Q.pop();
            if(Now.A == C || Now.B == C)
            {
                cout << Now.pOpt.size() << endl;
                while(!Now.pOpt.empty())
                {
                    cout << Now.pOpt.front() << endl;
                    Now.pOpt.pop();
                }
                bFlag = true;
                break;
            }
            for(int i = 0; i < 6; i++)
            {
                Pots Next = Opt(Now, i);
                if(!pVisited[Next.A][Next.B])
                {
                    Q.push(Next);
                    pVisited[Next.A][Next.B] = true;
                }
            }
        }
        if(!bFlag) { cout << "impossible" << endl; }
    }
    return 0;
}
 
Pots Opt(Pots Now, int k)
{
    switch(k)
    {
        case 0:
            return Fill(Now, 0);
        case 1:
            return Fill(Now, 1);
        case 2:
            return Drop(Now, 0);
        case 3:
            return Drop(Now, 1);
        case 4:
            return Pour(Now, 0);
        case 5:
            return Pour(Now, 1);
    }
}
 
Pots Fill(Pots Now, int x)
{
    if(x == 0) { Now.A = A; Now.pOpt.push("FILL(1)"); }
    else { Now.B = B; Now.pOpt.push("FILL(2)"); }
    return Now;
}
 
Pots Drop(Pots Now, int x)
{
    if(x == 0) { Now.A = 0; Now.pOpt.push("DROP(1)"); }
    else { Now.B = 0; Now.pOpt.push("DROP(2)"); }
    return Now;
}
 
Pots Pour(Pots Now, int x)
{
    if(x == 0)
    {
        Now.B += Now.A;
        if(Now.B > B) { Now.A = Now.B - B; Now.B = B; }
        else { Now.A = 0; }
        Now.pOpt.push("POUR(1,2)");
    }
    else
    {
        Now.A += Now.B;
        if(Now.A > A) { Now.B = Now.A - A; Now.A = A; }
        else { Now.B = 0; }
        Now.pOpt.push("POUR(2,1)");
    }
    return Now;
}
```

## FZU 2150

暴力枚举两个起点，然后 bfs。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
#include <queue>
 
using namespace std;
 
const int MAX = 16;
 
const int dx[] = { 1, -1, 0, 0 };
const int dy[] = { 0, 0, 1, -1 };
 
struct Pos
{
    Pos(int _x, int _y, int _ans)
    { x = _x; y = _y; ans = _ans; }
     
    int x, y, ans;
};
 
int T, N, M;
int pMap[MAX][MAX];
bool pVisited[MAX][MAX];
queue<Pos> Q;
 
bool Check();
int Bfs(Pos A, Pos B);
 
int main()
{
    string strTmp;
    cin >> T;
    for(int k = 1; k <= T; k++)
    {
        cin >> N >> M;
        int ans = 2147483647;
        bool bFlag = false;
        for(int i = 1; i <= N; i++)
        {
            cin >> strTmp;
            for(int j = 1; j <= M; j++)
            {
                if(strTmp[j - 1] == '.') { pMap[i][j] = 1; }
                else { pMap[i][j] = 0; }
            }
        }
        for(int i = 1; i <= N; i++)
        {
            for(int j = 1; j <= M; j++)
            {
                for(int p = 1; p <= N; p++)
                {
                    for(int q = 1; q <= M; q++)
                    {
                        if(pMap[i][j] || pMap[p][q]) { continue; }
                        int nTmp = Bfs(Pos(i, j, 0), Pos(p, q, 0));
                        if(Check()) { ans = min(ans, nTmp); bFlag = true; }
                    }
                }
            }
        }
        cout << "Case " << k << ": ";
        if(bFlag) { cout << ans << endl; }
        else { cout << -1 << endl; }
    }
    return 0;
}
 
int Bfs(Pos A, Pos B)
{
    int nRet = 0;
    while(!Q.empty()) { Q.pop(); }
    memset(pVisited, false, sizeof(pVisited));
    Q.push(A); pVisited[A.x][A.y] = true;
    Q.push(B); pVisited[B.x][B.y] = true;
    while(!Q.empty())
    {
        Pos Now = Q.front(); Q.pop();
        nRet = max(nRet, Now.ans);
        for(int i = 0; i < 4; i++)
        {
            Pos Next = Now; Next.ans++;
            Next.x += dx[i]; Next.y += dy[i];
            if(Next.x >= 1 && Next.x <= N &&
                Next.y >= 1 && Next.y <= M &&
                !pVisited[Next.x][Next.y] && !pMap[Next.x][Next.y])
            {
                Q.push(Next);
                pVisited[Next.x][Next.y] = true;
            }
        }
    }
    return nRet;
}
 
bool Check()
{
    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= M; j++)
        {
            if(!pMap[i][j] && !pVisited[i][j])
            { return false; }
        }
    }
    return true;
}
```

## UVa 11624

注意可能有多个点起火，设定一个全局时间量，用来控制人以及火的运动顺序，先处理火，再处理人。然后就是 bfs 水题。

```cpp
#include <iostream>
#include <memory.h>
#include <queue>
 
using namespace std;
 
const int MAX = 1024;
 
const int dx[] = { 1, -1, 0, 0 };
const int dy[] = { 0, 0, 1, -1 };
 
struct Pos
{
    Pos(int _x = 0, int _y = 0, int _ans = 0)
    { x = _x; y = _y; ans = _ans; }
 
    int x, y, ans;
};
 
int T, R, C;
int pMap[MAX][MAX];
bool pVJ[MAX][MAX], pVF[MAX][MAX];
queue<Pos> J, F;
 
int main()
{
    string strTmp;
    cin >> T;
    for(int k = 1; k <= T; k++)
    {
        cin >> R >> C;
        bool bFlag = false;
        while(!J.empty()) { J.pop(); }
        while(!F.empty()) { F.pop(); }
        memset(pVJ, false, sizeof(pVJ));
        memset(pVF, false, sizeof(pVF));
        for(int i = 1; i <= R; i++)
        {
            cin >> strTmp;
            for(int j = 1; j <= C; j++)
            {
                if(strTmp[j - 1] == '#') { pMap[i][j] = 1; }
                else { pMap[i][j] = 0; }
                if(strTmp[j - 1] == 'J') { J.push(Pos(i, j)); pVJ[i][j] = true; }
                if(strTmp[j - 1] == 'F') { F.push(Pos(i, j)); pVF[i][j] = true; }
            }
        }
        int nTime = 0;
        while(!J.empty())
        {
            while(!F.empty() && F.front().ans <= nTime)
            {
                Pos FN = F.front(); F.pop();
                for(int i = 0; i < 4; i++)
                {
                    Pos Next = FN; Next.ans++;
                    Next.x += dx[i]; Next.y += dy[i];
                    if(Next.x >= 1 && Next.x <= R && Next.y >= 1 && Next.y <= C &&
                        !pMap[Next.x][Next.y] && !pVF[Next.x][Next.y])
                    {
                        F.push(Next);
                        pVF[Next.x][Next.y] = true;
                    }
                }
            }
            while(!J.empty() && J.front().ans  <= nTime)
            {
                Pos JN = J.front(); J.pop();
                if(JN.x == 1 || JN.x == R || JN.y == 1 || JN.y == C) { cout << JN.ans + 1 << endl; bFlag = true; break; }
                for(int i = 0; i < 4; i++)
                {
                    Pos Next = JN; Next.ans++;
                    Next.x += dx[i]; Next.y += dy[i];
                    if(Next.x >= 1 && Next.x <= R && Next.y >= 1 && Next.y <= C &&
                        !pMap[Next.x][Next.y] && !pVF[Next.x][Next.y] && !pVJ[Next.x][Next.y])
                    {
                        J.push(Next);
                        pVJ[Next.x][Next.y] = true;
                    }
                }
            }
            if(bFlag) { break; }
            nTime++;
        }
        if(!bFlag) { cout << "IMPOSSIBLE" << endl; }
    }
    return 0;
}
```

## POJ 3984

bfs 水题。

```cpp
#include <iostream>
#include <memory.h>
#include <queue>
 
using namespace std;
 
const int MAX = 8;
 
const int dx[] = { 1, -1, 0, 0 };
const int dy[] = { 0, 0, 1, -1 };
 
struct Pos
{
    Pos(int _x = 0, int _y = 0)
    { x = _x; y = _y; }
    int x, y;
};
 
struct State
{
    State(int _x = 0, int _y = 0)
    {
        Now = Pos(_x, _y);
        while(!Ans.empty()) { Ans.pop(); }
    }
     
    Pos Now;
    queue<Pos> Ans;
};
 
int pMap[MAX][MAX];
bool pVisited[MAX][MAX];
queue<State> Q;
 
int main()
{
    for(int i = 1; i <= 5; i++)
    {
        for(int j = 1; j <= 5; j++)
        { cin >> pMap[i][j]; }
    }
    while(!Q.empty()) { Q.pop(); }
    memset(pVisited, false, sizeof(pVisited));
    Q.push(State(1, 1)); pVisited[1][1] = true;
    while(!Q.empty())
    {
        State Now = Q.front(); Q.pop();
        if(Now.Now.x == 5 && Now.Now.y == 5)
        {
            while(!Now.Ans.empty())
            {
                Pos Cur = Now.Ans.front();
                cout << "(" << Cur.x - 1 << ", " << Cur.y - 1 << ")" << endl;
                Now.Ans.pop();
            }
            cout << "(4, 4)" << endl;
            break;
        }
        for(int i = 0; i < 4; i++)
        {
            int nx = Now.Now.x + dx[i];
            int ny = Now.Now.y + dy[i];
            if(nx >= 1 && nx <= 5 && ny >= 1 && ny <= 5 &&
                !pVisited[nx][ny] && !pMap[nx][ny])
            {
                State Next = Now;
                Next.Now = Pos(nx, ny);
                Next.Ans.push(Now.Now);
                Q.push(Next);
                pVisited[nx][ny] = true;
            }
        }
    }
    return 0;
}
```

## HDU 1241

求连通块个数，直接 dfs 即可。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
#include <queue>
 
using namespace std;
 
const int MAX = 128;
 
const int dx[] = { -1, 0, 1, -1, 1, -1, 0, 1 };
const int dy[] = { 1, 1, 1, 0, 0, -1, -1, -1 };
 
int N, M;
int pMap[MAX][MAX];
bool pVisited[MAX][MAX];
 
void dfs(int x, int y);
 
int main()
{
    string strTmp;
    while(cin >> N >> M)
    {
        if(N == 0 && M == 0) { break; }
        for(int i = 1; i <= N; i++)
        {
            cin >> strTmp;
            for(int j = 1; j <= M; j++)
            {
                if(strTmp[j - 1] == '*') { pMap[i][j] = 1; }
                else { pMap[i][j] = 0; }
            }
        }
        int ans = 0;
        memset(pVisited, false, sizeof(pVisited));
        for(int i = 1; i <= N; i++)
        {
            for(int j = 1; j <= M; j++)
            {
                if(!pMap[i][j] && !pVisited[i][j])
                {
                    dfs(i, j);
                    ans++;
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}
 
void dfs(int x, int y)
{
    pVisited[x][y] = true;
    for(int i = 0; i < 8; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 1 && nx <= N && ny >= 1 && ny <= M &&
            !pMap[nx][ny] && !pVisited[nx][ny])
        { dfs(nx, ny); }
    }
}
```

## HDU 1495

这道题目和 POJ 3414 非常的类似，但相较来说更简单，也是一道 bfs 水题。

```cpp
#include <iostream>
#include <memory.h>
#include <queue>
 
using namespace std;
 
const int MAX = 128;
 
struct Cola
{
    Cola(int _S = 0, int _N = 0, int _M = 0, int _ans = 0)
    { S = _S; N = _N; M = _M; ans = _ans; }
 
    int S, N, M, ans;
};
 
int S, N, M;
bool pVisited[MAX][MAX][MAX];
queue<Cola> Q;
 
Cola Opt(Cola Now, int k);
bool Check(Cola Now);
 
int main()
{
    while(cin >> S >> N >> M)
    {
        if(S == 0 && N == 0 && M == 0) { break; }
        if(S & 1) { cout << "NO" << endl; }
        else
        {
            bool bFlag = false;
            memset(pVisited, false, sizeof(pVisited));
            while(!Q.empty()) { Q.pop(); }  // 队列忘记清空
            Q.push(Cola(S, 0, 0, 0)); pVisited[S][0][0] = true;
            while(!Q.empty())
            {
                Cola Now = Q.front(); Q.pop();
                if(Check(Now))
                {
                    cout << Now.ans << endl;
                    bFlag = true;
                    break;
                }
                for(int i = 0; i < 6; i++)
                {
                    Cola Next = Opt(Now, i);
                    if(!pVisited[Next.S][Next.N][Next.M])
                    {
                        Q.push(Cola(Next.S, Next.N, Next.M, Next.ans));
                        pVisited[Next.S][Next.N][Next.M] = true;
                    }
                }
            }
            if(!bFlag) { cout << "NO" << endl; }
        }
    }
    return 0;
}
 
Cola Opt(Cola Now, int k)
{
    if(k == 0)
    {
        Now.N += Now.S;
        if(Now.N > N) { Now.S = Now.N - N; Now.N = N; }
        else { Now.S = 0; }
    }
    if(k == 1)
    {
        Now.S += Now.N;
        Now.N = 0;
    }
    if(k == 2)
    {
        Now.M += Now.S;
        if(Now.M > M) { Now.S = Now.M - M; Now.M = M; }
        else { Now.S = 0; }
    }
    if(k == 3)
    {
        Now.S += Now.M;
        Now.M = 0;
    }
    if(k == 4)
    {
        Now.N += Now.M;
        if(Now.N > N) { Now.M = Now.N - N; Now.N = N; }
        else { Now.M = 0; }
    }
    if(k == 5)
    {
        Now.M += Now.N;
        if(Now.M > M) { Now.N = Now.M - M; Now.M = M; }
        else { Now.N = 0; }
    }
    Now.ans++;
    return Now;
}
 
bool Check(Cola Now)
{
    int x = Now.S, y = Now.N, z = Now.M, p = S / 2;
    return (x == p && y == p) || (x == p && z == p) || (y == p && z == p);
}
```

## HDU 2612

首先计算 $Y$ 和 $M$ 走到地图上每个点的最小时间，然后枚举每个点，计算 $Y$ 和 $M$ 走到该点时间和的最小值，最后结果乘以 11 分钟即可。

```cpp
#include <iostream>
#include <memory.h>
#include <string>
#include <queue>
 
using namespace std;
 
const int MAX = 256;
 
const int dx[] = { 1, -1, 0, 0 };
const int dy[] = { 0, 0, 1, -1 };
 
struct Pos
{
    Pos(int _x = 0, int _y = 0, int _s = 0)
    { x = _x; y = _y; s = _s; }
     
    int x, y, s;
};
 
Pos SY, SM;
int N, M;
int pMap[MAX][MAX];
int pAns[2][MAX][MAX];
bool pVisited[MAX][MAX];
queue<Pos> Q;
 
void Solve(Pos S, int k);
 
int main()
{
    string strTmp;
    while(cin >> N >> M)
    {
        memset(pAns, -1, sizeof(pAns));
        for(int i = 1; i <= N; i++)
        {
            cin >> strTmp;
            for(int j = 1; j <= M; j++)
            {
                if(strTmp[j - 1] == '#') { pMap[i][j] = 1; }
                else if(strTmp[j - 1] == '@') { pMap[i][j] = 2; }
                else { pMap[i][j] = 0; }
                if(strTmp[j - 1] == 'Y') { SY = Pos(i, j, 0); }
                if(strTmp[j - 1] == 'M') { SM = Pos(i, j, 0); }
            }
        }
        Solve(SY, 0); Solve(SM, 1);
        int ans = 2147483647;
        for(int i = 1; i <= N; i++)
        {
            for(int j = 1; j <= M; j++)
            {
                if(pMap[i][j] == 2 && pAns[0][i][j] != -1 && pAns[1][i][j] != -1)
                { ans = min(ans, pAns[0][i][j] + pAns[1][i][j]); }
            }
        }
        cout << ans * 11 << endl;
    }
    return 0;
}
 
void Solve(Pos S, int k)
{
    while(!Q.empty()) { Q.pop(); }
    memset(pVisited, false, sizeof(pVisited));
    Q.push(S); pVisited[S.x][S.y] = true;
    while(!Q.empty())
    {
        Pos Now = Q.front(); Q.pop();
        if(pAns[k][Now.x][Now.y] == -1)
        { pAns[k][Now.x][Now.y] = Now.s; }
        for(int i = 0; i < 4; i++)
        {
            int nx = Now.x + dx[i];
            int ny = Now.y + dy[i];
            if(nx >= 1 && nx <= N && ny >= 1 && ny <= M &&
                !pVisited[nx][ny] && pMap[nx][ny] != 1)
            {
                Q.push(Pos(nx, ny, Now.s + 1));
                pVisited[nx][ny] = true;
            }
        }
    }
}
```

刷完这个专题，感觉对 bfs 的理解更加深入透彻了。
