cd $1;

echo "\033[1;44;37mCURRENT PATH :\033[1;37m `(pwd)` \033[0m"

ls -al;


# echo "\033[31mTotal Files in this Folder: \033[32m`(ls -l|grep ^-|wc -l)`\033[0m"
# echo "\033[31mTotal Folders in this Folder: \033[32m`ls -l | grep "^d" | wc -l`\033[0m"

# 初始化文件和文件夹的计数器
file_count=0
dir_count=0

# 读取当前目录下的所有项
for item in *; do
  # 如果是文件，则增加文件计数器
  if [ -f "$item" ]; then
    let "file_count++"
  # 如果是文件夹，则增加文件夹计数器
  elif [ -d "$item" ]; then
    let "dir_count++"
  fi
done

# 输出结果
echo "\033[31mFiles in current Path:\033[32m $file_count"
echo "\033[31mFolders in current Path:\033[32m $dir_count\033[0m"
