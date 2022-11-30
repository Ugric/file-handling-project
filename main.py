from calc import Students

students = Students('data.txt')

while True:
  print("1. Print the Class Average")
  print("2. Print top three best students")
  print("3. Bottom three students overall")
  opt = int(input("\nSelect option number: "))
  print()
  if opt == 1:
    print(f"class average | {students.average()}")
  elif opt == 2:
    leaderboard = students.leaderboard()
    best = leaderboard[0:3]
    for i in range(len(best)):
      print(i+1,"|",best[i],"-", students.student_average(best[i]))
  elif opt == 3:
    leaderboard = students.leaderboard()
    worst = leaderboard[len(leaderboard)-3:len(leaderboard)]
    for i in range(len(worst)):
      print(i+len(leaderboard)-2,"|",worst[i],"-", students.student_average(worst[i]))
  print()