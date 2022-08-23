# Linux 配置 GitHub 账号


## Step 1 生成 SSH 私钥/公钥

打开终端，使用 ssh-keygen 工具生成 SSH 私钥（[GitHub 推荐方法](https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)）：

```shell
[kwang@Slave02 ~]$ ssh-keygen -t ecdsa -b 521 -C "prc.wkai@gmail.com"
Generating public/private ecdsa key pair.
Enter file in which to save the key (/home/kwang/.ssh/id_ecdsa): /home/kwang/.ssh/id_ecdsa
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/kwang/.ssh/id_ecdsa.
Your public key has been saved in /home/kwang/.ssh/id_ecdsa.pub.
The key fingerprint is:
14:21:b7:06:4c:e4:cd:39:c8:1f:bd:09:64:42:80:3b prc.wkai@gmail.com
The key's randomart image is:
+--[ECDSA  521]---+
|   ..*B *.       |
|  .  o.@ =       |
|   .  + @ .      |
|  E    + + o     |
|   .    S o      |
|                 |
|                 |
|                 |
|                 |
+-----------------+
```

## Step 2 配置 SSH 公钥

登录 GitHub 主页，在个人设置中选择“SSH and GPG keys”，单击“New SSH key”，将上一步中生成的公钥（id_ecdsa.pub）复制进来（下图）。

{{< image src="/images/2022/Linux 配置 GitHub 账号/GitHub 配置 SSH 公钥.png" caption="GitHub 配置 SSH 公钥" >}}

## Step 3 克隆 Repo

在服务器终端运行 git 配置账号和对应的 repo：

```shell
[kwang@Slave02 ~]$ git clone "git@github.com:Ivy-End/Prometheus.git"
Cloning into 'Prometheus'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), 12.50 KiB | 0 bytes/s, done.
Checking connectivity... done.
```

## Step 4 配置 Git 用户

```shell
[kwang@Slave02 ~/Prometheus]$ git config --global user.name "Ivy-End"
[kwang@Slave02 ~/Prometheus]$ git config --global user.email "prc.wkai@gmail.com"
```

## Step 5 上传文件

```shell
[kwang@Slave02 ~/Prometheus]$ git add *
[kwang@Slave02 ~/Prometheus]$ git commit -m 'Prometheus Project Initialization'
[main 544218b] Prometheus Project Initialization
1 file changed, 2 insertions(+), 1 deletion(-)
[kwang@Slave02 ~/Prometheus]$ git push
Counting objects: 3, done.
Delta compression using up to 192 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 405 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:Ivy-End/Prometheus.git
  2ed25ef..544218b  main -> main
```

## Step 6 下传文件

```shell
[kwang@Slave02 ~/Prometheus]$ git pull
Already up-to-date.
```
