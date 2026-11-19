# Звіт до роботи
## Тема: Автоматизація за допомогою GitHub Actions
### Мета роботи: _Навчитись налаштовувати CI/CD pipeline за допомогою GitHub Actions, створювати workflow з різними тригерами, jobs та умовами_;

---

[![Makson Workflow](https://github.com/Quzay/OOP/actions/workflows/python-app.yml/badge.svg)](https://github.com/Quzay/OOP/actions/workflows/python-app.yml)
[![Second Workflow](https://github.com/Quzay/OOP/actions/workflows/second.yml/badge.svg)](https://github.com/Quzay/OOP/actions/workflows/second.yml)

---
### Виконання роботи

#### 1. Створення першого Workflow з шаблону
Створив workflow з шаблону `Python application` через вкладку `Actions` → `New workflow`. Змінив назву на `Makson Workflow` та закомітив файл.

![](screenshots/screenshot-2026-11-19_12-56-20.png)

#### 2. Запуск вручну (workflow_dispatch) з параметром
Додав тригер `workflow_dispatch` з параметром `name`. При ручному запуску передається імʼя користувача:
```yaml
workflow_dispatch:
  inputs:
    name:
      description: 'Імʼя користувача'
      default: 'Executer'
      required: true
```
![](screenshots/screenshot-2026-11-19_12-58-00.png)

#### 3. Запуск по розкладу (cron)
Додав тригер `schedule` з запуском щопонеділка о 10:00:
```yaml
schedule:
  - cron: '0 10 * * 1'
```

#### 4. Два jobs в одному workflow
```yaml
jobs:
  run_python:
    name: Run Python Script
  second_job:
    name: Second Job
```
![](screenshots/screenshot-2026-11-19_12-58-24.png)

#### 5. Умова if для кроку
Крок `Send greeting` виконується лише якщо передане імʼя не є `Executer`. При запуску з імʼям `Maks` — крок виконався і вивів `Hello Maks`:
```yaml
- name: Send greeting
  run: echo "Hello ${{ github.event.inputs.name }}"
  if: github.event.inputs.name != 'Executer'
```
![](screenshots/screenshot-2026-11-19_12-59-32.png)

#### 6. Два окремих Workflow
Створив два файли — `python-app.yml` та `second.yml` з різними назвами. Обидва відображаються у вкладці `Actions`:

![](screenshots/screenshot-2026-11-19_13-03-35.png)

![](screenshots/screenshot-2026-11-19_13-04-15.png)

#### 7. Баджі в README
Додав баджі статусу обох workflow у `README.md` репо.