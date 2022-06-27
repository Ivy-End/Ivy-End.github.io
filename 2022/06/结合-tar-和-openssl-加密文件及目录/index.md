# 结合 TAR 和 OpenSSL 加密文件及目录


当需要在网络上传递敏感数据时，通常需要对文件和目录进行加密，而普通的加密方法又非常容易被破解。为了应对这一难题，我们可以采用 RedHat 系统中的 TAR 打包工具和 OpenSSL 实现数据的加密。

## 加密

```shell
# 1. 切换到需要进行加密的文件目录下
[user@Server ~]$ cd <Directory to be encrypted>
# 2. 使用下列语句对文件目录进行加密
#      enc     表示使用加密进行编码
#      -e      表示使用加密选项
#      -aes256 表示使用 aes256 加密算法
#      -out    表示加密输出的文件
[user@Server ~]$ tar -czf - * | openssl enc -e -aes256 -out File.tar.gz
# 3. 输入秘钥
enter aes-256-cbc encryption password:
Verifying -enter aes-256-cbc-encryption password:
```

## 解密

```shell
# 1. 使用下列语句对加密文件进行解密
#      enc     表示使用加密进行编码
#      -e      表示使用加密选项
#      -aes256 表示使用 aes256 加密算法
#      -out    表示加密输出的文件
[user@Server ~]$ openssl enc -d -aes256 -in <Filename> | tar -xzv
# 3. 输入秘钥
enter aes-256-cbc encryption password:
```

