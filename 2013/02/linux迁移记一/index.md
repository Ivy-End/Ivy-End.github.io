# Linux迁移记（一）


由于各种各样的原因，之前很多次向 Linux 迁移的计划未能实现。主要是因为有些程序只能在 Windows 上运行，比如我们最常用的 QQ。此次迁移的主要原因和以往大致相同：

* Windows 系列的系统臃肿而且不实用，很多东西华而不实。
* Windows 系列的系统及其程序属于商业行为，为了追求自由、共享和开源。

我选择的是 Ubuntu 12.04 LTS，主要还是看中了 LTS（Long Term Support），这样可以获取更长时间的技术支持。

安装过程就略过不提了。我采用的是 USB 安装，毕竟刻录光盘很奢侈。将移动硬盘分出一个 4GB 的分区，然后用 Universal USB Installer 写了启动引导，接下去的过程就很简单了，因为都是 GUI 界面，相对容易些。

装完系统就是折腾了，Linux 就是用来折腾的。下面慢慢介绍。

## 换上 Gnome3

由于 Ubuntu 自带的 Unity 界面非常不稳定，主要是个人不喜欢那种风格。所以毅然决然的换了 Gnome3。由于 Ubuntu 早已将其加入到了软件源中，所以直接 `apt-get` 就可以了。

```shell
sudo apt-get install gnome-shell
```

安装结束以后就可以使用了。可能是个人癖好吧，我还是把 Unity 删了，命令如下：

```shell
sudo apt-get --auto-remove purge unity
sudo apt-get --auto-remove purge unity-commonp
sudo apt-get --auto-remove purge unity-lens*
sudo apt-get --auto-remove purge unity-services
sudo apt-get --auto-remove purge unity-asset-pool
```

切记不可使用这条命令：

```shell
sudo apt-get --auto-remove purge unity*
```

因为把所有关于 Unity 的东西都删除以后会无法进入系统。这样就基本完成了桌面的更换，为了操作方便，我们还需安装一个软件来配置 Gnome3 桌面：

```shell
sudo apt-get install gnome-tweak-tool
```

## 软件整理

这个方面主要包括卸载一些不必要的软件以及安装一些必要的软件。卸载就不多说了，这是个智者见智，仁者见仁的事情。主要将一下软件安装。

浏览器使用谷歌的 Chromium，输入法也使用了谷歌的 `googlepinyin`。个人很喜欢谷歌，简洁而且功能强大。

接下去主要讲解一下在 Ubuntu 上使用 QQ 的方法——不用整天网页挂 WebQQ，不用 Wine。

众所周知，在 Linux 下有一款支持多种即时通讯账户的软件叫做——Pidgin，默认不支持 QQ，我们只需要安装一个插件就行了。

### Step 1：安装 Pidgin

```shell
sudo apt-get install pidgin
```

### Step 2：安装插件 pidgin-lwqq

```shell
sudo add-apt-repository ppa:lainme/pidgin-lwqq
sudo apt-get update
sudo apt-get install libpurple0 pidgin-lwqq
```

### Step 3：Enjoy it!

不得不说，Pidgin 真是解决了一个大难题，因为很多同学都在用 QQ，所以不用 QQ 也很难取得联系。有了这款软件就方便多了。接下来是下载软件，我选择了 `aria2`。一来是终端模式的，看起来舒服；二来支持断点续传；这两样加起来也足够了。而且速度也很快。安装方法：

```shell
sudo apt-get aria2
```

使用方法：

```shell
#一般使用
aria2c
#分段下载 为分段数目，取值介于1~5之间 aria2c -s
#断点续传 aria2c -c
#下载BitTorrent文件 aria2c -o
```

至于编程，已经做好放弃 VS 之类的准备了，转战 QT。主要方面应该是跨平台应用和网页开发吧。
