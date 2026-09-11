# =========================================================
# اليوم 8: الدوال الأساسية Functions
# =========================================================

# تعريف البيانات التجريبية
my_orders = [
    {"id": 101, "item": "Laptop", "price": 800, "status": "completed"},
    {"id": 102, "item": "Phone", "price": 500, "status": "pending"},
    {"id": 103, "item": "Headphones", "price": 100, "status": "pending"},
    {"id": 104, "item": "Keyboard", "price": 50, "status": "completed"}
]

# الدالة 1: تصفية الطلبات المعلقة
def filter_pending_orders(orders_list):
    pending = []
    for order in orders_list:
        if order["status"] == "pending":
            pending.append(order)
    return pending

# الدالة 2: حساب المجموع والمتوسط
def calculate_financials(orders_list):
    total = 0
    for order in orders_list:
        total += order["price"]
    avg = total / len(orders_list)
    return total, avg

# الدالة 3: استخراج الطلبات الغالية (أكبر من سعر معين)
def get_high_value_orders(orders_list, min_price):
    result = []
    for order in orders_list:
        if order["price"] >= min_price:
            result.append(order)
    return result

# --- استدعاء وتشغيل الدوال ---
print("1. الطلبات المعلقة:", filter_pending_orders(my_orders))

total_amount, average_amount = calculate_financials(my_orders)
print(f"2. إجمالي المبيعات: {total_amount}$ | المتوسط: {average_amount}$")

expensive_orders = get_high_value_orders(my_orders, 400)
print("3. الطلبات فوق 400$:", expensive_orders)
