import os
from scanner import scan_log_file, track_pid_jobs

if __name__ == "__main__":
    log_file_path = 'logs[83].log'
    
    scanned_logs = scan_log_file(log_file_path)

    track_jobs = track_pid_jobs(scanned_logs)
    for pid, job in track_jobs.items():
        print(f"PID: {pid}, Job: {job['job_description']}, Start Time: {job['start_time']}, End Time: {job['end_time']}")
