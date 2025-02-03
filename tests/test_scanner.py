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

