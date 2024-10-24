from datetime import datetime, timezone, timedelta
import os

def programmers_count_info():
    total_count = 0
    levels = os.listdir("./프로그래머스")
    levels.sort()
    count_info=''
    for level in levels:
        problems_list = os.listdir(f"./프로그래머스/{level}")
        count = len(problems_list)
        count_info+=f"- {level} 레벨 : {count}\n"
        total_count += count

    programmers_info = (f"### 프로그래머스 - {datetime.now(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %H:%M')}\n"
                        f"#### 총 문제 수 : {total_count}\n")
    programmers_info+=count_info
    return programmers_info

if __name__ == "__main__":
    file_number=0
    file_name="programmers-solving-count"
    with open(f"./md_files/0-md-files-number.md", 'r', encoding='utf-8') as f:
        md_files_number=f.read()
        md_files=md_files_number.split()
        for md_file in md_files:
            if file_name in md_file:
                file_number=md_file.split('-')[0]
        for remove_file in os.listdir("./md_files"):
            if file_name in remove_file:
                os.remove(f"./md_files/{remove_file}")
    content = programmers_count_info()
    with open(f"./md_files/{file_number}-{file_name}.md", 'w', encoding='utf-8') as f:
        f.write(content)

