# Syntax der while-Schleife
# while bedingung:

"""count = 1
# die Schleife wird ausgeführt, solange count kleiner oder gleich 5 ist
while count <= 5:
    print(count)
    count += 1 #Erhöht count um 1 nach jeder Iteration

#____________________________________________________________________________________________________

i = 1
n = 5

while i <= n:
    print(i)
    i = i + 1
"""
#___________________________________________________________

# Die Schleife wird ausgeführt, solange der Benutzer nicht "ende" eingibt.

while True:
    user_input = input("Geben Sie etwas ein (oder 'ende', um das Programm zu beenden): ")

    if user_input == 'ende':
        break # Beendet die Schleife, wenn der Benutzer "ende" eingibt

    print(f"Sie haben {user_input} eingeben.")

#_____________________________________________________________
