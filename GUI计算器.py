import tkinter as tk
import os
from tkinter import messagebox as me

window=tk.Tk()
window.geometry('400x320')
window.title('计算器')
window.resizable(0, 0)

contentVar = tk.StringVar(window, '')
a=tk.Entry(window,textvariable=contentVar)
a.place(x=10,y=10,width=190,height=40)
a['state'] = 'readonly'


contentVar2 = tk.StringVar(window, '')
b=tk.Entry(window,textvariable=contentVar2)
b.place(x=190,y=10,width=190,height=40)
b['state'] = 'readonly'

def but(i):

    operation = ('+', '-', '*', '/', '.','(',')','%','//','^' )
    content = contentVar.get()
    if i in '0123456789':
        content+=i

    elif i in operation:
        content += i

    elif i == '=':
        try:
            # 对输入的表达式求值
            answer = str(eval(content))
            contentVar2.set(answer)
            content += '='

            #保存数据
            with open('b.txt', 'a', encoding='utf-8') as wfile:
                wfile.write(content)
                wfile.write(answer)
                wfile.write('\n')
        except:
            tk.messagebox.showerror('错误', '表达式有误')
            return

    elif i == 'AC':
        #清除文本框
        content = ''
        contentVar2.set('')

    contentVar.set(content)

def back():
        content2 = contentVar.get()
        contentVar.set(content2[:-1])

def show():
    if os.path.exists('b.txt'):
        os.startfile('b.txt')
    else:
        me.showwarning(message='没有任何数据')


n1=tk.Button(window,text='AC',command=lambda :but('AC'))
n1.place(x=10,y=60,width=90,height=40)

n2=tk.Button(window,text='+',command=lambda :but('+'))
n2.place(x=280,y=60,width=120,height=40)

n3=tk.Button(window,text='7',command=lambda:but('7'))
n3.place(x=10,y=100,width=90,height=40)

n4=tk.Button(window,text='8',command=lambda :but('8'))
n4.place(x=100,y=100,width=90,height=40)

n5=tk.Button(window,text='9',command=lambda :but('9'))
n5.place(x=190,y=100,width=90,height=40)

n6=tk.Button(window,text='---',command=lambda :but('-'))
n6.place(x=280,y=100,width=120,height=40)

n7=tk.Button(window,text='4',command=lambda :but('4'))
n7.place(x=10,y=140,width=90,height=40)

n8=tk.Button(window,text='5',command=lambda :but('5'))
n8.place(x=100,y=140,width=90,height=40)

n9=tk.Button(window,text='6',command=lambda :but('6'))
n9.place(x=190,y=140,width=90,height=40)

n10=tk.Button(window,text='*',command=lambda :but('*'))
n10.place(x=280,y=140,width=120,height=40)

n11=tk.Button(window,text='1',command=lambda :but('1'))
n11.place(x=10,y=180,width=90,height=40)

n12=tk.Button(window,text='2',command=lambda :but('2'))
n12.place(x=100,y=180,width=90,height=40)

n13=tk.Button(window,text='3',command=lambda :but('3'))
n13.place(x=190,y=180,width=90,height=40)

n14=tk.Button(window,text='/',command=lambda :but('/'))
n14.place(x=280,y=180,width=120,height=40)

n15=tk.Button(window,text='0',command=lambda :but('0'))
n15.place(x=10,y=220,width=90,height=40)

n16=tk.Button(window,text='.',command=lambda :but('.'))
n16.place(x=190,y=220,width=90,height=40)

n17=tk.Button(window,text='=',command=lambda :but('='))
n17.place(x=280,y=220,width=120,height=40)

n18=tk.Button(window,text='(',command=lambda :but('('))
n18.place(x=100,y=60,width=90,height=40)


n19=tk.Button(window,text=')',command=lambda :but(')'))
n19.place(x=190,y=60,width=90,height=40)

n20=tk.Button(window,text='<--',command=lambda :back())
n20.place(x=100,y=220,width=90,height=40)

n21=tk.Button(window,text='查看历史数据',command=lambda :show())
n21.place(x=10,y=260,width=90,height=40)

n22=tk.Button(window,text='%',command=lambda :but('%'))
n22.place(x=100,y=260,width=90,height=40)

n23=tk.Button(window,text='//',command=lambda :but('//'))
n23.place(x=190,y=260,width=90,height=40)

n24=tk.Button(window,text='^',command=lambda :but('^'))
n24.place(x=280,y=260,width=120,height=40)



window.mainloop()


