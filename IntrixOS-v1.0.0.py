import os
import time
import webbrowser

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    print("Калькулятор")
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))
    if operator == '+':
        print(f"Результат: {num1 + num2}")
    elif operator == '-':
        print(f"Результат: {num1 - num2}")
    elif operator == '*':
        print(f"Результат: {num1 * num2}")
    elif operator == '/':
        print(f"Результат: {num1 / num2}")
    else:
        print("Неверный оператор")

def timer():
    seconds = int(input("Введите время в секундах: "))
    print("Таймер запущен...")
    time.sleep(seconds)
    print("Время вышло!")

def stopwatch():
    input("Нажмите Enter для начала секундомера...")
    start_time = time.time()
    input("Нажмите Enter для остановки секундомера...")
    elapsed_time = time.time() - start_time
    print(f"Прошло времени: {elapsed_time:.2f} секунд")

def authors():
    print("Авторы проекта: Vidasik / HSM")

def open_website():
    webbrowser.open("http://intrix-os.rf.gd")

def settings():
    print("Настройки: Изменение цветов текста и фона")
    text_color = input("Введите цвет текста: ")
    background_color = input("Введите цвет фона: ")
    print(f"Цвет текста: {text_color}, Цвет фона: {background_color}")

def device_info():
    print("Информация об устройстве:")
    print(f"ОС: {os.name}")

def ascii_art():
    print(r"""
                                                                    .!J?:                           
                                                      .~7JJ7!^    .7B@@@#.                          
                                                    ~5#@@@@@@@B7:?#@@@@B7                           
                                                  ~P@@@@&PPB@@@@&@@@@B7                             
                                                ~G@@@@#J:   ^5&@@@@@?                               
                                               ^@@@@@B:       :Y&@@@#J                              
                                                ?#@@@@B?.       :Y&@@@5                             
                                                 .7B@@@@#?.       5@@@@:                            
                                                    !G@@@@#J:   :J&@@@P                             
                                           .7YJ^      !G@@@@&Y~Y&@@@@Y.                             
                                   ^?Y7^ .J#@@@&.       ~P@@@@@@@@@P~                               
                                 ^5@@@@&G#@@@@G~          ^5@@@@@5^                                 
                               ~P@@@@@@@@@@@P~   .!YY!      ^J57^                                   
                              Y@@@@&Y~Y&@@@@G~ .7B@@@@~                                             
                             5@@@&J:   :J#@@@@B#@@@@B7                                              
                            :@@@@5       .?#@@@@@@B!                                                
                             P@@@&Y:       .7B@@@@#!                                                
                             .Y@@@@&Y:       :B@@@@&:                                               
                               Y@@@@@&5^   :J#@@@@G~                                                
                             7B@@@@@@@@@BPP&@@@@P~                                                  
                           7B@@@@#?^JB@@@@@@@#5~                                                    
                          .&@@@B7.   .~!JJJ7^.                                                      
                           ^?J!.                                                                    
    """)
    print("Сделано на Python")

def main_menu():
    while True:
        clear_screen()
        print("IntrixOS v1.0 by Vidasik")
        print("                        ")
        print("1. Калькулятор")
        print("2. Таймер")
        print("3. Секундомер")
        print("4. Авторы проекта")
        print("5. Переход на сайт")
        print("6. Настройки")
        print("7. Информация об устройстве")
        print("8. Лого IntrixOS (ASCII)")
        print("0. Выход")
        choice = input("Выберите опцию: ")
        
        if choice == '1':
            calculator()
        elif choice == '2':
            timer()
        elif choice == '3':
            stopwatch()
        elif choice == '4':
            authors()
        elif choice == '5':
            open_website()
        elif choice == '6':
            settings()
        elif choice == '7':
            device_info()
        elif choice == '8':
            ascii_art()
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
        input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main_menu()
