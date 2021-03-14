import tkinter as tk
import random as rd

studyQuestionsIT = [] # The empty list where I will put all the questions I want from a specific field.
                      # You can change the name to whatever subject you want. I intend to make it able to import, change, save, and export a TXT file in the future.
def addQuestions(list, questionList): # Function to add many elements to a pre-existing list
  for item in questionList:
    list.append(item)

addQuestions(studyQuestionsIT, ["Quelle est la deuxième étape du dépannage?", "Quelle est la premiére étape du dépannage?", "Quelle est la troisième étape du dépannage?", "Quelle est la quatriéme étape du dépannage?"
, "Quelle est la cinquième étape du dépannage?", "Quelle est la sixième étape du dépannage?", "C'est quoi le SSH?", "C'est quoi le SSH?", "C'est quoi le HTTP?", "C'est quoi le IMAP?", "C'est quoi le LSP?", "C'est quoi le DNS?", "C'est quoi le DHCP?", "C'est quoi le FTP?", "C'est quoi le LDAP?", "C'est quoi le SMTP?", "A quoi ça ser une Masque Sous Réseau?", "C'est quoi une passerelle?",
"A quoi ça ser la commande ipconfig?", "A quoi ça ser la commande ipconfig /all?" "A quoi ça ser la commande tracert?", "Qu'est ce que c'est un Réseau?", "Qu'est ce que c'est un périphérique intermédiaire?", "Qu'est ce que c'est un péripherique hôte?", "Qu'est ce que c'est un VPN?", "Qu'est ce que c'est un WAN?" ])

# Creation of the Window
root = tk.Tk()
root.withdraw() # Hides the window so that it runs on the background
def open_window(): # Function to create the windows at a random interval of time between 20 and 30 minutes
  global root
  top = tk.Toplevel()
  text = tk.Label(top, text = rd.choice(studyQuestionsIT))
  text.grid()
  root.after((rd.randint(1200, 1800)), open_window) #After the window is created, the function is called again in order to summon the next window when the time comes

root.after((rd.randint(1200, 1800)), open_window)
root.mainloop()