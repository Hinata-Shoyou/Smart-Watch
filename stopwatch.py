import tkinter as tk
import time

class StopwatchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Секундомер с миллисекундами")
        self.geometry("300x150")
        self['background'] = 'black'
        self.is_running = False
        self.start_time = 0

        self.label = tk.Label(self, background ="black", foreground ="white", text="00:00.000", font=("Helvetica", 32))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self, background ="blue", foreground ="white", font=("Helvetica", 20), text="Старт", command=self.start_stop)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self, background ="red", foreground ="white", font=("Helvetica", 20), text="Сброс", command=self.reset)
        self.reset_button.pack(side=tk.RIGHT, padx=10)


    
    def start_stop(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.start_time = time.time()
            self.update()
            self.start_button.config(text="Стоп")
        else:
            self.start_button.config(text="Старт")

    def update(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
            self.label.config(text=f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}")
        self.after(1, self.update)

    def reset(self):
        self.is_running = False
        self.start_time = 0
        self.label.config(text="00:00.000")
        self.start_button.config(text="Старт")

def main():
    root = StopwatchApp()
    #app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



