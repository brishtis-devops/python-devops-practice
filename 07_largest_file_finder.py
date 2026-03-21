import os

directory = input("Enter directory path: ")

largest_file = None
largest_size = 0

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)

        try:
            size = os.path.getsize(file_path)

            if size > largest_size:
                largest_size = size
                largest_file = file_path

        except Exception as e:
            print (f"Error accessing {file_path}: {e}")

if largest_file:
    print(f"\nLargest File: {largest_file}")
    print(f"Size: {largest_size} bytes")
else:
    print("No files found in the directory.")
    
