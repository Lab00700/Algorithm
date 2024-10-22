from datetime import datetime
from pytz import timezone
import os

def count_programmers():
    info = []
    total_count = 0
    levels = os.listdir("./프로그래머스")
    levels.sort()
    for level in levels:
        problems_list = os.listdir(f"./프로그래머스/{level}")
        count = len(problems_list)
        levels_info = [level, count]
        info.append(levels_info)
        total_count += count
    return info, total_count


def programmers_make_info(levels_info, total_count):
    info = f"### 프로그래머스 레벨 별 문제 수\n총 문제 수 : {total_count}\n\n마지막 업데이트 : {datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M')}\n\n"
    for level_info in levels_info:
        temp = f"- {level_info[0]} 레벨 문제 수 : {level_info[1]}\n"
        info += temp
    return info


def make_solving_count(info):
    return f"""# 백준, 프로그래머스 코딩
{info}
"""


def update_solving_count():
    programmers_info, programmers_total_count = count_programmers()
    info = programmers_make_info(programmers_info, programmers_total_count)
    solving_count = make_solving_count(info)
    return solving_count


if __name__ == "__main__":
    solving_count = update_solving_count()
    with open("./Solving-count.md", 'w', encoding='utf-8') as f:
        f.write(solving_count)
