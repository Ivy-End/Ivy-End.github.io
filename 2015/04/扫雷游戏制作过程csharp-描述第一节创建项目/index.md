# 扫雷游戏制作过程（CSharp 描述）：第一节、创建项目


这一系列的文章主要受许宏旭的启发而来。他目前在连载更新一篇使用 C# 制作五子棋的教程。选择这一项目的主要原因是 Windows 8.1 系统上的扫雷需要前往应用商店下载，显得有些麻烦。因此想自己制作一个。主要采用 C# 语言进行实现。主要功能与原来的扫雷游戏基本相同，进行修改的地方主要是扫雷区的界面。如有不恰当的地方，还望指正。

该项目现已根据文章进度托管在[GitHub](https://github.com/Ivy-End/Minesweeper)上，读者可以自行查看。

玩过扫雷的读者应该知道，扫雷需要用到三种图片素材——地雷、红旗、问号。当右击一个方块的时候，会插上红旗，表示游戏者认为该方块内有地雷；再次右击该方块，会变成问号，表示不确定该方块内是否有地雷；第三次右击该方块，问号消失，恢复到初始的状态。我们前往[Iconfinder](https://www.iconfinder.com)寻找合适的图标，并且通过 Photoshop 或者 Illustrator 的处理得到我们所需要的图标。文章中含有下载地址的图标资源可以使用右键—目标另存为进行下载。

通过一定的搜索以及图片的处理，我们得到了下面一组素材图标。

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_01.png" caption="Mine Sweeper 素材" >}}

除了这些素材以外，我们还需要找一个图标，使得整个程序看上去更加正式一点，这里使用图标如下，注意程序图标的后缀为ico。

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_02.png" caption="Mine Sweeper 图标" >}}

接下来，我们打开Visual Studio 2013开始创建工程，界面如下：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_03.png" caption="Visual Studio 2013" >}}

依次展开文件—新建—项目，选择“Visual C#”中的“Windows 窗体应用程序”，项目名称填写为“Minesweeper”，单击确定创建项目。如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_04.png" caption="创建项目" >}}

创建好的项目如下图所示。

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_05.png" caption="项目创建完毕" >}}

我们需要对这个窗口的几项属性进行修改，首先通过 Text 属性将它的标题修改为“Minesweeper”；通过FormBorderStyle属性将它的大小设置为“FixedSingle”，即为不可调节窗口大小；通过 MaximizeBox 属性将它的最大化按钮设置为“False”，即最大化按钮失效；通过 Name 属性将它的名称修改为“Form_Main”，修改这个属性主要用于后面书写代码的方便；通过 BackColor 属性将它的背景修改为“White”。如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_06.png" caption="属性修改" >}}

我们可以顺便修改一下这个窗口的代码文件的名称。在右上方找到解决方案资源管理器，右击Form_1.cs—重命名—Form_Main.cs，程序会自动将下面包含的文件名也都改成一致的名称。如图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_07.png" caption="文件名修改" >}}

接下来我们需要修改一下程序的图标，将刚才下载的 favicon 文件放到 Minesweeper/Minesweeper 文件夹下，同时将三个图标资源放到 Minesweeper/Minesweeper/Resources 文件夹下（Resources 文件夹需要自己新建），如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_08.png" caption="创建 Resources 文件夹" >}}

在属性栏中找到 Icon 属性，并且定位到 favicon.ico 文件，如下图所示：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_09.png" caption="设置 Icon" >}}

此时，我们按下快捷键 Ctrl + S 对整个工程进行保存，并且按下快捷键 Ctrl + F5 运行查看我们的程序，效果如下：

{{< image src="/images/2015/扫雷游戏制作过程（CSharp 描述）：第一节、创建项目/mineSweeper_1_10.png" caption="运行结果" >}}

到目前为止，我们的程序只是一个空白的界面，下一节中我们将介绍程序的界面布局的设计。
