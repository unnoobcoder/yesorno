import tkinter
from random import randint
root = tkinter.Tk()
root.title('Yes or no?')
root.geometry('500x300')
start_label = tkinter.Label(root, text='Pres enter to start please', font=('Arial', 11))
start_label.pack()
standardPhoto = tkinter.PhotoImage(file='hawking.gif')
yesPhoto = tkinter.PhotoImage(file='yes.gif')
noPhoto = tkinter.PhotoImage(file='no.gif')
yesnoPhoto = tkinter.Label(root, image=(standardPhoto))
yesnoPhoto.pack()
x = randint(27,100)
answer = 'default'
if (x % 2) == 0:
    oddX = True
else:
    oddX = False
def startingProgram(event):
    calculate()
    displayImage()

def calculate():
    
    global answer
    if oddX == True:
        answer = 'yes'

def displayImage():
    global answer

    if answer == 'yes':
        yesnoPhoto.config(image = yesPhoto)
    else:
        yesnoPhoto.config(image = noPhoto)
root.bind('<Return>', startingProgram)
root.mainloop()
print(x)
print(oddX)


