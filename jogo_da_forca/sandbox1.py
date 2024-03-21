from tkinter import *
from ttkthemes import ThemedTk
from tkinter import messagebox
from re import sub as resub
from re import match
"import win32gui, win32con"
from functools import partial
from string import ascii_uppercase, ascii_lowercase, digits
from sys import executable, argv
from os import execl

# Game variables
letra = {}
palavra = ''
can_start = False
letras_acertadas = ''
ascii_uppercase = ''.join(ascii_uppercase + 'áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ')


def start_game(*args, **kwargs):
    global palavra
    global can_start
    palavra = texx.get().upper().split()

    while '' in palavra:
        for space in palavra:
            if space == '':
                palavra.pop(palavra.index(space))
    iteration = len(palavra)
    backup = [[], []]
    while iteration > 0:
        for index, word in enumerate(palavra):
            if len(word) > 0:
                backup[0].append(index)
                backup[1].append(word)
                palavra.insert(palavra.index(word) + 1, ' ')
                palavra.remove(word)
            iteration -= 1
    plus = 0
    for i in range(len(palavra)):
        palavra.insert(backup[0][i] + plus, backup[1][i])
        plus += 1

    palavra = resub(pattern='[ ]', repl='  ', string=''.join(palavra))
    have_number = match(pattern=f'.*[{digits}].*', string=palavra)
    if len(texx.get()) > 0 and not have_number:
        tela_palavra.destroy()
        can_start = True
    else:
        messagebox.showerror('error', 'A palavra não pode conter digitos ou estar vazia!')
        can_start = False


tela_palavra = Tk()

x = 300
y = 200

sx = (tela_palavra.winfo_screenwidth() / 2) - (x / 2)
sy = (tela_palavra.winfo_screenheight() / 2) - (y / 2)

tela_palavra.config(bg='cyan')
tela_palavra.title('Esolha uma palavra')
tela_palavra.geometry(f'{x}x{y}+{sx:.0f}+{sy:.0f}')
tela_palavra.resizable(False, False)
tela_palavra.focus_set()
tela_palavra.bind("<Return>", start_game)

Label(tela_palavra, text='ESCOLHA UMA PALAVRA', bg='cyan', font='Ivy 16 bold').pack(fill=X, side=TOP)

texx = Entry(tela_palavra, width=x, relief='solid')
texx.pack(fill=X, side=TOP, padx=5)
texx.focus_set()

Button(tela_palavra, text='COMEÇAR JOGO', relief='solid', font='Ivy 14 bold',
       padx=10, pady=20, command=start_game).pack(side=BOTTOM)

tela_palavra.mainloop()

chances = 6


# Functions
def verificar(letter, *args):
    global letras_acertadas
    global chances

    if type(letter) != str:
        letter = str(letter.char).upper()

    vogals = ['A', 'E', 'I', 'O', 'U']
    special_A: list = ['á', 'Á', 'à', 'À', 'â', 'Â', 'ã', 'Ã']
    special_E: list = ['é', 'É', 'è', 'È', 'ê', 'Ê']
    special_I: list = ['í', 'Í', 'ì', 'Ì', 'î', 'Î']
    special_O: list = ['ó', 'Ó', 'ò', 'Ò', 'ô', 'Ô', 'õ', 'Õ']
    special_U: list = ['ú', 'Ú', 'ù', 'Ù', 'û', 'Û']
    special_chars: list = ['ç', 'C', 'Ç']
    finded = False

    if letter in palavra and letter not in vogals and letter != 'C':
        letras_acertadas += letter
        letra[letter]['bg'] = 'green'
        letra[letter]['state'] = 'disabled'
        app.unbind(f"<Key-{letter.lower()}>")
        modal['text'] = f'TEM LETRA {letter}!'
        modal['fg'] = 'green'
        palavra_advinhada = resub(pattern=f'[^{letras_acertadas} ]', repl=' ', string=palavra)
    elif letter not in palavra or letter in vogals or letter == 'C':
        if letter == 'A':
            for l in palavra:
                if l in special_A or l == 'A':
                    letras_acertadas += f'{vogals[0]}'.join([a for a in special_A])
                    letra[letter]['bg'] = 'green'
                    letra[letter]['state'] = 'disabled'
                    app.unbind(f"<Key-{letter}>")
                    modal['text'] = f'TEM LETRA {letter.lower()}!'
                    modal['fg'] = 'green'
                    palavra_advinhada = resub(pattern=f'[^{letras_acertadas} ]', repl=' ', string=palavra)
                    finded = True
                    break
                else:
                    finded = False
            if not finded:
                chances -= 1
                letra[letter]['bg'] = 'red'
                letra[letter]['state'] = 'disabled'
                app.unbind(f"<Key-{letter.lower()}>")
                modal['text'] = f'NÃO TEM LETRA {letter}\nCHANCES {chances + 1} -> {chances}'
                modal['fg'] = 'red'
                chan['text'] = f'CHANCES: {chances}'
        elif letter == 'E':
            for l in palavra:
                if l in special_E or l == 'E':
                    letras_acertadas += f'{vogals[1]}'.join([a for a in special_E])
                    letra[letter]['bg'] = 'green'
                    letra[letter]['state'] = 'disabled'
                    app.unbind(f"<Key-{letter.lower()}>")
                    modal['text'] = f'TEM LETRA {letter}!'
                    modal['fg'] = 'green'
                    palavra_advinhada = resub(pattern=f'[^{letras_acertadas} ]', repl=' ', string=palavra)
                    finded = True
                    break
                else:
                    finded = False
            if not finded:
                chances -= 1
                letra[letter]['bg'] = 'red'
                letra[letter]['state'] = 'disabled'
                app.unbind(f"<Key-{letter.lower()}>")
                modal['text'] = f'NÃO TEM LETRA {letter}\nCHANCES {chances + 1} -> {chances}'
                modal['fg'] = 'red'
                chan['text'] = f'CHANCES: {chances}'
        elif letter == 'I':
            for l in palavra:
                if l in special_I or l == 'I':
                    letras_acertadas += f'{vogals[2]}'.join([a for a in special_I])
                    letra[letter]['bg'] = 'green'
                    letra[letter]['state'] = 'disabled'
                    app.unbind(f"<Key-{letter.lower()}>")
                    modal['text'] = f'TEM LETRA {letter}!'
                    modal['fg'] = 'green'
                    palavra_advinhada = resub(pattern=f'[^{letras_acertadas} ]', repl=' ', string=palavra)
                    finded = True
                    break
                else:
                    finded = False
            if not finded:
                chances -= 1
                letra[letter]['bg'] = 'red'
                letra[letter]['state'] = 'disabled'
                app.unbind(f"<Key-{letter.lower()}>")
                modal['text'] = f'NÃO TEM LETRA {letter}\nCHANCES {chances + 1} -> {chances}'
                modal['fg'] = 'red'
                chan['text'] = f'CHANCES: {chances}'
        elif letter == 'O':
            for l in palavra:
                if l in special_O or l == 'O':
                    letras_acertadas += f'{vogals[3]}'.join([a for a in special_O])
                    letra[letter]['bg'] = 'green'
                    letra[letter]['state'] = 'disabled'
                    app.unbind(f"<Key-{letter.lower()}>")
                    modal['text'] = f'TEM LETRA {letter}!'
                    modal['fg'] = 'green'
                    palavra_advinhada = resub(pattern=f'[^{letras_acertadas} ]', repl=' ', string=palavra)
                    finded = True
                    break
                else:
                    finded = False
            if not finded:
                chances -= 1
                letra[letter]['bg'] = 'red'
                letra[letter]['state'] = 'disabled'
                app.unbind(f"<Key-{letter.lower()}>")
                modal['text'] = f'NÃO TEM LETRA {letter}\nCHANCES {chances + 1} -> {chances}'
                modal['fg'] = 'red'
                chan['text'] = f'CHANCES: {chances}'
        elif letter == 'U':
            for l in palavra:
                if l in special_U or l == 'U':
                    letras_acertadas += f'{vogals[4]}'.join([a for a in special_U])
                    letra[letter]['bg'] = 'green'
                    letra[letter]['state'] = 'disabled'
                    app.unbind(f"<Key-{letter.lower()}>")
                    modal['text'] = f'TEM LETRA {letter}!'
                    modal['fg'] = 'green'
                    palavra_advinhada = resub(pattern=f'[^{letras_acertadas} ]', repl=' ', string=palavra)
                    finded = True
                    break
                else:
                    finded = False
            if not finded:
                chances -= 1
                letra[letter]['bg'] = 'red'
                letra[letter]['state'] = 'disabled'
                app.unbind(f"<Key-{letter.lower()}>")
                modal['text'] = f'NÃO TEM LETRA {letter}\nCHANCES {chances + 1} -> {chances}'
                modal['fg'] = 'red'
                chan['text'] = f'CHANCES: {chances}'
        elif letter == 'C':
            for l in palavra:
                if l in special_chars:
                    letras_acertadas += 'C'.join([a for a in special_chars])
                    letra[letter]['bg'] = 'green'
                    letra[letter]['state'] = 'disabled'
                    app.unbind(f"<Key-{letter.lower()}>")
                    modal['text'] = f'TEM LETRA {letter}!'
                    modal['fg'] = 'green'
                    palavra_advinhada = resub(pattern=f'[^{letras_acertadas} ]', repl=' ', string=palavra)
                    finded = True
                    break
                else:
                    finded = False
            if not finded:
                chances -= 1
                letra[letter]['bg'] = 'red'
                letra[letter]['state'] = 'disabled'
                app.unbind(f"<Key-{letter.lower()}>")
                modal['text'] = f'NÃO TEM LETRA {letter}\nCHANCES {chances + 1} -> {chances}'
                modal['fg'] = 'red'
                chan['text'] = f'CHANCES: {chances}'
        else:
            chances -= 1
            letra[letter]['bg'] = 'red'
            letra[letter]['state'] = 'disabled'
            app.unbind(f"<Key-{letter.lower()}>")
            modal['text'] = f'NÃO TEM LETRA {letter}\nCHANCES {chances + 1} -> {chances}'
            modal['fg'] = 'red'
            chan['text'] = f'CHANCES: {chances}'
    if chances == 0:
        messagebox.showinfo('DERROTA', 'VOCÊ PERDEU')
        for btn in letra.keys():
            letra[btn]['state'] = 'disabled'
        close_button.grid(row=4, column=0, columnspan=13, sticky=NSEW, pady=1)
        for letter in ascii_lowercase:
            app.unbind(f"<Key-{letter}>")
        app.bind('<Return>', restart_game)
    try:
        if palavra_advinhada == palavra:
            messagebox.showinfo('VITÓRIA', 'VOCÊ GANHOU')
            for btn in letra.keys():
                letra[btn]['state'] = 'disabled'
            close_button.grid(row=4, column=0, columnspan=13, sticky=NSEW, pady=20)
            for letter in ascii_lowercase:
                app.unbind(f"<Key-{letter}>")
            app.bind('<Return>', restart_game)
    except UnboundLocalError:
        pass
    palavra_label['text'] = resub(pattern=f'[^{letras_acertadas} ]', repl='_ ', string=palavra)


def restart_game(*args):
    python = executable
    execl(python, python, *argv)


if not can_start:
    exit(0)

"""
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)


def close_window(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    

window = win32gui.GetForegroundWindow()
close_window(window)
"""


# Creating window
app = ThemedTk(theme='black')

x = 900
y = 600

sx = (app.winfo_screenwidth() / 2) - (x / 2)
sy = (app.winfo_screenheight() / 2) - (y / 2)

# Window configurations
app.geometry(f'{x}x{y}+{sx:.0f}+{sy:.0f}')
app.title('Jogo da Forca')
app.resizable(False, False)
app.after(1, app.focus_force())

for letter in ascii_lowercase:
    app.bind(f'<Key-{letter}>', verificar)

# Container
container = Frame(app, bg='cyan')
container.pack(fill=BOTH, expand=True)

# Frames
title = Frame(container, bg='cyan', width=560, height=40)
title.grid(row=0, column=0, columnspan=1)

palavra_f = Frame(container, bg='cyan', width=560, height=100)
palavra_f.grid(row=1, column=0, columnspan=1)

principal = Frame(container, bg='cyan', width=560, height=360)
principal.grid(row=3, column=0, columnspan=1, pady=10)

# Labels
text_title = Label(title, text='JOGO DA FORCA', bg='cyan',
                   fg='black', font='Ivy 15 bold', anchor='center')
text_title.grid(row=0, column=0, sticky=NSEW)

palavra_label = Label(palavra_f, text=resub(pattern=f'[{ascii_uppercase}]', repl='_ ', string=palavra),
                      bg='white', width=68, height=4,
                      relief='solid', font='Ivy 16 bold', anchor='center')
palavra_label.grid(row=0, column=0, sticky=NSEW, padx=5)

chan = Label(container, text=f'CHANCES: {chances}', bg='cyan', font='Ivy 12 bold', anchor='center')
chan.grid(row=2, column=0, sticky=NSEW)

modal = Label(principal, text='', bg='cyan', fg='black', font='Ivy 15 bold', anchor='center')
modal.grid(row=3, column=0, columnspan=13, sticky=NSEW, pady=75)

# Creating buttons
i = 0
for letter in ascii_uppercase:
    i += 1
    letra[letter] = Button(principal, text=f'{letter}', relief='solid', font='Ivy 14 bold',
                           width=4, height=2, command=partial(verificar, letter))
    if i == 26:
        break

(lin, col) = (0, 0)
for key in letra.keys():
    if col == 13:
        col = 0
        lin = 1
    letra[key].grid(row=lin, column=col, padx=2, pady=5)
    col += 1

close_button = Button(principal, text='RECOMEÇAR', relief='solid',
                      width=5, height=3, command=restart_game)

# Main loop
app.mainloop()
