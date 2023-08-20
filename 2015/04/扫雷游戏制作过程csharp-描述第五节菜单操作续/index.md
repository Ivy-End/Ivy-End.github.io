# 扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）


上一节中，我们还剩下 Setting 和 Rank 两个菜单项目没有设置事件，是因为它们都涉及到了弹出一个新的窗口。这一节，我们将主要介绍创建窗口的方法，以及窗口之间的数据通信。

首先，我们新建一个窗口，在右侧找到解决方案资源管理器，右击 Minesweeper 项目名，选择添加，如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_01.png" caption="菜单示意图" >}}

选择新建项，如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_02.png" caption="菜单示意图" >}}

在弹出的窗口中选择 Windows 窗体，并将名称修改为 Form_Setting.cs，单击确定，如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_03.png" caption="新建窗口示意图" >}}

将新建的窗口 Icon 属性修改为扫雷的图标，将 MaximizeBox 属性修改为 False，将 Name 属性修改为 Form_Setting，将 BackColor 属性修改为 White，将 Text 属性修改为 Minesweeper，将 FormBorderStyle 属性改为 FixedSingle。

在左边工具箱面板下公共控件中找到 Label 控件，双击添加到窗口中，将它的 Name 属性修改为 Label_Width，Text 属性修改为“Width:”，并移动到合适的位置，再在工具箱面板中找到 NumericUpDown 控件，双击添加到窗口中，将它的 Name 属性修改为 NumericUpDown_Width，Minimum 属性修改为 1，Maximun 属性修改为 30，（其中 Minimum 以及 Maximum 的属性表示为数字的变化范围。）TextAlign 属性修改为 Center。其中 Minimum以 及 Maximum 的属性表示为数字的变化范围。如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_04.png" caption="窗口示意图" >}}

重复上述操作，添加雷区高度（Height），地雷数目（Mine）的控件，其中高度的变化范围为 1 至 16，数目的变化范围为 1 至 99。如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_05.png" caption="窗口示意图" >}}

接下来我们需要添加两个按钮，用来确定修改以及取消修改。在左侧工具箱面板的公共控件中找到 Button 控件，双击添加到窗体中，将它的 Name 属性修改为 Button_OK，Text 属性修改为 OK。同时添加一个取消按钮（Cancel），如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_06.png" caption="窗口示意图" >}}

然后拖动窗口右下方的白点，调整窗口大小到合适的位置，如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_07.png" caption="窗口示意图" >}}

接下来我们用同样的方法和设置来创建一个排行榜的窗口（Form_Rank）。

放置三个标签，分别表示初级（Label_Beginner）、中级（Label_Intermediate）、高级（Label_Expert）的最高分，并且加入两个按钮，表示重新计分（Button_Reset）、确定（OK），如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_08.png" caption="窗口示意图" >}}

接下来，我们就可以调用这两个窗口了。打开 Form_Main 窗口，为 Setting 和 Rank 分别添加单击事件（双击菜单项，程序自动添加该时间），并且写下如下代码：

```csharp
        private void settingSToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form_Setting Setting = new Form_Setting();
            Setting.ShowDialog();
        }
        
        private void rankRToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form_Rank Rank = new Form_Rank();
            Rank.ShowDialog();
        }
```

这样，我们就完成了对窗口的调用。接下去，我们先来实现较为简单的 Rank 窗口。每次读取最高分的数据，这也就要求我们每次记录得分。

打开 Settings 文件，添加三种等级的最高分，并且将初始值都设置为 999，如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_10.png" caption="Setting 示意图" >}}

打开排名窗口，双击窗口标题栏，程序会自动添加一个 Load 事件，我们在这里添加如下代码：

```csharp
        private void Form_Rank_Load(object sender, EventArgs e)
        {
            // 读取数据
            int nBeginner = Propoerties.Settings.Default.Beginner;
            int nIntermediate = Propoerties.Settings.Default.Intermediate;
            int nExport = Propoerties.Settings.Default.Export;

            // 显示内容
            Label_Beginer.Text = String.Format("Beginner:        {0}", nBeginner);
            Label_Intermeidate.Text = String.Format("Intermediate:        {0}", nIntermediate);
            Label_Expert.Text = String.Format("Expert:        {0}", nExpert);
        }
```

这样，我们调试一下，就可以看到排名的效果了：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_12.png" caption="Rank 示意图" >}}

接下去我们需要为 Reset 以及 OK 按钮添加事件。首先考虑 OK 按钮，双击按钮，添加单击事件，并且添加如下代码：

```csharp
        private void Button_OK_Click(object sender, EventArgs e)
        {
            this.close();   // 关闭窗口，非退出程序
        }
```

对于 Reset 按钮，我们添加如下代码：

```csharp
        private void Button_Reset_Click(object sender, EventArgs e)
        {
            // 将所有记录设置为 999 即完成初始化
            Propoerties.Settings.Default.Beginner = 999;
            Propoerties.Settings.Default.Intermediate = 999;
            Propoerties.Settings.Default.Export = 999;
            Propoerties.Settings.Default.Save();    // 保存设置
        }
```

这样，我们就完成了排行榜的功能。接下来我们来考虑设置窗口的功能。我们首先为 Cancel 按钮添加如下代码：

```csharp
        private void Button_Cancel_Click(object sender, EventArgs e)
        {
            this.close();   // 关闭窗口，非退出程序
        }
```

我们考虑 OK 按钮，我们需要和 Form_Main 窗口进行通信，修改 Form_Setting 的构造函数，如图所示：

```csharp
        Form_Main Main;

        public Form_Setting(Form_Main _Main)
        {
            InitializeComponent();

            Main = _Main;   // 传递父窗口实例
        }
```

接着将 Form_Main 中 nWidth、nHeight、nMine 变量设置为公有类型：

```csharp
        public int nWidth;  // 表示雷区的宽度
        public int nHeight;  // 表示雷区的高度
        public int nMineCnt;  // 表示地雷的数量
```

然后修改对 Setting 窗口的调用函数：

```csharp
        private void settingSToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form_Setting Setting = new Form_Setting(this);  // 将本身作为参数传递过去
            Setting.ShowDialog();
        }
```

至此，我们就完成了 Setting 窗口和 Main 窗口的信息连接，双击 Setting 窗口的标题栏，修改它的 Load 事件如下，以实现对 Main 窗口中原有游戏参数的读取：

```csharp
        private void Form_Setting_Load(object sender, EventArgs e)
        {
            NumericUpDown_Width.Value = Convert.ToDecimal(Main.nWidth);
            NumericUpDown_Height.Value = Convert.ToDecimal(Main.nHeight);
            NumericUpDown_Mine.Value = Convert.ToDecimal(Main.nMineCnt);
        }
```

这样，我们运行的时候就可以看到 Setting 窗口自动获取了 Main 中的游戏参数：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_20.png" caption="Setting 窗口示意图" >}}

接下来我们为 OK 按钮添加如下的事件：

```csharp
        private void Button_OK_Click(object sender, EventArgs e)
        {
            Main.nWidth = Convert.ToDecimal(NumericUpDown_Width.Value);
            Main.nHeight = Convert.ToDecimal(NumericUpDown_Height.Value);
            Main.nMineCnt = Convert.ToDecimal(NumericUpDown_Mine.Value);
            this.Close();
        }
```

这样，我们就完成了游戏规模的设置，有时候，我们发现弹出来的设置窗口以及排行窗口显示的位置都偏左上角，我们对它进行一些调整，修改它们的 StartPosition 属性为 CenterParent。

最后，在调用完设置窗口后，还需要 UpdateSize 一下来实现对游戏规模的修改：

```csharp
        private void settingSToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form_Setting Setting = new Form_Setting(this);  // 将本身作为参数传递过去
            Setting.ShowDialog();
            UpdateSize();
        }
```

最终我们可以实现各种大小的雷区：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第五节、菜单操作（续）/mineSweeper_5_23.png" caption="运行效果" >}}

这一节暂且讲到这里，下一节我们将会介绍地雷数目以及时间秒数的显示，以及扫雷内部模型的建立。
