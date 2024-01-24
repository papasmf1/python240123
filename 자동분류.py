import os
import shutil

def move_files_by_extension(src_folder, dest_folder, extensions):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file in os.listdir(src_folder):
        if file.lower().endswith(extensions):
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, file)

            shutil.move(src_path, dest_path)
            print(f"Moved: {file}")

# 다운로드 폴더
download_folder = r'C:\Users\ETV\Downloads'

# 이미지 파일을 저장할 폴더
images_folder = r'C:\Users\ETV\Downloads\images'
move_files_by_extension(download_folder, images_folder, ('.jpg', '.jpeg'))

# 데이터 파일을 저장할 폴더
data_folder = r'C:\Users\ETV\Downloads\data'
move_files_by_extension(download_folder, data_folder, ('.csv', '.xlsx'))

# 문서 파일을 저장할 폴더
docs_folder = r'C:\Users\ETV\Downloads\docs'
move_files_by_extension(download_folder, docs_folder, '.pdf')
