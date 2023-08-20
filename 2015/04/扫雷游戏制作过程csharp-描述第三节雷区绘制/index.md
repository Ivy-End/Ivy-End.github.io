# 扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制


这一节我们主要涉及界面中雷区的绘制方法。

首先来考虑几个问题。为了保存整个雷区的信息，我们需要哪些数据。显然，除了要保存雷区的宽度和高度（分别定义为宽和高方向上方块的个数）外，还需要保存地雷的数目。这样我们需要用到三个变量 nWidth, nHeight, nMineCnt 分别保存雷区的宽度、雷区的高度以及地雷的数目。

右击窗口，选择查看代码，也可以使用快捷键 F7，如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_01.png" caption="菜单示意图" >}}

可以看到这样的代码界面：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_02.png" caption="代码界面" >}}

添加如下所示的代码，用来定义扫雷区域的基本变量，它们的含义在上文或者注释中都有提及：

```csharp
namespace Minesweeper
{
    public partial class Form_Main : Form
    {
        int nWidth;     // 表示雷区的宽度
        int nHeight;    // 表示雷区的高度
        int nMineCnt;   // 表示地雷的数目

        public Form_Main()
        {
            InitializeComponent();
        }
    }
}
```

为了方便设置这三个参数，我们可以定义一个新的函数 SetGame，如下所示：

```csharp
namespace Minesweeper
{
    public partial class Form_Main : Form
    {
        int nWidth;     // 表示雷区的宽度
        int nHeight;    // 表示雷区的高度
        int nMineCnt;   // 表示地雷的数目

        public Form_Main()
        {
            InitializeComponent();
        }

        private void SetGame(int Width, int Height, int MineCnt)
        {
            nWidth = Width;
            nHeight = Height;
            nMineCnt = MineCnt;
        }
    }
}
```
这样，我们就可以通过调用 SetGame 函数来设置游戏的参数了。为了方便阅读，我们可以为这个函数加上一个注释，在函数名上方输入"///"，程序会自动生成一个注释块，如下所示：

```csharp
namespace Minesweeper
{
    public partial class Form_Main : Form
    {
        int nWidth;     // 表示雷区的宽度
        int nHeight;    // 表示雷区的高度
        int nMineCnt;   // 表示地雷的数目

        public Form_Main()
        {
            InitializeComponent();
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="Width"></param>
        /// <param name="Height"></param>
        /// <param name="MineCnt"></param>
        private void SetGame(int Width, int Height, int MineCnt)
        {
            nWidth = Width;
            nHeight = Height;
            nMineCnt = MineCnt;
        }
    }
}
```

输入相关信息，第二行的内容是用来对函数的作用进行说明，下面的三行分别用来对三个参数的作用进行说明，将它们修改如下：

```csharp
        /// <summary>
        /// 游戏参数设置
        /// </summary>
        /// <param name="Width">雷区宽度</param>
        /// <param name="Height">雷区高度</param>
        /// <param name="MineCnt">地雷数目</param>
        private void SetGame(int Width, int Height, int MineCnt)
        {
            nWidth = Width;
            nHeight = Height;
            nMineCnt = MineCnt;
        }
```

这样当我们输入这个函数的时候（当然，我们目前还不需要调用这个函数。），就会显示出来对应的注释，如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_07.png" caption="注释示意图" >}}

到目前为止，我们的代码应该是这样的：

```csharp
namespace Minesweeper
{
    public partial class Form_Main : Form
    {
        int nWidth;     // 表示雷区的宽度
        int nHeight;    // 表示雷区的高度
        int nMineCnt;   // 表示地雷的数目

        public Form_Main()
        {
            InitializeComponent();
        }

        /// <summary>
        /// 游戏参数设置
        /// </summary>
        /// <param name="Width">雷区宽度</param>
        /// <param name="Height">雷区高度</param>
        /// <param name="MineCnt">地雷数目</param>
        private void SetGame(int Width, int Height, int MineCnt)
        {
            nWidth = Width;
            nHeight = Height;
            nMineCnt = MineCnt;
        }
    }
}
```

接下来我们可以定义几个辅助函数，分别表示设置游戏参数为初级、中级、高级，如下图所示：

```csharp
        /// <summary>
        /// 设置游戏等级为初级
        /// </summary>
        private void SetGameBeginner()
        {
            SetGame(10, 10, 10);
        }
        
        /// <summary>
        /// 设置游戏等级为中级
        /// </summary>
        private void SetGameIntermediate()
        {
            SetGame(16, 16, 40);
        }
        
        /// <summary>
        /// 设置游戏等级为高级
        /// </summary>
        private void SetGameExpert()
        {
            SetGame(30, 16, 99);
        }
```

在我们开始游戏的时候，我们希望它自动获取上次的游戏设置，如果这是第一次开始游戏，那么将游戏设置为初级。

我们先来看一下第一个需求，自动获取上次的游戏设置，这就意味着我们需要在上次游戏关闭的时候将上次的游戏设置保存下来。保存到哪里呢，我们在这里采用 Setting 文件来保存这些数据。工程创建的时候，系统会自动生成一个 Setting 文件。因此我们不需要自己创建，只需要使用原有的 Setting 文件即可。在右方解决方案资源管理器面板中展开 Properties，右击 Settings.settings，选择打开即可。

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_10.png" caption="解决方案资源管理器" >}}

打开后的界面如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_11.png" caption="Settings.settings 示意图" >}}

按照下图对它进行设置，设置完成后按Ctrl + S进行保存。

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_12.png" caption="Settings.settings 设置示意图" >}}

注意到第四栏值，我们将它初始化为初级的参数，也就完成了我们刚才的第二个需求——无法找到上一次设置的时候，我们将它置为初级模式。

就行了，我们需要通过代码将这些参数读入到定义的变量中去，加入如下图所示的代码：

```csharp
        public Form_Main()
        {
            InitializeComponent();

            // 初始化游戏参数
            nWidth = Properties.Settings.Default.Width;
            nHeight = Properties.Settings.Default.Height;
            nMineCnt = Properties.Settings.Default.MineCnt;
        }
```

有了这些参数我们就可以绘制雷区了，我们假定雷区为 32×32 的小方块，并且四周有一圈宽度为 1 的留白，用于与其它雷区区别，这样，每个雷区的实际大小为 34×34。

接下去，我们将窗口切换到界面布局，选中主窗口，在左边的属性面板中，单击事件按钮，并找到 Paint 事件，双击该条目，系统会自动创建一个事件，我们将在这里绘制雷区。如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_14.png" caption="创建事件" >}}

添加 Paint 事件以后，程序会自动跳到代码编辑窗口，并且会看到如下的代码：

```csharp
        private void Form_Main_Paint(object sender, PaintEventArgs e)
        {

        }
```

将Paint函数中的内容修改如下：

```csharp
        private void Form_Main_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = this.CreateGraphics();     // 创建绘图句柄

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
                    g.FillRectangle(Brushes.SandyBrown, new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));   // 绘制雷区方块
                }
            }
        }
```

然后，我们按下 Ctrl + F5 就可以看到下面的效果：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_17.png" caption="阶段性效果" >}}

看上去感觉样式很奇怪，后边多出了很多空白的区域，而且下方还有一些部分没有显示出来，因为我们还没有根据游戏的参数调整窗口的大小。新建一个名为 UpdateSize 的函数，输入下图的代码：

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
        }
```

接下来我们在 SetGame 函数中调用这个函数，使得修改游戏参数的时候自动修改窗口大小，代码如下：

```csharp
        /// <summary>
        /// 游戏参数设置
        /// </summary>
        /// <param name="Width">雷区宽度</param>
        /// <param name="Height">雷区高度</param>
        /// <param name="MineCnt">地雷数目</param>
        private void SetGame(int Width, int Height, int MineCnt)
        {
            nWidth = Width;
            nHeight = Height;
            nMineCnt = MineCnt;
            UpdateSize();
        }
```

最后不要忘记了在初始化读入上次游戏参数后也需要修改窗口大小，代码如下：

```csharp
        public Form_Main()
        {
            InitializeComponent();

            // 初始化游戏参数
            nWidth = Properties.Settings.Default.Width;
            nHeight = Properties.Settings.Default.Height;
            nMineCnt = Properties.Settings.Default.MineCnt;
            UpdateSize();
        }
```

最后按 Ctrl + F5 编译运行，得到最终结果：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第三节、雷区绘制/mineSweeper_3_21.png" caption="运行效果" >}}

到目前为止，扫雷的界面已经基本出来了，下一节我们主要介绍一下菜单的相关代码。
