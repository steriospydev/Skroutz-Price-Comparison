#!/bin/bash

# Define the geckodriver version and the URL to download
GECKODRIVER_VERSION="v0.30.0"
GECKODRIVER_URL="https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VERSION}/geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz"

# Create a `tmp` directory in the current directory, if it doesn't exist
mkdir -p tmp/project/

# Download the geckodriver archive to the `project` folder inside the `tmp` directory
echo "Downloading geckodriver ${GECKODRIVER_VERSION} ..."
if ! wget -q "$GECKODRIVER_URL" -O tmp/project/geckodriver.tar.gz; then
    echo "Failed to download geckodriver archive."
    exit 1
fi

# Extract the archive
echo "Extracting geckodriver archive ..."
if ! tar -xzf tmp/project/geckodriver.tar.gz -C tmp/project/; then
    echo "Failed to extract geckodriver archive."
    exit 1
fi

# Move the geckodriver binary to /usr/local/bin/
echo "Installing geckodriver binary to /usr/local/bin/ ..."
if ! sudo mv tmp/project/geckodriver /usr/local/bin/; then
    echo "Failed to install geckodriver binary."
    exit 1
fi

# Set the correct permissions on the geckodriver binary
echo "Setting permissions on geckodriver binary ..."
if ! sudo chmod 755 /usr/local/bin/geckodriver; then
    echo "Failed to set permissions on geckodriver binary."
    exit 1
fi

echo "Geckodriver installation completed successfully."
