# 扫雷游戏制作过程（CSharp 描述）：第七节、内部实现（续）


这一节我们主要讲解扫雷时鼠标单击的事件。我们首先介绍左键单击的事件，分为两种情况——遇到地雷，游戏结束；不是地雷，自动点开相邻的非地雷区域，并且显示对应地雷区域周围地雷的数目。

我们首先需要为 Form_Main 添加 MouseDown 以及 MouseUp 事件，分别用来监测鼠标按下以及弹起的事件信息。再定义两个全局变量，用来标识鼠标左键以及右键是否被按下，代码如下：

```csharp
        bool bMouseLeft;    // 鼠标左键是否被按下
        bool bMouseRight;   // 鼠标右键是否被按下
```

在 MouseDown 事件中输入下面的代码：

```csharp
        private void Form_Main_MouseDown(object sender, MouseEventArgs e)
        {
            if(e.Button == MouseButtons.Left)   // 鼠标左键被按下
            {
                bMouseLeft = true;
            }
            if(e.Button == MouseButtons.Right)  // 鼠标右键被按下
            {
                bMouseRight = true;
            }
        }
```

在 MouseUp 事件中，我们需要获取鼠标弹起前按下的鼠标按键的状态信息，代码如下：

```csharp
        private void Form_Main_MouseUp(object sender, MouseEventArgs e)
        {
            if(bMouseLeft && BMouseRight)   // 左右键同时按下
            {

            }
            else if(bMouseLeft)   // 左键被按下
            {
                
            }
            else if(bMouseRight)  // 右键被按下
            {
                
            }
        }
```

我们首先处理鼠标左键按下的情况，这里分为两种情况，在前文中已经介绍过。但是在处理之前，我们需要获取游戏者单击的是哪个雷区，因此我们需要加入一些用以判断当前鼠标所属区域的代码。但是回顾一下，我们上一节中在 MouseMove 事件中已经获得了当前鼠标所属的区域，并且保存在了全局变量中，因此，我们直接调用即可：

```csharp
        private void Form_Main_MouseUp(object sender, MouseEventArgs e)
        {
            if(MouseFocus.X == 0 && MouseFocus.Y == 0)  // 不在地雷区域
            {
                return;     // 不做任何处理
            }
            if(bMouseLeft && BMouseRight)   // 左右键同时按下
            {
                
            }
            else if(bMouseLeft)   // 左键被按下
            {
                if(pMine[MouseFocus.X, MouseFocus.Y] != -1)
                {
                    // 非地雷，自动打开周围非地雷区域
                }
                else
                {
                    // 地雷，游戏结束
                }
            }
            else if(bMouseRight)  // 右键被按下
            {
                
            }
            bMouseLeft = bMouseRight = false;
        }
```

我们首先来处理非地雷的情况。也就是说我们需要寻找所有相邻的非地雷区域，这里我们才有深度优先搜索（Depth First Search），首先定义一个函数如下：

```csharp
        private void dfs(int sx, int sy)
        {
            pState[sx, sy] = 1; // 访问该点
            for(int i = 0; i < 4; i++)
            {
                // 获取相邻点的坐标
                int x = sx + px[i];
                int y = sy + py[i];
                if(x >= 1 && x <= nWidth && y >= 1 && y <= nHeight &&
                    pMine[x, y] != -1 && pMine[sx, sy] == 0 &&
                    (pState[x, y] == 0 || pState[x, y] == 3)) // 不是地雷，处于地雷区域，且未点开，或者标记为问号
                {
                    dfs(x, y);  // 访问该点
                }
            }
        }
```

在 MouseUp 函数中调用，并且刷新绘图区域：

```csharp
            else if(bMouseLeft)   // 左键被按下
            {
                if(pMine[MouseFocus.X, MouseFocus.Y] != -1)
                {
                    dfs(MouseFocus.X, MouseFocus.Y);
                }
                else
                {
                    // 地雷，游戏结束
                }
            }
```

此时，我们运行程序，单击雷区，与上一节结束时的程序没有什么区别，因为我们还没有更新绘图函数，用下面的代码更新 PaintGame 函数主循环中的代码：

```csharp
        /// <summary>
        /// 绘制游戏区
        /// </summary>
        private void PaintGame(Graphics g)
        {
            g.Clear(Color.White);   // 清空绘图区
            // 我们需要使雷区在用户显示的区域上下左右保持 6px 的偏移量，使得整体看起来更加协调
            int nOffsetX = 6;   // X 方向偏移量
            int nOffsetY = 6 + MenuStrip_Main.Height;   // Y 方向偏移量
            for (int i = 1; i <= nWidth; i++)   // 绘制行
            {
                for (int j = 1; j <= nHeight; j++)  // 绘制列
                {
                    // 第一个参数为笔刷，这里采用内置笔刷 SandyBrown
                    // 第二个参数为方块的参数，这里采用左上角坐标以及长宽的形式给出
                    // 34 表示每个雷区的大小，再加上偏移量就是我们当前雷区的起始位置，由于要空出 1px 的间隔，因此还需要加 1
                    // 由此可以得到每个方块在雷区中的位置，然后利用循环绘制出来

                    if(pState[i, j] == 0) // 未点开
                    {
                        if(i == MouseFocus.X && j == MouseFocus.Y)  // 是否为高亮点
                        {
                            g.FillRectangle(Brushes.SolidBrush(Color.FromArgb(100, Color.SandyBrown)), new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));
                        }
                        else 
                        {
                            g.FillRectangle(Brushes.SandyBrown, new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));   // 绘制雷区方块
                        }
                    }
                    else if(pState[i, j] == 1) // 点开
                    {
                        if(pMine[i, j] != -1)   // 非地雷
                        {
                            // 绘制背景
                            if(MouseFocus.X == i && MouseFocus.Y == j)
                            {
                                g.FillRectangle(Brushes.SolidBrush(Color.FromArgb(100, Color.LightGray)), new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));
                            }
                            else
                            {
                            g.FillRectangle(Brushes.LightGray, new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));
                            }
                            // 绘制数字
                            if(pMine[i, j] != 0)
                            {
                                Brush DrawBrush = new SolidBrush(Color.Blue);   // 定义钢笔
                                // 各个地雷数目的颜色
                                if (pMine[i, j] == 2) { DrawBrush = new SolidBrush(Color.Green); }
                                if (pMine[i, j] == 3) { DrawBrush = new SolidBrush(Color.Red); }
                                if (pMine[i, j] == 4) { DrawBrush = new SolidBrush(Color.DarkBlue); }
                                if (pMine[i, j] == 5) { DrawBrush = new SolidBrush(Color.DarkRed); }
                                if (pMine[i, j] == 6) { DrawBrush = new SolidBrush(Color.DarkSeaGreen); }
                                if (pMine[i, j] == 7) { DrawBrush = new SolidBrush(Color.Black); }
                                if (pMine[i, j] == 8) { DrawBrush = new SolidBrush(Color.DarkGray); }
                                SizeF Size = g.MeasureString(pMine[i, j].ToString(), new Font("Consolas", 16));
                                g.DrawString(pMine[i, j].ToString(), new Font("Consolas", 16), DrawBrush, nOffsetX + 34 * (i - 1) + 1 + (32 - Size.Width) / 2, nOffsetY + 34 * (j - 1) + 1 + (32 - Size.Height) / 2);
                            }
                        }
                    }
                }
            }
        }
```

此时，我们再次运行程序，单击某个格子，如果不是地雷，那么就可以看到下面的情况：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第七节、内部实现（续）/mineSweeper_7_08.png" caption="阶段性效果" >}}

接下来，我们先不处理游戏失败的情况，先来考虑右击事件，它主要用于更改标记，我们在右击函数中加入下面的代码：

```csharp
            else if(bMouseRight)  // 右键被按下
            {
                if(bMark)   // 可以使用标记
                {
                    if(pState[MouseFocus.X, MouseFocus.Y] == 0) // 未点开
                    {
                        pState[MouseFocus.X, MouseFocus.Y] = 2; // 红旗
                    }
                    else if(pState[MouseFocus.X, MouseFocus.Y] == 2) // 红旗
                    {
                        pState[MouseFocus.X, MouseFocus.Y] = 3; // 问号
                    }
                    else if(pState[MouseFocus.X, MouseFocus.Y] == 3) // 问号
                    {
                        pState[MouseFocus.X, MouseFocus.Y] = 0; // 未点开
                    }
                }
            }
            this.Refresh(); 
            bMouseLeft = bMouseRight = false;
        }
```

同样，我们现在运行程序还是不会有什么效果。我们需要更新PaintGame函数。再次之前，我们需要将我们的图标信息代入到工程中来，在导入之前我们需要将它们大尺寸分别修改为 24×24 和 20×20，以达到更好的显示效果。

在右侧解决方案资源管理器中找到 Resources.resx 文件，双击打开资源管理界面，将两张图片选中后拖动过去即可完成图片的导入。同时修改 PaintGame 函数的未点开功能部分如下：

```csharp
        /// <summary>
        /// 绘制游戏区
        /// </summary>
        private void PaintGame(Graphics g)
        {
            g.Clear(Color.White);   // 清空绘图区
            // 我们需要使雷区在用户显示的区域上下左右保持 6px 的偏移量，使得整体看起来更加协调
            int nOffsetX = 6;   // X 方向偏移量
            int nOffsetY = 6 + MenuStrip_Main.Height;   // Y 方向偏移量
            for (int i = 1; i <= nWidth; i++)   // 绘制行
            {
                for (int j = 1; j <= nHeight; j++)  // 绘制列
                {
                    // 第一个参数为笔刷，这里采用内置笔刷 SandyBrown
                    // 第二个参数为方块的参数，这里采用左上角坐标以及长宽的形式给出
                    // 34 表示每个雷区的大小，再加上偏移量就是我们当前雷区的起始位置，由于要空出 1px 的间隔，因此还需要加 1
                    // 由此可以得到每个方块在雷区中的位置，然后利用循环绘制出来

                    if(pState[i, j] == 0) // 未点开
                    {
                        // 绘制背景
                        if(i == MouseFocus.X && j == MouseFocus.Y)  // 是否为高亮点
                        {
                            g.FillRectangle(Brushes.SolidBrush(Color.FromArgb(100, Color.SandyBrown)), new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));
                        }
                        else 
                        {
                            g.FillRectangle(Brushes.SandyBrown, new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));   // 绘制雷区方块
                        }
                        // 绘制标记
                        if(pState[i, j] == 2)
                        {
                            g.DrawImage(Properties.Resources.Flag, nOffsetX + 34 * (i - 1) + 1 + 4, nOffsetY + 34 * (j - 1) + 1 + 2);   // 绘制红旗
                        }
                        if(pState[i, j] == 3)
                        {
                            g.DrawImage(Properties.Resources.Doubt, nOffsetX + 34 * (i - 1) + 1 + 4, nOffsetY + 34 * (j - 1) + 1 + 2);   // 绘制问号
                        }
                    }
                    else if(pState[i, j] == 1) // 点开
                    {
                        if(pMine[i, j] != -1)   // 非地雷
                        {
                            // 绘制背景
                            if(MouseFocus.X == i && MouseFocus.Y == j)
                            {
                                g.FillRectangle(Brushes.SolidBrush(Color.FromArgb(100, Color.LightGray)), new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));
                            }
                            else
                            {
                            g.FillRectangle(Brushes.LightGray, new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));
                            }
                            // 绘制数字
                            if(pMine[i, j] != 0)
                            {
                                Brush DrawBrush = new SolidBrush(Color.Blue);   // 定义钢笔
                                // 各个地雷数目的颜色
                                if (pMine[i, j] == 2) { DrawBrush = new SolidBrush(Color.Green); }
                                if (pMine[i, j] == 3) { DrawBrush = new SolidBrush(Color.Red); }
                                if (pMine[i, j] == 4) { DrawBrush = new SolidBrush(Color.DarkBlue); }
                                if (pMine[i, j] == 5) { DrawBrush = new SolidBrush(Color.DarkRed); }
                                if (pMine[i, j] == 6) { DrawBrush = new SolidBrush(Color.DarkSeaGreen); }
                                if (pMine[i, j] == 7) { DrawBrush = new SolidBrush(Color.Black); }
                                if (pMine[i, j] == 8) { DrawBrush = new SolidBrush(Color.DarkGray); }
                                SizeF Size = g.MeasureString(pMine[i, j].ToString(), new Font("Consolas", 16));
                                g.DrawString(pMine[i, j].ToString(), new Font("Consolas", 16), DrawBrush, nOffsetX + 34 * (i - 1) + 1 + (32 - Size.Width) / 2, nOffsetY + 34 * (j - 1) + 1 + (32 - Size.Height) / 2);
                            }
                        }
                    }
                }
            }
        }
```

此时，我们发现当我们的区域处于红旗或者问号的时候，左击的时候还是会打开该区域，修改左击代码如下：

```csharp
            else if(bMouseLeft)   // 左键被按下
            {
                if(pMine[MouseFocus.X, MouseFocus.Y] != -1 && pState[MouseFocus.X, MouseFocus.Y] == 0)
                {
                    dfs(MouseFocus.X, MouseFocus.Y);
                }
                else
                {
                    // 地雷，游戏结束
                }
            }
```

此时，我们以及完成了基本的游戏功能了。接下来我们还需要完成一个鼠标左右键同时按下的事件，代码如下：

```csharp
            if(bMouseLeft && BMouseRight)   // 左右键同时按下
            {
                if(pState[MouseFocus.X, MouseFocus.Y] == 1 && pMine[MouseFocus.X, MouseFocus.Y] > 0)    // 为数字区域
                {
                    int nFlagCnt = 0, nDoubtCnt = 0, nSysCnt = pMine[MouseFocus.X, MouseFocus.Y];   // 记录红旗数目，问号数目，九宫格地雷数目
                    for(int i = 0; i < 8; i++)
                    {
                        // 获取偏移量
                        int x = MouseFocus.X + dx[i];
                        int y = MouseFocus.Y + dy[i];
                        if(pState[x, y] == 2)   // 红旗
                        {
                            nFlagCnt++;
                        }
                        if(pState[x, y] == 3)   // 问号
                        {
                            nDoubtCnt++;
                        }
                        if(nFlagCnt == nSysCnt || nFlagCnt + nDoubtCnt == nSysCnt) // 打开九宫格
                        {
                            bool bFlag = OpenMine(MouseFocus.X, MouseFocus.Y);
                            if(!bFlag)  // 周围有地雷
                            {
                                // 结束游戏
                            }
                        }
                    }
                }
            }
```

这里，我们缺少一个 OpenMine 函数，定义如下：

```csharp
        private tool OpenMine(int sx, int sy)
        {
            bool bFlag = true;  // 默认周围无雷
            for (int i = 0; i < 8; i++)
            {
                // 获取偏移量
                int x = MouseFocus.X + dx[i];
                int y = MouseFocus.Y + dy[i];
                if (pState[x, y] == 0)  // 问号
                {
                    pState[x, y] = 1;   // 打开
                    if(pMine[x, y] == -1)   // 有地雷
                    {
                        bFlag = false;
                        break;
                    }
                }
            }
            return bFlag;
        }
```

此时，如果我们运行程序，很有可能出现下面的情况，有的地方是一个白色的区域，没有任何内容：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第七节、内部实现（续）/mineSweeper_7_14.png" caption="阶段性效果" >}}

出现这种结果，也就意味着出现了地雷，因为我们的 PaintGame 函数暂时还没有绘制地雷的功能。

细心的读者可能发现了一个问题，地图上有了一面红旗，底下的状态栏中却仍然显示地雷数目为 10，我们通过修改右击事件来修复这个问题：

```csharp
        private void Form_Main_MouseUp(object sender, MouseEventArgs e)
        {
            if(MouseFocus.X == 0 && MouseFocus.Y == 0)  // 不在地雷区域
            {
                return;     // 不做任何处理
            }
            if(bMouseLeft && BMouseRight)   // 左右键同时按下
            {
                if(pState[MouseFocus.X, MouseFocus.Y] == 1 && pMine[MouseFocus.X, MouseFocus.Y] > 0)    // 为数字区域
                {
                    int nFlagCnt = 0, nDoubtCnt = 0, nSysCnt = pMine[MouseFocus.X, MouseFocus.Y];   // 记录红旗数目，问号数目，九宫格地雷数目
                    for(int i = 0; i < 8; i++)
                    {
                        // 获取偏移量
                        int x = MouseFocus.X + dx[i];
                        int y = MouseFocus.Y + dy[i];
                        if(pState[x, y] == 2)   // 红旗
                        {
                            nFlagCnt++;
                        }
                        if(pState[x, y] == 3)   // 问号
                        {
                            nDoubtCnt++;
                        }
                        if(nFlagCnt == nSysCnt || nFlagCnt + nDoubtCnt == nSysCnt) // 打开九宫格
                        {
                            bool bFlag = OpenMine(MouseFocus.X, MouseFocus.Y);
                            if(!bFlag)  // 周围有地雷
                            {
                                // 结束游戏
                            }
                        }
                    }
                }
            }
            else if(bMouseLeft)   // 左键被按下
            {
                if(pMine[MouseFocus.X, MouseFocus.Y] != -1 && pState[MouseFocus.X, MouseFocus.Y] == 0)
                {
                    dfs(MouseFocus.X, MouseFocus.Y);
                }
                else
                {
                    // 地雷，游戏结束
                }
            }
            else if(bMouseRight)  // 右键被按下
            {
                if(bMark)   // 可以使用标记
                {
                    if(pState[MouseFocus.X, MouseFocus.Y] == 0) // 未点开
                    {
                        pState[MouseFocus.X, MouseFocus.Y] = 2; // 红旗
                        Label_Mine.Text = Convert.ToString(Convert.ToInt32(Label_Mine.Text) - 1);   // 剩余地雷数目减 1
                    }
                    else if(pState[MouseFocus.X, MouseFocus.Y] == 2) // 红旗
                    {
                        pState[MouseFocus.X, MouseFocus.Y] = 3; // 问号
                        Label_Mine.Text = Convert.ToString(Convert.ToInt32(Label_Mine.Text) + 1);   // 剩余地雷数目加 1
                    }
                    else if(pState[MouseFocus.X, MouseFocus.Y] == 3) // 问号
                    {
                        pState[MouseFocus.X, MouseFocus.Y] = 0; // 未点开
                    }
                }
            }
            this.Refresh(); 
            bMouseLeft = bMouseRight = false;
        }
```

最终，我们会看到这样的效果：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第七节、内部实现（续）/mineSweeper_7_16.png" caption="运行效果" >}}

我们将在下一节中介绍游戏结束的相关内容。
