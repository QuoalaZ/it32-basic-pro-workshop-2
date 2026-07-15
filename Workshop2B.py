name = input("ชื่อ : ")
age = int(input("อายุ : "))
height = int(input("ส่วนสูง : "))
strength = int(input("พละกำลัง  : "))
money = int(input("เงินติดตัว : "))

if age >= 18 and height >= 180 and strength >= 8 and money >= 1000:
    print("\nผลการคัดกรอง: ผ่าน")
    print("ตำแหน่ง: Divine Crusader")
elif age >= 18 and height >= 170 and strength >= 6 and money >= 500:
    print("\nผลการคัดกรอง: ผ่าน")
    print("ตำแหน่ง: Grand Marshall")
elif age >= 18 and height >= 160 and strength >= 4 and money >= 250:
    print("\nผลการคัดกรอง: ผ่าน")
    print("ตำแหน่ง: Nature's Warth")
elif age >= 18 and height >= 150 and strength >= 2 and money >= 100:
    print("\nผลการคัดกรอง: ผ่าน")
    print("ตำแหน่ง: Beast Tamer Warrior")
else:
    print("\nผลการคัดกรอง: ไม่ผ่าน")

print("ชื่อ: ", name)
print("อายุ : ", age, "year")
print("ส่วนสูง : ", height, "cm")
print("พละกำลัง : ", strength, )
print("เงินติดตัว : ", money, "SPD")
