import os
from scanner import scan_log_file

if __name__ == "__main__":
    log_file_path = 'logs[83].log'
    
    scanned_logs = scan_log_file(log_file_path)
    for log in scanned_logs:
        print(log)
