# 算法专题：求解线性方程组


求解线性方程组的有效方法是高斯消元。这个算法我看了半个下午才真正理解并且写了出来。

这个算法的核心思想就是将一个方程组的增广矩阵通过初等行变换转变成上三角矩阵，然后求解各个未知数的解。

我写的高斯消元是将所有系数看成一个矩阵来求解的。

下面来简要讲一下高斯消元的过程：

首先，我们根据方程组写出增广矩阵。每次都找 $ x_{i} $ 系数的绝对值最大的那个方程，将它移到上方，而将下面的方程组的 $ x_{i} $ 的系数全部化成 0。以此类推，到最后再逆序求解每个未知数的解。

我们来看一个例子，求解方程组 $ \begin{cases}2x+y-z=8\\\ -3x-y+2z=-11\\\ -2x+y+2z=-3\end{cases} $

首先我们写出它的增广矩阵 $$ \begin{bmatrix}\left.\begin{matrix}2 & 1 & -1\\\ -3 & -1 & 2\\\ -2 & 1 & 2\end{matrix}\right|\begin{matrix}8\\\ -11\\\ -3\end{matrix}\end{bmatrix} $$ 接下来我们按照算法步骤来求解这个方程组 $$ \begin{bmatrix} \left.\begin{matrix} 2 & 1 & -1\\\ -3 & -1 & 2\\\ -2 & 1 & 2 \end{matrix}\right| \begin{matrix} 8\\\ -11\\\ -3 \end{matrix} \end{bmatrix}\Rightarrow \begin{bmatrix} \left.\begin{matrix} -3 & -1 & 2\\\ 2 & 1 & -1\\\ -2 & 1 & 2 \end{matrix}\right| \begin{matrix} -11\\\ 8\\\ -3 \end{matrix}\end{bmatrix}\Rightarrow \begin{bmatrix} \left.\begin{matrix} -3 & -1 & 2\\\ 0 & \frac{1}{3} & \frac{1}{3}\\\ 0 & \frac{5}{3} & \frac{2}{3} \end{matrix}\right| \begin{matrix}-11\\\ \frac{2}{3}\\\ \frac{13}{3} \end{matrix} \end{bmatrix}\Rightarrow \begin{bmatrix} \left.\begin{matrix} -3 & -1 & 2\\\ 0 & \frac{1}{3} & \frac{1}{3}\\\ 0 & 0 & -1 \end{matrix}\right| \begin{matrix} -11\\\ \frac{2}{3}\\\ 1 \end{matrix} \end{bmatrix}\\\ \Rightarrow z=-1,y=3\times\left ( \frac{2}{3}-\frac{1}{3}\times\left ( -1 \right )\right )=3,x=-\frac{1}{3}\times\left ( -11+3-2*\left ( -1 \right ) \right )=2 $$ 

表达能力有限，我也只能解释成这样了。

当时我在网上找资料的时候还抱怨作者为什么不解释清楚点，现在发现，不是作者不愿意解释清楚，这个算法实在难以解释清楚。

代码如下：

```cpp
#include <iostream>

using namespace std;

const int MAX = 1024;

int N;
double f[MAX][MAX], ans[MAX];    // f[][]为系数（包括常数），ans[]为结果

double fabs(double x);    // double的绝对值
void Gauss();

int main()
{
    cin >> N;
    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= N + 1; j++)    // 读取所有系数（包括常数）方程已化为ax+by+…+c=0的形式
        { cin >> f[i][j]; }
    }
    Gauss();
    return 0;
}

void Gauss()
{
    int nRow = 0;    // 保存当前系数绝对值最大的行
    double dMax = 0.0f;    // 保存当前最大绝对值的系数
    for(int i = 1; i <= N; i++)    // 对于每一列都处理
    {
        dMax = f[i][i]; nRow = i;    // 初始化
        for(int j = i + 1; j <= N; j++)    // 比较下面所有行的第i列的系数
        {
            if(fabs(f[j][i]) > fabs(dMax))    // 取绝对值最大的系数
            {
                dMax = f[j][i];
                nRow = j;
            }
        }
        if(dMax != f[i][i])    // 如果不是当前行最大
        {
            for(int j = i; j <= N + 1; j++)
            { swap(f[nRow][j], f[i][j]); }    // 交换这两个方程组的位置
        }
        for(int j = i + 1; j <= N; j++)    // 对于下面的所有方程
        {
            double dTmp = f[j][i] / f[i][i];    // 计算要将第i列的系数消去所需要的倍率
            for(int k = i; k <= N + 1; k++)    // 对于第j行的方程的每一项的系数都要进行处理
            {
                // 用第nRow行的方程乘以dTmp后去减第j行的方程，这样就可以把第j行的方程的第i列的系数消去
                double dMinus = dTmp * f[i][k];    
                f[j][k] -= dMinus;
            }
        }
    }
    ans[N + 1] = 1.0f;    // 预处理，为了下面的循环方便
    for(int i = N; i >= 1; i--)    // 逆序求解
    {
        for(int j = i; j <= N + 1; j++)
        {
            ans[i] -= f[i][j] * ans[j];    // 减去已求解的未知数乘以其在当前求解的方程中的系数
        }
        ans[i] /= f[i][i];    // 将该未知数的系数化为1，得到结果
    }
    for(int i = 1; i <= N; i++)
    { cout << ans[i] << " "; }
    cout << endl;
}

double fabs(double x)
{
    if(x < 0) { x = -x; }
    return x;
}
```

关于高斯消元，这只是一个列主元的算法，还有全主元的，不过个人觉得列主元的就足够用了。
