import functools
import os
import contextlib

def dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open(os.devnull, 'w') as fnull:
            with contextlib.redirect_stdout(fnull):
                return func(*args, **kwargs)
    return wrapper

def hp():
    hp = 100
    def changes_hp(sum):
        nonlocal hp
        hp += sum
        if hp > 100:
            hp = 100
            print("HP не может быть бодьше 100. Установлено на 100.")
        elif hp < 0:
            hp = 0
            print("HP не может быть меньше 0. Установлено на 0.")
        return hp
    return changes_hp
hero_hp = hp()

#@dec
def display_hp(hero):
    current_hp = hero(0)  # Получаем текущее HP без изменения
    print(f"Текущее HP героя: {current_hp}")  # Выводим текущее HP

def main():
    while True:
        display_hp(hero_hp)

        uron = int(input("Введите количество урона, который нужно нанести (или 0 для выхода): "))
        if uron == 0:
            break
        hill = -uron
        hero_hp(hill)

        hill_sum = int(input("Введите количество здоровья, которое нужно восстановить: "))
        hero_hp(hill_sum)
if __name__ == "__main__":
    main()