class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        self.name = self.name.capitalize()
        MyName.total_names += 1 
        self.my_id = self.total_names
        self.domain = "itcollege.lviv.ua"
        if not self.name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

    @property
    def whoami(self) -> str: 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    
    @property
    def full_name(self):
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    
    def create_email(self, domain=None) -> str:
        if domain:
            return f"{self.name}@{domain}"
        return f"{self.name}@{self.domain}"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    
    def say_hello(self,message="Hello to everyone!") -> str:
        """Static method
        """
        return f"You say: {message} from {self.name}"
    
    def number_of_letters(self):
        return len(self.name)
    
    def save_to_file(self, filename="users.txt"):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")

print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta","maksym", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
FULL NAME: {me.full_name}
My name has {me.number_of_letters()} letters.
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")