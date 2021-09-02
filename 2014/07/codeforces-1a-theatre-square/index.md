# Codeforces 1A - Theatre Square


[1A Theatre Square](https://codeforces.com/contest/1/problem/A)

## Analysis

Calculate the number of flagstones used to cover the length and width, then multiply them to get the correct answer.

Notice: Pay attention to the data range. Use `unsigned long long`.

## Solution

```cpp
#include <iostream>

using namespace std;

int main()
{
    unsigned long long n, m, a, ans = 0;
    cin >> n >> m >> a;
    if(n % a == 0) { n /= a; }
    else { n = n / a + 1; }
    if(m % a == 0) { m /= a; }
    else { m = m / a + 1; } 
    cout << n * m << endl; 
    return 0; 
} 
```
