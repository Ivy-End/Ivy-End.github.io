# 2048 游戏制作过程（Java 描述）：第一节、创建项目


自从关于扫雷游戏制作过程的文章发布后，有同学让我写一些关于移动开发的文章，并且建议以雷电这款游戏为例。然而考虑到该项目对于初学者来说代码量较大，所以暂且不涉及这部分，转而使用较为简单的 2048 游戏作为例子，可能对于初学者来说更容易上手，并且也更容易自己动手实现出来。

本项目已根据文章进度托管在 GitHub 上：[2048](https://github.com/Ivy-End/2048)，读者可以自行查看。

由于没有 Mac，因此只能介绍关于 Android 平台相关的开发知识。然而进行 Android 开发之前，需要搭建 Android 开发环境，这一步比较有难度的，主要是各个软件的配置较为麻烦，使得很多初学者望而却步。目前主流的 IDE 有 Eclipse 以及 Android Studio，本文将以 Android Studio 作为集成开发环境，对 2048 游戏的开发过程进行详细的介绍。

然而 Android Studio 的配置并不如 Visual Studio 一样简单，下面将简单介绍一下 Android Studio 集成开发环境的部署，具体的细节步骤读者可以查阅相关资料。

1. 安装 JDK，根据自己的操作系统选择合适的 JDK 版本，我们常用的是 Windows x64 版本；
2. 安装 Andorid Studio；
3. 启动 Android Studio，配置 Gradle，该部分较为繁琐，需要自行下载对应版本的 Gradle 包，读者可以参考相关资料；
4. （可选）安装 Genymotion，也可以使用 Android Studio 默认的模拟器，但是速度较慢。

至此，假设读者已经配置完成了 Android 开发环境并且能够正常运行了。接下来，我们进行 2048 游戏项目的创建。首先打开 Android Studio，弹出如下图所示的界面：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_01.png" caption="Android Studio" >}}

单击 Start a new Android Studio project 创建一个新的 Android Studio 项目，弹出如下界面：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_02.png" caption="Android Studio 创建项目" >}}

这里需要填写三个内容：

* Application name，项目名称，这里我们填写"Game2048"；
* Company Domain，开发者信息，常小数点分割每一个部分，读者可以修改这部分的内容为自己的信息；
* Project location，项目地址，选择一个用以保存项目文件的位置。

单击 Next，进入下一步：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_03.png" caption="Android Studio 创建项目" >}}

这里需要我们选择该项目的使用平台，我们选择默认的 Phone and Tablet，其中的 Minimum SDK 表示所兼容的最低 API 版本，我们保持默认。单击 Next，进入下一步：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_04.png" caption="Android Studio 创建项目" >}}

接下来需要选择应用的初始界面，由于我们的界面需要自己开发，所以这里不需要进行修改，直接默认即可。单击 Next，进入下一步：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_05.png" caption="Android Studio 创建项目" >}}

这里需要我们对上一步默认选择的 Activity 进行一些属性的填写，保持默认，单击 Finish，完成项目的创建，稍作等待后，项目已经新建完成：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_06.png" caption="Android Studio 项目创建完毕" >}}

我们首先打开 Genymotion，界面如下：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_07.png" caption="Genymotion" >}}

单击 Start 按钮，启动 Android 模拟器，界面如下：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_08.png" caption="Genymotion Android 模拟器" >}}

若一开始打开时显示为横屏模式，只需要单击右侧的旋转屏幕按钮即可切换到竖屏模式。

接下来，我们切换到 Android Studio 中，选择 Run 菜单项中的 Run 'app'，也可以直接按工具栏中的快捷按钮，弹出如下的对话框：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_09.png" caption="运行 Android App" >}}

如果我们的 Genymotion 模拟器打开的话，Android Studio 会自动选择它作为默认的调试设备，这里我们直接单击 OK 即可，接着解锁模拟器中的 Android 系统，稍作等待，可以看到运行的 Android 应用：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_10.png" caption="运行 Android App" >}}

接下来，我们需要将它的标题栏去掉。切换到 Android Studio 界面，双击打开左侧的 app/manifests 文件夹下的 AndroidManifests.xml 文件，修改高亮行代码如下图所示：

```xml
<?xml version="1.0" encoding="utf-8">
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.ivy.end.game2048" >

    <application
        android:allowBackup="true"
        android:icon="@drawable/ic_launcher"
        android:label="Game2048"
        android:theme="@style/Theme.Appcompat.Light.NoActionBar" >
        <activity
            android:name=".MainActivity"
            android:label="Game2048">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android:intent:category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

接下来找到左侧的 app/res/menu 文件夹下的 menu_main.xml，右击 Delete 将其删除，在弹出的对话框中勾选 Safe delete (with usage search) 以及 Search  in comments and strings 这两个复选框，如下图所示：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_12.png" caption="删除文件" >}}

程序显示找到了引用项目，因为我们在主界面中调用了这个菜单，否则不会显示这个菜单。我们单击 Delete Anyway：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_13.png" caption="删除文件" >}}

接下来，双击打开 app/java/com.ivy.end.game2048 文件夹（并非 com.ivy.end.game2048(androidTest)）下的 MainActiviy 文件，将其中多余的代码（即刚才检测到调用了菜单的部分）全部删除，最终结果如下图所示：

```java
package com.ivy.end.game2048;

import ...

public class MainActivity extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
```

此时，再次运行程序，即可看到这样的效果：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第一节、创建项目/game2048_1_15.png" caption="运行效果" >}}

下一节将介绍修改 App 的应用图标以及名称，并且进行最基本的界面布局。
