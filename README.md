# LSEG-log-monitoring-application

LSEG Coding Challenge

The LSEG-log-monitoring-application is designed to monitor and process log files.

The main application file, `app/app.py`, initializes and runs the log monitoring application. The core functionality for scanning and processing log files is implemented in `app/scanner.py`. This module includes logic to read log files, parse their contents, calculate the processing duration and identify warnings or errors when processing time exceeds baseline. 

The `tests/test_scanner.py` file contains unit tests to ensure that the functions and methods in `scanner.py` work correctly.

## Project Structure

The project consists of the following main files:

- `app/app.py`: The main application file that initializes and runs the log monitoring application.
- `app/scanner.py`: Contains the logic for scanning and processing log files.
- `tests/test_scanner.py`: Contains unit tests for the `scanner.py` module.

## Getting Started

### Prerequisites

- Python 3.x
- Pip
- Required Python packages (`requirements.txt`)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/LSEG-log-monitoring-application.git
    ```
2. Navigate to the project directory:
    ```sh
    cd LSEG-log-monitoring-application
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the application, execute the following command:
```sh
python3 app/app.py
```
```
# Output
Log file scanned successfully
PID jobs tracked successfully
Job duration calculated successfully
Report generated, Please open report.log to see WARNINGS and ERRORS
```


## Running Tests

To run the tests, use the following command:
```sh
pytest tests/test_scanner.py
```

