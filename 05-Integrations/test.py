import argparse
import configparser
import json
import sys
import requests

def send_pagerduty_alert(routing_key, service_url, message_body):
    """Sends an incident to PagerDuty Events API V2."""
    payload = {
        "routing_key": routing_key,
        "event_action": "trigger",
        "payload": {
            "summary": "IAM Policy Broad Roles Violation",
            "source": "GCP Automation Script",
            "severity": "critical",
            "custom_details": {
                "violations": message_body
            }
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(service_url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        print(f"✅ PagerDuty alert triggered successfully. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error triggering PagerDuty alert: {e}", file=sys.stderr)
        sys.exit(1)

def send_slack_message(webhook_url, message_body):
    """Sends a message to a Slack channel via webhook."""
    payload = {
        "text": f"IAM Policy Broad Roles Violations Detected:\n```{message_body}```"
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        print(f"✅ Slack message sent successfully. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error sending Slack message: {e}", file=sys.stderr)
        sys.exit(1)

def send_ms_teams_message(webhook_url, message_body):
    """Sends a message to a Microsoft Teams channel via webhook."""
    payload = {
        "text": "IAM Policy Broad Roles Violations Detected",
        "sections": [{
            "activityTitle": "IAM Policy Audit Report",
            "activitySubtitle": "Broad Roles Violation",
            "text": f"```\n{message_body}\n```"
        }]
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        print(f"✅ MS Teams message sent successfully. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error sending MS Teams message: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Trigger alerts on various platforms.")
    parser.add_argument("-c", "--config", required=True, help="Path to the configuration file (e.g., alert.config)")
    
    # Read the output from stdin
    message_body = sys.stdin.read().strip()
    if not message_body:
        print("Error: No message content provided via standard input.", file=sys.stderr)
        sys.exit(1)
        
    config = configparser.ConfigParser()
    config.read(parser.parse_args().config)
    
    service_choice = config['DEFAULT'].get('service_choice')
    
    if service_choice == "PagerDuty":
        pd_config = config['PagerDuty']
        send_pagerduty_alert(pd_config['routing_key'], pd_config['service_url'], message_body)
    elif service_choice == "Slack":
        slack_config = config['Slack']
        send_slack_message(slack_config['webhook_url'], message_body)
    elif service_choice == "MS_Teams":
        teams_config = config['MS_Teams']
        send_ms_teams_message(teams_config['webhook_url'], message_body)
    else:
        print(f"Error: Invalid service '{service_choice}' configured.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()