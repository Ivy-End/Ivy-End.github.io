# 浅谈线性同余及中国剩余定理


我记得在计算机复赛前一天晚上本想看看同余方程的解法，结果第二天就考到了。明天是数学竞赛初赛，简略的复习一下线性同余及中国剩余定理，顺便记下一些笔记。

**定理1**：令 $m$ 为正整数。若 $\begin{cases} a \equiv b \pmod m \\\ c \equiv d \pmod m \end{cases}$，那么 $\begin{cases} a+c \equiv b+d \pmod m \\\ ac \equiv bd \pmod m\end{cases}$。

**证明**：因为 $\begin{cases} a \equiv b \pmod m \\\ c \equiv d \pmod m\end{cases}$，所以有整数 $s$ 和 $t$ 使 $\begin{cases} b=a+sm \\\ d=c+tm\end{cases}$。于是 $$ \begin{cases} b+d=(a+sm)+(c+tm)=(a+c)+m(s+t)\\\ bd=(a+sm)(c+tm)=ac+m(at+cs+stm) \end{cases} \Rightarrow \begin{cases} a+c \equiv b+d \pmod m \\\ ac \equiv bd \pmod m \end{cases}$$

**例**：由于 $\begin{cases} 7 \equiv 2 \pmod 5 \\\ 11 \equiv 1 \pmod 5\end{cases}$，从定理1知 $\begin{cases} 18 = 7+11 \equiv 2+1=3 \pmod 5 \\\ 77 = 7 \cdot 11 \equiv 2 \cdot 1=2 \pmod 5\end{cases}$。

**定理2**：如果 $a$ 和 $m$ 为互素的整数，$m > 1$，则存在 $a$ 的模 $m$ 的逆。而且这个逆模 $m$ 是唯一的。（即有小于 $m$ 的唯一正整数 $\overline{a}$，如果这样的 $\overline{a}$ 存在的话。这样的 $\overline{a}$ 称为 $a$ 模 $m$ 逆，且 $a$ 的任何别的模 $m$ 逆均和 $\overline{a}$ 模 $m$ 同余。）

**证明**：由定理 1 及 $\gcd \left ( a,m \right )=1$ 知，有整数 $s$ 和 $t$ 使 $$sa+tm=1$$ 于是 $$sa+tm \equiv 1 \pmod m$$ 由于 $tm \equiv 0 \pmod m$，所以 $$sa \equiv 1 \pmod m$$ 结论是 $s$ 为 $a$ 的模 $m$ 逆。

**例**：求 $3$ 的模 $7$ 逆。

**解**：由于 $\gcd \left ( 3,7 \right )=1$，定理 3 说明存在 $3$ 模 $7$ 的逆。若用欧几里得算法求 $3$ 和 $7$ 的最大公约数，算法很快结束：$$7=2 \cdot 3 + 1$$ 从这一等式看到 $$-2 \cdot 3 + 1 \cdot 7=1$$ 这说明 -2 是 3 模 7 的一个逆。（注意，模 $7$ 同余于 $-2$ 的每个整数也是 $3$ 的逆，例如 $5,-9,12$ 等。）

**例**：求线性同余 $3x \equiv 4 \pmod 7$ 的解。

**解**：易知 $-2$ 是 $3$ 模 $7$ 的逆。在同余式的两边同乘以 $-2$ 得 $$-2 \cdot 3x \equiv -2 \cdot 4 \pmod 7$$ 因为 $\begin{cases} -6 \equiv 1 \pmod 7 \\\ -8 \equiv 6 \pmod 7\end{cases}$，所以若 $x$ 是解，必有 $$x \equiv -8 \equiv 6 \pmod 7$$ 于是由定理 1，有 $$3x \equiv 3 \cdot 6 \equiv 18 \equiv 4 \pmod 7 $$ 这说明所有这种 $x$ 满足问题中的同余式。结论是，同余方程的解是使 $x \equiv 6 \pmod 7$ 的整数。

从有关线性同余系统的中国古典问题而得名的中国剩余定理，可以这样叙述：只要线性同余系统的模数两两互素，则该系统有解，而且以所有模数之乘积取模，解是唯一的。

**定理3（中国剩余定理）**：令 $m_{1},m_{2},\cdots,m_{n}$ 为两两互素的正整数，则同余方程组 $$ \begin{cases} x \equiv a_{1} \pmod {m_{1}}\\\ x \equiv a_{2} \pmod {m_{2}}\\\ \vdots \\\ x \equiv a_{1} \pmod {m_{n}} \end{cases}$$ 唯一的模 $m=m_{1}m_{2} \cdots m_{n}$ 解。（即有一个解 $x$，使 $0 \leq x \leq m$，且所有其他的解均与此解模 $m$ 同余。）

**证明**：要建立这一定理，需要证明有一个解存在，而且是模 $m$ 唯一的。下面将给出构造这样一个解的方法以证明解的存在。

要构造一个适合各方程的解，首先对 $k=1,2, \cdots ,n$，令 $M_{k}=\frac{m}{m_{k}}$，即 $M_{k}$ 是除 $m_{k}$ 以外所有模数的乘积。由于 $i \neq k$ 时，$m_{i}$ 和 $m_{k}$ 没有大于 1 的公因子，所以 $\gcd \left ( m_{k},M_{k} \right )=1$。从而由定理 2 知有整数 $y_{k}$，即 $M_{k}$ 模 $m_{k}$ 的逆，使得 $$M_{k}y_{k} \equiv 1 \pmod {m_{k}}$$ 要得到适合所有方程的解，令 $$x=a_{1}M_{1}y_{1}+a_{2}M_{2}y_{2}+\cdots+a_{n}M_{n}y_{n}$$ 现要证明 $x$ 就是这样一个解。

首先注意，由于只要 $j \neq k$，就有 $M_{j} \equiv 0 \pmod {m_{k}}$，在 $x$ 的求和表达式中除第 $k$ 项以外的各项模 $m_{k}$ 均同余于 $0$。由于 $M_{k}y_{k} \equiv 1 \pmod {m_{k}}$，可以看出对 $k=1,2, \cdots ,n$，均有 $$x \equiv a_{n}M_{n}y_{n} \equiv a_{k} \pmod {m_{k}}$$。这就证明了 $x$ 是这 $n$ 个同余方程的公共解。

**例**：求同余方程组 $\begin{cases} x \equiv 2 \pmod 3\\\ x \equiv 3 \pmod 5\\\ x \equiv 2 \pmod 7 \end{cases}$ 的解。

**解**：首先令 $m=3 \cdot 5 \cdot 7=105$，$M_{1}=\frac {m} {3}=35$，$M_{2}=\frac {m} {5}=21$，$M_{3}=\frac {m} {7}=15$。可看到 $2$ 是 $M_{1}=35$ 的模 $3$ 逆，因为 $35 \equiv 2 \pmod 3$；$1$ 是 $M_{2}=21$ 的模 $5$ 逆，因为 $21 \equiv 1 \pmod 5$；$1$ 也是 $M_{3}=15$ 的模 $7$ 逆，因为 $15 \equiv -1 \pmod 4$。于是这一方程组的解是满足下列式子的那些 $x$： $$ x \equiv a_{1}M_{1}y_{1}+a_{2}M_{2}y_{2}+a_{3}M_{3}y_{3}=2 \cdot 35 \cdot 2 + 3 \cdot 21 \cdot 1 + 2 \cdot 15 \cdot 1=233 \equiv 23 \pmod {105} $$

可以见 $23$ 是所有解当中最小的正整数。结论是 $23$ 是最小的正整数，除以 $3$ 时余 $2$，除以 $5$ 时余 $3$，除以 $7$ 时余 $2$。
