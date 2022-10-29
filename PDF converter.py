from tkinter import *
from tkinter import filedialog as fd
from pdf2docx import parse
import pathlib


def callback():
    name = fd.askopenfilename()
    ePath.config(state='normal')
    ePath.delete('0', END)
    ePath.insert('1', name)
    ePath.config(state='readonly')


def converte():
    pdf_file = ePath.get()
    word_file = pathlib.Path(pdf_file)
    word_file = word_file.stem + '.docx'
    parse(pdf_file, word_file)
    Label(root, text='Готово', bg='gray', font='Arial 15 bold', fg='lime').pack(pady=10)


root = Tk()
root.title('Конвертер PDF to  Word')
root.geometry('400x300+300+300')
root.resizable(width=False, height=False)
root['bg'] = 'gray'

Button(root, text='Выбрать PDF', font='Arial 15 bold',
       fg='lime', bg='gray', command=callback).pack(pady=10)

lbPath = Label(root, text='Путь к файлу:', fg='lime', bg='gray', font='Arial 15 bold')
lbPath.pack()

ePath = Entry(root, width=60, state='readonly')
ePath.pack(pady=10)

btdConvert = Button(root, text='Конвертировать', font='Aria 15 bold',
                    fg='blue', bg='gray', command=converte).pack(pady=10)

root.mainloop()
