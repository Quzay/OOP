from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from google.adk.agents.llm_agent import Agent


# ============================================================================
# OOP-ПАРАДИГМИ: Абстракція, Наслідування, Інкапсуляція, Поліморфізм
# ============================================================================

class Transport(ABC):
    """Абстрактний клас транспортного маршруту (АБСТРАКЦІЯ)."""

    def __init__(self, route_number: str, departure: str) -> None:
        self.route_number = route_number
        self.departure = departure

    @abstractmethod
    def get_schedule(self) -> Dict:
        """Абстрактний метод — реалізується в підклассах (ПОЛІМОРФІЗМ)."""
        raise NotImplementedError


class Bus(Transport):
    """Клас автобусу — НАСЛІДУВАННЯ від Transport (ПОЛІМОРФІЗМ)."""

    def __init__(self, route_number: str, departure: str, stops: List[str]) -> None:
        super().__init__(route_number, departure)
        self.stops = stops

    def get_schedule(self) -> Dict:
        """Реалізація для автобусу (ПОЛІМОРФІЗМ)."""
        return {
            "type": "Bus",
            "route_number": self.route_number,
            "departure": self.departure,
            "stops": list(self.stops),
        }


class Train(Transport):
    """Клас поїзду — НАСЛІДУВАННЯ від Transport (ПОЛІМОРФІЗМ)."""

    def __init__(self, route_number: str, departure: str, stations: List[str], travel_time_min: int) -> None:
        super().__init__(route_number, departure)
        self.stations = stations
        self.travel_time_min = travel_time_min

    def get_schedule(self) -> Dict:
        """Реалізація для поїзду (ПОЛІМОРФІЗМ)."""
        return {
            "type": "Train",
            "route_number": self.route_number,
            "departure": self.departure,
            "stations": list(self.stations),
            "travel_time_min": int(self.travel_time_min),
        }


class Schedule:
    """Клас розкладу — демонструє ІНКАПСУЛЯЦІЮ (приватний __routes)."""

    def __init__(self) -> None:
        self.__routes: Dict[str, Transport] = {}  # ІНКАПСУЛЯЦІЯ: приватний словник

    def add_route(self, transport: Transport) -> None:
        """Додає маршрут у розклад."""
        self.__routes[transport.route_number] = transport

    def find_route(self, route_number: str) -> Optional[Transport]:
        """Пошук маршруту за номером."""
        return self.__routes.get(route_number)

    def list_routes(self) -> Dict[str, Dict]:
        """Повертає всі маршрути — використовує ПОЛІМОРФІЗМ (get_schedule)."""
        return {rn: t.get_schedule() for rn, t in self.__routes.items()}


# ============================================================================
# ІНСТРУМЕНТ ДЛЯ AI АГЕНТА
# ============================================================================

def get_transport_schedule(route_number: str) -> Dict:
    """Інструмент: повертає розклад для маршруту або {"found": False}."""
    sched = Schedule()
    # Попередньо визначені маршрути
    sched.add_route(Bus("B1", "08:00", ["Stop A", "Stop B", "Stop C"]))
    sched.add_route(Bus("B2", "10:15", ["Stop D", "Stop E"]))
    sched.add_route(Train("T1", "09:30", ["Station X", "Station Y"], 120))
    sched.add_route(Train("T2", "13:00", ["Station Z", "Station W"], 95))

    found = sched.find_route(route_number)
    if not found:
        return {"found": False}
    return found.get_schedule()


# ============================================================================
# AI АГЕНТ З ПРОМПТОМ
# ============================================================================

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Помічник з громадського транспорту.',
    instruction=(
        'Інструкція агенту: коли користувач просить інформацію по конкретному номеру маршруту, НЕ проси уточнити місто. '
        'Виклич внутрішню функцію get_transport_schedule(route_number) і використай її результат для відповіді. '
        'Ніколи не повідомляй користувачу про внутрішні виклики, інструменти, код, логи або сирі JSON/структури — не використовуй слова "Інструменти", "Вихід інструментів" або показуй фрагменти коду. '
        'Формуй відповідь українською лише як людський текст: наведений номер маршруту, час відправлення, зупинки/станції та час у дорозі (якщо є). '
        'Якщо маршрут не знайдено — відповідай коротко: «Маршрут не знайдено». Для інших запитів поводься як звичайний помічник.'
    ),
    tools=[get_transport_schedule]
)

