# ფუნქცია არის კოდის ბლოკი რომელიც შეგვიძლია გამოვიძახოდ რამდენჯერაც გვინდა კოდის გამეორების გარეშე

def greet(name):
    print(f"Hello {name}")

greet("Luka")


def add_name(name):
    names = ["luka", "nika", "giorgi", "saba", "dato"]
    names.append(name)


def check_index(name, index):
    names = ["luka", "nika", "giorgi", "saba", "dato"]

    if index > len(names):
        print("Index out of range")

    else:
        names.append(name)
    
add_name("khvicha")
check_index("ana", 5)
check_index("kote", 7)