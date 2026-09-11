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
    ================================================================================
import json

# 1. إنشاء ملف بيانات عميل وهمي للبدء به
client_data = {
    "name": "Crystal",
    "service": "Python Automation",
    "status": "pending"
}

# حفظ الملف البدائي
with open("client_profile.json", "w") as f:
    json.dump(client_data, f, indent=4)

# 2. قراءة الملف وتعديل حالة العميل
with open("client_profile.json", "r") as f:
    data = json.load(f)

# تعديل الحالة إلى نشط
data["status"] = "active"

# 3. إعادة حفظ الملف بعد التعديل
with open("client_profile.json", "w") as f:
    json.dump(data, f, indent=4)

print("تم تعديل حقل العميل وحفظه بنجاح! الحالة الجديدة:", data["status"])
print("--- النتيجة النهائية ---")
print("اسم العميل:", client["name"])
print("الباكة الحالية:", client["plan"])
print("حالة الحساب:", client["status"])
print("تم تحديث الملف بنجاح على الجهاز!")
===============================================================================================
import json

# محاولة فتح ملف غير موجود لتجربة حماية السكريبت من الأخطاء
file_name = "missing_file.json"

try:
    with open(file_name, "r") as f:
        data = json.load(f)
        print("تمت القراءة بنجاح!")
except FileNotFoundError:
    print(f"تنبيه: الملف '{file_name}' غير موجود! سيتم إنشاء ملف جديد افتراضي.")
    
    # إنشاء ملف بديل تلقائياً حتى لا يتوقف العمل
    default_data = {"name": "Unknown", "status": "new"}
    with open(file_name, "w") as f:
        json.dump(default_data, f, indent=4)
        print("تم إنشاء الملف الافتراضي بنجاح!")
        ===============================================================================
