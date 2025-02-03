from scanner import scan_log_file, track_pid_jobs, calculate_job_duration, generate_report

if __name__ == "__main__":
    log_file_path = 'logs/logs[83].log'
    
    scanned_logs = scan_log_file(log_file_path)
    track_jobs = track_pid_jobs(scanned_logs)
    job_duration = calculate_job_duration(track_jobs)       

    generate_report(job_duration)
