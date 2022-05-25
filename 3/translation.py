#pip install googletrans==3.1.0a0

from tkinter import *
from googletrans import Translator

window = Tk()
window.geometry('600x400')
window.title('Переводчик')
window.resizable(width=False, height=False)
window['bg'] = 'black'

lang = 'en'


def changeToRu():
    global lang
    lang = 'ru'

def changeToEn():
    global lang
    lang = 'en'

translator = Translator()
def translate():
    global lang
    input = text1.get('1.0', END)
    result = translator.translate(input, dest=lang)
    text2.delete('1.0', END)
    text2.insert('1.0', result.text)


label = Label(window,
              bg='black',
              fg='white',
              font='Arial 16 bold',
              text='Введите текст для перевода'
              )
label.place(relx=0.5, y=30, anchor=CENTER)

text1 = Text(window,
             width=40,
             height=5,
             font='Arial 12'
             )
text1.place(relx=0.5, y=100, anchor=CENTER)

buttonRu = Button(window,
                  bg='lime',
                  fg='white',
                  font='Arial 16 bold',
                  text='RU',
                  command=changeToRu
                )
buttonRu.place(relx=0.3, y=200, anchor=CENTER)

button = Button(window,
                bg='red',
                fg='white',
                font='Arial 16 bold',
                text='Перевод',
                command=translate
                )
button.place(relx=0.5, y=200, anchor=CENTER)

buttonEn = Button(window,
                  bg='blue',
                  fg='white',
                  font='Arial 16 bold',
                  text='EN',
                  command=changeToEn
                  )
buttonEn.place(relx=0.7, y=200, anchor=CENTER)

text2 = Text(window,
             width=40,
             height=5,
             font='Arial 12'
             )
text2.place(relx=0.5, y=330, anchor=CENTER)







window.mainloop()
