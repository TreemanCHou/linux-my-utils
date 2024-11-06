# linux-my-utils

Some useful scripts used by myself on linux server. 

Current version: 0.0.0

## Introduction

This repository is inspired by a often occurring situation: Every time I change my working directory using `cd`, I have to type `ls` to check the files in the directory. So I write a script `cdl.sh` to combine `cd` and `ls` together.

After that, I write some other scripts to make my work more efficient. This repository includes the most useful (only for myself XD) scripts I have written. Hope it can help others too :)

## Environment

This section introduce the environment I use to develop and test these scripts. The scripts should work on other linux distributions, but I can't guarantee that.

Basic information:

- OS: Ubuntu 20.04
- Shell: zsh
- Editor: vim

Other information:

- python: 3.9.7 (with conda 22.9.0)

## Installation

To use these scripts, clone this repository to your local machine:

```bash
git clone
cd linux-my-utils
current_path=$(pwd)
echo -e 'alias cdl="source $current_path/cdl.sh"\nalias its="sh $current_path/its.sh"\nalias upload="sh $current_path/upload.sh"\nalias download="sh $current_path/download.sh"\nalias lc="sh $current_path/count.sh"\n# alias unzip="uz"\n\n# Some kuaijiefangshi\nalias zshrc="vim ~/.zshrc"\nalias bashrc="vim ~/.bashrc"\nalias condarc="vim ~/.condarc"\nalias vimrc="vim ~/.vimrc"\nalias cls="clear"' >> ~/.zshrc
```

## Features

### cdl

This script is used to combine `cd` and `ls` together. It will change the working directory and list the files in the directory at the same time.

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

This script is used to count the number of files and folders in the current directory. This function is also included in `cdl.sh`. For those folders with too many files, it's better to use this script to count the number of files and folders.

```bash
user@server:/home/user $ lc

drwxr-xr-x  3 user user  180 Nov  5 21:31 .
drwxr-xr-x  3 user user  180 Nov  5 21:31 ..
drwxr-xr-x  3 user user  180 Nov  5 21:31 test.txt
drwxr-xr-x  3 user user  180 Nov  5 21:31 test2.txt
drwxr-xr-x  3 user user  180 Nov  5 21:31 test3.txt
Files in current Path: 3
Folders in current Path: 2
```

### its

This script only repeats your feeling.
    
```bash
user@server:/home/user $ its cool!
Yep, it's cool!
```

### Other aliases

To make you modify the configuration files more easily, I also provide some aliases to open the configuration files using `vim`.

```bash
user@server:/home/user $ zshrc
user@server:/home/user $ bashrc
user@server:/home/user $ condarc
```

Those aliases are used to open the configuration files of `zsh`, `bash`, and `conda`.

For those who want to clear the terminal, but still used to type `cls` in windows, I also provide an alias `cls` to clear the terminal. XD

```bash
user@server:/home/user $ cls
```

## Contact

If you have any questions or suggestions, please feel free to contact me or put an issue in this repository. I will reply as soon as possible.

mailbox: llm410402@gmail.com