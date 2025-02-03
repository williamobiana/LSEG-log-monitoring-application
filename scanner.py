import os
from datetime import datetime

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
        job_des = log['job_description']
        log_entry = log['log_entry']
        pid = log['pid']

        # If the PID is not in the tracker, add it with the job description
        if pid not in pid_job_tracker:
            pid_job_tracker[pid] = {
            'job_description': job_des,
            'start_time': None,
            'end_time': None
            }
        
        # Track the start and end times of the job
        if 'START' in log_entry:
            pid_job_tracker[pid]['start_time'] = timestamp
        elif 'END' in log_entry:
            pid_job_tracker[pid]['end_time'] = timestamp

    return pid_job_tracker


def calculate_job_duration(pid_job_tracker):
    pid_job_duration = {}

    # Calculate the duration of each job
    for pid, job in pid_job_tracker.items():
        start_time = job['start_time']
        end_time = job['end_time']

        # If both start and end times are present, calculate the duration
        if start_time and end_time:
            # convert the timestamps to datetime 
            start_datetime = datetime.strptime(start_time, '%H:%M:%S')
            end_datetime = datetime.strptime(end_time, '%H:%M:%S')

            # calculate the duration and add it to the pid_job_duration
            duration = end_datetime - start_datetime
            pid_job_duration[pid] = {
                'job_description': job['job_description'],
                'start_time': start_time,
                'end_time': end_time,
                'duration': duration
            }

        # If the end time is missing, add the job as incomplete
        else:
            pid_job_duration[pid] = {
                'job_description': job['job_description'],
                'start_time': start_time,
                'end_time': end_time,
                'duration': "Incomplete (No End Time)"
            }

    return pid_job_duration
    