from scoreManager import ScoreManager

# Class
SM = ScoreManager("input.json", "output.json")

# 讀取 json 檔案，回傳到 student_of_class 陣列
student_of_class = SM.load_json_file_to_list()

# 逐一輸入分數
for obj in student_of_class:
    score = input()
    SM.set_score(obj["name"], score)

    # 輸出
    SM.write_score_to_file(student_of_class)
