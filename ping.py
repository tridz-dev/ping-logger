import os
from ping3 import ping
import time
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("ping.env")

# Get environment variables or default values
DNS = os.getenv('DNS')
GATEWAY = os.getenv('GATEWAY')
EXTRA = os.getenv('EXTRA')  # No default; skip if not set
EXTRA2 = os.getenv('EXTRA2')  # Additional IP 1
EXTRA3 = os.getenv('EXTRA3')  # Additional IP 2
EXTRA4 = os.getenv('EXTRA4')
# Create a list of addresses to ping
addresses = [DNS, GATEWAY]
if EXTRA:
    addresses.append(EXTRA)
if EXTRA2:
    addresses.append(EXTRA2)
if EXTRA3:
    addresses.append(EXTRA3)
if EXTRA4:
    addresses.append(EXTRA4)

log_filename = 'ping.log'

# Create a rotating log file handler that rotates every hour, keeps 168 hours (7 days)
log_handler = TimedRotatingFileHandler(log_filename, when='H', interval=1, backupCount=168)

# Set the log format
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)

# Create a logger and add the log handler
logger = logging.getLogger('PingLogger')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

print(f"Starting ping monitor for addresses: {addresses}")
print("Press Ctrl+C to stop")

try:
    while True:
        for address in addresses:
            try:
                # Ping the IP address
                response_time = ping(address, timeout=1)

                if response_time is not None:
                    # Log the ping response time to the file
                    log_message = f'Ping to {address} successful. Response time: {response_time*1000:.2f} ms'
                    logger.info(log_message)
                else:
                    # Log the failure to ping
                    log_message = f'Ping to {address} failed.'
                    logger.warning(log_message)
            except Exception as e:
                # Log any unexpected exceptions
                log_message = f'Error pinging {address}: {e}'
                logger.error(log_message)

        time.sleep(1)  # Sleep for 1 second

except KeyboardInterrupt:
    print("\nPing monitor stopped by user")
    logger.info("Ping monitor stopped")