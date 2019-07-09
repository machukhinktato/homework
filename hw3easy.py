# Первая задача


def id_info(name, age, city):
    print(name, ",", age, "год(а), проживает в городе", city)


name = input("Добрый День, укажите пожалуйста Ваше имя: ")
age = input("Сколько Вам лет: ")
city = input("В каком городе проживаете: ")
id_info(name, age, city)


# Вторая задача


def check_bigger_num(first_num, second_num, third_num):
    print(max(first_num, second_num, third_num))


num1 = input("Пожалуйста введите первое число: ")
num2 = input("Пожалуйста введите второе число: ")
num3 = input("Пожалуйста введите третье число: ")
check_bigger_num(num1, num2, num3)

# Третья задача

y = "y"
n = "n"
st_list = []
print("Эта программа позволит Вам измерить количечство строковых аргументов!")
answer = input("Вы готовы? (y/n)")
while answer == y:
    answer = input("Добавьте строчный элемент: ")
    st_list.append(answer)
    answer = input("Продолжаем? (y/n)")

print("Самым тяжелым элементов оказался: ", (max(st_list)))


