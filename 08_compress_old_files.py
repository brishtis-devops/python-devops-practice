import os
import time
import zipfile

directory = input("Enter the directory path: ")
current_time = time.time()

zip_filename = "old_files.zip"
zipf = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root,file)

        file_mtime = os.path.getmtime(file_path)

        if (current_time - file_mtime) > (7 * 24 * 60 * 60):
            print(f"Compressing: {file_path}")
            zipf.write(file_path)

zipf.close()
print(f"\nAll old files compressed into {zip_filename}")

