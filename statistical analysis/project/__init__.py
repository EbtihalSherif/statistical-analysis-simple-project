import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math



def secondFrame():
    canvasImport.destroy()
    canvasChoose.pack()
    browseButton_desc = tk.Button(text="calculate descriptive statistics", command=cominedFunDesc, bg='steel blue',
                                  fg='white',
                                  font=('helvetica', 12, 'bold'))
    canvasChoose.create_window(150, 150)
    browseButton_desc.place(x=30, y=100)
    browseButton_reg = tk.Button(text="calculate correlations/regressions", command=cominedFunreg, bg='steel blue',
                                 fg='white', font=('helvetica', 12, 'bold'))
    browseButton_reg.place(x=15, y=170)


def getCSV():
    global df
    global df2

    global import_file_path
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)
    print(df)
    secondFrame()
    canvasImport.destroy()


def cominedFunDesc():
    canvasChoose.destroy()
    descAnalysis()


def cominedFunreg():
    canvasChoose.delete("all")
    canvasChoose.destroy()
    correlations()


def descAnalysis():
    canvasdesc = tk.Canvas(root, width=1000, height=300, bg='White', relief='raised')
    canvasdesc.pack()

    figure1 = plt.Figure(figsize=(5, 4), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df.plot(kind='bar', legend=True, ax=ax1)

    df2 = pd.read_csv(import_file_path)
    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df.plot(kind='line', legend=True, ax=ax2)

    mean1 = df['Salary'].mean()
    sum1 = df['Salary'].sum()
    max1 = df['Salary'].max()
    min1 = df['Salary'].min()
    count1 = df['Salary'].count()
    median1 = df['Salary'].median()
    std1 = df['Salary'].std()
    var1 = df['Salary'].var()

    label_mean = tk.Label(text="The mean of salaries is : " + str(mean1), bg='White', fg='steel blue',
                          font=('helvetica', 12, 'bold'))
    label_mean.place(x=100, y=70)
    label_med = tk.Label(text='Median salary: ' + str(median1), bg='White', fg='steel blue',
                         font=('helvetica', 12, 'bold'))
    label_med.place(x=100, y=120)

    label_sum = tk.Label(text='Sum of salaries: ' + str(sum1), bg='White', fg='steel blue',
                         font=('helvetica', 12, 'bold'))
    label_sum.place(x=100, y=170)
    label_max = tk.Label(text='Max salary: ' + str(max1), bg='White', fg='steel blue',
                         font=('helvetica', 12, 'bold'))
    label_max.place(x=100, y=220)
    label_min = tk.Label(text='Min salary: ' + str(min1), bg='White', fg='steel blue',
                         font=('helvetica', 12, 'bold'))
    label_min.place(x=500, y=70)
    label_stv = tk.Label(text='Standard deviation of salaries: ' + str(std1), bg='White', fg='steel blue',
                         font=('helvetica', 12, 'bold'))
    label_stv.place(x=500, y=120)
    label_var = tk.Label(text='Variance of salaries: ' + str(var1), bg='White', fg='steel blue',
                         font=('helvetica', 12, 'bold'))
    label_var.place(x=500, y=170)
    print('Mean salary: ' + str(mean1))
    print('Sum of salaries: ' + str(sum1))
    print('Max salary: ' + str(max1))
    print('Min salary: ' + str(min1))
    print('Count of salaries: ' + str(count1))
    print('Median salary: ' + str(median1))
    print('Std of salaries: ' + str(std1))
    print('Var of salaries: ' + str(var1))


# plt.show()


def correlations():
    canvasreg = tk.Canvas(root, width=500, height=300, bg='White', relief='raised')
    canvasreg.pack()
    hours = df['Hours']
    salary = df['Salary']

    n = np.size(hours)
    print(n)

    m_x, m_y = np.mean(hours), np.mean(salary)
    SS_xy = np.sum(hours * salary) - n * m_y * m_x
    SS_xx = np.sum(hours * hours) - n * m_x * m_x
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    plt.scatter(hours, salary, color="m",
                marker="o", s=30)
    y_pred = b_0 + b_1 * hours
    plt.plot(hours, y_pred, color="g")

    figure4 = plt.Figure(figsize=(5, 4), dpi=100)
    ax4 = figure4.add_subplot(111)
    ax4.scatter(hours, salary, color="m",
                marker="o", edgecolors='r', s=30)

    ax4.plot(hours, y_pred, color="g")

    scatter4 = FigureCanvasTkAgg(figure4, root)
    scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)

    ax4.legend()
    ax4.set_xlabel('hours')
    ax4.set_title('hours Vs. salary')
    correlation_val = hours.corr(salary)
    label_val = tk.Label(text=" The correlation value of data is : " + str(correlation_val), bg='White',
                         fg='steel blue',
                         font=('helvetica', 12, 'bold'))
    label_val.place(x=30, y=100)
    if correlation_val > 0:
        if correlation_val > 0.9 :
             if correlation_val <= 1:
               label_comment = tk.Label(text=" The correlation is positive and perfect", bg='White',
                                     fg='steel blue',
                                     font=('helvetica', 12, 'bold'))

               label_comment.place(x=30, y=150)
        if correlation_val > 0.5 :
            if correlation_val <= 0.9:
               label_comment = tk.Label(text=" The correlation is positive and strong", bg='White',
                                     fg='steel blue',
                                     font=('helvetica', 12, 'bold'))

               label_comment.place(x=30, y=150)

        if correlation_val > 0 :
            if correlation_val <= 0.5:
               label_comment = tk.Label(text=" The correlation is positive and weak", bg='White',
                                     fg='steel blue',
                                     font=('helvetica', 12, 'bold'))

               label_comment.place(x=30, y=150)
    if correlation_val < 0:
        correlation_val=abs(correlation_val)
        if correlation_val > 0.9 :
             if correlation_val <= 1:
               label_comment = tk.Label(text=" The correlation is negative and perfect", bg='White',
                                     fg='steel blue',
                                     font=('helvetica', 12, 'bold'))

               label_comment.place(x=30, y=150)
        if correlation_val > -0.5 :
            if correlation_val <= -0.9:
               label_comment = tk.Label(text=" The correlation is negative and strong", bg='White',
                                     fg='steel blue',
                                     font=('helvetica', 12, 'bold'))

               label_comment.place(x=30, y=150)

        if correlation_val > 0 :
            if correlation_val <= 0.5:
               label_comment = tk.Label(text=" The correlation is negative and weak", bg='White',
                                     fg='steel blue',
                                     font=('helvetica', 12, 'bold'))

               label_comment.place(x=30, y=150)




root = tk.Tk()
canvasImport = tk.Canvas(root, width=300, height=300, bg='White', relief='raised')
canvasImport.pack()
canvasChoose = tk.Canvas(root, width=300, height=300, bg='White', relief='raised')

browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='steel blue', fg='white',
                             font=('helvetica', 12, 'bold'))

canvasImport.create_window(150, 150, window=browseButton_CSV)

root.mainloop()


