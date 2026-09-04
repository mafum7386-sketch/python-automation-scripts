# =========================================================
# اليوم 3: قراءة وكتابة ملفات JSON
# =========================================================

import json

# 1. إنشاء بيانات الطلبية وحفظها في ملف json
order_data = {
    "client": "Karim",
    "item": "Laptop",
    "status": "pending"
}

with open("order.json", "w") as file:
    json.dump(order_data, file, indent=4)

# 2. قراءة الملف والتعديل عليه
with open("order.json", "r") as file:
    data = json.load(file)

# تعديل حالة الطلب
data["status"] = "completed"

# إعادة الحفظ بعد التعديل
with open("order.json", "w") as file:
    json.dump(data, file, indent=4)

print("تم التعديل والحفظ بنجاح! الحالة الحالية:", data["status"])

# =========================================================
# ملاحظات اليوم 3:
# - json.dump: لحفظ البيانات من بايثون إلى ملف (Write).
# - json.load: لقراءة البيانات من ملف إلى بايثون (Read).
# - "w" تعني كتابة، و "r" تعني قراءة.
# =========================================================
