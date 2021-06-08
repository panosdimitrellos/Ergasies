import subprocess

# Δημιουργούμε μια κενή λίστα
reposList = []

# Αριθμός repositories ως input
n = int(input("Enter number of repositories : "))

# Παίρνει τα repositories ως input και τα βάζει στην λίστα reposList
print("Enter the repositories :")
for i in range(0, n):
    repo = input()
    reposList.append(repo)

# Εκτυπώνει την λίστα reposList με τα στοιχεία της
print(reposList)

# Αυτή η συνάρητηση ελέγχει τα repositories με την βοήθεια του truffleHog και εκτυπώνει τα κλειδία
# Για πιο στοχευμένα αποτελέσματα πάνω στα API keys χρησιμοποιήσαμε --rules C:\rulesAPIkeys.json
def scan():
    for x in reposList:
        print("~~~~~~~~~~~~~~~~~~~~~~~ HERE ARE THE KEYS  OF {name} REPOSITORY ~~~~~~~~~~~~~~~~~~~~~~~".format(name=x))
        subprocess.run('truffleHog --rules C:\APIkeysrules.json --regex --entropy=False {name}'.format(name=x))
    return

exec("scan()")