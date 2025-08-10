import argparse
import configparser
import json
import sys
import requests
import os

# The existing functions for PagerDuty, Slack, and MS Teams go here...

def send_telegram_message(bot_token, chat_id, message_body):
    """Sends a message to a Telegram chat via the Bot API."""
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"IAM Policy Broad Roles Violations Detected:\n```{message_body}```",
        "parse_mode": "MarkdownV2"
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(telegram_url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        print(f"✅ Telegram message sent successfully. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error sending Telegram message: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Trigger alerts on various platforms.")
    parser.add_argument("-c", "--config", 
                        default="alert.config", 
                        help="Path to the configuration file (e.g., alert.config)")
    
    args = parser.parse_args()
    config_file_path = args.config
    
    if not os.path.exists(config_file_path):
        print(f"Error: Configuration file not found at '{config_file_path}'.", file=sys.stderr)
        sys.exit(1)
        
    message_body = sys.stdin.read().strip()
    if not message_body:
        print("Error: No message content provided via standard input.", file=sys.stderr)
        sys.exit(1)
        
    config = configparser.ConfigParser()
    config.read(config_file_path)
    
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
    elif service_choice == "Telegram":
        telegram_config = config['Telegram']
        send_telegram_message(telegram_config['bot_token'], telegram_config['chat_id'], message_body)
    else:
        print(f"Error: Invalid service '{service_choice}' configured.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
