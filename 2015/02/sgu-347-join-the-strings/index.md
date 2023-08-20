# SGU 347 - Join the Strings


## Description

His Royal Highness King of Berland Berl XV was a very wise man and had a very accomplished wife, who was aware of the fact, that prominent and outstanding personalities once having written down their names on the pages of glorious History, remain there forever. His Royal Highness King Berl XV experienced an intrinsic, lost nowadays, deep and sincere sense of respect and trust for his beloved spouse. So he decided to acquire a chronicler of his own. Due to the ambiguous nature of misunderstanding and the crying injustice of history to ambiguity, he decided to leave all his royal responsibilities aside and made up his royal mind to find the chronicler, who will make him famous, depicting all his heroic deeds truthfully and gloriously enough.

The King assembled the greatest minds of his kingdom at the Academic Chroniclers Meeting (ACM), as he named it, and decided to test their might. The task was to build the Smallest Lexicographical Concatenation (SLC) out of the given $N$ strings. SLC of $N$ strings $s_1,\cdots, s_N$ is the lexicographically smallest their concatenation $s_{i_1} + \cdots + s_{i_N}$, where $ i_1,\cdots, i_N $ is a permutation of integers from 1 through $N$. It's a great privilege to be a chronicler, so don't miss your chance and don't screw it up! Make the king choose you!

## Input

The first line of the input file contains a single integer $N$ ($1\leq N\leq 100$) indicating the number of strings. The following $N$ lines contain $N$ strings, one string per line. The length of each string is no more than 100 characters. Each string consists only of lowercase Latin letters. There are no any leading or trailing spaces.

## Output

Print the SLC of the given $N$ strings to the output file as a single line.

## Sample Input

```
6
it
looks
lilke
an
easy
problem
```

## Sample Output

```
aneasyitlikelooksproblem
```

## Analysis

一开始没看题意，只看了输入输出，以为是按字典序连接后输出，后来才发现是使得连接后的字典序最小。

既然要使得连接后的字典序列最小，那么对于任意两个相邻的字符串 $x, y$ 当且仅当 $x + y$ 的字典序比 $y + x$ 的字典序大的时候交换，因此直接排序即可。

对于直接按字典序最小排序输出的一个很好的反例是：对于两个字符串 ac 和 aca，应该输出 acaac，而不是 acaca。

## Solution

```cpp
#include <iostream>
#include <string>
#include <algorithm>
 
using namespace std;
 
const int MAX = 128;
 
string pData[MAX];
 
int cmp(string x, string y)
{ return x + y < y + x; }
 
int main()
{
    int N;
    while(cin >> N)
    {
        for(int i = 1; i <= N; i++)
        { cin >> pData[i]; }
        sort(pData + 1, pData + N + 1, cmp);
        for(int i = 1; i <= N; i++)
        { cout << pData[i]; }
        cout << endl;
    }
    return 0;
}
```

这道题目总的来说不难，但是要把总的字典序最小转换到排序的问题上，本身还是具有一定难度的。

而且以后一定要认真看题，不能直接看输入输出。

不过觉得这道题目好像还在考英语。
