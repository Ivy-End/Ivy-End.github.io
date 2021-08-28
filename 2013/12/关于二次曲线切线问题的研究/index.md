# 关于二次曲线切线问题的研究


很早就想整理这部分的知识了，迫于时间原因，一直拖到现在。下面就圆、椭圆、双曲线、抛物线的切点弦进行一些研究。主要涉及两个方面，一个是关于曲线上某点的切线方程，另一个是关于曲线的切点弦方程。

## 一、关于曲线上某点的切线方程

### 1、圆

我们都知道，过圆 $ x^{2}+y^{2}=r^{2}\left ( r > 0 \right ) $ 上一点 $ P\left(x_{0},y_{0}\right) $ 的切线方程是 $ x_{0}x+y_{0}y=r^{2} $ 。下面我们就更为一般的情形进行探究：

**定理1.1**：给定圆 $ C:\left ( x-a \right )^{2}+\left ( y- b\right )^{2}=r^{2}\left ( r > 0 \right ) $ ，以及圆上一点 $ P\left(x_{0},y_{0}\right) $ ，则过该点的切线方程为 $$ \left ( x_{0}-a \right )\left ( x-a \right )+\left ( y_{0}-b \right )\left ( y-b \right )=r^{2} $$

**证明**：对于圆 $ C:\left ( x-a \right )^{2}+\left ( y- b\right )^{2}=r^{2} $ ，两边同时对 $ x $ 求导，得 $$ 2\left ( x-a \right )+2\left ( y-b \right )\cdot\frac{dy}{dx}=0 $$ 其中 $ \frac{dy}{dx})即为(y' $ ，只是导数两种不同的记号，化简整理得 $$ \frac{dy}{dx}=-\frac{x-a}{y-b} $$ 那么我们可以写出切线方程为 $$ y-y_{0}=-\frac{x_{0}-a}{y_{0}-b}\left ( x-x_{0} \right ) $$ 进一步化简得 $$ \left ( x_{0}-a \right )x+\left ( y_{0}-b \right )y-\left ( x_{0}^{2}+y_{0}^{2} \right )+ax_{0}+by_{0}=0 $$ 又 $ P\left(x_{0},y_{0}\right) $ 在圆 $ C $ 上，则 $ \left ( x_{0}-a \right )^{2}+\left ( y_{0}-b \right )^{2}=r^{2} $ ，代入上式化简得 $$ \left ( x_{0}-a \right )\left ( x-a \right )+\left ( y_{0}-b \right )\left ( y-b \right )=r^{2} $$ 证毕。

### 2、椭圆

有了上面的基础，我们可以猜测到椭圆上某点的切线方程。

**定理1.2**：给定椭圆 $ C:\frac{\left ( x-m \right )^{2}}{a^{2}}+\frac{\left ( y-n \right )^{2}}{b^{2}}=1\left ( a > b > 0 \right ) $ ，以及椭圆上一点 $ P\left(x_{0},y_{0}\right) $ ，则过该点的切线方程为 $$ \frac{\left ( x_{0}-m \right )\left ( x-m \right )}{a^{2}}+\frac{\left ( y_{0}-n \right )\left ( y-n \right )}{b^{2}}=1. $$ 证明略。

### 3、双曲线

**定理1.3**：给定双曲线 $ C:\frac{\left ( x-m \right )^{2}}{a^{2}}-\frac{\left ( y-n \right )^{2}}{b^{2}}=1\left ( a > 0, b > 0 \right ) $ ，以及双曲线上一点 $ P\left(x_{0},y_{0}\right) $ ，则过该点的切线方程为 $$ \frac{\left ( x_{0}-m \right )\left ( x-m \right )}{a^{2}}-\frac{\left ( y_{0}-n \right )\left ( y-n \right )}{b^{2}}=1 $$ 证明略。对于焦点在 $ y $ 轴上的情形，读者可以自行推导。

### 4、抛物线

**定理1.4**：给定抛物线 $ C:y^{2}=2p\left ( x-a \right )\left ( p > 0 \right ) $ ，以及抛物线上一点 $ P\left(x_{0},y_{0}\right) $ ，则过该点的切线方程为 $$ y_{0}y=p(x+x_{0}-2a) $$ 证明略。对于其他三种情形，读者可以自行推导。

## 二、关于曲线外某点的切点弦方程
### 1、圆

类似的，圆 $ x^{2}+y^{2}=r^{2}\left ( r > 0 \right ) $ 外一点 $ P\left(x_{0},y_{0}\right) $ 的切点弦方程是 $ x_{0}x+y_{0}y=r^{2} $ 。下面我们就更为一般的情形进行探究：

**定理2.1**：给定圆 $ C:\left ( x-a \right )^{2}+\left ( y- b\right )^{2}=r^{2}\left ( r > 0 \right ) $ ，以及圆外一点 $ P\left(x_{0},y_{0}\right) $ ，则该点的切点弦方程为 $$ \left ( x_{0}-a \right )\left ( x-a \right )+\left ( y_{0}-b \right )\left ( y-b \right )=r^{2} $$

**证明**：设过 $ P $ 的切线与圆 $ C $ 相交于点 $ A\left ( x_{1},y_{1} \right ))以及(B\left ( x_{2},y_{2} \right ) $ ，首先过点 $ A $ 的切线同时经过点 $ P $ ，切线方程为 $$ \left ( x_{1}-a \right )\left ( x-a \right )+\left ( y_{1}-b \right )\left ( y-b \right )=r^{2} $$ 又过点 $ B $ 的切线同时也经过点 $ P $ ，切线方程为 $$ \left ( x_{2}-a \right )\left ( x-a \right )+\left ( y_{2}-b \right )\left ( y-b \right )=r^{2} $$ 综合上述两个方程，便可以得到过点 $ A,B $ 的方程，即点(P)的切点弦方程 $$ \left ( x_{0}-a \right )\left ( x-a \right )+\left ( y_{0}-b \right )\left ( y-b \right )=r^{2} $$

### 2、椭圆

**定理2.2**：给定椭圆 $ C:\frac{\left ( x-m \right )^{2}}{a^{2}}+\frac{\left ( y-n \right )^{2}}{b^{2}}=1\left ( a > b > 0 \right ) $ ，以及椭圆上一点 $ P\left(x_{0},y_{0}\right) $ ，则该点的切点弦方程为 $$ \frac{\left ( x_{0}-m \right )\left ( x-m \right )}{a^{2}}+\frac{\left ( y_{0}-n \right )\left ( y-n \right )}{b^{2}}=1 $$ 证明略。

### 3、双曲线

**定理2.3**：给定双曲线 $ C:\frac{\left ( x-m \right )^{2}}{a^{2}}-\frac{\left ( y-n \right )^{2}}{b^{2}}=1\left ( a > 0, b > 0 \right ) $ ，以及双曲线上一点 $ P\left(x_{0},y_{0}\right) $ ，则该点的切点弦方程为 $$ \frac{\left ( x_{0}-m \right )\left ( x-m \right )}{a^{2}}-\frac{\left ( y_{0}-n \right )\left ( y-n \right )}{b^{2}}=1 $$ 证明略。对于焦点在 $ y $ 轴上的情形，读者可以自行推导。

### 4、抛物线

**定理2.4**：给定抛物线 $ C:y^{2}=2p\left ( x-a \right )\left ( p > 0 \right ) $ ，以及抛物线上一点 $ P\left(x_{0},y_{0}\right) $ ，则该点的切点弦方程为 $$ y_{0}y=p(x+x_{0}-2a) $$ 证明略。对于其他三种情形，读者可以自行推导。 至此，关于二次曲线的两种切线问题已经阐述完毕。从上述过程我们可以看出，过曲线上某点的切线方程和过曲线外某点的切点弦方程的形式是完全一致的，这正是数学的魅力所在！
