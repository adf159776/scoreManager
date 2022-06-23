class ScoreManager:
  def __init__(self, inputFile, outputFile):
    self.input = inputFile
    self.output = outputFile
    self.list = []
  def set_score(self, name, score):
    for stu in self.list:
      if stu["name"] == name:
        stu["score"] = float(score)
  def load_json_file_to_list(self):
    import json
    f = open(self.input, "r")
    s = f.readline()
    while s:
        self.list.append(json.loads(s))
        s = f.readline()
    f.close()
    return self.list
  def write_score_to_file(self, student_of_class):
    import json
    m = 0
    for sco in student_of_class:
        m = m+sco["score"]
    o = open(self.output, "w")
    o.write(json.dumps({"student":student_of_class,"total":m,"average":m/len(student_of_class)}))
    o.close()
