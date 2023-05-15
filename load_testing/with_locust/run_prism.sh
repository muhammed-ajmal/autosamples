#!/bin/bash

# Install Prism if not already installed
if ! command -v prism &> /dev/null
then
    echo "Prism could not be found, installing..."
    npm install -g @stoplight/prism-cli
fi

# Run Prism mock server
prism mock openapi-schema.yaml