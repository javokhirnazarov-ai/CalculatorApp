# 🧮 Murakkab Kalkulyator

Python va Flask yordamida yaratilgan zamonaviy web interfeysi bilan murakkab kalkulyator dasturi.

## ✨ Xususiyatlar

### 📊 Matematik Operatsiyalar
- **Asosiy operatsiyalar**: Qo'shish, ayirish, ko'paytirish, bo'lish
- **Trigonometriya**: sin, cos, tan (gradusda)
- **Logarifmlar**: log (10 asosda), ln (natural logarifm)
- **Darajalar**: x², x³, xʸ, √, ∛
- **Maxsus**: Faktorial (n!), Teskari son (1/x), Foiz (%)
- **Konstantalar**: π (Pi), e (Eyler soni)

### 💾 Xotira Funksiyalari
- **M+**: Xotiraga qo'shish
- **M-**: Xotiradan ayirish
- **MR**: Xotirani chaqirish
- **MC**: Xotirani tozalash

### 📜 Tarix
- Barcha hisoblashlar avtomatik saqlanadi
- Oxirgi 50 ta hisoblash ko'rsatiladi
- Tarixdan biror natijani bosish orqali uni qayta ishlatish mumkin
- Tarixni tozalash imkoniyati

### 🎨 Zamonaviy Dizayn
- Gradient ranglar va glassmorphism effektlari
- Smooth animatsiyalar va hover effektlari
- Responsive dizayn (mobil qurilmalar uchun moslashtirilgan)
- Dark mode interfeys

### ⌨️ Klaviatura Qo'llab-quvvatlash
- Raqamlar: `0-9`
- Operatorlar: `+`, `-`, `*`, `/`
- Hisoblash: `Enter`
- Tozalash: `Escape`
- O'chirish: `Backspace`
- Qavslar: `(`, `)`

## 🚀 O'rnatish va Ishga Tushirish

### 1. Kutubxonalarni O'rnatish

```bash
pip install -r requirements.txt
```

### 2. Dasturni Ishga Tushirish

```bash
python app.py
```

Dastur avtomatik ravishda brauzeringizda `http://127.0.0.1:5000` manzilida ochiladi.

## 📦 EXE Fayl Yaratish

Windows uchun mustaqil `.exe` fayl yaratish:

```bash
build.bat
```

Yaratilgan fayl `dist/Murakkab_Kalkulyator.exe` papkasida bo'ladi.

**Eslatma**: EXE fayl yaratish bir necha daqiqa vaqt olishi mumkin.

## 📁 Loyiha Tuzilmasi

```
Calculator App/
│
├── app.py                 # Flask web server
├── calculator.py          # Kalkulyator mantiqiy qismi
├── requirements.txt       # Python kutubxonalari
├── build.bat             # EXE yaratish skripti
├── README.md             # Ushbu fayl
│
├── templates/
│   └── index.html        # HTML interfeys
│
└── static/
    ├── style.css         # CSS dizayn
    └── script.js         # JavaScript mantiq
```

## 🎯 Foydalanish

### Oddiy Hisoblash
1. Raqamlarni va operatorlarni bosing
2. `=` tugmasini bosing yoki `Enter` tugmasini bosing

### Murakkab Funksiyalar
1. Raqamni kiriting
2. Kerakli funksiya tugmasini bosing (masalan, `sin`, `√`, `x²`)

### Xotira
1. Qiymatni hisoblang
2. `M+` yoki `M-` tugmasini bosing
3. `MR` tugmasi orqali xotirani chaqiring
4. `MC` tugmasi orqali xotirani tozalang

### Tarix
1. `📜 Tarix` tugmasini bosing
2. Tarixdagi biror natijani bosish orqali uni qayta ishlating
3. `Tozalash` tugmasi orqali tarixni tozalang

## 🛠️ Texnologiyalar

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Matematik**: Python `math` moduli
- **Build**: PyInstaller

## 📝 Litsenziya

Ushbu dastur o'quv maqsadlari uchun yaratilgan va erkin foydalanish uchun ochiq.

## 👨‍💻 Muallif

Python dasturlash tili yordamida yaratilgan murakkab kalkulyator dasturi.

---

**Eslatma**: Agar biror muammo yuzaga kelsa, `requirements.txt` faylida ko'rsatilgan kutubxonalar to'g'ri o'rnatilganligini tekshiring.
