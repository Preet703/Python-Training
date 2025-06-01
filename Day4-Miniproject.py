import os

def log_analyzer(log_file):
    summary = {"INFO": 0, "ERROR": 0, "WARNING": 0}
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    summary["ERROR"] += 1
                elif "WARNING" in line:
                    summary["WARNING"] += 1
                elif "INFO" in line:
                    summary["INFO"] += 1

        with open("summary.txt", 'w') as summary_file:
            for key, value in summary.items():
                summary_file.write(f"{key}: {value}\n")

        return summary["INFO"], summary["ERROR"], summary["WARNING"]

    except FileNotFoundError:
        print(f"Error: The file {log_file} does not exist.")
        return 0, 0, 0

def main():
    dir1 = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(dir1, "sample.log")

    info_count, error_count, warning_count = log_analyzer(log_file)
    print(f"INFO: {info_count}, ERROR: {error_count}, WARNING: {warning_count}")

if __name__ == "__main__":
    main()
