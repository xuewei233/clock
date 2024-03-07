# clock
import time
import os
import platform

def clear_screen():
    # 清除终端屏幕的函数
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def focus_timer(total_time, focus_interval, break_interval):
    while True:
        # 专注时间
        print("专注时间开始！")
        time.sleep(focus_interval * 60)  # 将分钟转换为秒

        # 休息时间
        clear_screen()
        print("休息一下！")
        time.sleep(break_interval * 60)  # 将分钟转换为秒

if __name__ == "__main__":
    total_time = 25  # 总计时长（分钟）
    focus_interval = 25  # 专注时间长度（分钟）
    break_interval = 5  # 休息时间长度（分钟）

    try:
        focus_timer(total_time, focus_interval, break_interval)
    except KeyboardInterrupt:
        print("\n计时器已停止。")
