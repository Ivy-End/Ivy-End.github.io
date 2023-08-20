# SGU 276 - Andrew's Troubles


## Description

Famous Berland ACM-ICPC team Anisovka consists of three programmers: Andrew, Michael and Ilya. A long time ago, during the first few months the team was founded, Andrew was very often late to the trainings and contests. To stimulate Andrew to be more punctual, Ilya and Andrew decided to introduce a new rule for team participants. If somebody is late (i.e. comes at least one second after appointed time) he owes a cup of tea to other team members. If he is late for 5 minutes, he owes two cups of tea. If he is late for 15 minutes, he owes three cups of tea. And if he is late for 30 minutes or more, he owes 4 cups of tea. 

The training starts at the time $S$ (counted in seconds, from some predefined moment of time) and Andrew comes at the time $P$ (also in seconds, counted from the same moment of time).

Your task is to find how many cups of tea Andrew owes.

## Input

The input file contains single line with integer numbers $S$ and $P$ ($0\leq S, P\leq 10^4$). 

## Output

Write to the output file the number of cups Andrew owes.

## Sample Input #1

```
10 10
```

## Sample Output #1

```
0
```

## Sample Input #2

```
10 11
```

## Sample Output #2

```
1
```

## Sample Input #3

```
0 300
```

## Sample Output #3

```

```

## Analysis

水题。

## Solution

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    int S, P;
    while(cin >> S >> P)
    {
        int nDiff = P - S;
        if(nDiff <= 0) { cout << 0 << endl; }
        else if(nDiff >= 1 && nDiff < 300) { cout << 1 << endl; }
        else if(nDiff >= 300 && nDiff < 900) { cout << 2 << endl; }
        else if(nDiff >= 900 && nDiff < 1800) { cout << 3 << endl; }
        else { cout << 4 << endl; }
    }
    return 0;
}
```

练练手。
