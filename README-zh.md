# linux-my-utils

一些我在 Linux 服务器上使用的实用脚本。
[简体中文](./README.md) | [English](./README-en.md)

当前版本：0.0.0


## 💁‍♂️ 介绍

这个仓库的灵感来源于一个常见的场景：每次我使用 `cd` 切换工作目录时，都得输入 `ls` 来查看目录中的文件，十分麻烦。所以我写了一个脚本 `cdl.sh`，将 `cd` 和 `ls` 结合起来。

除此之外，我还写了一些其他的脚本来提高工作效率。这个仓库包含了我写的最有用的（仅对我有用 XD）脚本。希望它也能帮助到别人 :)

## 💻️ 环境

这里介绍我用来开发和测试这些脚本的环境。这些脚本应该在其他 Linux 发行版上也能运行，但我无法保证。

基本信息：

- 操作系统：Ubuntu 20.04
- Shell：zsh
- 编辑器：vim

其他信息：

- python：3.9.7（配合 conda 22.9.0）

## ⬇️ 安装

要使用这些脚本，可以将该仓库克隆到本地机器：

```bash
git clone https://github.com/TreemanCHou/linux-my-utils.git
cd linux-my-utils
current_path=$(pwd)
echo -e 'alias cdl="source $current_path/cdl.sh"\nalias its="sh $current_path/its.sh"\nalias upload="sh $current_path/upload.sh"\nalias download="sh $current_path/download.sh"\nalias lc="sh $current_path/count.sh"\n# alias unzip="uz"\n\n# 一些快捷方式\nalias zshrc="vim ~/.zshrc"\nalias bashrc="vim ~/.bashrc"\nalias condarc="vim ~/.condarc"\nalias vimrc="vim ~/.vimrc"\nalias cls="clear"' >> ~/.zshrc
```
## 💡 功能

### cdl

这个脚本用于将 cd 和 ls 合并在一起。它将更改工作目录，并同时列出该目录中的文件。

```bash
user@server:/home/user $ cdl <directory>
CURRENT PATH : /home/user/<directory>
total 36
drwxr-xr-x  3 user user  180 Nov  5 21:31 .
drwxr-xr-x  3 user user  180 Nov  5 21:31 ..
Files in current Path: 0
Folders in current Path: 0
user@server:/home/user/<directory> $
```

### lc
这个脚本用于统计当前目录中的文件和文件夹数量。这个功能也包含在 cdl.sh 中。对于那些包含过多文件的文件夹，使用这个脚本来统计文件和文件夹的数量。

```bash
user@server:/home/user $ lc

drwxr-xr-x  3 user user  180 Nov  5 21:31 .
drwxr-xr-x  3 user user  180 Nov  5 21:31 ..
drwxr-xr-x  3 user user  180 Nov  5 21:31 test.txt
drwxr-xr-x  3 user user  180 Nov  5 21:31 test2.txt
drwxr-xr-x  3 user user  180 Nov  5 21:31 test3.txt
Files in current Path: 3
Folders in current Path: 0
```

### its
复读你的感叹词。

```bash
user@server:/home/user $ its cool!
Yep, it's cool!
```

### 其他 aliases

为了更容易修改配置文件，我还提供了一些别名，可以使用 vim 打开配置文件。

```bash
user@server:/home/user $ zshrc
user@server:/home/user $ bashrc
user@server:/home/user $ condarc
```

这些别名用于打开 `zsh`、`bash` 和 `conda` 的配置文件。

对于那些想清空终端，但仍然习惯在 Windows 中输入 `cls` 的用户，我还提供了一个 `cls` 别名来清空终端。XD


```bash
user@server:/home/user $ cls
```

## ✉️ 联系方式

如果你有任何问题或建议，请随时与我联系，或在该仓库中提交问题。我会尽快回复。

邮箱：llm410402@gmail.com
