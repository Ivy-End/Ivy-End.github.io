# 扫雷游戏制作过程（CSharp 描述）：第六节、内部实现


在进行内部实现之前，我们先来考虑一下扫雷的内部逻辑。首先，我们需要保存每个点上是否有地雷，如果没有地雷，那么要显示与它紧邻的八个格子中一共有多少的地雷。还需保存每个雷区的状态（点开，未点开，红旗，问号）。我们考虑定义两个常量，表示地雷的最大范围：

```csharp
        const int MAX_WIDTH = 64;   // 最大宽度
        const int MAX_HEIGHT = 32;  // 最大高度
```

接下来定义两个数组，用来保存上述两种数据。对于第一类数据，我们使用 -1 表示该区域有地雷，使用数字表示与它紧邻的八个格子中一共有多少地雷；对于第二类数据，我们使用 0 表示未点开，1 表示点开，2 表示红旗，3 表示问号。如下图所示：

```csharp
        int[,] pMine = new int[MAX_WIDTH, MAX_HEIGHT];  // 第一类数据
        int[,] pState = new int[MAX_WIDTH, MAX_HEIGHT];  // 第二类数据
```

接下来我们需要初始化游戏数据，双击 New Game 菜单，输入游戏的初始化代码：

```csharp
        private void newGameNToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 以下两行清空数组
            Array.Clear(pMine, 0, pMine.Length);
            Array.Clear(pState, 0, pState.Length);
            // 初始化地雷数据
            Random Rand = new Random();
            for(int i = 1; i <= nMineCnt; ) // 地雷总数
            {
                // 随机地雷坐标 (x, y)
                int x = Rand.Next(nWidth) + 1;
                int y = Rand.Next(nHeight) + 1;
                if (pMine[x, y] != -1)
                {
                    pMine[x, y] = -1; i++;
                }
            }
            for(int i = 1 ; i <= nWidth; i++)   // 枚举宽度
            {
                for(int j = 1; j <= nHeight; j++)   // 枚举高度
                {
                    if(pMine[i, j] != -1)   // 不是地雷，显示周围地雷数
                    {
                        for(int k = 0; k < 8; k++)  // 八个方向拓展
                        {
                            if(pMine[i + dx[k], j + dy[k]] == -1) // 找到地雷
                            {
                                pMine[i, j]++;  // 地雷数自增
                            }
                        }
                    }
                }
            }
        }
```

其中涉及到了 dx 以及 dy 这两个偏移量常量数组的定义，如下图所示：

```csharp
        int[] dx = new int[] { -1, 0, 1, -1, 1, -1, 0, 1 };     // x 坐标偏移量
        int[] dy = new int[] { 1, 1, 1, 0, 0, -1, -1, -1 };     // y 坐标偏移量
```

接下来我我们来实现一些特效，例如高亮当前鼠标悬浮位置的雷区，打开设计窗口，添加 MouseMove 事件：

```csharp
        private void Form_Main_MouseMove(object sender, MouseEventArgs e)
        {
            int x = (e.X - 6) / 36 + 1;     // 获取 x 位置
            int y = (e.Y - MenuStrip_Main.Height - 6) / 36 + 1;     // 获取 y 位置
            MouseFocus.X = x; MouseFocus.Y = y; // 设置当前高亮点
            PaintGame();    // 重绘雷区
        }
```

为此，我们还需要定义一个变量 MouseFocus 来记录当前的高亮点，代码分别如下：

```csharp
        Point MouseFocus;   // 高亮点记录
```

同时，我们需要在初始化的时候对它进行清零操作，将下面的清零代码加入到刚才的初始化函数中：

```csharp
        // 重置高亮点
        MouseFocus.X = 0; MouseFocus.Y = 0;
```

接下来我们需要修改 PaintGame 函数，添加对高亮点的绘制：

```csharp
        /// <summary>
        /// 绘制游戏区
        /// </summary>
        private void PaintGame()
        {
            Graphics g = this.CreateGraphics();     // 创建绘图句柄
            g.FillRectangle(Brushes.White, new Rectangle(0, 0, this.Width, this.Height));
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

                    if(i == MouseFocus.X && j == MouseFocus.Y) // 是否为高亮点
                    {
                        g.FillRectangle(Brushes.SolidBrush(Color.FromArgb(100, Color.SandyBrown)), new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));
                    }
                    else 
                    {
                        g.FillRectangle(Brushes.SandyBrown, new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));   // 绘制雷区方块
                    }
                }
            }
        }
```

此时，我们可以尝试运行，然而却发现界面会一直在闪，使得游戏体验急剧下降，为了修复这个问题，我们只需要在构造函数中添加一句代码，开启双缓冲即可，代码如下：

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

            UpdateSize();
            SelectLevel();
        }
```

然而我们发现效果并没有很大的提升，这是由于我们之前定义的 PaintGame 函数所导致的，它不断的定义新的 Graphics 实例，使得这个过程变得很慢，我们可以直接使用 Paint 事件中的 Graphics 实例。首先修改 PaintGame 函数的定义以及部分实现，如下图所示：

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

                    if(i == MouseFocus.X && j == MouseFocus.Y) // 是否为高亮点
                    {
                        g.FillRectangle(Brushes.SolidBrush(Color.FromArgb(100, Color.SandyBrown)), new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));
                    }
                    else 
                    {
                        g.FillRectangle(Brushes.SandyBrown, new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));   // 绘制雷区方块
                    }
                }
            }
        }
```

同时修改 Paint 事件中的调用函数：

```csharp
        private void Form_Main_Paint(object sender, PaintEventArgs e)
        {
            PaintGame(e.Graphics);
        }
```

对于其它非 Paint 函数调用的 PaintGame 函数，一律修改为 `this.Refresh();` 即可，如下图所示：

```csharp
        /// <summary>
        /// 自动更新窗口大小
        /// <summary>
        private void UpdateSize()
        {
            int nOffsetX = this.Width - this.ClientSize.Width;  // 包含了窗口标题栏以及上下边框的高度
            int nOffsetY = this.Height - this.ClientSize.Height;    // 包含了左右边框的宽度
            int nAdditionY = MenuStrip_Main.Height + TableLayoutPanel_Main.Height;  // 包含了菜单栏以及下方显示信息栏的高度
            this.Width = 12 + 34 * nWidth + nOffsetX;   // 设置窗口高度，34 为每个雷区的高度，12 为上下总空隙（6px + 6px），再加上偏移量
            this.Height = 12 + 34 * nHeight + nAdditionY + nOffsetY;    // 设置窗口宽度，同理
            // PaintGame()
            this.Refresh();
        }
```

```csharp
        private void Form_Main_MouseMove(object sender, MouseEventArgs e)
        {
            int x = (e.X - 6) / 36 + 1;     // 获取 x 位置
            int y = (e.Y - MenuStrip_Main.Height - 6) / 36 + 1;     // 获取 y 位置
            MouseFocus.X = x; MouseFocus.Y = y; // 设置当前高亮点
            this.Refresh();     // 重绘雷区
        }
```

再次运行的时候，我们发现已经没有了之前的闪屏问题了。然而我们却发现了新的问题，对于当前移动到的位置坐标获取不准确，我们进行下面的调整：

```csharp
        private void Form_Main_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.X < 6 || e.X > 6 + nWidth * 34 ||
                e.Y < 6 + MenuStrip_Main.Height ||
                e.Y > 6 + MenuStrip_Main.Height + nHeight * 34)     // 不在地雷区域
            {
                MouseFocus.X = 0; MouseFocus.Y = 0;
            }
            else
            {
                int x = (e.X - 6) / 36 + 1;     // 获取 x 位置
                int y = (e.Y - MenuStrip_Main.Height - 6) / 36 + 1;     // 获取 y 位置
                MouseFocus.X = x; MouseFocus.Y = y; // 设置当前高亮点
            }            
            this.Refresh();     // 重绘雷区
        }
```

此时，我们运行程序的时候，就会发现界面基本已经完成了。

接下来我们需要为 Setting 菜单添加一个单击确定按钮以后就自动开始游戏的功能，为此我们只需要修改 UpdateSize 函数，代码如下：

```csharp
        /// <summary>
        /// 自动更新窗口大小
        /// <summary>
        private void UpdateSize()
        {
            int nOffsetX = this.Width - this.ClientSize.Width;  // 包含了窗口标题栏以及上下边框的高度
            int nOffsetY = this.Height - this.ClientSize.Height;    // 包含了左右边框的宽度
            int nAdditionY = MenuStrip_Main.Height + TableLayoutPanel_Main.Height;  // 包含了菜单栏以及下方显示信息栏的高度
            this.Width = 12 + 34 * nWidth + nOffsetX;   // 设置窗口高度，34 为每个雷区的高度，12 为上下总空隙（6px + 6px），再加上偏移量
            this.Height = 12 + 34 * nHeight + nAdditionY + nOffsetY;    // 设置窗口宽度，同理
            newGameNToolStripMenuItem_Click(new object(), new EvenetArgs());    // 调用新建游戏函数
        }
```

接下来我们需要修改一下显示地雷数目以及计时的标签，在新建游戏的函数中修改如下：

```csharp
        Label_Mine.Text = nMineCnt.ToString();  // 显示地雷数目
        Label_Timer.Text = "0"; // 计时器清零
        Timer_Main.Enabled = true;  // 启动计时器计时
```

运行后，我们发现计时器并没有显示出来，因为我们还没有为计时器摄制事件。在设计窗口页面中双击计时器，程序自动创建计时器事件，输入下面的代码：

```csharp
        private void Timer_Main_Tick(object sender, EventArgs e)
        {
            Label_Timer.Text = Convert.ToString(Convert.ToInt32(Label_Timer.Text) + 1); // 自增 1 秒
        }
```

同时记得在设计页面中将记时器的 Interval 属性设置为 1000，表示每秒执行一次计时器事件代码。

最后，我们运行程序，效果如下：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第六节、内部实现/mineSweeper_6_18.png" caption="运行效果" >}}

下一讲将会涉及具体的鼠标单击以及右击雷区时的逻辑事件的判定。
