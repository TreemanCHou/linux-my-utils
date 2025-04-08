# Analyze audit log. Written by JackDann.
# Version 0.1

# Example audit log:
# ----
# time->Wed Apr  2 14:48:48 2025
# type=PROCTITLE msg=audit(1743576528.904:249): proctitle=2F7573722F62696E2F6E76696469612D6D6F6470726F6265002D73002D663D2F70726F632F6472697665722F6E76696469612F6361706162696C69746965732F6D69672F636F6E666967
# type=PATH msg=audit(1743576528.904:249): item=1 name="/lib64/ld-linux-x86-64.so.2" inode=3541397 dev=fd:00 mode=0100755 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
# type=PATH msg=audit(1743576528.904:249): item=0 name="/usr/bin/nvidia-modprobe" inode=3539640 dev=fd:00 mode=0104755 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
# type=CWD msg=audit(1743576528.904:249): cwd="/data3/private/lb2024/sparsify"
# type=EXECVE msg=audit(1743576528.904:249): argc=3 a0="/usr/bin/nvidia-modprobe" a1="-s" a2="-f=/proc/driver/nvidia/capabilities/mig/config"
# type=SYSCALL msg=audit(1743576528.904:249): arch=c000003e syscall=59 success=yes exit=0 a0=7fb8f3bab490 a1=7fff65f6fea0 a2=7fff65f6ff48 a3=28 items=2 ppid=2842520 pid=2912632 auid=1015 uid=1015 gid=1015 euid=0 suid=0 fsuid=0 egid=1015 sgid=1015 fsgid=1015 tty=pts227 ses=1896 comm="nvidia-modprobe" exe="/usr/bin/nvidia-modprobe" subj=unconfined key="user_commands"
# ----
# time->Wed Apr  2 14:48:48 2025
# type=PROCTITLE msg=audit(1743576528.908:250): proctitle=2F7573722F62696E2F6E76696469612D6D6F6470726F6265002D73002D663D2F70726F632F6472697665722F6E76696469612F6361706162696C69746965732F6D69672F6D6F6E69746F72
# type=PATH msg=audit(1743576528.908:250): item=1 name="/lib64/ld-linux-x86-64.so.2" inode=3541397 dev=fd:00 mode=0100755 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
# type=PATH msg=audit(1743576528.908:250): item=0 name="/usr/bin/nvidia-modprobe" inode=3539640 dev=fd:00 mode=0104755 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
# type=CWD msg=audit(1743576528.908:250): cwd="/data3/private/lb2024/sparsify"
# type=EXECVE msg=audit(1743576528.908:250): argc=3 a0="/usr/bin/nvidia-modprobe" a1="-s" a2="-f=/proc/driver/nvidia/capabilities/mig/monitor"
# type=SYSCALL msg=audit(1743576528.908:250): arch=c000003e syscall=59 success=yes exit=0 a0=7fb8f3bab490 a1=7fff65f6fea0 a2=7fff65f6ff48 a3=28 items=2 ppid=2842520 pid=2912633 auid=1015 uid=1015 gid=1015 euid=0 suid=0 fsuid=0 egid=1015 sgid=1015 fsgid=1015 tty=pts227 ses=1896 comm="nvidia-modprobe" exe="/usr/bin/nvidia-modprobe" subj=unconfined key="user_commands"
# ----

# Example output:
# ---- Apr 2 14:48:48 2025 lb2024(1015) ----
# workdir: /data3/private/lb2024/sparsify
# command: /usr/bin/nvidia-modprobe -s -f=/proc/driver/nvidia/capabilities/mig/config
# pid    : 2912632 ppid: 2842520 status: success
import pwd
import sys
import re
import os
import time
import psutil


import argparse

args = argparse.ArgumentParser(description="Analyze audit log.")
args.add_argument("-ts", "--timestart", type=str, default="week-ago", help="Time start. An example date using the en_US.utf8 locale is 09/03/2009. An example of time is 18:00:00.")
args.add_argument("-te", "--timeend", type=str, default="now", help="Time end. An example date using the en_US.utf8 locale is 09/03/2009. An example of time is 18:00:00.")
args.add_argument("-c", "--cache", type=str, default="/data3/private/llm2022/audit.log", help="Cache file name.\nThis Program will create a file named audit.log in a directory. This file might be very large. So please make sure you have enough space.")
args.add_argument("-n", "--not-all", action="store_true", help="Not show all logs.\nBy default, this program will show all logs including subprocesses, but most of them may not be valuable. If you want to show only the logs whose parent process is a shell (That means a user executed it straightly), please use this option.")
args.add_argument("--no-color", action="store_true", help="Not print colorful.\nFor default, this program will print colorful logs. If you want to disable it, please use this option. This might be useful when you want to redirect the output to a file.")
args.add_argument("--no-myself", action="store_true", help="Do not show your own logs, Only show other users' logs.\n ")
args = args.parse_args()

NO_COLOR = args.no_color
NO_MYSELF = args.no_myself

def get_process_name(pid):
    """
    Get the process name by pid.
    """
    try:
        process = psutil.Process(pid)
        return process.name()
    except psutil.NoSuchProcess:
        return None

def is_bash(ppid):
    # To check if the parent process is a shell (bash, zsh, sh)
    try:
        name = get_process_name(ppid)
        if name:
            if name in ("bash", "zsh", "sh"):
                return name
            else:
                return False
        else:
            return False 
    except psutil.NoSuchProcess:
        return False



def color_print(text, color):
    """
    Print text in the specified color.
    """
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m',
        'gray': '\033[90m',
        'bold_white': '\033[1;37m',
        'bold_red': '\033[1;31m',
        'bold_green': '\033[1;32m',
        'bold_yellow': '\033[1;33m',
        'bold_blue': '\033[1;34m',
        'bold_magenta': '\033[1;35m',
        'bold_cyan': '\033[1;36m',
        'bold_gray': '\033[1;90m',
        'bold_black': '\033[1;30m',
    }
    if NO_COLOR:
        return text
    return f"{colors[color]}{text}{colors['reset']}" if color in colors else text

class logitem:
    """
    Class to store log items.
    """
    def __init__(self, itemtxt):
        self._origin_text = itemtxt
        self._time = self._get_time(itemtxt)
        self._username = self._get_username(itemtxt)
        self._command = self._get_command(itemtxt)
        self._status = self._get_status(itemtxt)

        pid_ppid_line = itemtxt.split('type=SYSCALL')[1].split('\n')[0]
        self._pid = self._get_pid(pid_ppid_line)
        self._ppid = self._get_ppid(pid_ppid_line)
        self._workdir = self._get_workdir(itemtxt)
        self.is_myself = False
        if NO_MYSELF:
            # get the username
            my_username = pwd.getpwuid(os.getuid()).pw_name
            if my_username == self._username:
                # if the username is the same as the current user, skip this log
                self.is_myself = True
                # By default, the log is shown. Only when the --no-myself option is used, the log is not shown.

        try:
            self._is_parent_bash = is_bash(int(self._ppid))
        except ValueError:
            print(color_print('ERROR: CANNOT GET PARENT', 'red'))
            print(itemtxt)
            print(self._get_ppid(itemtxt))
            print(self._ppid)
            print(self._pid)
            print(self._get_pid(itemtxt))
            exit()

    def _get_time(self, itemtxt):
        """
        Extract time from the log item.
        """
        time_str = itemtxt.split('time->')[1].split('\n')[0]
        return time_str
    
    def _get_username(self, itemtxt):
        """
        Extract username from the log item.
        """
        auid = itemtxt.split('auid=')[1].split(' ')[0]
        # get username using getpwuid
        username = auid

        try:
            username = pwd.getpwuid(int(username)).pw_name
        except KeyError:
            username = f"unknown({username})"
        return username
    
    def _get_command(self, itemtxt):
        """
        Extract command from the log item.
        """
        command = itemtxt.split('a0=')[1].split(' ')[0]
        # command = command.replace('"', '')
        try:
            argline = itemtxt.split('argc=')[1].split('\n')[0]
            argnum = int(itemtxt.split('argc=')[1].split(' ')[0])
            args = []
            for i in range(argnum):
                regex = f'a{i}'
                arg = re.search(f'{regex}=[\"\'][^ ]+[\"\']', argline)
                if arg:
                    arg = arg.group(0)
                    arg = arg.split('=')[1]
                    args.append(arg)
            args = args[1:]
        except IndexError:
            # No argc
            argline = itemtxt
            command = argline.split('exe=')[1].split(' ')[0]
            args = []
        return command + ' ' + ' '.join(args)

    def _get_status(self, itemtxt):
        """
        Get the state of the log item.
        """
        exit_code = self._origin_text.split('exit=')[1].split(' ')[0]
        status = "success(0)" if exit_code == "0" else f"failed({exit_code})"
        if status == "success(0)":
            status = color_print(status, 'green')
        else:
            status = color_print(status, 'red')
    
    def _get_pid(self, itemtxt):
        """
        Get the pid of the log item.
        """
        pid = itemtxt.split('pid=')[1].split(' ')[0]
        return pid
    
    def _get_ppid(self, itemtxt):
        """
        Get the ppid of the log item.
        """
        # print('=========================')
        devided = itemtxt.split('ppid=')[1]
        if devided.startswith(','):
            devided = itemtxt.split('ppid=')[2]
        ppid = devided.split(' ')[0].split(',')[0]
        return ppid
    
    def _get_workdir(self, itemtxt):
        """
        Get the workdir of the log item.
        """
        try:
            workdir = itemtxt.split('cwd=')[1].split(' ')[0].split('\n')[0]
        except IndexError:
            workdir = ""
        return workdir
    
    def level(self):
        """
        Get the level of the log item.
        """
        if self._is_parent_bash:
            return 1
        else:
            return 0

    def __str__(self):
        if self._is_parent_bash and self._command != '"sleep" "180"':
            # Theoretically, I want to show the process whose parent is shell
            # because that means the process is started by user.
            # However, although I try to get the parent process name, and when it is shell, return true,
            # but ... When I set this judgement to "if not self._is_parent_bash", it works. QWQ
            line1 = f"---- {color_print(self._time, 'bold_yellow')} {color_print(self._username, 'green')} ----"
            line2 = f"{color_print('workdir:', 'bold_cyan')} {self._workdir}\t{color_print('father:', 'bold_cyan')} {color_print(get_process_name(int(self._ppid)), 'blue')}"
            line3 = f"{color_print('command:', 'bold_cyan')} {self._command}"
            line4 = f"{color_print('pid:', 'bold_cyan')} {self._pid} {color_print('ppid:', 'bold_cyan')} {self._ppid} {color_print('status:', 'bold_cyan')} {self._status}"
            return f"{line1}\n{line2}\n{line3}\n{line4}"
        else:
            # all info print by gray, only ppid in blue.
            # and show the parent process name
            # Example format:
            # ---- Apr 2 14:48:48 2025 lb2024(1015) ----
            # subprocess: /usr/bin/nvidia-modprobe father: /bin/python 
            # ppid: 2842520  pid: 2912632 status: success
            line1 = f"{color_print('---- ' + self._time, 'gray')} {color_print(self._username + ' ----', 'gray')}"
            line2 = f"{color_print('subprocess:', 'gray')} {color_print(self._command, 'gray')} {color_print('father:', 'gray')} {color_print(get_process_name(int(self._ppid)), 'blue')}"
            line3 = f"{color_print('ppid:', 'gray')} {color_print(self._ppid, 'gray')} {color_print('pid:', 'gray')} {color_print(self._pid, 'gray')} {color_print('status:', 'gray')} {self._status}"
            return f"{line1}\n{line2}\n{line3}"
        


if __name__ == "__main__":

    # print(pwd.getpwuid(1015).pw_name)
    # audit log from command "sudo ausearch -k user_commands"
    command = "sudo ausearch -k user_commands -ts " + args.timestart + " -te " + args.timeend
    print('[INFO] Executing Command: ' + command)
    print('[INFO] Extracting audit log ...')
    # if len(sys.argv) > 1:
    #     command = sys.argv[1]
    # # print(command)
    # run command and get output
    log_tmp_file = '/data3/private/llm2022/audit.log'

    os.system(command + " > " + log_tmp_file)
    with open(log_tmp_file, "r") as f:
        auditlog = f.read()
    # split log by ----
    print('[INFO] Log extracted. Analyzing ...')
    logs = []
    for item in auditlog.split("----"):
        if len(item) > 0:
            t = logitem(item)
            if t.is_myself:
                continue
            logs.append(t)

    # print logs
    for item in logs:
        if args.not_all:
            if item.level() == 0:
                continue
        print(item)
        print()
    # clean log file
    os.system("rm " + log_tmp_file)
