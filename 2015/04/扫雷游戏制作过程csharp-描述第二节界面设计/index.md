# 扫雷游戏制作过程（CSharp 描述）：第二节、界面设计


这一节我们主要介绍关于扫雷游戏界面的设计，此处我们借鉴经典扫雷界面的设计方法，首先需要创建一个菜单栏。具体方法在左边找到工具箱窗口，展开其中的菜单和工具栏，找到 MenuStrip 选项，如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第二节、界面设计/mineSweeper_2_01.png" caption="添加 MenuStrip" >}}

只需要双击该条目就可以在窗口中新建一个菜单栏，如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第二节、界面设计/mineSweeper_2_02.png" caption="MenuStrip 添加效果" >}}

对于这个控件（我们习惯上将窗口中的东西称作为控件），我们还是需要修改它的一些属性，对于个人习惯而言，我习惯于修改它的 Name 属性，这样编程的时候不至于将很多控件混淆。我们将它的 Name 属性修改为“MenuStrip_Main”。单击“请在此键入”，输入“Game(&G)”，其中 &G 整体会显示成 G 这个字母下面加一个下划线，这样在用户使用的时候就可以通过按下字母 G 来访问这个按键了。（当然，顶层菜单还需要按下 Alt 键，例如 Alt + G 键。）输入以后的界面如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第二节、界面设计/mineSweeper_2_03.png" caption="添加菜单项" >}}

使用同样的方法，创建如下图所示的一个菜单栏：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第二节、界面设计/mineSweeper_2_04.png" caption="菜单示意图" >}}

注意到，图中的分割线，只需要输入一个减号，即“-”，再按下回车键即可得到。

我们一次介绍一下各个选项的功能，以便读者对它们有一个基本的了解。菜单一共有两组，一个为游戏（Game），一个为帮助（Help）：其中游戏菜单下分别包含了新游戏（New Game）、初级（Beginner）、中级（Intermediate）、高级（Expert）、设置（Setting）、标记（Mark）、音效（Audio）、排行榜（Rank）、退出（Exit）；而帮助菜单下仅包含关于（About）。

其中新游戏用来开始一场新的游戏；初级、中级、高级，用于选择不同的游戏难度；设置用于自定义扫雷区域的大小以及地雷的数目；标记用于设置是否启用红旗、问号这一类的标记；音效用于设置是否启用音效；排行榜用于对游戏时间进行排名（仅记录初级、中级、高级的结果，对于自定义游戏的结果不进行记录）；退出用于退出游戏。最后，关于用来显示游戏的一些关于信息。

对于初级、中级、高级、标记、音效这几个菜单，我们需要在它的前面显示它的状态，即是否被选中，如果选中了就会在它的前面出现一个勾，如果没有选中，则没有，这是我们以后需要实现的功能，在此先进行说明。

至此，我们的菜单栏就制作完成了。接下来我们需要制作一个用来记录地雷数目以及用时的功能。我们选择工具箱中容器的 TableLayoutPanel，双击该项目，会在窗口中创建一个 TableLayoutPanel 控件。同样我们先将它的 Name 属性修改为“TableLayoutPanel_Main”。展开它的 Size 属性，将 Height 属性修改为 48。同时修改它的 Dock 属性，选择 Bottom，如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第二节、界面设计/mineSweeper_2_05.png" caption="TableLayoutPanel 属性设置" >}}

我们会发现它会自动吸附在底部，如果改成别的参数则会吸附在别的位置，这里我们设置为 Bottom。同时将 RowCount 属性设置为 1，ColumnCount 属性设置为 9。打开 Columns 属性对话框，按照下图进行修改：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第二节、界面设计/mineSweeper_2_06.png" caption="TableLayoutPanel 行列样式" >}}

这里进行一些解释，其中 Column1、Column3、Column5、Column7、Column9 为中心对称的，用来设置边距，不放置任何控件，纯粹为了排版需要。接下来我们需要在 Column2、Column8 中分别放置地雷（Mine_Show.png）以及秒表（Timer.png）的图标，表示剩余的地雷数目以及已用时长。而 Columns4、Columns6 中分别放置用于显示地雷数目以及已用时长的文本。下载地址：地雷、秒表。

在工具箱中展开公共控件，找到 PictureBox，将它拖动到 TableLayoutPanel 的第二个列中，同时将它的 Name 属性设置为“PictureBox_Mine”，Dock 属性设置为 Fill（表示充满整个页面，此处的页面即 TableLayoutPanel 中 Column2 全部），BackgroundImage 属性定位到Mine_Show.png文件（通过导入按钮），BackgroundImageLayout 属性设置为 Stretch（表示自动缩放图像大小）。使用同样的方法加入一个 PictureBox 控件，将它放到 Column8 中，同时将 Name 属性设置为“PictureBox_Timer”，BackgroundImage 属性定位到 Timer.png 文件，其余与 PictureBox_Mine 设置相同。其中图片导入的方法如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第二节、界面设计/mineSweeper_2_07.png" caption="TableLayoutPanel PixtureBox 资源设置" >}}

接下来我们需要添加两个用于显示内容的 Label 控件，展开工具箱中的公共控件，找到 Label 控件，分别拖动到 Column4 和 Column6，并且将 Dock 属性设置为 Fill，TextAlign 属性设置为 MiddleCenter（使文字显示在控件中心），Font 属性设置为“Consolas, 16.2pt”（即 Consolas 字体，字号三号）。其 Name 属性及 Text 属性分别修改为“Label_Mine”和“Label_Timer”。同时将它们的 ForeColor 属性分别设置为“DarkRed”和“HotTrack”（这项属性用于设置文字显示的颜色）。

至此界面已经基本完成了，但是我们还需要增加一个控件——Timer，用来计时。展开工具箱中的组件，双击 Timer。这个控件不会在界面上显示，但是会在后台进行计时功能。同样，我们将它的 Name 属性修改为“Timer_Main”，Interval 属性修改为“1000”（这里为计时间隔，以毫秒为单位，此处为 1000 毫秒，即 1 秒计时一次）。

最后按下 Ctrl + F5 进行编译查看结果，相较于第一节中的界面已经有了很大的改观，如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第二节、界面设计/mineSweeper_2_08.png" caption="运行效果" >}}

到这里或许读者会问，最为重要的扫雷区域怎么制作呢，关于这个区域，我们将会使用程序来生成，而不是使用控件。我们将会在下一节中进行讲解。
