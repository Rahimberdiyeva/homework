import time
from colorama import init, Fore, Back

init()

class Zwerushka:
    def __init__(self):
        self.sytost = 10
        self.radost = 10

    def kormit(self):
        if self.sytost < 10:
            self.sytost += 1
            print(f"{Fore.GREEN}Вы покормили зверушку.")
        else:
            print(f"{Fore.YELLOW}Зверушка уже сыта.")

    def играть(self):
        if self.sytost > 0:
            self.sytost -= 1
            self.radost += 1
            print(f"{Fore.BLUE}Вы поиграли с зверушкой.")
        else:
            print(f"{Fore.RED}Зверушка голодна и не может играть.")

    def proverka_sostoyaniye(self):
        print(f"{Fore.YELLOW}Сытость: {self.sytost}")
        print(f"Радость: {self.radost}")

    def nach_igry(self):
        print(f"{Back.WHITE}{Fore.BLACK}Игра началась!")
        while self.sytost > 0 and self.radost > 0:
            print("\nВыберите действие:")
            print("1. Покормить зверушку")
            print("2. Поиграть с зверушкой")
            print("3. Проверить состояние зверушки")
            print("4. Завершить игру")

            choice = input("Ваш выбор: ")
            if choice == "1":
                self.kormit()
            elif choice == "2":
                self.играть()
            elif choice == "3":
                self.proverka_sostoyaniye()
            elif choice == "4":
                break
            else:
                print("Некорректный выбор, попробуйте снова.")

            self.sytost -= 1
            self.radost -= 1
            time.sleep(1)  # Задержка на 1 секунду

            if self.sytost == 0:
                print(f"{Fore.RED}Зверушка умерла от голода.")
                break

            if self.radost == 0:
                print(f"{Fore.MAGENTA}Зверушка погрустела и ушла.")
                break

        print(f"{Back.WHITE}{Fore.GREEN}Игра завершена.")

po = Zwerushka()
po.nach_igry()