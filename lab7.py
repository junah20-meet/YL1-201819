##import tkinter as tk
##from tkinter import simpledialog
##
##Then when ever you want to ask the user for input use this code:
##greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
##if greeting in ("Arrr!"):
##    print("Go away, pirate.")
##else:
##    print("Greetings, hater of pirates!")


##import tkinter as tk
##from tkinter import simpledialog
##
##year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))
##
##if year <= 1900:
##    print ('Woah, thats the past!')
##elif year > 1900 and year < 2020:
##    print ("That's totally the present!")
##else:
##    print ("Far out, that's the future!!")


##class Person:
##  def __init__(self, firstname, lastname):
##    self.first_name = firstname
##    self.last_name = lastname
##  def speak(self):
##      print("My name is" + "" + self.first_name + " " + self.last_name)
##
##me = Person("Brandon", "Walsh")
##you = Person("Ethan", "Reed")
##
##me.speak()
##you.speak()


import tkinter as tk
from tkinter import simpledialog

exam_one = int(simpledialog.askstring("Input", " exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input", " exam grade two: ", parent=tk.Tk().withdraw()))

exam_three = int(simpledialog.askstring("Input", " exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + str(letter_grade))

if letter_grade is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")


