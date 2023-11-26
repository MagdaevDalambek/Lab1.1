print("Magdaev Dalambek")
def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} * {j} = {i*j}")
            print("\n")

multiplication_table(5)  # Вывод таблицы умножения до 5