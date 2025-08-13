# Python Scripts Collection

A comprehensive collection of Python scripts organized by skill level and purpose, designed to help developers learn Python concepts and provide practical utilities for various tasks.

## 🗂️ Directory Structure

### **01-Basics** - Python Fundamentals
Core Python programming concepts and syntax including:
- Basic Python syntax and output (`hello_world.py`)
- Data structures (lists, dictionaries, sets, tuples, arrays)
- Control flow (loops, conditional statements)
- Functions and modules
- Error handling with try-except blocks
- String formatting techniques
- JSON file operations
- Mathematical operations

**Prerequisites:** Python 3.6+ (uses only standard library)

### **02-Intermediate** - Advanced Python Features
Intermediate Python concepts including:
- **Decorators** - Function wrappers and advanced functionality
- **List Comprehensions** - Concise and readable list transformations
- Best practices for intermediate Python development

**Prerequisites:** Python 3.6+, basic Python knowledge

### **03-Fancy** - Fun and Visual Projects
Entertainment and educational scripts showcasing:
- **Mandelbrot Fractal Generator** - Mathematical visualization using NumPy and Matplotlib
- **Turtle Spirograph** - Colorful animated graphics using built-in turtle module
- **Simple Chatbot** - Rule-based conversational AI
- **QR Code Generator** - Create QR codes for URLs and text
- **Duplicate IP Detector** - Log analysis tool for network monitoring

**Prerequisites:** Python 3.6+, external libraries (see requirements.txt)

### **04-GCP** - Google Cloud Platform Management
Production-ready scripts for GCP resource management:
- **VM Management** - Automated shutdown of development instances
- **Disk Cleanup** - Find and remove unattached disks
- **IP Address Management** - Clean up unused static IPs
- **Security Auditing** - Check for public buckets and broad IAM permissions
- **Policy Review** - Audit IAM policies for compliance

**Prerequisites:** Python 3.7+, GCP SDK, appropriate IAM permissions

### **05-Integrations** - Multi-Platform Alert System
Professional notification and alerting tool:
- **PagerDuty Integration** - Create critical incidents
- **Slack Notifications** - Send formatted messages to channels
- **Microsoft Teams** - Structured message cards
- **Telegram Bot** - MarkdownV2 formatted messages
- **IAM Policy Monitoring** - Specialized for security violations

**Prerequisites:** Python 3.6+, platform-specific API credentials

### **05-Killer Libraries** - Essential Python Tools
Demonstration scripts for a duplicate IP detection utility:
- **Advanced Log Analysis** - Regex-based IP extraction from various log formats
- **Statistical Reporting** - Detailed occurrence tracking and CSV export
- **Command-line Interface** - Professional CLI with argparse

**Prerequisites:** Python 3.6+ (uses only built-in modules)

### **06-Killer Libraries** - Essential Python Libraries
Comprehensive examples of 9 powerful Python libraries:
- **Pandas** - Data analysis and manipulation
- **Requests** - HTTP client library
- **BeautifulSoup** - HTML/XML parsing
- **Pathlib** - Modern file system operations
- **Typer** - CLI applications made easy
- **Rich** - Beautiful terminal output
- **Schedule** - Job scheduling
- **Playwright** - Web browser automation

**Prerequisites:** Python 3.6+, virtual environment recommended

## 🚀 Quick Start

### For Beginners
1. Start with **01-Basics** - Learn Python fundamentals
2. Progress to **02-Intermediate** - Advanced language features
3. Explore **03-Fancy** - Fun projects to apply your skills

### For Practical Applications
1. **04-GCP** - Cloud infrastructure management
2. **05-Integrations** - Professional alerting systems
3. **06-Killer Libraries** - Essential third-party tools

## 📋 Installation Guide

### Basic Setup (01-Basics, 02-Intermediate, 05-Killer Libraries)
```bash
# No external dependencies required
python3 --version  # Verify Python 3.6+
```

### Projects with Dependencies
```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Install project-specific requirements
cd 03-Fancy && pip install -r requirements.txt
cd 04-GCP && pip install -r requirements.txt
cd 05-Integrations && pip install -r requirements.txt
cd 06-Killer Libraries && pip install -r requirements.txt
```

### Special Setup for Web Automation
```bash
# For Playwright (06-Killer Libraries)
python3 -m playwright install
```

## 🎯 Learning Path

### **Beginner Path** (Estimated: 2-3 weeks)
1. **Week 1:** Complete all scripts in `01-Basics`
2. **Week 2:** Master `02-Intermediate` concepts
3. **Week 3:** Build projects from `03-Fancy`

### **Professional Development Path** (Estimated: 4-6 weeks)
1. **Weeks 1-2:** Foundations (`01-Basics`, `02-Intermediate`)
2. **Week 3:** Essential libraries (`06-Killer Libraries`)
3. **Week 4:** Cloud operations (`04-GCP`)
4. **Weeks 5-6:** Production systems (`05-Integrations`)

### **Practical Applications Path**
Choose directories based on your immediate needs:
- **Data Analysis:** `06-Killer Libraries` (Pandas, BeautifulSoup)
- **System Administration:** `04-GCP`, `05-Killer Libraries`
- **DevOps/Monitoring:** `05-Integrations`, `04-GCP`
- **Web Development:** `06-Killer Libraries` (Requests, Playwright)

## 🔧 Prerequisites by Directory

| Directory | Python Version | External Dependencies | Special Requirements |
|-----------|----------------|----------------------|---------------------|
| 01-Basics | 3.6+ | None | None |
| 02-Intermediate | 3.6+ | None | None |
| 03-Fancy | 3.6+ | NumPy, Matplotlib, QRCode | Graphics environment |
| 04-GCP | 3.7+ | Google Cloud SDK | GCP account, IAM roles |
| 05-Integrations | 3.6+ | Requests | API credentials |
| 05-Killer Libraries | 3.6+ | None | None |
| 06-Killer Libraries | 3.6+ | 9 third-party libraries | Virtual environment |

## 🛡️ Security Notes

- **04-GCP**: Contains destructive operations (VM shutdown, resource deletion)
- **05-Integrations**: Requires secure handling of API credentials
- Always test scripts in development environments first
- Review IAM permissions before running GCP scripts

## 🤝 Contributing

Each directory has its own detailed README with specific contribution guidelines. General principles:
- Follow existing code structure and error handling patterns
- Include comprehensive documentation
- Test thoroughly before submitting
- Update requirements.txt when adding dependencies

## 📄 License

This project is open source and available under the **GNU General Public License v3.0**.

See the [LICENSE](LICENSE) file in each directory for complete terms.

## 📞 Support

- Check individual directory READMEs for specific guidance
- Review Python documentation for language concepts
- Test examples in the recommended learning order

---

**Ready to start your Python journey? Choose your path above and dive in! 🐍✨**
