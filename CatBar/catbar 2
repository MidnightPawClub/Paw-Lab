import os
import time

def paw_progress(total=10, task_name="Untitled"):
    for i in range(1, total+1):
        input(f"[{task_name}] Press Enter to complete step {i}/{total}...")
        os.system('cls' if os.name=='nt' else 'clear')
        paw = "🐾" * i
        empty = "____" * (total - i)
        print(f"ψ(>ω<)ψ {paw}{empty} [{i*10}%]")
        if i == total:
            print(f"\n🎉 {task_name} Complete! Treat yourself with a tuna snack!")
#D老师倾情修改版，太晚了明天再来补充注释(｀・ω・´)
