#!/usr/bin/env python3
"""
Duplicate IP Address Detector
============================

A script to detect duplicate IP addresses from log files.
Supports various log formats and provides detailed analysis.

Usage:
    python3 duplicate_ip_detector.py <logfile> [options]
    
Examples:
    python3 duplicate_ip_detector.py access.log
    python3 duplicate_ip_detector.py --min-count 5 --format apache access.log
    python3 duplicate_ip_detector.py --output duplicates.txt server.log
"""

import re
import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import List, Dict, Tuple, Set


class IPDetector:
    """Detect and analyze duplicate IP addresses from log files."""
    
    # IP address regex pattern (IPv4)
    IP_PATTERN = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    
    # Common log format patterns
    LOG_FORMATS = {
        'apache': re.compile(r'^(\d+\.\d+\.\d+\.\d+)'),
        'nginx': re.compile(r'^(\d+\.\d+\.\d+\.\d+)'),
        'generic': IP_PATTERN
    }
    
    def __init__(self, log_format: str = 'generic'):
        """Initialize the IP detector with specified log format."""
        self.format = log_format
        self.pattern = self.LOG_FORMATS.get(log_format, self.IP_PATTERN)
        self.ip_counts = Counter()
        self.ip_lines = defaultdict(list)
        self.total_lines = 0
        
    def extract_ips_from_line(self, line: str, line_num: int) -> List[str]:
        """Extract IP addresses from a single line."""
        if self.format in ['apache', 'nginx']:
            # For specific formats, extract first IP only
            match = self.pattern.match(line.strip())
            return [match.group(1)] if match else []
        else:
            # For generic format, find all IPs in the line
            return self.pattern.findall(line)
    
    def is_valid_ip(self, ip: str) -> bool:
        """Validate if IP address is properly formatted."""
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        try:
            return all(0 <= int(part) <= 255 for part in parts)
        except ValueError:
            return False
    
    def process_log_file(self, filepath: str, encoding: str = 'utf-8') -> None:
        """Process the log file and extract IP addresses."""
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                for line_num, line in enumerate(file, 1):
                    self.total_lines += 1
                    line = line.strip()
                    if not line:
                        continue
                        
                    ips = self.extract_ips_from_line(line, line_num)
                    for ip in ips:
                        if self.is_valid_ip(ip):
                            self.ip_counts[ip] += 1
                            self.ip_lines[ip].append(line_num)
                            
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Error: Could not decode file '{filepath}'. Try different encoding.")
            sys.exit(1)
        except Exception as e:
            print(f"Error processing file: {e}")
            sys.exit(1)
    
    def get_duplicates(self, min_count: int = 2) -> Dict[str, int]:
        """Get IP addresses that appear more than min_count times."""
        return {ip: count for ip, count in self.ip_counts.items() if count >= min_count}
    
    def get_statistics(self) -> Dict[str, int]:
        """Get overall statistics about the log analysis."""
        duplicates = self.get_duplicates()
        return {
            'total_lines': self.total_lines,
            'unique_ips': len(self.ip_counts),
            'total_ip_occurrences': sum(self.ip_counts.values()),
            'duplicate_ips': len(duplicates),
            'duplicate_occurrences': sum(duplicates.values())
        }
    
    def print_report(self, min_count: int = 2, show_lines: bool = False, top_n: int = None) -> None:
        """Print a detailed report of duplicate IP addresses."""
        duplicates = self.get_duplicates(min_count)
        stats = self.get_statistics()
        
        # Header
        print("=" * 60)
        print("🔍 DUPLICATE IP ADDRESS DETECTION REPORT")
        print("=" * 60)
        
        # Statistics
        print(f"\n📊 STATISTICS:")
        print(f"   Total lines processed: {stats['total_lines']:,}")
        print(f"   Unique IP addresses: {stats['unique_ips']:,}")
        print(f"   Total IP occurrences: {stats['total_ip_occurrences']:,}")
        print(f"   IPs appearing ≥{min_count} times: {stats['duplicate_ips']:,}")
        
        if not duplicates:
            print(f"\n✅ No duplicate IP addresses found (threshold: {min_count})")
            return
        
        # Sort duplicates by count (descending)
        sorted_duplicates = sorted(duplicates.items(), key=lambda x: x[1], reverse=True)
        
        # Limit to top N if specified
        if top_n:
            sorted_duplicates = sorted_duplicates[:top_n]
        
        print(f"\n🚨 DUPLICATE IPs (showing {'top ' + str(top_n) if top_n else 'all'}):")
        print("-" * 60)
        
        for ip, count in sorted_duplicates:
            print(f"   {ip:<15} | {count:>5} occurrences", end="")
            
            if show_lines:
                lines = self.ip_lines[ip]
                if len(lines) <= 5:
                    print(f" | Lines: {', '.join(map(str, lines))}")
                else:
                    print(f" | Lines: {', '.join(map(str, lines[:3]))}...+{len(lines)-3} more")
            else:
                print()
        
        print("-" * 60)
    
    def save_report(self, output_file: str, min_count: int = 2) -> None:
        """Save duplicate IPs to a file."""
        duplicates = self.get_duplicates(min_count)
        
        try:
            with open(output_file, 'w') as f:
                f.write("IP Address,Count,First Line,Last Line\n")
                for ip, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
                    lines = self.ip_lines[ip]
                    first_line = min(lines)
                    last_line = max(lines)
                    f.write(f"{ip},{count},{first_line},{last_line}\n")
            
            print(f"📁 Report saved to: {output_file}")
            
        except Exception as e:
            print(f"Error saving report: {e}")


def create_sample_log():
    """Create a sample log file for testing."""
    sample_content = """192.168.1.1 - - [25/Dec/2024:10:00:01] "GET / HTTP/1.1" 200 1234
10.0.0.1 - - [25/Dec/2024:10:00:02] "GET /api HTTP/1.1" 404 567
192.168.1.1 - - [25/Dec/2024:10:00:03] "POST /login HTTP/1.1" 200 890
203.0.113.1 - - [25/Dec/2024:10:00:04] "GET /home HTTP/1.1" 200 2345
192.168.1.1 - - [25/Dec/2024:10:00:05] "GET /dashboard HTTP/1.1" 200 3456
10.0.0.1 - - [25/Dec/2024:10:00:06] "GET /profile HTTP/1.1" 200 1111
192.168.1.100 - - [25/Dec/2024:10:00:07] "GET /search HTTP/1.1" 200 777
192.168.1.1 - - [25/Dec/2024:10:00:08] "GET /logout HTTP/1.1" 200 456
203.0.113.1 - - [25/Dec/2024:10:00:09] "GET /help HTTP/1.1" 200 888
192.168.1.1 - - [25/Dec/2024:10:00:10] "GET /settings HTTP/1.1" 200 999"""
    
    with open('sample_access.log', 'w') as f:
        f.write(sample_content)
    print("📝 Created sample_access.log for testing")


def main():
    """Main function to handle command line arguments and run the detector."""
    parser = argparse.ArgumentParser(
        description="Detect duplicate IP addresses in log files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s access.log
  %(prog)s --min-count 5 --format apache access.log
  %(prog)s --output duplicates.csv --show-lines server.log
  %(prog)s --create-sample  # Create a sample log for testing
        """
    )
    
    parser.add_argument('logfile', nargs='?', help='Path to the log file to analyze')
    parser.add_argument('--min-count', '-c', type=int, default=2,
                        help='Minimum count to consider as duplicate (default: 2)')
    parser.add_argument('--format', '-f', choices=['apache', 'nginx', 'generic'], 
                        default='generic', help='Log format (default: generic)')
    parser.add_argument('--output', '-o', help='Save results to CSV file')
    parser.add_argument('--show-lines', '-l', action='store_true',
                        help='Show line numbers where IPs appear')
    parser.add_argument('--top', '-t', type=int, help='Show only top N duplicate IPs')
    parser.add_argument('--encoding', '-e', default='utf-8',
                        help='File encoding (default: utf-8)')
    parser.add_argument('--create-sample', action='store_true',
                        help='Create a sample log file for testing')
    
    args = parser.parse_args()
    
    # Create sample log if requested
    if args.create_sample:
        create_sample_log()
        return
    
    # Validate arguments
    if not args.logfile:
        parser.error("logfile is required (use --create-sample to generate test data)")
    
    if not Path(args.logfile).exists():
        print(f"Error: File '{args.logfile}' does not exist.")
        sys.exit(1)
    
    # Run the detector
    print(f"🔍 Analyzing log file: {args.logfile}")
    print(f"📋 Format: {args.format}, Min count: {args.min_count}")
    
    detector = IPDetector(args.format)
    detector.process_log_file(args.logfile, args.encoding)
    detector.print_report(args.min_count, args.show_lines, args.top)
    
    # Save to file if requested
    if args.output:
        detector.save_report(args.output, args.min_count)


if __name__ == "__main__":
    main()
