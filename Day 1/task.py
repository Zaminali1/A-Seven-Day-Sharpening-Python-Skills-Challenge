### Task 1: Save and Read Notes

# * Ask user to write a note
# * Save it in `notes.txt`
# * Show all notes afterward


# with open("notes.txt","w") as note:
#     note.write(input("Write a Note : "))
#     print(note)







### Task 2: Save Profile in JSON

# * Ask user name, age, and goal
# * Save in `profile.json`
# * Read and print it

import json
prof={
    "name":input("Enter your Name "),
    " age":int(input("Enter Your Age")),
    "Goal":input("What is your goal")
     
}

with open("profile.json","w") as profi:
    json.dump(prof,profi,indent=2)
    print(profi)









with open("hey.txt","w") as fff:
    fff.write("Hello how")