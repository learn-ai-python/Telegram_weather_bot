# 🤖 Telegram weather bot туторіал
Створення Telegram-бота, щоб отримувати поточний час у різних точках світу.

## 🎬 Відео-туторіали
- [Крок-1](https://vm.tiktok.com/ZMYhjR4Ws/)
- [Крок-2](https://vm.tiktok.com/ZMYhjR6XW/)
- [Крок-3](https://vm.tiktok.com/ZMYhjFKYF/)
- [Крок-4](https://vm.tiktok.com/ZMYhjF2RU/)


## 📑 Текстові версії відео-туторіалів
#### 1️⃣ Крок-1
Спочатку ми знаходимо **@BotFather** для "реєстрації" нашого бота.
Для старту BotFather виконуємо команду **`/start`**.
Створюємо наш новий бот за допомогою команди **`/newbot`**.
Назвемо наш бот як My Telegram Bot (як заголовок). 
Придумаємо йому унікальний нікнейм (як посилання).
Після цього отримаємо **секретний токен**.

#### 2️⃣ Крок-2
Тепер ми налаштуємо запуск нашого коду. 
Для цього ми використаємо хмарний сервіс **[PythonAnywhere](https://www.pythonanywhere.com/)**. 
Для запуску такого боту буде достатньо безкоштовної версії.
Тому, реєструємося та створюємо там новий файл із розширенням **`*.py`**.

#### 3️⃣ Крок-3
Далі ми напишемо код до боту. 
Нехай за допомогою даного боту користувач зможе отримувати **поточний час у різних точках світу**.
- У рядках 1-3 ми імпортуємо необхідні бібліотеки.
- У рядку 5 ми ініціалізуємо наш бот, у лапках ми вказуємо наш унікальний секретний токен, який ми отримали у першій частині. Свій я ще не вставила.
- У рядку 8 ми задаємо обробку команди **`/start`**.
- У рядках 9-11 ми створюємо функцію, яка буде повертати нам текст **'Вітаю! Що Ви хочете дізнатися?'**, після того, як користувач напише у бот команду **`/start`**.
- У рядках 13-16 ми описуємо відповідь бота на команду від користувача **`/time`**.
- У рядках 19-38 ми описуємо команди для бота, коли користувач буде вводити те чи інше місто.
- Як бачимо, у рядку 19 вказано, що користувач має ввести із клавіатури текст. У нашому випадку - це міста, про яке користувач хоче дізнатися час.
Ця функція складається із умови **`if-elif-else`**.
Загальна логіка наступна: користувач вводить місто із клавіатури. 
Якщо таке місто наявне у нашій умові **`if-elif-else`**, то спочатку ми отримуємо поточний час для того часового поясу, де розміщене наше місто (рядки 22, 27 та 32). 
Тоді ми форматуємо дату час за шаблоном (рядки 23, 28, 33) та передаємо інформацію користувачу (рядки 24, 29, 34).
Якщо ж користувач ввів із клавіатури місто, якого нема у переліку, то за допомогою коду у рядках 36-38 ми повідомляємо про це користувача.
- У рядках 41-43 ми запускаємо нашого бота.
- А сам код запускається через кнопку **`Run`** у інтерфейсі PythonAnywhere.

#### 4️⃣ Крок-4
Відкриваємо наш телеграм. 
Переходимо за посиланням до нашого бота. 
І тестуємо: виконуємо команду **`/start`** для запуску бота.



