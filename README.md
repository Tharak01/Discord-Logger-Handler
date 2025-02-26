# Discord Logger

A simple, flexible Discord logging package that sends logs to Discord channels via webhooks.

## Installation

```bash
pip install discord-logger-handler
```

## Quick Start

```python
from discrd_logger import DiscordLogger

# Initialize the logger
logger = DiscordLogger(
    webhook_url="your_discord_webhook_url",
    app_name="MyApp",
    min_level="DEBUG"  # Optional, defaults to "DEBUG"
)

# Send logs at different levels
logger.debug("Debug message", extra_field="debug value")
logger.info("Info message", user="john_doe")
logger.warning("Warning message", system_resources="running low")
logger.error("Error message", error_code=500)
logger.critical("Critical message", affected_users=1000)
```

## Features

- Multiple log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Custom fields support via kwargs
- Color-coded embeds in Discord
- Fallback to standard Python logging
- Timezone-aware timestamps
- Simple and intuitive API

## Configuration

The logger can be configured with the following parameters:

- `webhook_url`: Your Discord webhook URL
- `app_name`: Name of your application (appears in log titles)
- `min_level`: Minimum logging level to process

## Examples

### Basic Usage

```python
logger = DiscordLogger("webhook_url", "MyApp")
logger.info("User logged in", user_id="123", ip="192.168.1.1")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
