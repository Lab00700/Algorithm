import os

def count_programmers():
    info = []
    total_count = 0
    directory_list = os.listdir("./프로그래머스")
    directory_list.sort()
    for level in directory_list:
        list = os.listdir(f"./프로그래머스/{level}")
        count = len(list)
        temp = [level, count]
        info.append(temp)
        total_count += count
    return info, total_count


def programmers_make_info(dir_info, total_file_count):
    info = f"### 프로그래머스 레벨 별 문제 수\n총 문제 수 : {total_file_count}\n"
    for directory_files_info in dir_info:
        temp = f"- {directory_files_info[0]} 레벨 문제 수 : {directory_files_info[1]}\n"
        info += temp
    return info


def make_read_me(info):
    return f"""# 백준, 프로그래머스 코딩
{info}
"""


def update_readme():
    programmers_info, programmers_total_count = count_programmers()
    info = programmers_make_info(programmers_info, programmers_total_count)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
