import json

class Students:
  """Calculate the class average from a file"""
  def __init__(self, file: str):
    """Load json file"""
    self.data: dict = json.load(open(file, "r"))
  def student(self,  student: str):
    return self.data[student]
  def student_average(self, student: str):
    """Calculate a specific students average"""
    score = self.student(student)
    return sum(score) / len(score)
    
  def average(self):
    """Claculate the whole class average"""
    average = 0
    for student in self.data:
      average += self.student_average(student)
    return average / len(self.data.keys())
  def leaderboard(self):
    """Creates a list of names sorted by best to worse average score"""
    students = list(self.data.keys())
    students.sort(key=lambda name: self.student_average(name), reverse=True)
    return students