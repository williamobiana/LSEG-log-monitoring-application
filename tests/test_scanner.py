import os
import pytest
from datetime import datetime, timedelta
from scanner import scan_log_file, track_pid_jobs, calculate_job_duration, generate_report

@pytest.fixture
def log_file():
    log_file_path = 'logs[83].log'
    return log_file_path

# Test the scan_log_file function
def test_scan_log_file(log_file):
    scanned_logs = scan_log_file(log_file)

    # assert the timestamp, job_description, log_entry and pid exist in the scanned logs
    for log in scanned_logs:
        assert 'timestamp' in log
        assert 'job_description' in log
        assert 'log_entry' in log
        assert 'pid' in log


# Test the track_pid_jobs function
def test_track_pid_jobs(log_file):
    scanned_logs = scan_log_file(log_file)
    track_jobs = track_pid_jobs(scanned_logs)

    # assert the pid, job_description, start_time and end_time exist in the track jobs
    for pid, job in track_jobs.items():
        assert 'job_description' in job
        assert 'start_time' in job
        assert 'end_time' in job


# Test the calculate_job_duration function
def test_calculate_job_duration(log_file):
    scanned_logs = scan_log_file(log_file)
    track_jobs = track_pid_jobs(scanned_logs)
    job_duration = calculate_job_duration(track_jobs)
    
    # assert that the duration is present
    for pid, job in job_duration.items():
        assert job['duration'] is not None

