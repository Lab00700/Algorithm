import os

def readme_content_info():
    md_files_list = os.listdir("./md_files")
    readme_info = ''
    with open(f"./md_files/0-md-files-number.md", 'r', encoding='utf-8') as f:
        md_files_number = f.read()
        md_files = md_files_number.split()
        for md_file_name in md_files_list:
            for md_file in md_files:
                if md_file_name[2:] in md_file and md_file_name != md_file:
                    os.renames(md_file_name, md_file)
        md_files_list = md_files

    for md_file in md_files_list:
        with open(f"./md_files/{md_file}", 'r', encoding='utf-8') as f:
            file_content = f.read()
            readme_info+=f"{file_content}\n\n"

    return readme_info

if __name__ == "__main__":
    file_number=0
    file_name="programmers-solving-count"

    content = readme_content_info()
    with open(f".README.md", 'w', encoding='utf-8') as f:
        f.write(content)
