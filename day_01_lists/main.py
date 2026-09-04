# 1. عمل قائمة فيها 3 عملاء (كل عميل عبارة عن dictionary)
clients = [
    {"name": "أحمد", "email": "ahmed@mail.com", "order": "حاسوب"},
    {"name": "سارة", "email": "sara@mail.com", "order": "هاتف"},
    {"name": "كريم", "email": "karim@mail.com", "order": "سماعات"}
]

# 2. طباعة بياناتهم
for c in clients:
    print(c["name"], "-", c["email"], "-", c["order"])import arabic_reshaper
from bidi.algorithm import get_display

def fix_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

clients = [
    {"name": "أحمد", "email": "ahmed@mail.com", "order": "حاسوب"},
    {"name": "سارة", "email": "sara@mail.com", "order": "هاتف"},
    {"name": "كريم", "email": "karim@mail.com", "order": "سماعات"}
]

for c in clients:
    name = fix_text(c["name"])
    order = fix_text(c["order"])
    print(name, "-", c["email"], "-", order)
