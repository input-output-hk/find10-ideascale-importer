# Set the Earthly version to 0.7
VERSION 0.7

# Use current debian stable with python
FROM python:3.11-slim

# Environment variables for python
ENV PYTHONUNBUFFERED=true

# Build base container and install python requirements
build-reqs:
    WORKDIR /ideascale-importer

    # Install system dependencies
    RUN apt-get update && \
        apt-get install -y --no-install-recommends curl build-essential #libxml2-dev libxslt-dev zlib1g-dev python3-lxml

    ## apt cleanup
    RUN apt-get clean && \
        rm -rf /var/lib/apt/lists/*

    # Install package dependencies from requirements
    COPY requirements.txt ./
    RUN pip install -r requirements.txt

# Build container with main script and extras.
build:
    FROM +build-reqs
    # Copy the package files to the container
    COPY --dir scripts examples templates main.py README.md ./

    SAVE ARTIFACT /ideascale-importer

# Run the script.
#
# This target requires that the `api_token` to be provided as a secret.
#
# The simplest way to accomplish this, is to put it in a `./secret` file, so that Earthly can retrieve it.
# It also needs to be provided by CI to work there.
run:
    FROM +build
    # These args can be passed as earthly CLI arguments.
    ARG api_token
    ARG ideascale_url="https://temp-cardano-sandbox.ideascale.com"
    ARG fund="11"
    ARG fund_campaign_id="395"
    ARG fund_group_id="91"
    ARG output_dir="./data"
    ARG stages="--stages 4747 --stages 4748 --stages 4749 --stages 4750 --stages 4751 --stages 4753 --stages 4754 --stages 4755 --stages 4756 --stages 4757 --stages 4759 --stages 4760 --stages 4761 --stages 4762 --stages 4763 --stages 4765 --stages 4766 --stages 4767 --stages 4768 --stages 4769 --stages 4771 --stages 4772 --stages 4773 --stages 4774 --stages 4775 --stages 4777 --stages 4778 --stages 4779 --stages 4780 --stages 4781 --stages 4783 --stages 4784 --stages 4785 --stages 4786 --stages 4787"

    # Reset the $output_dir
    RUN rm -rf $output_dir && mkdir -p $output_dir

    # Run the script
    RUN --no-cache --secret api_token python3 main.py --fund $fund --ideascale-url $ideascale_url --fund-campaign-id $fund_campaign_id --fund-group-id $fund_group_id $stages --output-dir $output_dir --api-token $api_token
    SAVE ARTIFACT $output_dir data AS LOCAL data
