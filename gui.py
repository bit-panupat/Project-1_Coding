import tkinter as tk
from tkinter import messagebox

def calculate_calories():
    try:
        target = int(entry_target.get())
        time = int(entry_time.get())
        calorie = time * 7.73
        
        if calorie >= target:
            messagebox.showinfo("ผลลัพธ์", "สำเร็จเป้าหมายที่ตั้ง")
        else:
            calorie_deficit = target - calorie
            additional_time = calorie_deficit / 7.73
            messagebox.showinfo("ผลลัพธ์", f"ไม่สำเร็จเป้าหมายที่ตั้ง\nคุณต้องการออกกำลังกายอีก {additional_time:.2f} นาที")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลเป็นตัวเลข")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("คำนวณการลดแคลอรี่")

# สร้างและวางป้ายคำถาม
label_target = tk.Label(root, text="แคลอรี่ที่คุณต้องการลด:")
label_target.pack()

# สร้างช่องกรอกข้อมูล
entry_target = tk.Entry(root)
entry_target.pack()

label_time = tk.Label(root, text="จำนวนนาทีที่ต่อยมวย:")
label_time.pack()

entry_time = tk.Entry(root)
entry_time.pack()

# สร้างปุ่มคำนวณ
button_calculate = tk.Button(root, text="คำนวณ", command=calculate_calories)
button_calculate.pack()

# เริ่มต้นการแสดงหน้าต่าง
root.mainloop()
