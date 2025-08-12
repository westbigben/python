# Python Killer Libraries Demo Collection

A comprehensive collection of Python examples showcasing 9 powerful libraries that every Python developer should know. These are practical, runnable demonstrations designed to teach you the essentials of each library.

## 🚀 Quick Setup

### 1. Create a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# or
venv\Scripts\activate     # Windows (PowerShell)
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Playwright Browser Setup (Optional)
For the Playwright example to work, install browsers:
```bash
python3 -m playwright install
```

## 📚 Libraries Covered

### 🐼 **Pandas** - Data Analysis & Manipulation
**File:** `pandas_example.py`

Demonstrates reading CSV data, computing derived columns, grouping, and finding top records.

**Example Output:**
```
Full table:
 id          name category  price  quantity_sold  revenue
  1  Alpha Widget  widgets  19.99            150  2998.50
  2   Beta Widget  widgets  24.99             95  2374.05
  ...

Revenue by category:
category  revenue
 widgets  5372.55
  things  4750.00
  gizmos  1933.00
```

**Run:** `python3 pandas_example.py`

### 🌐 **Requests** - HTTP Library
**File:** `requests_example.py`

Makes API calls with error handling and fallback to local data when offline.

**Example Output:**
```
Requests demo — trying to GET https://api.github.com
Received keys from API: ['current_user_url', 'current_user_authorizations_html_url', ...]
Sample: current_user_url = https://api.github.com/user
```

**Run:** `python3 requests_example.py`

### 🍲 **BeautifulSoup** - HTML/XML Parsing
**File:** `beautifulsoup_example.py`

Parses local HTML file and extracts page title and all links.

**Example Output:**
```
BeautifulSoup demo — parsing local HTML: sample_page.html
Title: Sample Page
Found links:
- https://example.com
- https://httpbin.org/get
- https://github.com
```

**Run:** `python3 beautifulsoup_example.py`

### 📁 **Pathlib** - Modern File System Operations
**File:** `pathlib_example.py`

Demonstrates directory traversal and file searching with the modern `pathlib` module.

**Example Output:**
```
Pathlib demo — listing files in /path/to/directory
- pandas_example.py
- sample_page.html
- ...

Files containing "sample":
- sample_page.html
- sample_data.csv
- sample_api_response.json
```

**Run:** `python3 pathlib_example.py`

### 🖥️ **Typer** - CLI Applications Made Easy
**File:** `typer_example.py`

Creates a command-line interface with automatic help generation and type validation.

**Example Commands:**
```bash
# Show help
python3 typer_example.py --help

# Basic greeting
python3 typer_example.py "John"
# Output: Hello, John

# Excited greeting
python3 typer_example.py "Jane" --excited
# Output: Hello, Jane!!!
```

### 🎨 **Rich** - Beautiful Terminal Output
**File:** `rich_example.py`

Creates beautiful tables and progress bars in the terminal with colors and formatting.

**Example Output:**
```
Rich demo
           Top Sellers           
┏━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ id ┃ name          ┃  revenue ┃
┡━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━┩
│  1 │ Alpha Widget  │ $2998.50 │
│  2 │ Epsilon Thing │ $4750.00 │
└────┴───────────────┴──────────┘

Progress demo:
Processing... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01
```

**Run:** `python3 rich_example.py`

### ⏰ **Schedule** - Job Scheduling
**File:** `schedule_example.py`

Simple job scheduling with human-friendly syntax for recurring tasks.

**Example Output:**
```
Schedule demo — we will run the job 3 times rapidly.
Scheduled job: Hello from schedule!
Done with schedule demo.
```

**Run:** `python3 schedule_example.py`

### 🎭 **Playwright** - Web Browser Automation
**File:** `playwright_example.py`

Automates web browsers for testing, scraping, or automation tasks.

**Example Output:**
```
Playwright demo — launching headless browser...
Page title: Example Domain
```

**Requirements:** 
- Install browsers: `python3 -m playwright install`
- Internet connection for the demo

**Run:** `python3 playwright_example.py`

**Note:** Includes graceful fallback if Playwright isn't properly installed.

## 🎯 Interactive Demo Runner

**File:** `run_all_examples.py`

Run all examples in sequence with an interactive prompt between each one.

```bash
python3 run_all_examples.py
```

This will run each example and wait for you to press Enter before continuing to the next one. Type 'q' and press Enter to quit early.

## 📁 Sample Data Files

- **`sample_data.csv`** - Product sales data for Pandas demo
- **`sample_page.html`** - Local HTML file for BeautifulSoup parsing
- **`sample_api_response.json`** - Fallback JSON data for Requests demo (offline mode)

## 🔧 Dependencies

All dependencies are listed in `requirements.txt`:

```
pandas
requests
beautifulsoup4
typer[all]
rich
schedule
playwright
```

## 💡 Usage Tips

1. **Virtual Environment**: Always use a virtual environment to avoid conflicts
2. **Playwright Setup**: The Playwright example requires browser installation but gracefully handles missing dependencies
3. **Offline Mode**: The Requests example works offline using fallback data
4. **Error Handling**: All examples include proper error handling and informative messages
5. **Cross-Platform**: All examples work on Windows, macOS, and Linux

## 🚨 Troubleshooting

### Import Errors
If you see `ModuleNotFoundError`, ensure you've:
1. Activated your virtual environment
2. Installed requirements: `pip install -r requirements.txt`

### Playwright Issues
If Playwright fails:
1. Install browsers: `python3 -m playwright install`
2. Check internet connection
3. The example will skip gracefully if browsers aren't available

### Schedule Example
The schedule example runs quickly for demo purposes. In real applications, you'd typically run the scheduler in a longer loop or as a daemon.

## 🎓 Learning Path

1. Start with **Pathlib** and **Requests** - fundamental tools
2. Learn **Pandas** for data manipulation
3. Explore **BeautifulSoup** for web scraping
4. Try **Rich** and **Typer** for better CLI applications
5. Use **Schedule** for automation tasks
6. Master **Playwright** for web automation

Each library serves different purposes and together they form a powerful toolkit for Python development!

---

**Happy coding!** 🐍✨