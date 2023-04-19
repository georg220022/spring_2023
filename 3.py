import asyncio
import random
from typing import List


# Разделяемое состояние
class SharedState:
    items: List[int]

    def __init__(self):
        self.items = []

    # модификация состояния сервера
    async def modify(self, value: int):
        await asyncio.sleep(random.randint(1, 2))
        self.items.append(value)


# Имитация сервера. В нашем случае "запросы" модифицируют состояние сервера добавляя элементы в конец списка 'items'
class Server:
    state: SharedState

    def __init__(self, state: SharedState):
        self.state = state
        self.lock = asyncio.Lock()

    async def handle_request(self, value: int):
        # Решено методом научного тыка :)
        async with self.lock:
            await self.state.modify(value)


async def main():
    state = SharedState()
    server = Server(state)

    # запуск 10 запросов к серверу
    requests = [server.handle_request(value) for value in range(10)]
    await asyncio.gather(*requests)

    """    
    Ваша задача заключается в том, чтобы используя только asyncio исключить data race
    state в результате обработки запросов должен удовлетворять следующему условию:
    """
    print(state.items == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    for item in state.items:
        print(item)


if __name__ == "__main__":
    asyncio.run(main())
