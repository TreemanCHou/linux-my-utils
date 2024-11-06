ls -l $1
echo "\033[31mTotal Files in this Folder: \033[32m`(ls -l $1|grep ^-|wc -l)`\033[0m"
echo "\033[31mTotal Folders in this Folder: \033[32m`ls -l $1| grep "^d" | wc -l`\033[0m"
