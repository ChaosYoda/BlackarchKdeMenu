import subprocess
import sys

#list with applications that have a UI, format is "package,command"
#some packages do not match the command
execeptionList = ["armitage", "radare2-cutter,cutter", "zenmap"]
def getListOfTools()
    toolList = subprocess.run("pacman ")


def getToolsInGroup(group)
    # example comm -12 <(pacman -Qq | sort) <(pacman -Qqg blackarch-dos | sort)

    command = "comm -12 <(pacman -Qq | sort) <(pacman -Qqg " + group + "| sort)"



if __name__ == '__main__':
