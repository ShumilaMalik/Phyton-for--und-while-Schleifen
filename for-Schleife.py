"""
Die for-Schleife wird verwendet, um über Elemente eines Objektes zu iterieren
Was ist eine Iteration?
Eine Iteration ist ein Prozess, bei dem eine Aktion oder eine Grupe von 
Aktionen wiederholt wird.
"""

# Syntax einer for-Schleife
students = ["Max", "Julia", "Gina"] #Das ist eine Liste!

"""for student in students: #student ist eine temporäre Variable, die den Wert des zu Iterierendem Element übernimmt.
    print(student) #Einrückung nach der Schleife sehr wichtig!
# For-Schleife iteriert die Liste students und gibt für jedes Element in der Liste dessen Wert aus.

# Man kann auch einzelne Zeichen eines Strings Iterieren!
for letter in "letters":
    print("Das Wort enthaelt den Buchstaben " + letter)

for i in range(1,20):
    print(i)
"""

for student in range(2): #wiederholt die innere Schleif zwei mal
    for student in students:
        print(student)

for _ in range(10):
    print(_ + 1, "Hello World")