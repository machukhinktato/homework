#coding utf-8

print('Вас привествует программа по анализу Вашего здоровья')
name = input('Ваше имя? ')
family = input('Ваша фамилия? ')
age = int(input('Сколько Вам лет? '))
weight = int(input('Какой Ваш вес в настоящий момент? '))

if age <= 40 and weight > 50 or weight < 120:
    print('Уважаемый',name, family, 'Вам', age, 'при весе', weight, 'кг, у Вас замечательные показатели!')
else:
    print('Уважаемый',name, family, 'Вам', age, 'при весе', weight, 'Вам следует обратиться к врачу на осмотр!')