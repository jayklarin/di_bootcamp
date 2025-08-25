
# Access the value key of history
sample_dict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])




# Delete set of keys from Python Dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict[key]
print(sample_dict)


student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 14,
    'address' : 'Privet Drive, 4',
    'pets': ['Hedwig', 'Buckbeak'],
    'houses': {'main': 'Griffyndor', 'second': 'Slytherin'},
    'best_friends': ('Ron Weasley', 'Hermione Granger')
}

# for key in student_info.keys():
#     print(key)

# for value in student_info.values():
#       print(value)

#for item in student_info.items():
#    print(item)


grades = {'mike': 70, 'sarah': 85, 'tom': 90, 'anna': 65, 'miriam': 50}

for name, score in grades.items():
    if score >= 70:
        print(f"{name} passed with a score of {score}.")


students = ['Harry', 'Hermione', 'Ron', 'Draco']

for i, name in enumerate(students):
    students[i]= f'Welcome {name}'
print(students)
