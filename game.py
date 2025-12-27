import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combos in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combos[0]]["Text"] == buttons[comobs[1]]["Text"] == buttons[combos[2]]["Text"] != "":
            buttons[combos[0]].config(bg="green")
            buttons[combos[1]].config(bg="green")
            buttons[combos[2]].config(bg="green")
            messagebox.showinfo("TIC-TAC-Toe",f"Player {buttons[combos[0]]["Text"]} wins!")

def button_click(index):
    if buttons[index]["Text"] == "" and not winner:
        buttons[index]["Text"] == current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player= "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

