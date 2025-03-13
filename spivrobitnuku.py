def load(file_name):
    emps = []
    try:
        with open(file_name, "r") as f:
            for line in f:
                ln = line.strip()
                if ln == "":
                    continue
                parts = ln.split(",")
                if len(parts) >= 4:
                    emp = {"surname": parts[0], "name": parts[1], "age": parts[2], "pos": parts[3]}
                    emps.append(emp)
    except FileNotFoundError:
        with open(file_name, "w") as f:
            pass
        print("File not found. New file created instead this.")
    except Exception as ex:
        print("Load error:", ex)
    return emps

# Save
def save(file_name, emps):
    try:
        with open(file_name, "w") as f:
            for e in emps:
                f.write(e["surname"] + "," + e["name"] + "," + e["age"] + "," + e["pos"] + "\n")
        print("Saved.")
    except Exception as ex:
        print("Save error:", ex)

# Add 
def add(emps):
    s = input("Enter surname: ")
    n = input("Enter name: ")
    a = input("Enter age: ")
    p = input("Enter position: ")
    emp = {"surname": s, "name": n, "age": a, "pos": p}
    emps.append(emp)
    print("Employee added.")

# Edit
def edit(emps):
    if len(emps) == 0:
        print("No employees available.")
        return
    for i, e in enumerate(emps):
        print(f"{i}. {e['surname']} {e['name']}")
    try:
        idx = int(input("Enter index: "))
    except:
        print("Invalid input!")
        return
    if idx < 0 or idx >= len(emps):
        print("Index out range!")
        return
    e = emps[idx]
    s = input("Surname (" + e["surname"] + "): ")
    n = input("Name (" + e["name"] + "): ")
    a = input("Age (" + e["age"] + "): ")
    p = input("Position (" + e["pos"] + "): ")
    if s != "":
        e["surname"] = s
    if n != "":
        e["name"] = n
    if a != "":
        e["age"] = a
    if p != "":
        e["pos"] = p
    emps[idx] = e
    print("Employee updated.")

# Delete
def delete(emps):
    if len(emps) == 0:
        print("No employees avilable")
        return
    for i, e in enumerate(emps):
        print(f"{i}. {e['surname']} {e['name']}")
    try:
        idx = int(input("Enter index: "))
    except:
        print("Invalid input!")
        return
    if idx < 0 or idx >= len(emps):
        print("Index out of range!")
        return
    del emps[idx]
    print("Employee deleted.")

# Search
def search(emps):
    s = input("Enter surname to search: ")
    found = []
    for e in emps:
        if e["surname"] == s:
            found.append(e)
    if not found:
        print("No employees found.")
    else:
        for e in found:
            print(e["surname"], e["name"], e["age"], e["pos"])
        ans = input("Save results to file? (y/n): ")
        if ans == "y":
            fname = input("Enter name: ")
            try:
                with open(fname, "w") as out:
                    for e in found:
                        out.write(e["surname"] + "," + e["name"] + "," + e["age"] + "," + e["pos"] + "\n")
                print("Saved.")
            except Exception as ex:
                print("Err saving file:", ex)

# Display
def display(emps):
    opt = input("Display by age (a) or  letter (l): ")
    found = []
    if opt == "a":
        age = input("Enter age: ")
        for e in emps:
            if e["age"] == age:
                found.append(e)
    elif opt == "l":
        letter = input("Enter initial letter: ")
        for e in emps:
            if e["surname"][0] == letter:
                found.append(e)
    else:
        print("Invalid option here")
        return
    if not found:
        print("No employees found.")
    else:
        for e in found:
            print(e["surname"], e["name"], e["age"], e["pos"])

# Main
def main():
    fname = input("Enter filename to load: ")
    emps = load(fname)
    print("Loaded", len(emps), "employees.")
    choice = ""
    while choice != "7":
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Edit Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. Display Employee")
        print("6. Save")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add(emps)
        elif choice == "2":
            edit(emps)
        elif choice == "3":
            delete(emps)
        elif choice == "4":
            search(emps)
        elif choice == "5":
            display(emps)
        elif choice == "6":
            sf = input("Enter name to save: ")
            save(sf, emps)
        elif choice == "7":
            save(fname, emps)
            print("Goodbye!")
        else:
            print("err")

main()
