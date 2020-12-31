---
title: 浅谈伴随矩阵在逆矩阵求解中的应用
tags: 数学之美
publish: 2013-04-29 15:30:00 +08:00
---

最近数学课上讲了矩阵，很久以前便对矩阵很有兴趣，但由于一些原因没有深入学习。正好趁这个机会，有思考了一下关于矩阵的内容。目前应用较广的应该是运用逆矩阵求解线性方程组，尤其对于三元一次方程组，运用逆矩阵求解会非常方便。

一个方形矩阵的伴随矩阵是一个类似于逆矩阵的概念。如果矩阵可逆，那么它的逆矩阵和它的伴随矩阵之间只差一个系数。然而，伴随矩阵对不可逆的矩阵也有定义，并且不需要用到除法。我们对这种情况不做深入讨论。

**引理1**：对于一个$$n$$阶矩阵$$\mathbf{A}$$，以及两个整数$$i,j$$，其中$$1\leq i,j\leq n$$。去掉$$\mathbf{A}$$的第$$i$$行以及第$$j$$列，得到一个$$n-1$$阶子矩阵。记这个子矩阵的行列式为$$M_{ij}$$。称为余子式。

**引理2**：对于一个$$n$$阶矩阵$$\mathbf{A}$$，代数余子式是余子式$$M_{ij}$$与$$\left ( -1 \right )^{i+j}$$的乘积，记作$$C_{ij}$$。

**例**：对于矩阵$$\begin{bmatrix}
1 & 4 & 7\\
3 & 0 & 5\\
-1 & 9 & 11
\end{bmatrix}$$，计算它的代数余子式$$C_{23}$$。

**解**：首先计算余子式$$M_{23}$$，即原矩阵去掉第二行以及第三行所得的矩阵的行列式：$$\begin{bmatrix}
1 & 4 & \bigcirc \\
\bigcirc & \bigcirc & \bigcirc \\
-1 & 9 & \bigcirc
\end{bmatrix}$$，即$$\begin{vmatrix}
1 & 4\\
-1 & 9
\end{vmatrix}=\left ( 9-\left ( -4 \right ) \right )=13$$。因此$$C_{23}=\left ( -1 \right )^{2+3}\cdot M_{23}=-13$$。

**引理3**：对于一个$$n$$阶矩阵$$\mathbf{A}$$，由代数余子式组成的新的矩阵，称为该矩阵的余子矩阵。记作$$\mathbf{C}$$。

**引理4**：对于一个$$n$$阶矩阵$$\mathbf{A}$$，定义它的转置矩阵$$\mathbf{A^{T}}$$。转置矩阵$$\mathbf{A^{T}}$$可以通过下列操作得到：把$$\mathbf{A}$$的横行写为$$\mathbf{A^{T}}$$的纵行，把$$\mathbf{A}$$的纵行写为$$\mathbf{A^{T}}$$的横行。

**例**：$$\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}^{T}=\begin{bmatrix}
1 & 3\\
2 & 4
\end{bmatrix}$$。

**引理5**：对于一个$$n$$阶矩阵$$\mathbf{A}$$，它的余子矩阵$$\mathbf{C}$$的转置矩阵称为矩阵$$\mathbf{A}$$的伴随矩阵。记作$$\mathbf{A^{*}}=\mathbf{C^{T}}$$。

**例**：对于矩阵$$\mathbf{A}=\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}$$，求它的伴随矩阵$$\mathbf{A^{*}}$$。

**解**：$$\mathbf{A^{*}}=\begin{bmatrix}
C_{11} & C_{12}\\
C_{21} & C_{22}
\end{bmatrix}^{T}=\begin{bmatrix}
M_{11} & -M_{12}\\
-M_{21} & M_{22}
\end{bmatrix}^{T}=\begin{bmatrix}
d & -c\\
-b & a
\end{bmatrix}^{T}=\begin{bmatrix}
d & -b\\
-c & a
\end{bmatrix}$$。

**例**：对于矩阵$$\mathbf{A}=\begin{bmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}
\end{bmatrix}$$，求它的伴随矩阵$$\mathbf{A^{*}}$$。

**解**：$$\mathbf{A^{*}}=\begin{bmatrix}
C_{11} & C_{12} & C_{13}\\
C_{21} & C_{22} & C_{23}\\
C_{31} & C_{32} & C_{33}
\end{bmatrix}^{T}=\begin{bmatrix}
M_{11} & -M_{12} & M_{13}\\
-M_{21} & M_{22} & -M_{23}\\
M_{31} & -M_{32} & M_{33}
\end{bmatrix}^{T}\\
=\begin{bmatrix}
\begin{vmatrix}
a_{22} & a_{23}\\
a_{32} & a_{33}
\end{vmatrix} & -\begin{vmatrix}
a_{21} & a_{23}\\
a_{31} & a_{33}
\end{vmatrix} & \begin{vmatrix}
a_{21} & a_{22}\\
a_{31} & a_{32}
\end{vmatrix}\\ -\begin{vmatrix}
a_{12} & a_{13}\\
a_{32} & a_{33}
\end{vmatrix} & \begin{vmatrix}
a_{11} & a_{13}\\
a_{31} & a_{33}
\end{vmatrix} & -\begin{vmatrix}
a_{11} & a_{12}\\
a_{31} & a_{32}
\end{vmatrix}\\ \begin{vmatrix}
a_{12} & a_{13}\\
a_{22} & a_{23}
\end{vmatrix} & -\begin{vmatrix}
a_{11} & a_{13}\\
a_{21} & a_{23}
\end{vmatrix} & \begin{vmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}
\end{vmatrix}
\end{bmatrix}^{T}\\
=\begin{bmatrix}
\begin{vmatrix}
a_{22} & a_{23}\\
a_{32} & a_{33}
\end{vmatrix} & -\begin{vmatrix}
a_{12} & a_{13}\\
a_{32} & a_{33}
\end{vmatrix} & \begin{vmatrix}
a_{12} & a_{13}\\
a_{22} & a_{23}
\end{vmatrix}\\ -\begin{vmatrix}
a_{21} & a_{23}\\
a_{31} & a_{33}
\end{vmatrix} & \begin{vmatrix}
a_{11} & a_{13}\\
a_{31} & a_{33}
\end{vmatrix} & -\begin{vmatrix}
a_{11} & a_{13}\\
a_{21} & a_{23}
\end{vmatrix}\\ \begin{vmatrix}
a_{21} & a_{22}\\
a_{31} & a_{32}
\end{vmatrix} & -\begin{vmatrix}
a_{11} & a_{12}\\
a_{31} & a_{32}
\end{vmatrix} & \begin{vmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}
\end{vmatrix}
\end{bmatrix}$$
其中$$\begin{vmatrix}
a_{im} & a_{in}\\
a_{jm} & a_{jn}
\end{vmatrix}=a_{im}\cdot a_{jn}-a_{in}\cdot a_{jm}$$。

**例**：对于矩阵$$\mathbf{A}=\begin{bmatrix}
-3 & 2 & -5\\
-1 & 0 & -2\\
3 & -4 & 1
\end{bmatrix}$$，求它的伴随矩阵$$\mathbf{A^{*}}$$。

**解**：通过计算不难得出$$\mathbf{A^{*}}=\begin{bmatrix}
-8 & 18 & -4\\
-5 & 12 & -1\\
4 & -6 & 2
\end{bmatrix}$$。

**引理6**：对于一个$$n$$阶矩阵$$\mathbf{A}$$，它的逆矩阵$$\mathbf{A^{-1}}$$与伴随矩阵$$\mathbf{A^{*}}$$满足$$\mathbf{A^{-1}}=
\frac{\mathbf{A^{*}}}
{\begin{vmatrix}
\mathbf{A}
\end{vmatrix}}$$。其中$$\begin{vmatrix}
\mathbf{A}
\end{vmatrix}$$为矩阵$$\mathbf{A}$$的行列式。

**例**：对于矩阵$$\mathbf{A}=\begin{bmatrix}
3 & 2\\
2 & 1
\end{bmatrix}$$，求它的逆矩阵$$\mathbf{A^{-1}}$$。

**解**：$$\mathbf{A^{*}}=\begin{bmatrix}
1 & -2\\
-2 & 3
\end{bmatrix},\begin{vmatrix}
\mathbf{A}
\end{vmatrix}=\begin{vmatrix}
3 & 2\\
2 & 1
\end{vmatrix}=-1,\mathbf{A^{-1}}=\frac{1}{\begin{vmatrix}
\mathbf{A}
\end{vmatrix}}\cdot \mathbf{A^{*}}=\begin{bmatrix}
-1 & 2\\
2 & -3
\end{bmatrix}$$。

**例**：对于矩阵$$\mathbf{A}=\begin{bmatrix}
3 & -1 & 0\\
-1 & 2 & -1\\
-1 & -1 & 1
\end{bmatrix}$$，求它的逆矩阵$$\mathbf{A^{-1}}$$。

**解**：$$\mathbf{A^{*}}=\begin{bmatrix}
1 & 1 & 1\\
2 & 3 & 3\\
3 & 4 & 5
\end{bmatrix},\begin{vmatrix}
\mathbf{A}
\end{vmatrix}=\begin{vmatrix}
3 & -1 & 0\\
-1 & 2 & -1\\
-1 & -1 & 1
\end{vmatrix}=1,\mathbf{A^{-1}}=\frac{1}{\begin{vmatrix}
\mathbf{A}
\end{vmatrix}}\cdot \mathbf{A^{*}}=\begin{bmatrix}
1 & 1 & 1\\
2 & 3 & 3\\
3 & 4 & 5
\end{bmatrix}$$。

运用伴随矩阵来求解逆矩阵会方便很多，尤其是对于高阶矩阵。且使得逆矩阵的求法有规律可循，不需要死记公式。