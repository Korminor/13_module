import asyncio # импортируем модуль для работы с асинхронностью

async def start_strongman(name, power): # создаем участников и их логику name:имя участника и power: сила
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6): # указываем что количество шаров 5
        await asyncio.sleep(1/power) # указываем в зависимости от силы какая задержка у спортсмена в сек между шарами
        print(f'Силач {name} поднял {i}шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament(): # создаем задачи для трех спортсенов
    task_1 = asyncio.create_task(start_strongman('Andrey', 3)) # создаем спортсмена с именем и силой
    task_2 = asyncio.create_task(start_strongman('Dima', 5))
    task_3 = asyncio.create_task(start_strongman('Pavel', 2))
    await task_1 # указываем ожидание для каждой задачи чтоб программа не завершилась пока все не закончат
    await task_2
    await task_3


asyncio.run(start_tournament())# Запускаем выполнение программы
