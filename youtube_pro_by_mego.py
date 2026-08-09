import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytubefix import YouTube
import os
import threading

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("خطأ", "يا ميجو حط لينك الفيديو الأول!")
        return
    
    try:
        status_label.config(text="جاري جلب بيانات الفيديو... By Mego")
        yt = YouTube(url)
        
        # Get best progressive stream
        stream = yt.streams.get_highest_resolution()
        
        if not stream:
            stream = yt.streams.filter(progressive=True).first()
            
        save_path = filedialog.askdirectory(title="اختار مكان الحفظ يا ميجو")
        if not save_path:
            status_label.config(text="تم الإلغاء")
            return

        status_label.config(text=f"بيحمل: {yt.title[:30]}...")

        def start_dl():
            try:
                stream.download(output_path=save_path)
                status_label.config(text="تم التحميل بنجاح! By Mego 🔥")
                messagebox.showinfo("تم", f"الفيديو اتحمل بنجاح في:\n{save_path}")
            except Exception as e:
                status_label.config(text="حصل خطأ!")
                messagebox.showerror("خطأ", str(e))

        threading.Thread(target=start_dl).start()

    except Exception as e:
        status_label.config(text="لينك غير صحيح!")
        messagebox.showerror("خطأ", f"مش قادر اجيب الفيديو:\n{e}")

# --- UI ---
root = tk.Tk()
root.title("YouTube Pro - By Mego 🔥")
root.geometry("500x350")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

title_label = tk.Label(main_frame, text="YouTube Pro By Mego", font=("Arial", 18, "bold"), fg="#FF0000")
title_label.pack(pady=10)

url_label = tk.Label(main_frame, text="حط لينك اليوتيوب هنا:", font=("Arial", 11))
url_label.pack(anchor="w", pady=(10, 5))

url_entry = tk.Entry(main_frame, font=("Arial", 11), width=50)
url_entry.pack(pady=5, ipady=5)

download_btn = tk.Button(main_frame, text="تحميل 🔥", font=("Arial", 12, "bold"), bg="#FF0000", fg="white", command=download_video, height=2)
download_btn.pack(pady=20, fill="x")

status_label = tk.Label(main_frame, text="جاهز... مستنيك يا ميجو", font=("Arial", 10), fg="gray")
status_label.pack(pady=10)

root.mainloop()
