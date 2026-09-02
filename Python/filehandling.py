import  json
txt_data = "WHAT DO YOU CALL A BLACK MAN IN AMERICA?"
file = "C:/Users/damay/Desktop/file.txt"
with open(file, "a") as f:  
   f.write( "\n" + txt_data)
   print(f"file {file} created successfully.")

LIST = [
   "1: Book",
   "2: School tasks",
   "3: chores of the day",

]
list = "C:/Users/damay/Desktop/list.json"
with open(list, "x") as f:
    json.dump(LIST, f, indent=5)
    print(f"file {list} created successfully.")