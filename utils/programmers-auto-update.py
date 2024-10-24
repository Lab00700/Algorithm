from datetime import datetime, timezone, timedelta
import os

def count_programmers_info():
    total_count = 0
    levels = os.listdir("./프로그래머스")
    levels.sort()
    count_info=''
    for level in levels:
        problems_list = os.listdir(f"./프로그래머스/{level}")
        count = len(problems_list)
        count_info+=f"- {level} 레벨 문제 수 : {count}\n"
        total_count += count

    programmers_info = ("# 프로그래머스\n"
            f"### 프로그래머스 레벨 별 문제 수\n"
            f"총 문제 수 : {total_count}\n\n"
            f"마지막 업데이트 : {datetime.now(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %H:%M')}\n\n")
    programmers_info+=count_info
    return programmers_info

if __name__ == "__main__":
    solving_count = count_programmers_info()
    with open("./md_files/Solving-count.md", 'w', encoding='utf-8') as f:
        f.write(solving_count)
