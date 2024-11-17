conda_info(){
    if [ -n "$CONDA_DEFAULT_ENV" ]; then
        echo -n "${CONDA_DEFAULT_ENV}"
    fi
}
local conda_info_str=' $(conda_info)'


PROMPT="
%{${fg_bold[blue]}%}[%{${fg[cyan]}%}%t%{${fg_bold[blue]}%} ]%{${fg_bold[blue]}%} [ %{${fg[cyan]}%}%n@%m:%~\$(git_prompt_info)%{${fg_bold[yellow]}%}${conda_info_str}%{${fg_bold[blue]}%} ]%{$reset_color%}
 $ "

# git theming
ZSH_THEME_GIT_PROMPT_PREFIX="%{${fg_bold[green]}%}("
ZSH_THEME_GIT_PROMPT_SUFFIX=")%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="✔"
ZSH_THEME_GIT_PROMPT_DIRTY="✗"
