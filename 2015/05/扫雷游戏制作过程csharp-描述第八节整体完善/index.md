# 扫雷游戏制作过程（CSharp 描述）：第八节、整体完善


这一节我们将介绍结束游戏的方法，以及一些整体方面的完善。首先考虑失败的情况，它会将所有的地雷都显示出来。我们新建一个 GameLost 函数：

```csharp
    private void GameLost()
    {
        for(int i = 1; i<= nWidth; i++)
        {
            for(int j = 1; j<= nHeight; j++)
            {
                if(pMine[i, j] == -1 && (pState[i, j] == 0 || pState[i, j] == 3))   // 未点开或者标记为问号的雷
                {
                    pState[i, j] = 1;   // 点开该地雷
                }
            }
        }
    }
```

在游戏结束的地方调用 GameLost 函数，因为我们上一节中讲述的游戏结束都是失败的情况：
```csharp
                        if(nFlagCnt == nSysCnt || nFlagCnt + nDoubtCnt == nSysCnt) // 打开九宫格
                        {
                            bool bFlag = OpenMine(MouseFocus.X, MouseFocus.Y);
                            if(!bFlag)  // 周围有地雷
                            {
                                // 结束游戏
                                GameLost();
                            }
                        }
```

```csharp
                if(pMine[MouseFocus.X, MouseFocus.Y] != -1 && pState[MouseFocus.X, MouseFocus.Y] == 0)
                {
                    dfs(MouseFocus.X, MouseFocus.Y);
                }
                else
                {
                    // 地雷，游戏结束
                    GameLost();
                }
```

我们发现游戏结束的时候，虽然所有的格子都打开了，但是并没有显示出地雷的图标，我们将地雷的图标调整为 20×20，并且按照上一节的方法将它将入到 Resources.resx 文件中。同时修改 PaintGame 函数点开部分的代码如下：

```csharp
                    else if(pState[i, j] == 1) // 点开
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
                        // 绘制地雷
                        if(pMine[i, j] == -1)
                        {
                            g.DrawImage(Properties.Resources.Mine, nOffsetX + 34 * (i - 1) + 1 + 4, nOffsetY + 34 * (j - 1) + 1 + 2);   // 绘制地雷
                        }
                    }
```

此时，我们再次测试的时候，就会看到地雷的图标了：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第八节、整体完善/mineSweeper_8_05.png" caption="阶段性效果" >}}

然而，我们发现有一个问题，当我们单击数字的时候，会把所有的地雷都显示出来，也就是游戏结束。我们修改左击的事件：
```csharp
            else if(bMouseLeft)   // 左键被按下
            {
                if(pMine[MouseFocus.X, MouseFocus.Y] != -1)
                {
                    if(pState[MouseFocus.X, MouseFocus.Y] == 0)
                    {
                        dfs(MouseFocus.X, MouseFocus.Y);
                    }
                }
                else
                {
                    // 地雷，游戏结束
                    GameLost();
                }
            }
```

这时候，刚才的问题就得到了修复。但是我们却又发现了一个问题——游戏结束的时候，还是可以继续单击雷区，打开区域。为此，我们增加一个变量检测游戏是否结束，如果结束，则任何按键都视为无效。首先定义一个变量：

```csharp
        bool bGame; // 游戏是否结束
```

我们在游戏开始的时候对它进行初始化，在 New Game 菜单事件处理函数的末尾修改代码如下：

```csharp
            Label_Mine.Text = nMineCnt.ToString();  // 显示地雷数目
            Label_Timer.Text = "0"; // 计时器清零
            Timer_Main.Enable = true;  // 启动计时器计时
            bGame = false;  // 游戏暂未结束
```

将 GameLost 函数修改如下：

```csharp
    private void GameLost()
    {
        for(int i = 1; i<= nWidth; i++)
        {
            for(int j = 1; j<= nHeight; j++)
            {
                if(pMine[i, j] == -1 && (pState[i, j] == 0 || pState[i, j] == 3))   // 未点开或者标记为问号的雷
                {
                    pState[i, j] = 1;   // 点开该地雷
                }
            }
        }
        bGame = true;
    }
```

同时修改 MouseUp 事件，将开头代码修改如下：
```csharp
        private void Form_Main_MouseUp(object sender, MouseEventArgs e)
        {
            if(MouseFocus.X == 0 && MouseFocus.Y == 0 || bGame)  // 不在地雷区域或游戏结束
            {
                return;     // 不做任何处理
            }
```

至此，这个问题已经得到了修复。我们可以运行查看结果。

但是，我们现在还有一个判断游戏胜利的函数没有写，我们在每次打开地雷区域的时候判断游戏者是否胜利，首先定义一个 GameWin 函数如下：

```csharp
        private void GameWin()
        {
            int nCnt = 0;   // 用户标记红旗数目、问号数目、以及无标记未点开区域总数
            for(int i = 1; i <= nWidth; i++)
            {
                for(int j = 1; j <= nHeight; j++)
                {
                    if(pState[i, j] == 0 || pState[i, j] == 2 || pState[i, j] == 3) // 对应标记未点开区域、红旗区域、问号区域
                    {
                        nCnt++;
                    }
                }
            }
            if(nCnt == nMineCnt) // 胜利条件
            {
                Timer_Main.Enabled = false; // 关闭计时器
                MessageBox.Show(String.Format("游戏胜利，耗时：{0} 秒", Label_Timer.Text), "提示", MessageBoxButtons.OK);
                // 更新记录
                if (nWidth == 10 && nHeight == 10 && nMineCnt == 10) // 初级
                {
                    if (Properties.Settings.Default.Beginner > Convert.ToInt32(Label_Timer.Text))   // 更新记录
                    {
                        Properties.Settings.Default.Beginner = Convert.ToInt32(Label_Timer.Text)
                        Properties.Settings.Default.Beginner.Save();
                    }
                }
                else if (nWidth == 16 && nHeight == 16 && nMineCnt == 40) // 中级
                {
                    if (Properties.Settings.Default.Intermediate > Convert.ToInt32(Label_Timer.Text))   // 更新记录
                    {
                        Properties.Settings.Default.Intermediate = Convert.ToInt32(Label_Timer.Text)
                        Properties.Settings.Default.Intermediate.Save();
                    }
                }
                else if (nWidth == 30 && nHeight == 16 && nMineCnt == 40) // 高级
                {
                    if (Properties.Settings.Default.Expert > Convert.ToInt32(Label_Timer.Text))   // 更新记录
                    {
                        Properties.Settings.Default.Expert = Convert.ToInt32(Label_Timer.Text)
                        Properties.Settings.Default.Expert.Save();
                    }
                }
                bGame = true;
            }
        }
```

然后，在MouseUp最后调用该函数：

```csharp
            GameWin();
            this.Refresh();
            bMouseLeft = bMouseRight = false;
        }
```

此时，我们的游戏基本完成了，但是有时会有这样的问题，左右双击区域的时候，不会显示到数字边界上，我们在 OpenMine 的时候调用一下 dfs 函数即可，将 OpenMine 函数修改如下：

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
                        dfs(x, y);
                    }
                    else    // 有地雷
                    {
                        bFlag = false;
                        break;
                    }
                }
            }
            return bFlag;
        }
```

至此，我们的扫雷游戏基本完成了，接下来还需要处理的一个功能是音效，首先搜索音效资源：Bomb、Tick。然后按照之前的方法，将它们添加到 Resources.resx 文件中。

定义两个变量用来播放这两个音效，并且在构造函数中进行初始化，如下：

```csharp
        System.Media.SoundPlayer soundTick; // 计时
        System.Media.SoundPlayer soundBomb; // 爆炸
```

```csharp
        public Form_Main()
        {
            InitializeComponent();

            this.DoubleBuffered = true; // 开启双缓冲

            // 初始化游戏参数
            nWidth = Properties.Settings.Default.Width;
            nHeight = Properties.Settings.Default.Height;
            nMineCnt = Properties.Settings.Default.MineCnt;

            // 初始化
            bMark = Properties.Settings.Default.Mark;
            bAudio = Properties.Settings.Default.Audio;
            markMToolStripMenuItem.Checked = bMark;
            audioMToolStripMenuItem.Checked = bAudio;

            // 初始化音频
            soundTick = new System.Media.SoundPlayer(Properties.Resources.Tick);
            soundBomb = new System.Media.SoundPlayer(Properties.Resources.Bomb);

            UpdateSize();
            SelectLevel();
        }
```

接下来分别在计时器的事件以及 GameLost 函数中添加如下代码：

```csharp
    private void Timer_Main_Tick(object sender, EventArgs e)
    {
        if(bAudio)
        {
            soundTick.Play();   // 播放
        }
        Label_Timer.Text = Convert.ToString(Convert.ToInt32(Label_Timer.Text) + 1); // 自增 1 秒
    }
```

```csharp
    private void GameLost()
    {
        for(int i = 1; i<= nWidth; i++)
        {
            for(int j = 1; j<= nHeight; j++)
            {
                if(pMine[i, j] == -1 && (pState[i, j] == 0 || pState[i, j] == 3))   // 未点开或者标记为问号的雷
                {
                    pState[i, j] = 1;   // 点开该地雷
                }
            }
        }
        if(bAudio)
        {
            soundBomb.Play();
        }
        bGame = true;
    }
```

此外，我们还需要将音效的初始默认值设置为 False，只需要将 Setting 文件中的默认值改为 False 即可。此外，我们还需要在 GameLost 的时候停止计时器：

```csharp
    private void GameLost()
    {
        for(int i = 1; i<= nWidth; i++)
        {
            for(int j = 1; j<= nHeight; j++)
            {
                if(pMine[i, j] == -1 && (pState[i, j] == 0 || pState[i, j] == 3))   // 未点开或者标记为问号的雷
                {
                    pState[i, j] = 1;   // 点开该地雷
                }
            }
        }
        if(bAudio)
        {
            soundBomb.Play();
        }
        Timer_Main.Enabled = false; // 停用计时器
        bGame = true;
    }
```

至此，我们的一个扫雷游戏就制作完成了，效果如下：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第八节、整体完善/mineSweeper_8_20.png" caption="运行效果" >}}

但有时我们会发现雷区还没有被完全打开，就已经弹出了游戏结束的对话框，为此，我们只需要在 MouseUp 事件中将刷新和判断游戏胜利的语句换一下次序即可：

```csharp
            this.Refresh();
            GameWin();
            bMouseLeft = bMouseRight = false;
```

测试的时候，我们发现，单击 Rank 对话框中的 Reset 按钮，虽然数据库恢复了默认值，但是显示的值却没有马上恢复默认值，为此，双击 Rank 窗口中的 Reset 按钮，修改它的事件如下：

```csharp
        private void Button_Reset_Click(object sender, EventArgs e)
        {
            // 将标签设置为默认值
            Label_Beginer.Text = String.Format("Beginner:        {0}", 999);
            Label_Intermeidate.Text = String.Format("Intermediate:        {0}", 999);
            Label_Expert.Text = String.Format("Expert:        {0}", 999);

            // 将所有记录设置为 999 即完成初始化
            Propoerties.Settings.Default.Beginner = 999;
            Propoerties.Settings.Default.Intermediate = 999;
            Propoerties.Settings.Default.Export = 999;
            Propoerties.Settings.Default.Save();    // 保存设置
        }
```

至此，一个较为完善的扫雷游戏就完成了，我将它托管在了 GitHub 上：[Minesweeper](https://github.com/Ivy-End/Minesweeper)。
