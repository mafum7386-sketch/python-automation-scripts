# =========================================================
# اليوم 5: دمج مفاهيم الأسبوع الأول + التعامل مع الأخطاء
# =========================================================

import json

filename = "client_data.json"

# 1. محاولة قراءة ملف العميل مع معالجة خطأ عدم وجوده
try:
    with open(filename, "r") as f:
        client = json.load(f)
        print("تم العثور على ملف العميل وقراءته بنجاح!")
except FileNotFoundError:
    print("الملف غير موجود، جاري إنشاء ملف عميل جديد...")
    client = {
        "client_id": 101,
        "name": "Crystal",
        "plan": "Basic",
        "status": "pending"
    }

# 2. تعديل بيانات العميل
client["plan"] = "Premium"
client["status"] = "active"

# 3. حفظ البيانات المحدثة
with open(filename, "w") as f:
    json.dump(client, f, indent=4)

print("--- النتيجة النهائية ---")
print("اسم العميل:", client["name"])
print("الباكة الحالية:", client["plan"])
print("حالة الحساب:", client["status"])
print("تم تحديث الملف بنجاح على الجهاز!")
