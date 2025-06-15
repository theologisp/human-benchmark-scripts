# Human Benchmark Automation

This project automates tasks on [humanbenchmark.com](https://www.humanbenchmark.com) using Python and Selenium. It includes scripts for logging in (optional) and running the different tasks automatically.

## Requirements

- Python 3.7+
- Google Chrome browser

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/human_benchmark.git
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up credentials: (optional)**
   - Change the file named `credentials.txt` in the `scripts` folder.
   - Add your username on the first line and your password on the second line:
     ```
     your_username
     your_password
     ```
     If you dont do that (or credentials are wrong), the script will continue to the next step and do the task without logging in.

## Usage

### Example:

To run the Verbal Memory automation:

```sh
python scripts/VerbalMemory.py
```

- The script will open Chrome and start the Verbal Memory test.
- Press `ESC` at any time to stop the script (Chrome will remain open).

## Notes

- `ESC` is used as a fail-safe for the tasks that would otherwise run endlessly.
- Chrome will remain open after the script ends, thanks to the `detach` option.
- Make sure your Chrome browser is up to date for best compatibility with `webdriver-manager`.

