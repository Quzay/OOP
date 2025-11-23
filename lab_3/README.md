# Звіт до роботи
## Тема: Знайомство з ООП
### Мета роботи: _Навчитись використовувати основні принципи ООП, розглянути кострукції побудови класу та створення обєктів та навчитись працювати з ними_;

---
### Виконання роботи
#### Cтворив два нових файли [note.ipynb](note.ipynb) та [main.py](main.py).
- Виконав приклади які розглядали на лекції та вставив їх у [пайтон ноутбук](note.ipynb)
- у файлі main.py скопіював код із завдання і він вивів такий результат
![](/lab_3/screenshots/first_return.png)
1. Коли ми передаєм значення None створюється обєкт Anonymos тому що в `init` є даний рядок `self.name = name if name is not None else self.anonymous_user().name`
2. Щоб змінити текст можна привітання можна 
   - просто у метод `say_hello` а саме в `message="Hello to everyone!"` просто змінити текст привітання
   - або можна прибрати `staticmethod` і дописати `return f"You say: {message} from {self.name}"` щоб було видно від кого привітання
1. Також добавив функцію яка рахує кількість букв в імені 
    ```python
    def number_of_letters(self):
    return len(self.name)
    ```
1. Різна кількість імен виникає через те, що словник не зберігає дублікати ключів, а `None` під час створення об’єкта замінюється на "Anonymous"
1. Добавив рядок для того, щоб кожне ім'я було з великої літери
    ```python
    self.name = self.name.capitalize()
    ```
1. Змінив метод `crate_email` для того щоб можна було змінювати після @
    ```python
    def create_email(self, domain=None) -> str:
        if domain:
            return f"{self.name}@{domain}"
        return f"{self.name}@{self.domain}"
    ```
1. Добивив перевірку імнені щоб воно містило тільки букви
    ```python
    if not self.name.isalpha():
        raise ValueError("Ім'я може містити лише літери!")
    ```
1. Добавив властивість `full_name`
    ```python
    @property
    def full_name(self):
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    ```
1. Останнє що зробив в цій роботі це реалізував метод save_to_file(filename="users.txt"), який додає рядок із записом у файл;
    ```python
    def save_to_file(self, filename="users.txt"):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")
    ```
## Результат цих завдань 
![](/lab_3/screenshots/final_return.png)
### Також код можна переглянути у файлі [main.py](main.py)