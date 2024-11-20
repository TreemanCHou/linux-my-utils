echo "Installing My-Linux-Utils created by JackDann, Version: 0.0.0"

# 检测当前 shell 是否是 zsh
if [[ "$(readlink /proc/$$/exe)" == "/usr/bin/zsh" || "$(readlink /proc/$$/exe)" == "/bin/zsh" ]]; then
    echo "You are using zsh. Continuing ."
    
    echo "*** Step 1 : Installing oh-my-zsh ***"
    RUNZSH=no sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

    echo "*** Step 2 : Installing Zsh Plugins from github.com ***"
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-completions ~/.oh-my-zsh/custom/plugins/zsh-completions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting

    echo "*** Step 3 : Setting Conda-Adapted zsh themes ***"
    cp ./.zshrc-candidate ~/.zshrc
    cp ./zsh-themes/* ~/.oh-my-zsh/themes/

    echo "*** Step 4 : Other Script Settings . ***"
    mkdir ~/bin
    cp ./*.sh ~/bin
    cp ./.tmux.conf ~/ 
else
    echo "You are not using zsh."
    # 检测 zsh 是否安装
    if [[ -x "/usr/bin/zsh" || -x "/bin/zsh" ]]; then
        echo "zsh is installed. Attempting to switch your shell to zsh..."
        chsh -s "$(command -v zsh)"
        if [[ $? -eq 0 ]]; then
            echo "Successfully changed your shell to zsh. Please log out and log back in for the change to take effect."
            echo "*** Step 1 : Installing oh-my-zsh ***"
            sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

            echo "*** Step 2 : Installing Zsh Plugins from github.com ***"
            git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
            git clone https://github.com/zsh-users/zsh-completions ~/.oh-my-zsh/custom/plugins/zsh-completions
            git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting

            echo "*** Step 3 : Setting Conda-Adapted zsh themes ***"
            cp ./.zshrc-candidate ~/.zshrc
            cp ./zsh-themes/* ~/.oh-my-zsh/themes/

            echo "*** Step 4 : Other Script Settings . ***"
            mkdir ~/bin
            cp ./*.sh ~/bin
            cp ./.tmux.conf ~/ 
        else
            echo "Failed to change the default shell. Please run 'chsh -s $(command -v zsh)' manually with the correct permissions."
            exit 1
        fi
    else
        echo "zsh is not installed. Please install zsh using your package manager (e.g., 'sudo apt install zsh' on Debian-based systems)."
    fi
    exit 1
fi

exec zsh
