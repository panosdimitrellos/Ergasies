import subprocess
import requests
from bs4 import BeautifulSoup

# Παίρνουμε πρόσβαση στην δοσμένη ιστοσελίδα
result = requests.get("https://github.com/trending")

# Αποθηκεύουμε το περιεχόμενο της σελίδας απο τα request σε μια μεταβλητή
src = result.content

# Χρησιμοποιώντας το BeautifulSoup module μπορούμε να επεξεργαστούμε τα δεδομένα
soup = BeautifulSoup(src)

# Κενή λίστα για τα urls
urls = []

# Θέλουμε να εξάγουμε συγκεκριμένη πληροφορία και γιαυτό ψάχνουμε μέσα σε συγκεκριμένα χαρακτηριστικά της σελίδας
for h1_tag in soup.find_all("h1"):
    a_tag = h1_tag.find("a")
    try:
        urls.append(a_tag.attrs['href'])
    except:
        pass

# Εκτυπώνει την λίστα urls με τα στοιχεία της
print(urls)

# Αυτή η συνάρητηση ελέγχει τα repositories με την βοήθεια του truffleHog και εκτυπώνει τα κλειδία
# Για πιο στοχευμένα αποτελέσματα πάνω στα API keys χρησιμοποιήσαμε --rules C:\rulesAPIkeys.json
def scan():
    for x in urls:
        print("~~~~~~~~~~~~~~~~~~~~~~~ HERE ARE THE KEYS  OF {name} REPOSITORY ~~~~~~~~~~~~~~~~~~~~~~~".format(name=x))
        subprocess.run('truffleHog --rules C:\APIkeysrules.json --regex --entropy=False https://github.com{name}'.format(name=x))
    return


exec("scan()")