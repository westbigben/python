# Advanced Log Analysis Tools

A collection of professional-grade Python utilities for log file analysis and network monitoring, focusing on duplicate IP detection and security analysis.

## 🎯 Purpose

This directory contains advanced log analysis tools designed for system administrators, DevOps engineers, and security professionals who need to monitor and analyze server logs for patterns, anomalies, and security violations.

## 📁 Tools Overview

### **Duplicate IP Detector** (`duplicate_ip_detector.py`)

A comprehensive command-line tool for detecting and analyzing duplicate IP addresses in log files. Perfect for identifying potential security threats, monitoring user behavior, and analyzing traffic patterns.

#### ✨ Key Features

- **Multi-Format Support**: Apache, Nginx, and generic log formats
- **Flexible IP Detection**: IPv4 address validation and extraction
- **Statistical Analysis**: Detailed occurrence counting and reporting
- **Configurable Thresholds**: Set minimum occurrence counts for detection
- **Line Number Tracking**: Track exact locations of IP occurrences
- **Export Capabilities**: CSV output for further analysis
- **Sample Data Generation**: Built-in test data creation
- **Professional CLI**: Comprehensive command-line interface

#### 📊 Output Examples

**Console Report:**
```
=============================================================
🔍 DUPLICATE IP ADDRESS DETECTION REPORT
=============================================================

📊 STATISTICS:
   Total lines processed: 10
   Unique IP addresses: 4
   Total IP occurrences: 10
   IPs appearing ≥2 times: 2

🚨 DUPLICATE IPs:
-------------------------------------------------------------
   192.168.1.1    |     5 occurrences
   10.0.0.1       |     2 occurrences
   203.0.113.1    |     2 occurrences
-------------------------------------------------------------
```

**CSV Export:**
```csv
IP Address,Count,First Line,Last Line
192.168.1.1,5,1,8
10.0.0.1,2,2,6
203.0.113.1,2,4,9
```

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

### Setup
```bash
# Clone or navigate to this directory
cd "05-Killer Libraries"

# No installation required - uses only Python standard library
python3 --version  # Verify Python installation
```

## 🎮 Usage

### Quick Start

1. **Create sample data for testing:**
```bash
python3 duplicate_ip_detector.py --create-sample
```

2. **Analyze the sample log:**
```bash
python3 duplicate_ip_detector.py sample_access.log
```

### Advanced Usage Examples

#### Basic Detection
```bash
# Analyze any log file with default settings
python3 duplicate_ip_detector.py /var/log/access.log
```

#### Format-Specific Analysis
```bash
# Apache format logs
python3 duplicate_ip_detector.py --format apache /var/log/apache2/access.log

# Nginx format logs
python3 duplicate_ip_detector.py --format nginx /var/log/nginx/access.log

# Generic format (finds all IPs in each line)
python3 duplicate_ip_detector.py --format generic server.log
```

#### Threshold and Filtering
```bash
# Only show IPs appearing 5+ times
python3 duplicate_ip_detector.py --min-count 5 access.log

# Show only top 10 most frequent IPs
python3 duplicate_ip_detector.py --top 10 access.log

# Show line numbers where IPs appear
python3 duplicate_ip_detector.py --show-lines access.log
```

#### Export and Reporting
```bash
# Export results to CSV
python3 duplicate_ip_detector.py --output duplicates.csv access.log

# Comprehensive analysis with all options
python3 duplicate_ip_detector.py \
    --min-count 3 \
    --format apache \
    --show-lines \
    --top 20 \
    --output detailed_report.csv \
    /var/log/apache2/access.log
```

#### File Encoding
```bash
# Handle different file encodings
python3 duplicate_ip_detector.py --encoding latin1 old_log.txt
```

## 🔧 Command-Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--min-count` | `-c` | Minimum occurrences to consider duplicate | 2 |
| `--format` | `-f` | Log format: apache, nginx, generic | generic |
| `--output` | `-o` | Save results to CSV file | None |
| `--show-lines` | `-l` | Display line numbers of occurrences | False |
| `--top` | `-t` | Show only top N duplicate IPs | All |
| `--encoding` | `-e` | File encoding | utf-8 |
| `--create-sample` |  | Generate sample log for testing | False |

## 📋 Log Format Support

### Apache Common Log Format
```
192.168.1.1 - - [25/Dec/2024:10:00:01] "GET / HTTP/1.1" 200 1234
```

### Nginx Default Format  
```
192.168.1.1 - - [25/Dec/2024:10:00:01] "GET / HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
```

### Generic Format
Finds all IPv4 addresses in any line regardless of format:
```
2024-12-25 10:00:01 Connection from 192.168.1.1 to 10.0.0.5
[INFO] User 203.0.113.45 accessed resource via 172.16.0.1
```

## 🛡️ Security Applications

### Network Monitoring
- Detect potential brute force attacks (repeated login attempts)
- Identify suspicious IP addresses with unusual activity patterns
- Monitor for reconnaissance activities

### Traffic Analysis
- Analyze visitor patterns and behavior
- Identify automated bots vs. human users
- Track geographic distribution of traffic

### Compliance and Auditing
- Generate reports for security audits
- Track access patterns for compliance requirements
- Monitor for policy violations

## 🔍 Sample Data

The tool includes a sample log generator (`--create-sample`) that creates `sample_access.log` with:
- Multiple IP addresses with varying occurrence counts
- Apache Common Log Format entries
- Realistic timestamps and HTTP requests
- Perfect for testing and demonstration

## ⚡ Performance

- **Memory Efficient**: Processes large files line by line
- **Fast Processing**: Optimized regex patterns for IP extraction
- **Scalable**: Handles logs with millions of entries
- **Error Resilient**: Graceful handling of malformed lines and encoding issues

## 🔧 Customization

### Adding New Log Formats
Extend the `LOG_FORMATS` dictionary in the script:
```python
LOG_FORMATS = {
    'apache': re.compile(r'^(\d+\.\d+\.\d+\.\d+)'),
    'nginx': re.compile(r'^(\d+\.\d+\.\d+\.\d+)'),
    'custom': re.compile(r'your_custom_pattern'),
    'generic': IP_PATTERN
}
```

### Custom IP Validation
Modify the `is_valid_ip()` method to implement custom validation rules:
```python
def is_valid_ip(self, ip: str) -> bool:
    # Add custom validation logic
    if ip.startswith('127.'):  # Skip localhost
        return False
    return self.default_validation(ip)
```

## 🚨 Important Notes

- **Read-Only Tool**: This script only reads and analyzes log files, never modifies them
- **Privacy Considerations**: Be mindful of data privacy when sharing IP analysis results
- **Large Files**: For very large files (>1GB), consider using the `--top` option to limit output
- **Encoding**: Specify correct encoding for international or legacy log files

## 🔧 Troubleshooting

### Common Issues

1. **File Not Found**
   ```bash
   Error: File 'logfile.log' not found.
   ```
   - Verify the file path is correct
   - Check file permissions

2. **Encoding Errors**
   ```bash
   Error: Could not decode file. Try different encoding.
   ```
   - Try `--encoding latin1` or `--encoding cp1252`
   - Check the original file encoding

3. **No Results Found**
   - Lower the `--min-count` threshold
   - Verify the log format matches your file structure
   - Try `--format generic` for unknown formats

4. **Memory Issues with Large Files**
   - Use `--top N` to limit output
   - Process file in smaller chunks
   - Monitor system memory usage

## 🤝 Contributing

Contributions welcome for:
- Additional log format support
- Performance optimizations
- Enhanced statistical analysis
- New export formats (JSON, XML)
- Integration with SIEM systems

## 📄 License

This project is open source and available under the [GNU General Public License v3.0](../LICENSE).

---

**Perfect for system administrators, security analysts, and DevOps professionals! 🔍🛡️**
