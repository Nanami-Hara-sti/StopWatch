import tkinter as tk
import time


class StopwatchApp:
    def __init__(self, parent):
        # Frameを作成し、親ウィジェット(parent)に配置
        self.frame = tk.Frame(parent)
        self.frame.pack(side=tk.LEFT, padx=15, pady=15)

        # --- ストップウォッチの状態を管理する変数 ---
        self.running = False
        self.start_time = 0.0
        self.elapsed_time = 0.0

        # --- ラベル編集部品 ---
        self.label_var = tk.StringVar()
        self.label_var.set("タイマー")
        self.label_entry = tk.Entry(self.frame, textvariable=self.label_var, font=("Arial", 10), justify="center", width=8)
        self.label_entry.pack(pady=(0,2))

        # --- 画面の部品（ウィジェット）を作成 ---
        self.time_label = tk.Label(self.frame, text="00:00", font=("Arial", 40, "bold"))
        self.time_label.pack(pady=4)

        self.toggle_button = tk.Button(self.frame, text="Start", width=13, command=self.toggle)
        self.toggle_button.pack(pady=4)

        self.update()

    def toggle(self):
        """ボタンが押されたときの処理"""
        if self.running:
            # ストップ処理
            self.running = False
            self.toggle_button.config(text="Start")
        else:
            # スタート処理
            self.running = True
            self.toggle_button.config(text="Stop")
            # 停止していた時間分を考慮して、計測開始時刻を調整
            self.start_time = time.time() - self.elapsed_time

    def update(self):
        """時間を計算して表示を更新する処理"""
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self._display_time()
        self.frame.after(10, self.update)

    def _display_time(self):
        """経過時間を見やすい形式に変換してラベルに表示（時間:分）"""
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        # "00:00" の形式で文字列を作成
        time_string = f"{hours:02}:{minutes:02}"
        self.time_label.config(text=time_string)

# --- アプリケーションの実行 ---

class StopwatchManager:
    def __init__(self, root):
        self.root = root
        self.stopwatches = []
        self.frame = tk.Frame(root)
        self.frame.pack()

        # ボタン配置
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=4)
        self.add_btn = tk.Button(btn_frame, text="○", font=("Arial", 12), width=4, command=self.add_stopwatch)
        self.add_btn.pack(side=tk.LEFT, padx=4)
        self.remove_btn = tk.Button(btn_frame, text="×", font=("Arial", 12), width=4, command=self.remove_stopwatch)
        self.remove_btn.pack(side=tk.LEFT, padx=4)

        # 初期2つ
        self.add_stopwatch()
        self.add_stopwatch()

    def add_stopwatch(self):
        sw = StopwatchApp(self.frame)
        self.stopwatches.append(sw)
        self.update_window_size()

    def remove_stopwatch(self):
        if self.stopwatches:
            sw = self.stopwatches.pop()
            sw.frame.destroy()
            self.update_window_size()

    def update_window_size(self):
        width = max(205 * len(self.stopwatches), 205)
        self.root.geometry(f"{width}x200")

# --- アプリケーションの実行 ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("StopWatch")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    manager = StopwatchManager(root)

    # 初期ウィンドウサイズを縦200に
    root.geometry("410x200")

    root.mainloop()
