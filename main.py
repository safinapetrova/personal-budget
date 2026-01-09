from data_loader import create_sample_budget_data, load_budget_transactions
from reports import (
    generate_income_report_last_n_days,
    generate_expense_report_by_category,
    generate_expense_report_in_time_interval,
)


def display_main_menu():
    """Отображает главное меню программы."""
    print("\n" + "=" * 60)
    print(" Персональный бюджет — Главное меню")
    print("=" * 60)
    print("1. Просмотреть все транзакции")
    print("2. Отчёт 1: Поступления за N дней")
    print("3. Отчёт 2: Затраты по категории")
    print("4. Отчёт 3: Затраты в интервале времени")
    print("5. Выход")
    print("-" * 60)


def wait_for_user_to_return():
    """Ожидает нажатия Enter для возврата в меню."""
    input("\nНажмите Enter, чтобы вернуться в главное меню...")


def main():
    """Главная функция программы. Запускает цикл меню."""
    print("Добро пожаловать в программу 'Персональный бюджет'")
    create_sample_budget_data()

    while True:
        display_main_menu()
        user_choice = input("Выберите действие (1-5): ").strip()

        if user_choice == "1":
            transactions = load_budget_transactions()
            if transactions is None:
                print(" Не удалось загрузить данные.")
            else:
                print(f"\n Всего транзакций: {len(transactions)}")
                print(f"\n{'Дата':<10} | {'Время':<8} | {'Направление':<12} | "
                      f"{'Категория':<15} | {'Сумма':>8} | {'Контрагент':<25}")
                print("-" * 80)
                for transaction in transactions:
                    print(
                        f"{transaction['date']:<10} | "
                        f"{transaction['time']:<8} | "
                        f"{transaction['direction']:<12} | "
                        f"{transaction['category']:<15} | "
                        f"{transaction['amount']:>8.2f} | "
                        f"{transaction['counterparty']:<25}"
                    )
            wait_for_user_to_return()

        elif user_choice == "2":
            n_input = input("Введите количество дней N (например, 3): ").strip()
            if not n_input.isdigit():
                print("  N должно быть целым неотрицательным числом.")
            else:
                n_days = int(n_input)
                transactions = load_budget_transactions()
                if transactions is not None:
                    generate_income_report_last_n_days(transactions, n_days)
            wait_for_user_to_return()

        elif user_choice == "3":
            category = input(
                "Введите категорию (например, питание, транспорт): "
            ).strip()
            if not category:
                print("  Категория не может быть пустой.")
            else:
                transactions = load_budget_transactions()
                if transactions is not None:
                    generate_expense_report_by_category(transactions, category)
            wait_for_user_to_return()

        elif user_choice == "4":
            start = input("Начало интервала (HH:MM, например 18:00): ").strip()
            end = input("Конец интервала (HH:MM, например 21:00): ").strip()
            if not start or not end:
                print("  Интервал не может быть пустым.")
            else:
                transactions = load_budget_transactions()
                if transactions is not None:
                    generate_expense_report_in_time_interval(transactions, start, end)
            wait_for_user_to_return()

        elif user_choice == "5":
            print(" До свидания! Бюджет сохранён.")
            break

        else:
            print("  Некорректный выбор. Введите 1, 2, 3, 4 или 5.")
            wait_for_user_to_return()


if __name__ == "__main__":
    main()
