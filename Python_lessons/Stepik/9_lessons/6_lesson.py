
number_day = int(input())
now_weight = float(input())

need_weight = 100 - (number_day * 0.2)

if now_weight <= need_weight:
    print(f"Все идет по плану\n#{number_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {now_weight} кг, ЦЕЛЬ ПО ВЕСУ = {need_weight} кг")
else:
    print(f"Что-то пошло не так\n#{number_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {now_weight} кг, ЦЕЛЬ ПО ВЕСУ = {need_weight} кг")



# a = int(input())
# b = int(input())
#
# print(f"Для чисел {a} и {b}:\n  Сумма кубов: {a}**3 + {b}**3 = {a**3 + b**3}\n  Куб суммы: ({a} + {b})**3 = {(a + b)**3}")

# data = input()
# dollars = input()
# uans = input()
#
# print(f"На {data}: 1$ = {dollars}₽, 1¥ = {uans}₽")