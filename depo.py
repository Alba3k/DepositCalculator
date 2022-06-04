from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)

print("""\nДЕПОЗИТНЫЙ КАЛЬКУЛЯТОР. 

    Вы сможете рассчитать доход по вкладу, 
    оценить, как он меняется в зависимости от 
    разных сроков и условий выплаты процентов. """)

while True:
    print(Style.BRIGHT + Fore.YELLOW + '\n``````````````````````````````````````````````')
    user_deposit = float(input('Сумма вклада >>> '))
    print(Style.BRIGHT + Fore.YELLOW + '\n``````````````````````````````````````````````')
    print('''Выберите тип срока вклада на:

    1.Месяц
    2.Квартал
    3.Год

Для выхода из программы нажмите Q (q)''')
    user_month, user_qvrt, user_year, result_depo = 0, 0, 0, 0
    user_time_type = input('Тип вклада >>> ')
    if user_time_type == '1':
        user_month = int(input('Количество месяцев >>> '))
    elif user_time_type == '2':
        user_qvrt = int(input('Количество кварталов >>> '))
    elif user_time_type == '3':
        user_year = int(input('Количество лет >>> '))
    elif user_time_type == 'Q' or 'q':
        print(Style.BRIGHT + Fore.GREEN + 'Спасибо за использование программы ;-)')
        break
    else:
        print(Style.BRIGHT + Fore.RED + 'Вы ввели неверное значение')
        continue
    print(Style.BRIGHT + Fore.YELLOW + '\n``````````````````````````````````````````````')
    user_percent = float(input('Процентная ставка годовых, % >>> '))
    print(Style.BRIGHT + Fore.YELLOW + '\n``````````````````````````````````````````````')
    print('''Начисление %, c учетом капитализации да / нет:
    1.Да
    2.Нет''')
    user_cap_type = int(input('>>> '))
    if user_cap_type == 2:
        user_cap_type_period = ''
    elif user_cap_type == 1:
        print('''Капитализация % происходит:
    1.Ежемесячно''')
        user_cap_type_period = ''
        user_choice = int(input('>>> '))
        if user_choice == 1:
            user_cap_type_period = 'depo_cap_m'
        else:
            print(Style.BRIGHT + Fore.RED + 'Вы ввели неверное значение')
            continue
    elif user_cap_type not in (1, 2):
        print(Style.BRIGHT + Fore.RED + 'Вы ввели неверное значение')
        continue
    print(Style.BRIGHT + Fore.YELLOW + '\n``````````````````````````````````````````````')
    print('График начисления по вкладу: ')

    print(f'депозит: {user_deposit} размещен под {user_percent} %,')

#########################################################################################
    if user_month != 0 and user_cap_type_period == '':
        print(f'на срок месяцев: {user_month}')
        result_depo = round((user_deposit * (1 + (((user_percent / 12) * user_month)/100))),2) 
        result_percent = round((result_depo - user_deposit),2)
        print(f'''\nИтоговый результат: 
    начальный депозит: {user_deposit}
    начислено % по вкладу: {result_percent}
    всего к получению: {result_depo}''')
#########################################################################################
    elif user_month != 0 and user_cap_type_period == 'depo_cap_m':
        print(f'на срок месяцев: {user_month} с ежемесячной капитализацией %.')

        a = user_deposit
        b = (1 + (user_percent / 100)/12)
        c = pow(b, user_month)
        result_depo = round((a * c),2) 
        result_percent = round((result_depo - user_deposit),2)

        print(f'''\nИтоговый результат: 
    начальный депозит: {user_deposit}
    начислено % по вкладу: {result_percent}
    всего к получению: {result_depo}''')
#########################################################################################
    elif user_qvrt != 0 and user_cap_type_period == '':
        print(f'на срок кварталов: {user_qvrt}')
        result_depo = round((user_deposit * (1 + (((user_percent / 12) * user_qvrt * 3)/100))),2) 
        result_percent = round((result_depo - user_deposit),2)
        print(f'''\nИтоговый результат: 
    начальный депозит: {user_deposit}
    начислено % по вкладу: {result_percent}
    всего к получению: {result_depo}''')
#########################################################################################
    elif user_qvrt != 0 and user_cap_type_period == 'depo_cap_m':
        print(f'на срок кварталов: {user_qvrt} с ежемесячной капитализацией %.')

        a = user_deposit
        b = (1 + (user_percent / 100)/12)
        c = pow(b, (user_qvrt * 3))
        result_depo = round((a * c),2) 
        result_percent = round((result_depo - user_deposit),2)

        print(f'''\nИтоговый результат: 
    начальный депозит: {user_deposit}
    начислено % по вкладу: {result_percent}
    всего к получению: {result_depo}''')
#########################################################################################
    elif user_year != 0 and user_cap_type_period == '':
        print(f'на срок лет: {user_year}')
        result_depo = round((user_deposit * (1 + (((user_percent / 12) * user_year * 12)/100))),2) 
        result_percent = round((result_depo - user_deposit),2)
        print(f'''\nИтоговый результат: 
    начальный депозит: {user_deposit}
    начислено % по вкладу: {result_percent}
    всего к получению: {result_depo}''')
#########################################################################################
    elif user_year != 0 and user_cap_type_period == 'depo_cap_m':
        print(f'на срок лет: {user_year} с ежемесячной капитализацией %.')

        a = user_deposit
        b = (1 + (user_percent / 100)/12)
        c = pow(b, (user_year * 12))
        result_depo = round((a * c),2) 
        result_percent = round((result_depo - user_deposit),2)

        print(f'''\nИтоговый результат: 
    начальный депозит: {user_deposit}
    начислено % по вкладу: {result_percent}
    всего к получению: {result_depo}''')
#########################################################################################

    print(Style.BRIGHT + Fore.YELLOW + '\n``````````````````````````````````````````````')
#########################################################################################
       