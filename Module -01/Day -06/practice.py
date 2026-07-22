#before violation srp
class Report:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def build(self):
        return f"# {self.title}\n\n{self.body}"

    def save(self, path):
        with open(path, "w") as f:
            f.write(self.build())

    def email(self, address):
        print(f"Sending report to {address}...")
        
    #after srp is applied 
    class ReportBuilder:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def build(self):
        return f"# {self.title}\n\n{self.body}"


class ReportSaver:
    def save(self, content, path):
        with open(path, "w") as f:
            f.write(content)


class ReportMailer:
    def send(self, content, address):
        print(f"Sending report to {address}...")
    

builder = ReportBuilder("Q3 Summary", "Revenue is up 12%.")
content = builder.build()
ReportSaver().save(content, "report.md")
ReportMailer().send(content, "boss@example.com")

#before violates ocp
def print_area(shape):
    if shape["type"] == "circle":
        print(3.14159 * shape["radius"] ** 2)
    elif shape["type"] == "square":
        print(shape["side"] ** 2)
    elif shape["type"] == "triangle":
        print(0.5 * shape["base"] * shape["height"])

   #after ocp is applied
   from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def print_area(shape: Shape):
    print(shape.area())

print_area(Circle(4))
print_area(Square(3))
print_area(Triangle(6, 2))

#singleton
class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance

a = AppSettings()
b = AppSettings()

print(a.currency)          
print(a is b)              
print(id(a) == id(b))      

#Factory
class ShapeFactory:
    @staticmethod
    def create(kind, *args):
        shapes = {
            "circle": Circle,
            "square": Square,
            "triangle": Triangle,
        }
        if kind not in shapes:
            raise ValueError(f"Unknown shape type: {kind}")
        return shapes[kind](*args)

c = ShapeFactory.create("circle", 5)
s = ShapeFactory.create("square", 4)
t = ShapeFactory.create("triangle", 6, 3)

print(c.area(), s.area(), t.area())

#observer
from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, news):
        pass


class EmailSubscriber(Subscriber):
    def update(self, news):
        print(f"[Email] New article: {news}")


class SMSSubscriber(Subscriber):
    def update(self, news):
        print(f"[SMS] Breaking: {news}")


class NewsAgency:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, news):
        for sub in self._subscribers:
            sub.update(news)

agency = NewsAgency()
agency.subscribe(EmailSubscriber())
agency.subscribe(SMSSubscriber())

agency.notify("Ethiopia wins the AFCON qualifier!")from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, news):
        pass


class EmailSubscriber(Subscriber):
    def update(self, news):
        print(f"[Email] New article: {news}")


class SMSSubscriber(Subscriber):
    def update(self, news):
        print(f"[SMS] Breaking: {news}")


class NewsAgency:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, news):
        for sub in self._subscribers:
            sub.update(news)

agency = NewsAgency()
agency.subscribe(EmailSubscriber())
agency.subscribe(SMSSubscriber())

agency.notify("Ethiopia wins the AFCON qualifier!")

