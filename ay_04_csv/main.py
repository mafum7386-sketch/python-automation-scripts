import csv

# 1. تجهيز بيانات الجدول (الصف الأول هو العناوين، وباقي الأسطر هي البيانات)
data = [
    ["Name", "Item", "Price"],
    ["Karim", "Laptop", "800"],
    ["Crystal", "Phone", "400"]
]

# 2. فتح ملف جديد باسم orders.csv والكتابة فيه
with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("تم إنشاء جدول orders.csv بنجاح!")
# 3. قراءة الملف والبحث عن طلبية Crystal
with open("orders.csv", "r") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        if row["Name"] == "Crystal":
            print("Found Crystal order:", row["Item"], "for", row["Price"], "$")
import json

# 4. تحويل كل بيانات ملف الـ CSV إلى قائمة JSON وحفظها
with open("orders.csv", "r") as f:
    orders_list = list(csv.DictReader(f))

with open("orders.json", "w") as f:
    json.dump(orders_list, f, indent=4)

print("Converted CSV to orders.json successfully!")
    
