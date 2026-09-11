import json

# 1. دالة قراءة وتصفية البيانات مع معالجة الأخطاء
def process_orders_file(file_path):
    try:
        # محاولة فتح الملف وقراءته
        with open(file_path, 'r') as file:
            orders = json.load(file)
            
        pending_orders = []
        total_sales = 0
        
        # التكرار والفلترة والتجميع
        for order in orders:
            # التأكد من وجود حقل السعر والحالة لتجنب أخطاء المفاتيح المفقودة
            price = order.get("price", 0)
            status = order.get("status", "unknown")
            
            total_sales += price
            if status == "pending":
                pending_orders.append(order)
                
        avg_price = total_sales / len(orders) if orders else 0
        return pending_orders, total_sales, avg_price

    except FileNotFoundError:
        print(f"❌ خطأ: الملف '{file_path}' غير موجود في النظام!")
        return [], 0, 0
    except json.JSONDecodeError:
        print(f"❌ خطأ: تنسيق ملف JSON غير صحيح أو الملف فارغ!")
        return [], 0, 0
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع: {e}")
        return [], 0, 0

# 2. البيانات التجريبية واختبار السكريبت
file_name = "orders.json"

# إنشاء ملف تجريبي واختباره
sample_data = [
    {"id": 101, "item": "Laptop", "price": 800, "status": "completed"},
    {"id": 102, "item": "Phone", "price": 500, "status": "pending"},
    {"id": 103, "item": "Headphones", "price": 100, "status": "pending"}
]

# كتابة بيانات تجريبية في ملف
with open(file_name, 'w') as f:
    json.dump(sample_data, f)

# تشغيل الفاحص على الملف الصحيح
pending, total, avg = process_orders_file(file_name)

print("\n--- نتيجة فحص الطلبات الناجحة ---")
print(f"عدد الطلبات المعلقة: {len(pending)}")
print(f"إجمالي المبيعات: {total}$")
print(f"متوسط قيمة الطلب: {avg:.2f}$")

print("\n--- اختبار درع الحماية (ملف مفقود) ---")
process_orders_file("missing_file.json")
