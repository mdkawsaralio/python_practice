
class student:
  def __init__(self, name, roll, class_name):
    self.name=name
    self.roll=roll
    self.class_name=class_name

students={}


while True:
  print("1. Add Student")
  print("2. View Student")
  print("3. Exit")
  choice=int(input("Enter your choice: "))

  if choice==1:
    try:
      roll=int(input("Enter roll number: ").strip())
      if roll in students:
        print("Roll is already exists")
      else:
        name=input("Enter student name").strip()
        class_name=input("Enter Class name").strip()
        students[roll]= student(name, roll, class_name)
        print("Student added successfully")
    except ValueError:
      print("Invalid input")

  elif choice==2:
    try:
      roll=int(input("Enter roll number: ").strip())
      if roll not in students:
        print("Roll is not exists")
      else:
        print("Name",students[roll].name)
        print("Roll",students[roll].roll)
        print("Class",students[roll].class_name)
    except ValueError:
      print("Invalid input")
  elif choice==3:
    print("Thank's for visiting")
    break
  else:
    print("Invalid input")