from tkinter import *                       # импортируем библиотеки
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import random
import time

window = Tk() # создаем окно


window.geometry("780x450")     # устанавливаем размер окна
window.resizable(False, False) # запрещаем изменение размера окна

EditL = Entry(text = '0', font = ('Arial', 30)) # создаем  окно ввода
EditL.place(x = 460, y = 0, width = 320, height = 100) # распологаем окно
EditL.insert(0, '0') # выставляем значение окна

Kof = 0      # переменная которая отвечает за кофициент сложности
RNO_num = 0 
Score_num = 0 # переменная счета
Rand_num = 0 


file = open("Score.txt", "a") # создаем файл счета



def add_digit(digit):       # функции отвечаущая за дополнения чисел ввода
	global EditL
	value = EditL.get()
	if value[0] == '0' and len(value) == 1:
		value = value[1:]
	EditL.delete(0, tk.END)
	EditL.insert(0, value + digit)





def make_digit(digit):    # функция создания кнопок
	return Button(text = digit, font = ('Arial', 30), activebackground = 'grey', command = lambda: add_digit(digit))



def start():           # функция отвечающая за кнопку старт
	global RNO_num       # глобализируем переменные чтобы их можно было использовать в фунции
	global Rand_num
	global Kof

	R1 = 0		# рандомное число 1
	R2 = 0		# рандомное число 2
	a = False
	b = False


	# проверяем выбраную сложность (выбираем верхнюю границу чисел)
	if Difficult_list.get() == 'Очень легко':
		Rand_num = 100
		Kof = 0.5
		a = True
	elif Difficult_list.get() == 'Легко':
		Rand_num = 1000
		Kof = 1
		a = True
	elif Difficult_list.get() == 'Сложно':
		Rand_num = 10000
		Kof = 1.5
		a = True		
	elif Difficult_list.get() == 'Очень сложно':
		Rand_num = 100000
		Kof = 2
		a = True
	elif Difficult_list.get() == 'Нереально':
		Rand_num = 10000000
		Kof = 2.5
		a = True
	else:
		Helps.config(text = "Выбери знак и сложность.")
	
	# рандомизируем 1 и 2 число
	R1 = random.randint(0, Rand_num)
	R2 = random.randint(0, Rand_num)



	# вычисляем ответ
	if Sign_list.get() == '+':
		b = True
		First_num.config(text = str(R1))
		Second_num.config(text = str(R2))

		while (R1 + R2) > Rand_num:
			R1 = random.randint(0, Rand_num)
			R2 = random.randint(0, Rand_num)
			First_num.config(text = str(R1))
			Second_num.config(text = str(R2))
			RNO_num = R1 + R2

		RNO_num = R1 + R2
		Sign.config(text = '+')

	elif Sign_list.get() == '-':
		b = True
		Sign.config(text = '-')

		First_num.config(text = str(R1))
		Second_num.config(text = str(R2))

		while R2 > R1:
			R1 = random.randint(0, Rand_num)
			R2 = random.randint(0, Rand_num)
			First_num.config(text = str(R1))
			Second_num.config(text = str(R2))

		RNO_num = R1 - R2

	elif Sign_list.get() == '*':
		b = True
		First_num.config(text = str(R1))
		Second_num.config(text = str(R2))

		while (R1 * R2) > Rand_num:
			R1 = random.randint(0, Rand_num / 10)
			R2 = random.randint(0, Rand_num / 10)
			First_num.config(text = str(R1))
			Second_num.config(text = str(R2))
			RNO_num = R1 * R2
		
		RNO_num = R1 * R2
		Sign.config(text = '*')

	elif Sign_list.get() == '/':
		b = True
		Sign.config(text = '/')

		First_num.config(text = str(R1))
		Second_num.config(text = str(R2))

		while (R2 == 0) or (R1 % R2):
			R1 = random.randint(0, Rand_num)
			R2 = random.randint(0, Rand_num)
			First_num.config(text = str(R1))
			Second_num.config(text = str(R2))

		RNO_num = R1 / R2

	else:
		Helps.config(text = "Выбери знак и сложность.")
	if a and b:
		Enter['state'] = 'normal'
	





# функция кнопки Enter (ввод)
def enter_f():
	global RNO_num	 # глобализируем переменные чтобы их можно было использовать в фунции
	global Score_num
	global Kof

	# сравниваем введенный ответ с ответом полученым выше и ввыводим правильно или не правильно 
	if RNO_num == int(float(EditL.get())):
		Helps.config(text = "Это верно!")
		Score_num = Score_num + Kof
		Score_num1 = Score_num
		Score.config(text = str(round(Score_num1)))
		
	else:
		Helps.config(text = "Неправильно! Ответ: " + str(int(RNO_num)))
		Score_num = Score_num - Kof
		Score_num1 = Score_num
		Score.config(text = str(round(Score_num1)))

	# запускаем функцию старт, чтобы заново рандомизировать числа
	start()

	# удаляем все с поля ввода и выставляем там 0
	EditL.delete(0, tk.END)
	EditL.insert(0, '0')

# функция отвечающая за удаление чисел с поля ввода
def deleted():
	global EditL
	EditL.delete(0, tk.END) 
	EditL.insert(0, '0')

# функция "помощи"
def help1():
	messagebox.showwarning("Помощь", "Да тут все интуитивно понятно. Разбирайся сам!")




def sbros_f():
	global R1 			# глобализируем переменные чтобы их можно было использовать в фунции
	global Score_num
	global R2
	Score_num = 0
	R1 = 0
	R2 = 0

	Enter['state'] = 'disabled'

	Helps.config(text = "Выбери знак и сложность.")
	Score.config(text = '0')
	First_num.config(text = '0')
	Second_num.config(text = '0')
	Sign.config(text = '?')
	Sign_list.set("Выбери знак")
	Difficult_list.set("Выбири сложность")

# функция выхода
def exit_f():
	if messagebox.askyesno("Выход", "Вы хотите выйти?"):
		on_closing()

		

# функция отвечающая за сохранение данных
def on_closing():
	global Score_num
	today = time.strftime("%Y-%m-%d %H:%M", time.localtime())

	if Score_num == 1 or Score_num == -1:
		txt1 = ' '
	elif (Score_num > 1 and Score_num < 5) or (Score_num < -1 and Score_num > -5):
		txt1 = 'а'
	elif Score_num >= 5 or Score_num == 0 or Score_num <= -5:
		txt1 = 'ов'

	if messagebox.askyesno("Выход", "Вы хотите сохранить данные?"):
		file.write("\n" + today + " " + str(int(Score_num)) + " Балл" + txt1)
		window.destroy()

	else:
		window.destroy()



# метка вывода печвого числа
First_num = Label(text = '0', font = ('Arial', 30))
First_num.place(x = 0, y = 0, width = 170, height = 100)

# метка вывода знака
Sign = Label(text = '?', font = ('Arial', 30))
Sign.place(x = 170, y = 0, width = 80, height = 100)

# метка вывода второго числа
Second_num = Label(text = '0', font = ('Arial', 30))
Second_num.place(x = 250, y = 0, width = 170, height = 100)

# метка вывода равно
RNO = Label(text = '=', font = ('Arial', 30)).place(x = 420, y = 0, width = 40, height = 100)

# метка вывода правильных значений, небольшой помощи и правильность решения (правильно, не правильно)
Helps = Label(text = 'Выбери знак и сложность.', font = ('Arial', 30))
Helps.place(x = 0, y = 100, width = 780, height = 70)


# создание кнопок по функции
make_digit('1').place(x = 390, y = 170, width = 70, height = 70)
make_digit('2').place(x = 460, y = 170, width = 70, height = 70)
make_digit('3').place(x = 530, y = 170, width = 70, height = 70)
make_digit('4').place(x = 390, y = 240, width = 70, height = 70)
make_digit('5').place(x = 460, y = 240, width = 70, height = 70)
make_digit('6').place(x = 530, y = 240, width = 70, height = 70)
make_digit('7').place(x = 390, y = 310, width = 70, height = 70)
make_digit('8').place(x = 460, y = 310, width = 70, height = 70)
make_digit('9').place(x = 530, y = 310, width = 70, height = 70)
make_digit('0').place(x = 460, y = 380, width = 70, height = 70)

# кнопка старт
B_Start = Button(text = 'Начать', font = ('Arial', 30), activebackground = 'white', command = start).place(x = 600, y = 310, width = 180, height = 70)

# кнопка помощи
B_Help = Button(text = 'Помощь', font = ('Arial', 30), activebackground = 'white', command = help1).place(x = 0, y = 310, width = 180, height = 70)

# кнопка сброса
B_Sbros = Button(text = 'Сброс', font = ('Arial', 30), activebackground = 'white', command = sbros_f).place(x = 600, y = 380, width = 180, height = 70)

# кнопка выхода
B_Exit = Button(text = 'Выход', font = ('Arial', 30), activebackground = 'white', command = exit_f).place(x = 0, y = 380, width = 180, height = 70)

# кнопка ввода
Enter = Button(text = '⤶', font = ('Arial', 30), activebackground = 'grey', command = enter_f, state = DISABLED)
Enter.place(x = 530, y = 380, width = 70, height = 70)

# кнопка удаление с поля ввода
Del = Button(text = '←', font = ('Arial', 30), activebackground = 'grey', command = deleted).place(x = 390, y = 380, width = 70, height = 70)

# метка счета
Score = Label(text = '0', font = ('Arial', 30), bg = 'grey80', fg = 'black')
Score.place(x = 600, y = 170, width = 180, height = 140)

# создаем выпадающий список знаков
Sign_list = ttk.Combobox(state = "readonly", values = ["+", "-","*","/"], font = ('Arial', 30))
Sign_list.place(x = 0, y = 170, width = 390, height = 70)
Sign_list.set("Выбери знак")

# создаем выпадающий список сложностей
Difficult_list = ttk.Combobox(state = "readonly", values = ["Очень легко", "Легко", "Сложно", "Очень сложно", "Нереально"], font = ('Arial', 30))
Difficult_list.place(x = 0, y = 240, width = 390, height = 70)
Difficult_list.set("Выбири сложность")





# протокол закрытия который ДОЛЖЕН что-то делать
window.protocol("WM_DELETE_WINDOW", exit_f)

# зацикливаем окно
window.mainloop()

# закрываем файл
file.close()