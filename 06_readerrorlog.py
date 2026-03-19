
def extract_error_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    print(line.strip())
    except FileNotFoundError:
        print("File not found. Please check the file path.")

log_file = input("Enter the log file path: ")
extract_error_lines(log_file)
