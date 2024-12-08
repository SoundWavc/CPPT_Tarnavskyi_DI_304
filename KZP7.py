# Запитуємо у користувача розмір квадрата
n_rows = int(input("Введіть розмір квадрата: "))

# Запитуємо у користувача символ для заповнення квадрата
symbol = input("Введіть символ для заповнення: ")

if len(symbol) == 0:
    print("Некорректний символ. Відсутній символ.")
    exit()
elif len(symbol) > 1:
    print("Некорректний ввід. Забагато символів.")
    exit()

symbol = symbol[0]

# Створюємо двовимірний масив для зберігання символів квадрата
arr = []
arrIndx = 1 if n_rows % 2 == 1 else 2
for i in range(n_rows):
    if i >= n_rows // 2:
        arr.append([symbol] * arrIndx)
        arrIndx+=2

# Заповнюємо квадрат символами
for i in range(n_rows):
    arrIndx = 0
    for j in range(n_rows):
        # Заповнюємо квадрат за допомогою символу або пробілу
        if (i >= n_rows // 2 and (j >= n_rows - i - 1 and j <= i)):
            print(arr[i - (n_rows // 2)][arrIndx], end='')
            arrIndx+=1
        else:
            print(' ', end='')
    # Додаємо новий рядок на екран
    print()