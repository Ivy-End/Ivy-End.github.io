# Codeforces 1B - Spreadsheet


[1B Spreadsheet](https://codeforces.com/contest/1/problem/B)

## Analysis

The essence of this problem lays in the conversion between decimal ('0'-'9') and base 26 ('A'-'Z').

Notice: There is no number in the base 26 system that function as the number '0' in the decimal system, so when the decimal number is a multiple of 26, a special handle is needed.

`if(C % 26 == 0) { strTmp = 'Z' + strTmp; C /= 26; C--; continue; }`

In the code above, `C` means the column, while `strTmp` stands for the base 26 string after conversion.

## Solution

```cpp
#include <iostream>
#include <ctype.h>

using namespace std;

string Convert(string x);

int N;
string strInput; 

int main()
{
	cin >> N;
	for(int i = 1; i <= N; i++)
	{
		cin >> strInput;
		cout << Convert(strInput) << endl;
	}
	return 0;
} 

string Convert(string x)
{
	string strRet = ""; 
	int nTmp = 0;
	bool bTmp = false;
	for(int i = 0; i < x.size(); i++)
	{
		if(isdigit(x[i]) && !bTmp) { bTmp = true; nTmp++; }
		if(!isdigit(x[i])) { bTmp = false; }
	}
	if(nTmp == 1)
	{
		string R, C;
		int nC = 0, nHex = 1;
		for(int i = 0; i < x.size(); i++)
		{
			if(isalpha(x[i])) { C += x[i]; }
			else { R += x[i]; }
		}
		for(int i = 0; i < C.size(); i++)
		{
			nC += (C[C.size() - i - 1] - 'A' + 1) * nHex;
			nHex *= 26;
		}
		strRet += "R" + R + "C";
		string strTmp = "";
		while(nC)
		{
			strTmp = (char)(nC % 10 + 48) + strTmp;
			nC /= 10;
		}
		strRet += strTmp;
	}
	else
	{
		int C = 0;
		int nPos = x.find('C');
		for(int i = nPos + 1; i < x.size(); i++)
		{
			C *= 10;
			C += (x[i] - '0');
		}
		string strTmp = "";
		while(C)
		{
			if(C % 26 == 0) { strTmp = 'Z' + strTmp; C /= 26; C--; continue; }
			strTmp = (char)((C % 26) + 'A' - 1) + strTmp;
			C /= 26;
		}
		strRet = strTmp + x.substr(1, nPos - 1);
	}
	return strRet;
}
```
