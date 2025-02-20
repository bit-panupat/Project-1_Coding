target = int(input("กรอกแคลอรี่ที่คุณต้องการลด: "))
time = int(input("จำนวนนาทีที่ต่อยมวย :"))
calorie = time * 7.73
if calorie >= target:
    print("สำเร็จเป้าหมายที่ตั้ง")
else:
    print("ไม่สำเร็จเป้าหมายที่ตั้ง")
    calorie_deficit = target - calorie
    print("คุณต้องการออกกำลังกายอีก", calorie_deficit/7.73, "นาที")