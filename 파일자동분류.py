import os
import shutil

# 다운로드 폴더 경로(raw string notation)
download_folder = r'C:\Users\ETV\Downloads'

# 대상 폴더들의 경로
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
archive_folder = os.path.join(download_folder, 'Archive')
docs_folder = os.path.join(download_folder, 'docs')

# 대상 확장자들
image_extensions = ['.jpg', '.jpeg']
data_extensions = ['.csv', '.xlsx']
archive_extensions = ['.zip']
docs_extensions = ['.pdf']

# 대상 폴더들이 존재하지 않으면 생성
for folder in [image_folder, data_folder, archive_folder, docs_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 다운로드 폴더 내 파일들을 반복하면서 이동
for filename in os.listdir(download_folder):
    source_path = os.path.join(download_folder, filename)

    if os.path.isfile(source_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in image_extensions:
            shutil.move(source_path, os.path.join(image_folder, filename))
            print(f'Moved {filename} to images folder.')

        elif extension in data_extensions:
            shutil.move(source_path, os.path.join(data_folder, filename))
            print(f'Moved {filename} to data folder.')

        elif extension in archive_extensions:
            shutil.move(source_path, os.path.join(archive_folder, filename))
            print(f'Moved {filename} to Archive folder.')

        elif extension in docs_extensions:
            shutil.move(source_path, os.path.join(docs_folder, filename))
            print(f'Moved {filename} to docs folder.')

print('File sorting completed.')
