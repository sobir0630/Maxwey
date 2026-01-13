# 🍔 MaxWay – Online Ovqat Buyurtma Platformasi

## MaxWay — bu restoran va fast-food bizneslari uchun ishlab chiqilgan zamonaviy onlayn ovqat buyurtma qilish tizimi. Loyiha foydalanuvchilar uchun chiroyli va qulay interfeys, administratorlar uchun esa keng funksiyali dashboard taqdim etadi. Barcha buyurtmalar Telegram bot orqali real-time tarzda adminlarga yetkaziladi.

## 🎯 Loyihaning maqsadi

Mijozlarga ovqatlarni tez va oson buyurtma qilish imkonini berish

Administratorlarga buyurtmalarni qulay boshqarish

Buyurtmalarni Telegram orqali darhol xabardor qilish

Restoran ish jarayonini avtomatlashtirish

## 🚀 Asosiy imkoniyatlar
👤 Foydalanuvchilar uchun

🍕 Ovqatlar va kategoriyalarni ko‘rish

🛒 Savatchaga qo‘shish

📝 Buyurtma berish (ism, telefon, manzil bilan)

💻 Chiroyli va tushunarli web interfeys

📱 Mobil qurilmalarga mos dizayn

🧑‍💼 Admin / Dashboard

📦 Ovqat va kategoriyalarni boshqarish

🧾 Buyurtmalarni ko‘rish va nazorat qilish

🔄 Buyurtma holatini o‘zgartirish (yangi, tayyorlanmoqda, yetkazildi)

📊 Kunlik va umumiy buyurtmalar statistikasi

👥 Bir nechta adminlar bilan ishlash imkoniyati

🤖 Telegram Bot Integratsiyasi

🔔 Yangi buyurtma kelganda avtomatik xabar

📋 Buyurtma tafsilotlari Telegram orqali ko‘rinadi

⚡ Real-time ishlash

🧑‍🍳 Adminlar tezkor xabardor bo‘ladi

## 🛠 Texnologiyalar
```
Backend: Django

Frontend: HTML, CSS, JavaScript (zamonaviy UI)

Ma’lumotlar bazasi: PostgreSQL

Admin Panel: Django Admin + Custom Dashboard

Xabarnoma: Telegram Bot API
```
## 📂 Loyiha tuzilishi
```
maxway/
├── config/
├── dashboard/
│   ├── models/        # Ovqatlar va kategoriyalar
│   ├── signals/       # Buyurtmalar
│   ├── views/         # Admin panel va statistika
│   └── bot.py         # Telegram bot integratsiyasi
├── food/              # Asosiy sayt
├── templates/         # Frontend sahifalar
├── static/            # CSS, JS, rasmlar
├── config/            # Sozlamalar
├── manage.py
└── requirements.txt
```

⚙️ O‘rnatish
1. Repozitoriyani klonlash
git clone https://github.com/sobir0630/maxway.git
cd maxway

2. Virtual muhit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Kutubxonalarni o‘rnatish
pip install -r requirements.txt


4. Migratsiya va ishga tushirish
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

🔔 Telegram xabar namunasi
🍔 Yangi buyurtma!

👤 Mijoz: Sobirjon
📞 Telefon: +998 94 820 06 30
📍 Manzil: Samarqand shahri

🛒 Buyurtma:
- Burger x2
- Cola x1

💰 Jami: 78 000 so‘m
⏰ Vaqt: 14:32

📌 Kelajakdagi rejalar

🗺 Yetkazib berish hududlari

💳 Onlayn to‘lov integratsiyasi

📱 Mobil ilova

🧾 Chek (PDF) chiqarish

🔐 Admin rollari va huquqlari

👨‍💻 Muallif

Sobirjon Mamasoliyev
Backend Developer (Django)
📧 Email: mamasoliyevs538@gmail.com

🔗 GitHub: https://github.com/sobir0630