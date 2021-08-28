# 浅谈等价无穷小量代换原理


高数教了一段时间了，对于等价无穷小量代换法求极限为什么只能在乘除中使用，而不能在加减的情况下使用的条件感到有些疑惑，于是找了一些资料，仔细的研究了这个问题，整理如下：

## 等价无穷小的定义及常用的等价无穷小

无穷小量是指某变化过程中极限为 $ 0 $ 的变量。而等价无穷小量是指在某变化过程中比值极限为 $ 1 $ 的两个无穷小量。

常用的等价无穷小有： $$ \sin{x}\sim \tan{x}\sim\arctan{x}\sim\arcsin{x}\sim \ln{\left(1+x \right )}\sim x\left(x\rightarrow 0\right ) $$ $$ 1-\cos{x}\sim \frac{x^{2}}{2},\sqrt[n]{1+x}-1\sim \frac{x}{n} \left(x\rightarrow 0\right ) $$ 等价无穷小量在求极限问题中非常重要。恰当的使用等价无穷小量代换常常使极限问题大大简化。但是有时却不能使用等价无穷小量代换。

## 等价无穷小替换原理

**定理1**：设 $ \displaystyle\alpha,\alpha_{1},\beta,\beta_{1} $ 是某一变化过程中的无穷小量，且 $ \alpha \sim \alpha_{1},\beta \sim \beta_{1} $ ，若 $ \lim{\frac{\alpha}{\beta}} $ 存在，则 $$ \lim{\frac{\alpha}{\beta}}=\lim{\frac{\alpha_{1}}{\beta_{1}}} $$

**例1**：$$ \lim_{x\rightarrow 0}{\frac{\ln{\left(1+3x\right)}}{\sin{2x}}} $$

**解**：$$ \lim_{x\rightarrow 0}{\frac{\ln{\left(1+3x\right)}}{\sin{2x}}}=\lim_{x\rightarrow 0}{\frac{3x}{2x}}=\frac{3}{2} $$

**例2**：$$ \lim_{x\rightarrow 0}{\frac{\tan{x}-\sin{x}}{x^{3}}} $$

**错误解法**： $$ \lim_{x\rightarrow 0}{\frac{\tan{x}-\sin{x}}{x^{3}}}=\lim_{x\rightarrow 0}{\frac{x-x}{x^3}}=0 $$

**正确解法**：$$ \lim_{x\rightarrow 0}{\frac{\tan{x}-\sin{x}}{x^{3}}}=\lim_{x\rightarrow 0}{\frac{\sin{x}\left(1-\cos{x}\right)}{x^{3}\cdot\cos{x}}}=\lim_{x\rightarrow 0}{\frac{1-\cos{x}}{x^{2}\cdot\cos{x}}}=\lim_{x\rightarrow 0}{\frac{1}{2\cos{x}}}=\frac{1}{2} $$

从上面的解法可以看出，该题分子不能直接用等价无穷小量替代来做，下面我们分析产生错误的原因：等价无穷小之间本身一般并不相等，它们之间一般相差一个较它们高阶的无穷小，由函数 $ f\left(x\right) $ 在点 $ x=0 $ 处的泰勒公式，即麦克劳林公式：$$ f\left ( x \right )=f\left ( 0 \right )+f'\left ( 0 \right )x+\frac{f''\left ( 0 \right )}{2!}x^{2}+\cdots+\frac{f^{\left ( n \right )}\left ( 0 \right )}{n!}x^{n}+o\left ( x^{n} \right ) $$ 很容易有：$$ \tan{x}=x+\frac{x^{3}}{3}+\frac{2x^5}{15}+o\left ( x^{5} \right ) \quad \left ( x\rightarrow 0 \right ) $$  $$ \sin{x}=x+\frac{x^{3}}{3!}+\frac{x^{5}}{5!}+\frac{x^{7}}{7!}+\cdots+\frac{\left ( -1 \right )^{m-1}x^{2m-1}}{\left ( 2m-1 \right )!}+o\left ( x^{2m-1} \right ) \quad \left ( x\rightarrow 0 \right ) $$ 

由此可知， $ \sin{x} $ 与 $ \tan{x} $ 相差一个较 $ x $ 的三阶无穷小，此三阶无穷小与分母 $ x^{3} $ 相比不可忽略，因为把上述结论代入原式得 $$ \lim_{x\rightarrow 0}{\frac{\tan{x}-\sin{x}}{x^{3}}}=\lim{x\rightarrow 0}{\frac{\frac{x^{3}}{3}+\frac{x^{3}}{3!}+o\left ( x^{3} \right )}{x^{3}}}=\frac{1}{2} $$ 由此，我们可以得出：加减情况下不能随便使用等价无穷小。

下面我们给出一个在加减情况下使用等价无穷小的定理并加以证明。在这里我们只讨论减的情况，因为我们知道加上一个数可以看成减去这个数的负数。为方便，首先说明下面的定理及推论中的无穷小量其自变量都是 $ x $ ，其趋近过程都相同： $ x\rightarrow 0 $ ，在有关的极限中都省去了极限的趋近过程。

**定理2**：设 $ \alpha,\alpha_{1},\beta,\beta_{1} $ 是某一变化过程中的无穷小量，且 $ \alpha \sim \alpha_{1},\beta \sim \beta_{1} $ ，则 $ \alpha-\beta \sim \alpha_{1}-\beta_{1} $ 的充分必要条件是 $ \lim{\frac{\alpha}{\beta}}=k\neq 1 $ 。

**证明**：

$ 1^{\circ} $ 充分性：$$\alpha\sim\alpha_{1},\beta\sim\beta_{1}\Rightarrow \lim{\frac{\alpha}{\alpha_{1}}}=\lim{\frac{\beta}{\beta_{1}}}=1 $$ 又 $$ \lim{\frac{\alpha}{\beta}}=k\neq 1,\lim{\frac{\alpha_{1}}{\beta_{1}}}=k\neq 1 $$ 则 $$ \lim{\frac{\alpha-\beta}{\alpha_{1}-\beta_{1}}}=\lim{\frac{\frac{\alpha}{\beta_{1}}-\frac{\beta}{\beta_{1}}}{\frac{\alpha_{1}}{\beta_{1}}-1}}=\frac{k-1}{k-1}=1 $$ 即 $$ \alpha -\beta\sim \alpha_{1} - \beta_{1} $$

$ 2^{\circ} $ 必要性：$$ \alpha\sim\beta,\alpha_{1}\sim\beta_{1}\Rightarrow \lim{\frac{\alpha-\beta}{\alpha_{1}-\beta_{1}}}=1 $$ 即 $$ \lim{\left(\frac{\alpha-\beta}{\alpha_{1}-\beta_{1}}-1 \right )}=0 $$ 通分得 $$ \lim{\frac{\alpha-\alpha_{1}}{\alpha_{1}-\beta_{1}}}-\lim{\frac{\beta-\beta_{1}}{\alpha_{1}-\beta_{1}}}=0 $$ 所以 $$ \lim{\frac{\frac{\alpha}{\alpha_{1}}-1}{1-\frac{\beta}{\alpha_{1}}}}-\lim{\frac{1-\frac{\beta}{\beta_{1}}}{\frac{\alpha_{1}}{\beta_{1}}-1}}=0 $$ 又 $$ \lim{\frac{\alpha}{\alpha_{1}}}=1,\lim{\frac{\beta}{\beta_{1}}}=1 $$ 所以 $$ \lim{\frac{0}{1-\frac{\beta}{\alpha_{1}}}}-\lim{\frac{0}{\frac{\alpha_{1}}{\beta_{1}}-1}}=0 $$ 所以 $$ \lim{\frac{\beta_{1}}{\alpha_{1}}}=k\neq 1\Rightarrow \lim{\frac{\alpha_{1}}{\beta_{1}}}=k\neq 1 $$ 又 $$ \lim{\frac{\alpha}{\beta}}=\lim{\frac{\alpha_{1}}{\beta_{1}}} $$ 所以 $$ \lim{\frac{\alpha}{\beta}}=k\neq 1,\lim{\frac{\alpha_{1}}{\beta_{1}}}=k\neq 1 $$ 由 $ 1^{\circ},2^{\circ} $ 得，原命题成立。证毕。

这样一来，就得到了差形式无穷小量等价代换的充要条件。

**例3**：$$ \lim_{x\rightarrow 0}{\frac{1-\cos{x}+2\sin{x}}{\arcsin{2x}-\sin{x}}} $$

**解**：$$ 1-\cos{x}\sim\frac{x^{2}}{2},-2\sin{x}\sim -2x, 2\arcsin{x}\sim 2x,\sin{x}\sim x\left ( x\rightarrow 0 \right ) $$ 所以 $$ \lim_{x\rightarrow 0}{\frac{1-\cos{x}}{-2\sin{x}}}=0\neq 1,\lim_{x\rightarrow 0}{\frac{2\arcsin{x}}{\sin{x}}}=2\neq 1 $$ 由定理 2 得 $$ \lim_{x\rightarrow 0}{\frac{1-\cos{x}+2\sin{x}}{\arcsin{2x}-\sin{x}}}=\lim_{x\rightarrow}{\frac{\frac{x^{2}}{2}+2x}{x}}=2 $$

**例4**：$$ \lim_{x\rightarrow 0}{\frac{\arctan{2x}+\arcsin{5x}}{\sin{3x}}} $$

**解**：$$ \arctan{2x}\sim 2x,\arcsin{5x}\sim 5x,\sin{3x}\sim 3x\left ( x\rightarrow 0 \right ) $$ 又 $$ \lim{\frac{\arctan{2x}}{-\arcsin{5x}}}=-\frac{2}{5}\neq 1 $$ 由定理 2 得 $$ \lim_{x\rightarrow 0}{\frac{\arctan{2x}+\arcsin{5x}}{\sin{3x}}}=\frac{2x+5x}{3x}=\frac{7}{3} $$

## 总结

本文指出，在有加减的情况下不能随便运用等价无穷小代换求极限，并且指出了在有加减的情况下能够使用等价无穷小代换的充分必要条件。对于不满足条件的情况，根据给出的泰勒展开公式，可以求出。
