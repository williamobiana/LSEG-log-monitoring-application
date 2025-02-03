import os

def scan_log_file(file_path):
    try:
        # Open the log file and read the logs
        with open(file_path, 'r') as file:
            logs = file.readlines()

        # Scan the logs, split it into parts and add to scanned_logs list
        scanned_logs = []
        for log in logs:
            log_parts = log.strip().split(',')
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


def track_pid_jobs(scanned_logs):
    # Track the PID jobs and their start and end times
    pid_job_tracker = {}

    for log in scanned_logs:
        timestamp = log['timestamp']
        job = log['job_description']
        log_entry = log['log_entry']
        pid = log['pid']

        if pid not in pid_job_tracker:
            pid_job_tracker[pid] = {
                'start_time': timestamp,
                'end_time': timestamp,
                'jobs': []
            }

    