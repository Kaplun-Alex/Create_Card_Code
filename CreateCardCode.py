from tkinter import *
import tkinter.font
# import socket
# from threading import Thread
# import _thread
import pypyodbc

win = tkinter.Tk()
win.title("Create number")
win.geometry('600x450+100+100')
ButtonFont = tkinter.font.Font(family='Hervetica', size=10, weight='bold')
BigFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')
'''
db_host = '172.25.7.21\SQLEXPRESS'
db_name = 'NextAccess'
db_user = 'sa'
db_password = 'c9z1=XFEl,'

connection = ''
cursor = ''

connection = pypyodbc.connect(
    'Driver={SQL Server};''Server=' + db_host + ';''Database=' + db_name + ';''uid=' + db_user + ';''pwd=' + db_password + ';')
cursor = connection.cursor()


bratuha = "''"
chekSQLQuery = ("""select * from dbo.tblEmployees where colSurname = """+bratuha)
print(chekSQLQuery)

cursor.execute(chekSQLQuery)
results=cursor.fetchall()
'''


def chekbratuha():
    try:
        global bratuha
        bratuha = numberEntry.get()
        # bratuha = "'" + numberLabel.get() + "'"
        print(bratuha)
        cheksqlquery = (
                """select * from dbo.tblEmployees where colAccountNumber = """ + bratuha)  # - Проверка по индексу таблицы
        '''
        chekSQLQuery = ("""select * from dbo.tblEmployees where colSurname = """ + bratuha) # - Проверка по фамилии String
        '''
        print(cheksqlquery)
        cursor.execute(cheksqlquery)
        results = cursor.fetchone()
        print(results)
        if None == results:
            codeEntry.delete(0, END)
            statusEntry.delete(0, END)
            statusEntry.insert(0, 'Тіло не знайдене')
            stEntry.delete(0, END)
            stEntry.insert(0, 'Голяк, картки нема')
            print('Братуха відсутній в базі')
        else:
            statusEntry.delete(0, END)
            statusEntry.insert(0, 'Ништяяяк, це:' + ' ' + results[4] + ' ' + results[5])
            if results[1] == 0:
                stEntry.delete(0, END)
                stEntry.insert(0, 'Голяк, картки немає')
            else:
                codeEntry.delete(0, END)
                codeEntry.insert(0, results[1])
                stEntry.delete(0, END)
                stEntry.insert(0, 'Присутній')
                print('Братуха є в базі')
    except NameError:
        stEntry.delete(0, END)
        stEntry.insert(0, "ДО БАЗИ ПІД'ЄДНАЙСЯ ТЕЛЕПНЮ!")

def setCode():
    try:
        global numberEntry
        global codeEntry
        userid = numberEntry.get()
        print(userid)
        usercode = codeEntry.get()
        print(usercode)
        cursor.execute("""{CALL dbo.spSetCardNumber (""" + userid + """,""" + usercode + """,1)}""")
        cursor.commit()
    except NameError:
        stEntry.delete(0, END)
        stEntry.insert(0, "ДО БАЗИ ПІД'ЄДНАЙСЯ ТЕЛЕПНЮ!")

def chBaseSTB():
    closeconection()
    global cursor
    global connection
    db_host = '172.25.7.33'
    db_name = 'NextAccessAll'
    db_user = 'sa'
    db_password = 'Admin25112012'
    NOVYLabel.config(bg="#FF0000")
    STBLabel.config(bg="#00cc00")
    ICTVLabel.config(bg="#FF0000")
    try:
        connection = pypyodbc.connect(
            'Driver={SQL Server};''Server=' + db_host + ';''Database=' + db_name + ';''uid=' + db_user + ';''pwd=' + db_password + ';')
        cursor = connection.cursor()
        stEntry.delete(0, END)
        stEntry.insert(0, "Зв'язок з STB встановлено")
        return connection, cursor
    except:
        stEntry.delete(0, END)
        stEntry.insert(0, "Халепа! Зв'язок з STB відсутній")
        ICTVLabel.config(bg="#FF0000")
        STBLabel.config(bg="#FF0000")
        NOVYLabel.config(bg="#FF0000")


def chBaseNOVY():
    closeconection()
    global cursor
    global connection
    db_host = 'PROPUSK'
    db_name = 'NextAccess'
    db_user = 'sa'
    db_password = 'Admin25112012'
    NOVYLabel.config(bg="#00cc00")
    STBLabel.config(bg="#FF0000")
    ICTVLabel.config(bg="#FF0000")
    try:
        connection = pypyodbc.connect('Driver={SQL Server};''Server=' + db_host + ';''Database=' + db_name + ';''uid=' + db_user + ';''pwd=' + db_password + ';')
        cursor = connection.cursor()
        stEntry.delete(0, END)
        stEntry.insert(0, "Зв'язок з NOVY встановлено")
        return connection, cursor
    except:
        stEntry.delete(0, END)
        stEntry.insert(0, "Халепа! Зв'язок з NOVY відсутній")
        ICTVLabel.config(bg="#FF0000")
        STBLabel.config(bg="#FF0000")
        NOVYLabel.config(bg="#FF0000")


def chBaseICTV():
    closeconection()
    global cursor
    global connection
    db_host = '172.25.7.21\SQLEXPRESS'
    db_name = 'NextAccess'
    db_user = 'sa'
    db_password = 'c9z1=XFEl,'
    NOVYLabel.config(bg="#FF0000")
    STBLabel.config(bg="#FF0000")
    ICTVLabel.config(bg="#00cc00")
    try:
        connection = pypyodbc.connect('Driver={SQL Server};''Server=' + db_host + ';''Database=' + db_name + ';''uid=' + db_user + ';''pwd=' + db_password + ';')
        cursor = connection.cursor()
        stEntry.delete(0, END)
        stEntry.insert(0, "Зв'язок з ICTV встановлено")
        return connection, cursor
    except:
        stEntry.delete(0, END)
        stEntry.insert(0, "Халепа! Зв'язок з ICTV відсутній")
        ICTVLabel.config(bg="#FF0000")
        STBLabel.config(bg="#FF0000")
        NOVYLabel.config(bg="#FF0000")

def closeconection():
    try:
        connection.close()
    except NameError:
        print("Зв'язку не було")
def exitProgram():
    try:
        connection.close()
        win.destroy()
    except NameError:
        win.destroy()

stEntry = Entry(win, font=ButtonFont, bg='#C0C0C0')
stEntry.pack()
stEntry.place(x=20, y=420, height=20, width=460)
stEntry.delete(0, END)
stEntry.insert(0, 'Все заєбісь!')

numberEntry = Entry(win, font=ButtonFont)
numberEntry.pack()
numberEntry.place(x=20, y=150, height=40, width=250)

statusEntry = Entry(win, font=ButtonFont)
statusEntry.pack()
statusEntry.place(x=20, y=225, height=40, width=350)

codeEntry = Entry(win, font=ButtonFont)
codeEntry.pack()
codeEntry.place(x=20, y=305, height=40, width=200)

exitButton = Button(win, text="ВИХІД", font=ButtonFont, command=exitProgram, height=2, width=8)
exitButton.pack()
exitButton.place(x=515, y=400)

saveButton = Button(win, text="ЗАПИСАТИ БРАТУСІ НОВИЙ КОД КАРТКИ", font=ButtonFont, command=setCode, height=2,
                    width=35)
saveButton.pack()
saveButton.place(x=300, y=305)

chBratButton = Button(win, text='ПЕРЕВІРИТИ БРАТУХУ', font=ButtonFont, command=chekbratuha, height=2, width=20)
chBratButton.pack()
chBratButton.place(x=300, y=150)

nameLabel = Label(win, text='ПІБ Братухи', font=ButtonFont, justify=LEFT, width=30)
nameLabel.pack()
nameLabel.place(x=0, y=195)

numberLabel = Label(win, text='Внеси ID Братухи', font=ButtonFont, justify=LEFT, width=30)
numberLabel.pack()
numberLabel.place(x=0, y=125)

enterLabel = Label(win, text='Код картки!', font=ButtonFont, justify=LEFT, width=30)
enterLabel.pack()
enterLabel.place(x=0, y=275)

ICTVLabel = Label(win, text='БАЗА ICTV', font=ButtonFont, justify=LEFT, width=12)
ICTVLabel.pack()
ICTVLabel.place(x=460, y=20)

NOVYLabel = Label(win, text='БАЗА NOVY', font=ButtonFont, justify=LEFT, width=12)
NOVYLabel.pack()
NOVYLabel.place(x=250, y=20)

STBLabel = Label(win, text='БАЗА STB', font=ButtonFont, width=12)
STBLabel.pack()
STBLabel.place(x=30, y=20)

statusLabel = Label(win, text='Статус', font=ButtonFont, width=12)
statusLabel.pack()
statusLabel.place(x=0, y=390)

chSTBBase = Button(win, text="З'ЄДНАТИ", font=ButtonFont, command=chBaseSTB, height=1, width=10)
chSTBBase.pack()
chSTBBase.place(x=36, y=50)

chNOVYBase = Button(win, text="З'ЄДНАТИ", font=ButtonFont, command=chBaseNOVY, height=1, width=10)
chNOVYBase.pack()
chNOVYBase.place(x=256, y=50)

chICTVBase = Button(win, text="З'ЄДНАТИ", font=ButtonFont, command=chBaseICTV, height=1, width=10)
chICTVBase.pack()
chICTVBase.place(x=466, y=50)

mainloop()
