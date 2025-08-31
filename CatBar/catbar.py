import os #标准库模块 “Operating System”，即「操作系统模块」（和电脑系统有关的事）
def progress_bar(n=10):
    for i in range(1, n + 1):
        input("Press Enter to continue...")
        os.system("cls")#在 Windows 上清除终端屏幕
        #也可以写成这样：os.system("cls" if os.name == "nt" else "clear")。判断操作系统：nt-Windows；posix-Linux / macOS。"clear"（macOS/Linux 的清屏命令）
        print("ψ(*｀ー´)ψ" + "▋" * i)
