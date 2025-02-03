import os

def scan_log_file(file_path):
    try:
        # Open the log file and read the logs
        with open(file_path, 'r') as file:
            logs = file.readlines()

        # Scan the logs, split it into parts and add to scanned_logs list
        scanned_logs = []
        for log in logs:
            log_parts = log.split(',')
            scanned_logs.append({
                'timestamp': log_parts[0],
                'job_description': log_parts[1],
                'log_entry': log_parts[2],
                'pid': log_parts[3]
            })

        return scanned_logs

    except Exception as e:
        # Handle the exception if the log file is not found
        print(f"Error reading the log file: {e}")
        return []
