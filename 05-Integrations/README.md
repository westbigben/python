# Multi-Platform Alert Notification Tool

A Python-based tool for sending alerts and notifications across multiple platforms including PagerDuty, Slack, Microsoft Teams, and Telegram.

## Features

- **Multi-Platform Support**: Send alerts to PagerDuty, Slack, MS Teams, and Telegram
- **Configurable**: Easy configuration through a simple config file
- **Flexible Input**: Accepts message content via standard input
- **Error Handling**: Robust error handling with clear status messages
- **Timeout Protection**: Built-in timeout protection for API calls
- **IAM Policy Monitoring**: Specifically designed for monitoring IAM policy violations

## Prerequisites

- Python 3.6 or higher
- Valid API credentials for the platforms you want to use

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the `alert.config` file and modify it with your credentials:

```ini
[DEFAULT]
# Options: PagerDuty, Slack, MS_Teams, Telegram
service_choice = PagerDuty

[PagerDuty]
routing_key = "your_pagerduty_routing_key"
service_url = "https://events.pagerduty.com/v2/enqueue"

[Slack]
webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXX"

[MS_Teams]
webhook_url = "https://outlook.office.com/webhook/XXXXX/IncomingWebhook/XXXXX"

[Telegram]
bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
chat_id = "YOUR_TELEGRAM_CHAT_ID"
```

### Platform-Specific Setup

#### PagerDuty
- Create a PagerDuty account and service
- Generate an Events API V2 routing key
- Update the `routing_key` in your config
- The tool will create incidents with "critical" severity

#### Slack
- Create a Slack app in your workspace
- Add the "Incoming Webhooks" feature
- Copy the webhook URL to your config
- Messages are formatted with code blocks for better readability

#### Microsoft Teams
- Create a webhook in your Teams channel
- Copy the webhook URL to your config
- Messages include structured cards with activity titles and subtitles

#### Telegram
- Create a bot using @BotFather
- Get your bot token
- Find your chat ID (you can use @userinfobot)
- Messages support MarkdownV2 formatting

## Usage

### Basic Usage

Send a message using the default configuration:

```bash
echo "Your alert message here" | python trigger-alert.py
```

### Custom Configuration File

Specify a custom configuration file:

```bash
echo "Your alert message here" | python trigger-alert.py -c /path/to/your/config.ini
```

### Examples

#### Send a critical alert
```bash
echo "CRITICAL: Database connection failed" | python trigger-alert.py
```

#### Send from a file
```bash
cat alert-message.txt | python trigger-alert.py
```

#### Send with custom config
```bash
echo "Warning: High CPU usage detected" | python trigger-alert.py -c production-alerts.ini
```

#### IAM Policy Violation Alert
```bash
echo "User 'admin' has overly broad IAM permissions: roles/owner" | python trigger-alert.py
```

## Output

The tool provides clear feedback on success or failure:

- ✅ Success messages with status codes
- ❌ Error messages with details
- Exit codes for automation integration

## Error Handling

The tool includes comprehensive error handling:
- Configuration file validation
- API timeout protection (10 seconds)
- Network error handling
- Invalid service configuration detection

## Integration Examples

### With Monitoring Tools

```bash
# Example: Check disk space and alert if critical
df -h | awk '$5 > "90%" {print "WARNING: Disk usage at " $5 " on " $1}' | python trigger-alert.py
```

### With CI/CD Pipelines

```bash
# Example: Alert on deployment failure
if ! deploy_application; then
    echo "DEPLOYMENT FAILED: Application deployment to production failed" | python trigger-alert.py
fi
```

### With Log Monitoring

```bash
# Example: Monitor error logs
tail -f /var/log/app.log | grep "ERROR" | python trigger-alert.py
```

### With IAM Policy Auditing

```bash
# Example: Check for broad IAM roles
gcloud projects get-iam-policy PROJECT_ID --flatten="bindings[].members" --filter="bindings.role:roles/owner" --format="table(bindings.role)" | python trigger-alert.py
```

## Platform-Specific Features

### PagerDuty
- Creates incidents with "trigger" action
- Sets severity to "critical"
- Includes custom details with violation information
- Uses Events API V2 for modern integration

### Slack
- Formats messages with code blocks
- Clear violation detection messaging
- Webhook-based integration for simplicity

### Microsoft Teams
- Structured message cards
- Activity titles and subtitles
- Professional appearance in Teams channels

### Telegram
- MarkdownV2 formatting support
- Bot API integration
- Clean, readable message format

## Troubleshooting

### Common Issues

1. **Configuration file not found**
   - Ensure the config file exists and the path is correct
   - Use absolute paths if needed

2. **Invalid service choice**
   - Check that `service_choice` in your config matches one of the supported platforms
   - Ensure the platform name is exactly as specified (case-sensitive)

3. **API errors**
   - Verify your API credentials are correct
   - Check network connectivity
   - Ensure the target service is available

4. **Message not sent**
   - Verify the message content is provided via stdin
   - Check that the message isn't empty

5. **PagerDuty routing key issues**
   - Ensure you're using Events API V2 routing keys
   - Verify the service URL is correct

## Development Status

✅ **Complete**: This tool is fully implemented with all platform integrations working:
- PagerDuty integration with Events API V2
- Slack webhook integration
- Microsoft Teams webhook integration  
- Telegram Bot API integration

## Contributing

The tool is feature-complete, but contributions are welcome for:
- Additional platform integrations
- Enhanced error handling
- Performance improvements
- Additional configuration options
- Testing and documentation improvements

## License

This project is open source. Please check the repository for specific licensing information.

## Support

For issues or questions, please check the repository issues or create a new one. 