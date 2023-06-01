# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:33:02 2023

@author: kanis
"""

from tkinter import * 

root = Tk()
root.title("Min & Max profit with respect to month, week, day or anything")
root.geometry("400x400")

enter_month = Entry(root)
enter_month.place(relx = 0.5, rely = 0.2, anchor = CENTER)

enter_profit = Entry(root)
enter_profit.place(relx = 0.5, rely = 0.3, anchor = CENTER)

month_list = Label(root)
profit_list = Label(root)
max_profit1 = Label(root)
min_profit1 = Label(root)


list1 = []
list2 = []
def addmonth():
    month_list = enter_month.get()
    list1.append(month_list)
    month_list["text"] = "Your month/day/week list is : " + str(list1)

def addprofit():
    profit_list = enter_profit.get()
    list2.append(profit_list)
    profit_list["text"] = "Your profit/loss list is : " + str(list2)
    
def max_profit_month():
    max_profit = max(max_profit1)
    max_profit_index = profits.index(max_profit)
    print(max_profit_index)
    max_profit_month = month[max_profit_index]
    print("The maximum profit of " + str(max_profit) + "was recorded in the month of " + str(max_profit_month))
    
def min_profit_month():
    min_profit = min(min_profit1)
    min_profit_index = profits.index(min_profit)
    print(min_profit_index)
    min_profit_month = month[min_profit_index]
    print("The mimnium profit of " + str(min_profit) + "was recorded in the month of " + str(min_profit_month))

       
btn = Button(root, text = "Add to the month/day/week list", command =  addmonth)
btn.place(relx = 0.5, rely = 0.25, anchor = CENTER)

btn2 = Button(root, text = "Add to the profit/loss list : ", command = addprofit)
btn2.place(relx = 0.5, rely = 0.35, anchor = CENTER)

month_list.place(relx = 0.5, rely = 0.9, anchor = CENTER)
profit_list.place(relx = 0.5, rely = 0.10, anchor = CENTER)

btn1 = Button(root, text = "Which month you have the maxium profit?  ", command = max_profit_month)
btn1.place(relx = 0.3, rely = 0.5)

btn3 = Button(root, text="Which month you have the minimum profit or maximum loss? ", command =  min_profit_month)
btn3.place(relx = 0.6, rely = 0.5)

max_profit1.place(relx = 0.5, rely = 0.6, anchor = CENTER)
min_profit1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
     

root.mainloop()