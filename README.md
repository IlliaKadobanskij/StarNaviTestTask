# StarNaviTestTask

Це README-файл, який описує основні кроки для запуску мого Django проекту на іншому комп'ютері.

## Початок роботи

Ці інструкції допоможуть вам налаштувати копію проекту на вашому комп'ютері. Для початку потрібно виконати наступні кроки:

### 1. Клонування репозиторію

Спочатку склонуйте цей репозиторій на свій комп'ютер:

```bash
git clone <URL вашого репозиторію на GitHub>
```

### 2. Створення віртуального середовища (venv)

1) Відкрийте термінал або командний рядок у корені проекту.
2) Запустіть наступну команду для створення віртуального середовища:

```bash
python -m venv venv
```

### 3. Встановлення необхідних бібліотек

1) Активуйте віртуальне середовище, використовуючи наступну команду:

Для Windows:
```bash
venv\Scripts\activate
```
2) Встановіть необхідні бібліотеки, використовуючи зазначений файл requirements.txt:
```bash
pip install -r requirements.txt
```
### 4. Міграція бази даних
В активованому віртуальному середовищі запустіть наступні команди для міграції бази даних та створення суперкористувача:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
### 5. Запуск бота для заповнення бази даних
У корені проекту виконайте наступну команду для запуску бота, який заповнить базу даних:
```bash
python manage.py runscript StarNaviTestTask.bot.bot
```
Тепер ваш Django проект готовий до роботи на іншому комп'ютері!