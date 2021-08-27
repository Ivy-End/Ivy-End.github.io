# 扬州拾遗（一）：竞赛中的函数


## 一、函数问题基本方法

### 1. 数型结合法

**例1**：求方程 $ \left | x-1\right |=\frac{1}{x} $ 的正根的个数。

**解**：作图像得，正根个数为 $ 1 $ 。

**例2**：求函数 $ f\left(x\right)=\sqrt{x^{4}-3x^{2}-6x+13}-\sqrt{x^{4}-x^{2}+1} $ 的最大值。

**解**： $ f\left(x\right)=\sqrt{\left(x^{2}-2\right)^{2}+\left(x-3\right)^{2}}-\sqrt{\left(x^{2}-1\right)^{2}+x^{2}} $ 即表示点 $ P\left(x,x^{2}\right) $ 到点 $ A\left(3,2\right),B\left(0,1\right) $ 的距离之差，点 $ P $ 在抛物线 $ y=x^{2} $ 上。

易得点 $ P $ 在直线 $ l_{AB}:x-3y+3=0 $ 上，因此得到 $ P\left(\frac{1-\sqrt{37}}{6},\frac{19-\sqrt{37}}{18}\right) $ ，故 $$ \begin{align*} f\left(x\right)_{max} &=\sqrt{\left[\left(\frac{1-\sqrt{37}}{6}-3\right)^{2}+\left(\frac{19-\sqrt{37}}{18}-2\right)^{2}\right]-\left[\left(\frac{1-\sqrt{37}}{6}\right)^{2}+\left(\frac{19-\sqrt{37}}{18}-1\right)^{2}\right]} \\\ &=\frac{2\sqrt{245+34\sqrt{37}}}{9} \end{align*}$$

### 2. 函数性质的应用

**例3**：设 $ x,y\in\mathbf{R} $ ，且满足 $ \begin{cases} \left ( x-1 \right )^{3}+1997\left ( x-1 \right )=-1\\\ \left ( y-1 \right )^{3}+1997\left ( y-1 \right )=1 \end{cases} $ ，求 $ x+y $ 。

**解**：考虑函数 $ f\left(s\right)=s^{3}+1997s $ ，该函数既是奇函数又是增函数。又 $ f\left(x-1\right)=-f\left(y-1\right) $ ，得 $ \left(x-1\right)+\left(y-1\right)=0 $ ，因此 $ x+y=2 $ 。

**例4**：奇函数 $ f\left(x\right) $ 在定义域 $ \left(-1,1\right) $ 内是减函数，又 $ f\left(1-a\right)+f\left(1-a^{2}\right)<0 $ ，求 $ a $ 的取值范围。

**解**：首先由函数的定义域得 $ \begin{cases} -1<1-a<1\\\ -1<1-a^{2}<1 \end{cases} $ ，解得 $ 0< a< \sqrt{2} $ 。下面进行分类讨论：

$ 1^{\circ} \left | 1-a \right |< 1-a^{2}\Rightarrow 0< a< 1 $

$ 2^{\circ}\left | 1-a^{2} \right |< 1-a\Rightarrow -2< a< 0 $ （不符题意）。

综上所述， $ a\in\left ( 0,1 \right ) $ 。

**例5**：设 $ f\left(x\right) $ 是定义在 $ \left(-\infty,+\infty\right) $ 上以 $ 2 $ 为周期的函数，对 $ k\in\mathbf{Z} $ ，用 $ I_{k} $ 表示区间 $ \left(2k-1,2k+1\right] $ ，已知当 $ x\in I_{0} $ 时， $ f\left(x\right)=x^{2} $ ，求 $ f\left(x\right) $ 在 $ I_{k} $ 上的解析式。

**解**：根据图像的平移，易得 $ f\left(x\right)=\left(x-2k\right)^{2} $ 。

**例6**：解方程 $$ \left(3x-1\right)\left(\sqrt{9x^{2}-6x+5}+1\right)+\left ( 2x-3 \right )\left ( \sqrt{4x^{2}-12x+13}+1 \right )=0 $$

**解**：首先进行因式分解： $$ \left(3x-1\right)\left(\sqrt{\left ( 3x-1 \right )^{2}+4}+1\right)+\left ( 2x-3 \right )\left ( \sqrt{\left ( 2x-3 \right )^{2}+4}+1 \right )=0 $$ 
考察函数 $$ f\left ( s \right )=s\left ( \sqrt{s^{2}+4}+1 \right ) $$ 它既是奇函数又是增函数。因此上述方程转化为 $$ \left ( 3x-1 \right )+\left ( 2x-3 \right )=0 $$ 解得 $ x=\frac{4}{5} $ 。

### 3. 配方法

**例7**：求函数 $ y=x+\sqrt{2x+1} $ 的值域。

**解**：首先考虑定义域得 $ D_{y}=\left [ -\frac{1}{2},+\infty \right ) $ 。又 $$ y=\left ( \sqrt{x+\frac{1}{2}}+\sqrt{\frac{1}{2}} \right )^{2}-1\geq -\frac{1}{2} $$ 因此该函数的值域为 $ R_{y}=\left [ -\frac{1}{2},+\infty \right ) $ 。

### 4. 换元法

**例8**：求函数 $ y=\left ( \sqrt{1+x}+\sqrt{1-x}+2 \right )\left ( \sqrt{1-x^{2}}+1 \right ),x\in\left [ 0,1 \right ] $ 的值域。

**解**：令 $ s=\sqrt{1+x}+\sqrt{1-x} $ ，则 $ s^{2}=2\left ( \sqrt{1-x^{2}}+1\right ) $ ，且 $ s\in\left [ -\sqrt{2},\sqrt{2} \right ] $ 。代入得 $ y=\frac{1}{2}\cdot \left ( s+2 \right )\cdot s^{2}=\frac{1}{2}s^{3}+s^{2} $ ，易得该函数的值域为 $ R_{y}=\left [ 2+\sqrt{2},8 \right ] $ 。

### 5. 关于反函数

**例9**：若函数 $ y=f\left ( x \right ) $ 定义域、值域均为 $ \mathbf{R} $ ，且存在反函数。若 $ y=f\left ( x \right ) $ 在 $ \left(-\infty,+\infty\right) $ 上递增，求证： $ y=f^{-1}\left ( x \right ) $ 在 $ \left(-\infty,+\infty\right) $ 上递增。

**解**：不妨设 $ x_{1}>x_{2} $ ，则 $ f\left ( x_{1} \right )>f\left ( x_{2} \right ) $ ，因此 $$ f^{-1}\left ( f\left ( x_{1} \right ) \right )-f^{-1}\left ( f\left ( x_{2} \right ) \right )=x_{1}-x_{2}>0 $$ 所以 $ y=f^{-1}\left ( x \right ) $ 在 $ \left(-\infty,+\infty\right) $ 上递增。证毕。

**例10**：设函数 $ f\left ( x \right )=\sqrt[4]{\frac{4x+1}{3x+2}} $ ，解方程 $ f\left ( x \right )=f^{-1}\left ( x \right ) $ 。

**解**：即 $ \sqrt[4]{\frac{4x+1}{3x+2}}=x $ ，整理得 $$ \left ( x-1 \right )\left ( 3x^{4}+5x^{3}+5x^{2}+5x+1 \right )=0 $$ 显然 $ 3x^{4}+5x^{3}+5x^{2}+5x+1>0 $ ，故 $ x=1 $ 。

## 二、典型例题

**题1**：已知不等式 $ \sin^{2}x+a\cos x+a^{2}\geq 1+\cos x $ 对一切 $ x\in\mathbf{R} $ 恒成立，求 $ a $ 的取值范围。

**解**： $ \cos^{2}x+\left ( 1-a \right )\cos x - a^{2}\leq 0 $ ，其中 $ \cos x\in\left [ -1,1 \right ] $ 。令 $$ f\left ( x \right )=\cos^{2}x+\left ( 1-a \right )\cos x - a^{2} $$ 则 $$ \begin{cases} f\left ( -1 \right )\leq 0\\\ f\left ( 1 \right )\leq 0 \end{cases} \Rightarrow \begin{cases} a^{2}-a\geq 0\leq 0\\\ a^{2}-a-2\geq 0\leq 0 \end{cases} \Rightarrow a\in\left ( -\infty,-2 \right ]\cup\left [ 1,+\infty \right ) $$

**题2**：已知函数 $ f\left ( x \right ) $ 的定义域是 $ \left [ -\frac{1}{2},\frac{1}{2} \right ] $ ，求函数 $ g\left ( x \right )=f\left ( ax \right )+f\left ( \frac{x}{a} \right ) $ 的定义域 $ \left ( a> 0\right ) $ 。

**解**：根据函数函数 $ f\left ( x \right ) $ 的定义域很容易得到以下不等式 $ \begin{cases} -\frac{1}{2}\leq ax\leq \frac{1}{2}\\\ -\frac{1}{2}\leq \frac{x}{a}\leq \frac{1}{2} \end{cases} $ 。即 $ \begin{cases} -\frac{1}{2a}\leq x\leq \frac{1}{2a}\\\ -\frac{a}{2}\leq x\leq \frac{a}{2} \end{cases} $ 分类讨论得：

$ 1^{\circ}0< a\leq 1,D_{g}=\left [ -\frac{a}{2},\frac{a}{2} \right ] $

$ 2^{\circ}a> 1,D_{g}=\left [ -\frac{1}{2a},\frac{1}{2a} \right ] $ 

**题3**：已知 $ f\left(x\right) $ 是定义在 $ \mathbf{R} $ 上的函数， $ f\left(1\right)=1 $ ，且对任意 $ x\in\mathbf{R} $ 都有 $ f\left(x+5\right)\geq f\left(x\right) + 5,f\left(x+1\right)\leq f\left(x\right)+1 $ ，且 $ g\left ( x \right )=f\left ( x \right )+1-x $ 求 $ g\left(2012\right) $ 。

**解**： $ f\left ( x+5 \right )\leq f\left ( x+4 \right )+1\leq \cdots \leq f\left ( x \right )+5 $ ，又 $ f\left ( x \right )\geq f\left ( x \right )+5 $ ，故 $ f\left ( x \right )= f\left ( x \right )+5 $ 。运用数学归纳法，并结合 $ f\left ( 1 \right )=1 $ ，不难得到 $ f\left ( x \right )=x $ 。因此 $ g\left ( 2012 \right )=f\left ( 2012 \right )+1-2012=1 $ 。

**题4**：设函数 $ f:\mathbf{N^{\*}}\rightarrow \mathbf{N^{\*}} $ ，且严格递增。当 $ m,n $ 互质时， $ f\left ( m\cdot n \right )=f\left ( m \right )\cdot f\left ( n \right ) $ 。若 $ f\left ( 19 \right )=19 $ ，求 $ f\left ( f\left ( 19 \right ) \right )\cdot f\left ( 98 \right ) $ 的值。

**解**：由题意得，当 $ x\leq 19 $ 时，有 $ f\left ( x \right )=x $ 。又 $ f\left ( 17\cdot 19 \right )=f\left ( 17 \right )\cdot f\left ( 19 \right )=323 $ ，则当 $ x\leq 323 $ 时，有 $ f\left ( x \right )=x $ 。所以 $$ f\left ( f\left ( 19 \right ) \right )\cdot f\left ( 98 \right )=f\left ( 19 \right )\cdot f\left ( 98 \right )=19*98=1862 $$

**题5**：设函数 $ f:\mathbf{N^{\*}}\rightarrow \mathbf{N^{\*}} $ ，且严格递增。 $ f\left ( f\left ( n \right ) \right )=3n $ 。求 $ f\left ( 1 \right )+f\left ( 9 \right )+f\left ( 36 \right ) $ 。

**解**：首先可以得到 $ f\left ( f\left ( 1 \right ) \right )=3 $ 。不妨假设 $ f\left ( 1 \right )=1 $ ，代入得 $ f\left ( f\left ( 1 \right ) \right )=f\left ( 1 \right )=1\neq 3 $ ，矛盾。因此易证 $ f\left ( 1 \right )=2 $ 。于是可以列出： $$ f\left ( 2 \right )=f\left ( f\left ( 1 \right ) \right )=3,f\left ( 3 \right )=f\left ( f\left ( 2 \right ) \right )=6,f\left ( 6 \right )=f\left ( f\left ( 3 \right ) \right )=9,f\left ( 9 \right )=f\left ( f\left ( 6 \right ) \right )=18 $$ 于是得到 $ f\left ( 9 \right )=18 $ 。由 $ f\left ( 3 \right )=6,f\left ( 6 \right )=9 $ 再结合题中所给条件，得 $ f\left ( 4 \right )=7 $ 。因此 $$ f\left ( 7 \right )=f\left ( f\left ( 4 \right ) \right )=12,f\left ( 12 \right )=f\left ( f\left ( 7 \right ) \right )=21,f\left ( 21 \right )=f\left ( f\left ( 12 \right ) \right )=36,f\left ( 36 \right )=f\left ( f\left ( 21 \right ) \right )=63 $$ 于是得到 $ f\left ( 36 \right )=63 $ ，将以上的结果相加得 $ f\left ( 1 \right )+f\left ( 9 \right )+f\left ( 36 \right )=2+18+63=83 $ 。

**题6**：已知函数 $ f\left ( x \right )=\log_{x}{\left ( x+1 \right )},x\in\left ( 1,+\infty \right ) $ ，试比较 $ f\left ( x \right ),f\left ( x+1 \right ) $ 的大小。

**解**： $ \frac{f\left ( x+1 \right )}{f\left ( x \right )}=\frac{\log{\left (x+2 \right )}}{\log{\left (x+1 \right )}}\cdot \frac{\log{\left (x+1 \right )}}{\log{x}}=\frac{\log{\left ( x+2 \right )}}{\log{x}}> 1 $ ，所以 $ f\left ( x+1 \right )> f\left ( x \right ) $ 。

**题7**：已知 $ 3^{a}+13^{b}=17^{a},5^{a}+7^{b}=11^{b} $ ，试判断实数 $ a,b $ 的大小关系，并证明之。

**解**：当 $ a=1 $ 时， $ b> 1 $ ，得 $ b> a $ 。假设 $ b\leq a $ ，易得 $$ \begin{cases} 17^{a}\leq 3^{a}+13^{a}\\\ 5^{b}+7^{b}\leq 11^{b} \end{cases} \Rightarrow \begin{cases}1\leq \left ( \frac{3}{17} \right )^{a}+\left ( \frac{13}{17} \right )^{a}\\\ 1\geq \left ( \frac{5}{11} \right )^{b}+\left ( \frac{7}{11} \right )^{b} \end{cases} $$ 不妨令 $$ f\left ( x \right )=\left ( \frac{3}{11} \right )^{x}+\left ( \frac{13}{17} \right )^{x},g\left ( x \right )=\left ( \frac{5}{11} \right )^{x}+\left ( \frac{7}{11} \right )^{x} $$ 易得 $ f\left ( 1 \right )=\frac{16}{17}< g\left ( 1 \right )=\frac{12}{11} $ 。不成立。综上所述 $ b> a $ 。

**题8**：设 $ f\left ( x \right )=x^{n}+ax^{2}+bx+c $ ， $ n $ 为自然数。已知 $ f\left ( -1 \right )=0,f\left ( 1 \right )=-6,f\left ( 2 \right )=-9,f\left ( 3 \right )=-4,f\left ( 6 \right )=119 $ ，求 $ f\left ( x \right ) $ 。

**解**：将所给条件代入得 $ \begin{cases} \left ( -1 \right )^{n}+a-b+c=0\\\ 1+a+b+c=-6\\\ 2^{n}+4a+2b+c=-9\\\ 3^{n}+9a+3b+c=-4\\\ 6^{n}+36a+6b+c=119 \end{cases} $ 对 $ n $ 进行分类讨论：

 $ 1^{\circ}n $ 为奇数，上述方程组可化简得 $ \begin{cases}-1+a-b+c=0\\\ 1+a+b+c=-6\\\ 2^{n}+4a+2b+c=-9\\\ 3^{n}+9a+3b+c=-4\\\ 6^{n}+36a+6b+c=119 \end{cases} $ ，解得 $ \begin{cases}n=3\\\ a=-2\\\ b=-4\\\ c=-1 \end{cases} $ 。

 $ 2^{\circ}n $ 为偶数，上述方程组可化简得 $ \begin{cases} 1+a-b+c=0\\\ 1+a+b+c=-6\\\ 2^{n}+4a+2b+c=-9\\\ 3^{n}+9a+3b+c=-4\\\ 6^{n}+36a+6b+c=119 \end{cases} $ ，不成立。
 
 综上所述 $ f\left ( x \right )=x^{3}-2x^{2}-4x-1 $ 。

**题9**：已知 $ a,b,c $ 为非零实数， $ f\left ( x \right )=\frac{ax+b}{cx+d},x\in\mathbf{R} $ ，且 $ f\left ( 19 \right )=19,f(97)=97 $ 。若当 $ x\neq -\frac{d}{c} $ 时，对于任意实数 $ x $ ，均有 $ f\left ( f\left ( x \right ) \right )=x $ ，试求出 $ f\left ( x \right ) $ 值域以外的唯一数。

**解**：易知 $ x=19,x=97 $ 即为不动点，又为稳定点，又 $ f\left(x\right) $ 是经过反比例函数平移得到，很容易得到 $ f\left ( x \right )=\frac{58x-1843}{x-58} $ ，故所求数为 $ 58 $ 。

**题10**：设有函数 $ f\left ( x \right )=\sin{\left ( x+a_{1} \right )}+\frac{1}{1\times 2}\sin{\left ( x+a_{2} \right )}+\cdots +\frac{1}{\left ( n-1 \right )\times n}\sin{\left ( x+a_{n} \right )} $ ，其中 $ a_{1},a_{2},\cdots ,a_{n} $ 为常数，证明：（1）至少有一个实数，使 $ f\left ( x_{0} \right )\neq 0 $ ；（2）如果 $ f\left ( x_{1} \right )=f\left ( x_{2} \right )=0 $ ，则 $ x_{1}-x_{2}=m\pi $ （ $ m $ 是一个整数）。

**解**：

（1）令 $ x_{0}=\frac{\pi}{2}-a_{1} $ ，则 $ f\left ( x_{0} \right )\geq 1-\left ( \frac{1}{1\times 2}+\frac{1}{2\times 3}+\frac{1}{\left ( n-1 \right )\times n} \right )=1-\frac{n-1}{n}=\frac{1}{n}> 0 $ 。

（2） $$ \begin{align*} f\left ( x \right )&=\sin{x}\cos{a_{1}}+\cos{x}\sin{a_{1}}+\sum_{i=2}^{n}{\frac{1}{\left ( i-1 \right )\times i}\left ( \sin{x}\cos{a_{i}}+\cos{x}\sin{a_{i}} \right )} \\\ &=\left ( \cos{a_{1}}+\sum_{i=2}^{n}{\frac{1}{\left ( i-1 \right )\times i}\cdot \cos{a_{i}}} \right )\cdot \sin{x}+\left ( \sin{a_{1}}+\sum_{i=2}^{n}{\frac{1}{\left ( i-1 \right )\times i}\cdot \sin{a_{i}}} \right )\cdot \cos{x}\\\ &=A\sin{\left (x+\varphi \right ) } \\\ A &=\sqrt{\left ( \cos{a_{1}}+\sum_{i=2}^{n}{\frac{1}{\left ( i-1 \right )\times i}\cdot \cos{a_{i}}} \right )^{2}+\left ( \sin{a_{1}}+\sum_{i=2}^{n}{\frac{1}{\left ( i-1 \right )\times i}\cdot \sin{a_{i}}} \right )^{2}}\\\ \tan{\varphi } &=\frac{\left ( \cos{a_{1}}+\sum_{i=2}^{n}{\frac{1}{\left ( i-1 \right )\times i}\cdot \cos{a_{i}}} \right )}{\left ( \sin{a_{1}}+\sum_{i=2}^{n}{\frac{1}{\left ( i-1 \right )\times i}\cdot \sin{a_{i}}} \right )}\end{align*}$$ 由 $ A\sin{x+\varphi }=0 $ 得 $ x+\varphi=k\pi $ ，于是 $ x_{1}-x_{2}=\left(k_{1}-k_{2}\right)\pi=m\pi $ 。证毕。

**题11**：设正实数 $ x,y $ 满足 $ xy=1 $ ，求函数 $ f\left ( x,y \right )=\frac{x+y}{\left [ x \right ]\cdot \left [ y \right ]+\left [ x \right ]+\left [ y \right ]+1} $ 的值域（这里 $ \left [ z \right ] $ 表示不超过 $ z $ 的最大整数）。

**解**： 

$ 1^{\circ} x=y=1,f\left ( 1,1 \right )=\frac{1}{2} $ 

 $ 2^{\circ} $ 不妨设 $ x>1 $ ，则 $ \left [ y \right ]=0 $ ，记 $ x=m+\lambda $ ，其中 $ m=\left [ x \right ],\lambda =\left \\{ x \right \\} $ 。则 $$ f\left ( x,y \right )=\frac{x+\frac{1}{x}}{\left [ x \right ]+1}=\frac{x+\frac{1}{x}}{m+1}=\frac{m+\lambda +\frac{1}{m+\lambda }}{m+1} $$ 令 $ a_{m}=\frac{m+\frac{1}{m}}{m+1} $ ，则 $$ a_{m}\leq f\left ( x,y \right )< \frac{m+1+\frac{1}{m+1}}{m+1} $$ 又 $ a_{m+1}-a_{m}=\frac{m-2}{\left ( m-2 \right )m\left ( m+1 \right )}\Rightarrow a_{1}> a_{2}< a_{3}< \cdots < a_{m} $ 。因此 $$ \frac{5}{6}\leq f\left ( x,y \right )< 1 + \frac{1}{\left ( m+1 \right )^{2}}\leq \frac{5}{4} $$ 故值域为 $ R_{f}=\left [ \frac{5}{6},\frac{5}{4} \right ) $ 。 
 
 ## 三、二次函数

**例1**：已知 $ f\left ( x \right )=ax^{2}+bx $ ，满足 $ 1\leq f\left ( -1 \right )\leq 2 $ 且 $ 2\leq f\left ( 1 \right )\leq 4 $ ，求 $ f\left ( -2 \right ) $ 的取值范围。

**解**：

法一：由题设得， $ \begin{cases} 1\leq a-b\leq 2 & \left ( \textrm{i} \right )\\\ 2\leq a+b\leq 4 & \left ( \textrm{ii} \right ) \end{cases} $ ，由 $ 3\times \left ( \textrm{i} \right )+\left ( \textrm{ii} \right ) $ 得 $ 5\leq f\left ( -2 \right )\leq 10 $ 。

法二： $ \begin{cases} f\left ( -1 \right )=a-b\\\ f\left ( 1 \right )=a+b \end{cases} \Rightarrow \begin{cases} a=\frac{1}{2}\cdot \left [ f\left ( 1 \right ) + f\left ( -1 \right ) \right ]\\\ b=\frac{1}{2}\cdot \left [ f\left ( 1 \right ) - f\left ( -1 \right ) \right ] \end{cases} $ ，因此 $ f\left ( -2 \right )=f\left ( 1 \right )+3f\left ( -1 \right )\in\left [ 5,10 \right ] $ 。
