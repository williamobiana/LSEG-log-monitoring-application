import os
from scanner import scan_log_file, track_pid_jobs, calculate_job_duration, generate_report

if __name__ == "__main__":
    log_file_path = 'logs[83].log'
    
    scanned_logs = scan_log_file(log_file_path)
    track_jobs = track_pid_jobs(scanned_logs)
    job_duration = calculate_job_duration(track_jobs)

    for pid, job in job_duration.items():
        print(f"PID: {pid}")
        print(f"Job Description: {job['job_description']}")
        print(f"Start Time: {job['start_time']}")
        print(f"End Time: {job['end_time']}")
        print(f"Duration: {job['duration']}")
        print("-" * 30)        

    generate_report(job_duration)
