def search (name ,key):
    if key in name:
        print(f"'{key}' yup present in list")
    else:
        name.append(key)
        print("added to the grp")
        return name
    
name = ["chaitanya","kartik"]
search_name = input ()

new = search(name, search_name)
print(f"{new}")

