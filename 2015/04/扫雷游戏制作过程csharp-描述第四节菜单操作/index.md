# 扫雷游戏制作过程（CSharp 描述）：第四节、菜单操作


我们现在的程序单击菜单的时候不会有任何反应，这一节我们主要介绍菜单的相关代码，使得菜单能够正常使用。

在第二节中，我们曾经提出希望在对应级别（初级、中级、高级、自定义）的按钮的显示勾，以表示目前的游戏等级。我们有两个时候需要对它进行操作，一个是加载上次游戏设置的时候，一个是在游戏过程中进行设置的时候，我们先介绍第一种情况。按照下图修改代码：

```csharp
        /// <summary>
        /// 选择对应的游戏等级
        /// </summary>
        private void SelectLevel()
        {
            if (nWidth == 10 && nHeight == 10 && nMineCnt == 10)
            {
                beginnerBToolStripMenuItem.Checked = true;
                intermediateIToolStripMenuItem.Checked = false;
                expertEToolStripMenuItem.Checked = false;
                settingSToolStripMenuItem.Checked = false;
            }
            else if (nWidth == 16 && nHeight == 16 && nMineCnt == 40)
            {
                beginnerBToolStripMenuItem.Checked = false;
                intermediateIToolStripMenuItem.Checked = true;
                expertEToolStripMenuItem.Checked = false;
                settingSToolStripMenuItem.Checked = false;
            }
            else if (nWidth == 30 && nHeight == 16 && nMineCnt == 99)
            {
                beginnerBToolStripMenuItem.Checked = false;
                intermediateIToolStripMenuItem.Checked = false;
                expertEToolStripMenuItem.Checked = true;
                settingSToolStripMenuItem.Checked = false;
            }
            else
            {
                beginnerBToolStripMenuItem.Checked = false;
                intermediateIToolStripMenuItem.Checked = false;
                expertEToolStripMenuItem.Checked = false;
                settingSToolStripMenuItem.Checked = true;
            }
        }
```


注意到 beginnerBToolStripMenuItem、intermediateIToolStripMenuItem、expertEToolStripMenuItem、settingSToolStripMenuItem 分别表示四个等级的菜单的名称，通过修改它们的 Checked 属性来达到修改对应项目前面勾的状态。我们还需要在初始化函数中调用这个函数：

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

            SelectLevel();
        }
```

这时候，我们运行就会发现Beginner菜单前面的勾被选中了：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第四节、菜单操作/mineSweeper_4_03.png" caption="菜单示意图" >}}

下面我们来处理一下各个菜单按钮的事件，我们只需要双击菜单上的按钮，程序会自动创建对应的单击事件，我们只需要在其中书写代码即可。我们首先来创建 Beginner、Intermediate、Expert、Exit、About 菜单项目对应的事件。我们先介绍 Beginner、Intermediate、Expert 菜单项目对应的代码：

```csharp
        private void beginnerBToolStripMenuItem_Click(object sender, EventArgs e)
        {
            nWidth = 10; nHeight = 10; nMineCnt = 10;
            SelectLevel();
        }
        
        private void intermediateIToolStripMenuItem_Click(object sender, EventArgs e)
        {
            nWidth = 16; nHeight = 16; nMineCnt = 40;
            SelectLevel();
        }
        
        private void expertEToolStripMenuItem_Click(object sender, EventArgs e)
        {
            nWidth = 30; nHeight = 16; nMineCnt = 99;
            SelectLevel();
        }
```

接下来，我们处理 Exit 事件，我们希望在退出游戏之前询问游戏者是否确认退出，代码如下：

```csharp
        private void exitXToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if(MessageBox.Show("Are you sure to exit the game?", "Exit", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                Application.Exit();
            }
        }
```

然后，我们来处理 About 事件，我们希望得到类似 Windows 默认关于窗口的界面。为此，首先我们需要引用一个类，在代码的开头部分加上下图高亮部分的代码：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModal;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
```

为了实现这样的功能，我们需要调用 Windows 系统内部的一个 API，添加这样一个函数：

```csharp
        /// <summary>
        /// 系统关于对话框（API）
        /// </summary>
        /// <param name="hWnd">窗口句柄</param>
        /// <param name="szApp">标题文本</param>
        /// <param name="szOtherStuff">内容文本</param>
        /// <param name="hIcon">图标句柄</param>
        /// <returns></returns>
        [DllImport("shell32.dll")]
        public extern static int ShellAbout(IntPtr hWnd, string szApp, string szOtherStuff, IntPtr hIcon);
```

在 About 事件中添加如下代码进行调用：

```csharp
        private void aboutAToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ShellAbout(this.Handle, "Minesweeper", "A minesweeper game using CSharp language.", this.Icon.Handle);
        }
```

运行以后查看结果如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第四节、菜单操作/mineSweeper_4_09.png" caption="关于" >}}

可能细心的读者会发现，虽然我们通过菜单修改了游戏等级，但是我们窗口中的雷区却没有发生变化，因为我们没有在菜单被按下的时候没有调用 UpdateSize 函数。在三个按钮的事件中添加对 UpdateSize 函数的调用即可。代码如下：

```csharp
        private void beginnerBToolStripMenuItem_Click(object sender, EventArgs e)
        {
            nWidth = 10; nHeight = 10; nMineCnt = 10;
            SelectLevel();
            UpdateSize();
        }
        
        private void intermediateIToolStripMenuItem_Click(object sender, EventArgs e)
        {
            nWidth = 16; nHeight = 16; nMineCnt = 40;
            SelectLevel();
            UpdateSize();
        }
        
        private void expertEToolStripMenuItem_Click(object sender, EventArgs e)
        {
            nWidth = 30; nHeight = 16; nMineCnt = 99;
            SelectLevel();
            UpdateSize();
        }
```

在此运行的时候，我们发现修改游戏等级的时候，游戏界面也会发生相应的变化。但是还有一点瑕疵，就是在大规模变成小规模的时候，边上会有多余的雷区。为了修正这个 Bug，我们需要将原来 Paint 事件中代码放在一个新的函数 PaintGame 中，同时添加高亮区域的代码，并且在 Paint 事件中进行调用，代码如下：

```csharp
        private void Form_Main_Paint(object sender, PaintEventArgs e)
        {
            PaintGame();
        }

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
                    g.FillRectangle(Brushes.SandyBrown, new Rectangle(nOffsetX + 34 * (i - 1) + 1, nOffsetY + 34 * (j - 1) + 1, 32, 32));   // 绘制雷区方块
                }
            }
        }
```

除此之外，在UpdateSize最后也需要调用PaintGame函数，如下图所示：

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
            PaintGame()
        }
```

再次运行的时候，就会发现边上多余的雷区已经消失了。

接下来我们处理 Mark 以及 Audio 两个事件，我们需要定义两个变量来记录它们的数据，因为这对于我们以后的开发有很大的关系。如下图所示：

```csharp
namespace Minesweeper
{
    public partial class Form_Main : Form
    {
        int nWidth;     // 表示雷区的宽度
        int nHeight;    // 表示雷区的高度
        int nMineCnt;   // 表示地雷的数目

        bool bMark;     // 表示是否使用标记
        bool bAudio;    // 表示是否使用音效
    }
}
```

同样我们需要在游戏开始的时候读取上次的数据，如果没有则都设置为真。我们首先看 Setting 文件：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第四节、菜单操作/mineSweeper_4_14.png" caption="Setting 文件配置" >}}

同时加入以下代码：

```csharp
        public Form_Main()
        {
            InitializeComponent();

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

同时为 Mark 以及 Audio 菜单项目添加如下的事件：

```csharp
        private void markMToolStripMenuItem_Click(object sender, EventArgs e)
        {
            markMToolStripMenuItem.Checked = bMark = !bMark;
        }

        private void audioMToolStripMenuItem_Click(object sender, EventArgs e)
        {
            audioMToolStripMenuItem.Checked = bAudio = !bAudio;
        }
```

至此，我们还剩 New Game、Setting、Rank 三个菜单选项的事件没有涉及，因为它们需用用到更多的内容，我们将会在下一节中进行讲解。
