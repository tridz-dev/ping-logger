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
DNS = os.getenv('DNS', '8.8.8.8')
GATEWAY = os.getenv('GATEWAY', '192.168.1.1')
EXTRA = os.getenv('EXTRA')  # No default; skip if not set

# Create a list of addresses to ping
addresses = [DNS, GATEWAY]
if EXTRA:
    addresses.append(EXTRA)

log_filename = 'ping.log'

# Create a rotating log file handler that rotates every 7 days
log_handler = TimedRotatingFileHandler(log_filename, when='H', backupCount=168)

# Set the log format
log_formatter = logging.Formatter('%(asctime)s %(message)s')
log_handler.setFormatter(log_formatter)

# Create a logger and add the log handler
logger = logging.getLogger('PingLogger')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

while True:
    for address in addresses:
        try:
            # Ping the IP address
            response_time = ping(address, timeout=1)

            # Get the current timestamp
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if response_time is not None:
                # Log the ping response time to the file
                log_message = f'{current_time} - Ping to {address} successful. Response time: {response_time} ms'
                logger.info(log_message)
            else:
                # Log the failure to ping
                log_message = f'{current_time} - Ping to {address} failed.'
                logger.warning(log_message)

        except Exception as e:
            # Log any unexpected exceptions
            log_message = f'{current_time} - Error pinging {address}: {e}'
            logger.error(log_message)

    time.sleep(1)  # Sleep for 1 seconds
