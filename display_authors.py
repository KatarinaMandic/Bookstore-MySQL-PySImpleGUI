import mysql.connector as con
from bookstore_pack.Author import Author
import PySimpleGUI as sg

db = con.connect(
    host = 'localhost',
    port = 3306,
    user = 'pyadmin2',
    password = '1234',
    database = 'py_bookstore'
)

c = db.cursor(dictionary=True)
c.execute('SELECT * FROM authors;')
records = c.fetchall()

authors = []
for r in records:
    authors.append(Author(r))

sg.theme('DarkBlue')

layout = [ 
    [sg.Combo(authors, key = '_AUTHOR_'), sg.Button('Display Photo')],
    [sg.Image(key = '_PHOTO_')]
]

window = sg.Window('Authors', layout = layout, font = ('Arial', 20))

while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'Display Photo':
        author = values['_AUTHOR_']
        window['_PHOTO_'].Update(data = author.photo)
window.close()