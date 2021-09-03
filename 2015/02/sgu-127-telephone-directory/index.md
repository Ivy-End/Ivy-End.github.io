# SGU 127 - Telephone directory


## Description

CIA has decided to create a special telephone directory for its agents. The first 2 pages of the directory contain the name of the directory and instructions for agents, telephone number records begin on the third page. Each record takes exactly one line and consists of 2 parts: the phone number and the location of the phone. The phone number is 4 digits long. Phone numbers cannot start with digits 0 and 8. Each page of the telephone directory can contain not more then $K$ lines. Phone numbers should be sorted in increasing order. For the first phone number with a new first digit, the corresponding record should be on a new page of the phone directory. You are to write a program, that calculates the minimal number P pages in the directory. For this purpose, CIA gives you the list of numbers containing $N$ records, but since the information is confidential, without the phones locations.

## Input

The first line contains a natural number $K$ ($0 < K < 255$) - the maximum number of lines that one page can contain. The second line contains a natural $N$ ($0 < N < 8000$) - number of phone numbers supplied. Each of following $N$ lines contains a number consisting of 4 digits - phone numbers in any order, and it is known, that numbers in this list cannot repeat.

## Output

First line should contain a natural number $P$ - the number of pages in the telephone directory.

## Sample Input

```
5
10
1234
5678
1345
1456
1678
1111
5555
6789
6666
5000
```


## Sample Output

```
5
```

## Analysis

这是一道水题。事实上，我们只需要电话号码的第一位，因此，读入数据以后直接除以 1000 即可，然后记录一下以各个数字开头的电话号码有几个。

如果不能被 $K$ 整除，那么就需要 `Num / (K + 1)` 页，否则只需要 `Num / K` 页，这样处理的同时也满足了题目中每个新的首位电话号码另起一页的要求。

需要注意的是，最后要把题目中提到的电话簿开头 2 页加上去。

## Solution

```cpp
#include <iostream>
#include <memory.h>
 
using namespace std;
 
const int MAX = 16;
const int HEX = 1000;
 
int K, N;
int pData[MAX];
 
int main()
{
    while(cin >> K >> N)
    {
        int nTmp, ans = 0;
        for(int i = 1; i <= N; i++)
        {
            cin >> nTmp;
            pData[nTmp / HEX]++;
        }
        for(int i = 1; i <= 9; i++)
        { ans += pData[i] / K + (pData[i] % K != 0); }
        cout << ans + 2 << endl;
    }
    return 0;
}
```

被 101 卡了好久，一直做不出来，往后看看，这道水题居然排在了它的后面。
