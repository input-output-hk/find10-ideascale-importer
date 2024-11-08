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
# Example command:
#  earthly -P +run --fund 12 --fund_group_id 95 --fund_campaign_id 415 --stages "--stages 4793 --stages 4799 --stages 4805 --stages 4811 --sta#  earthly -P +run --fund 12 --fund_group_id 95 --fund_campaign_id 415 --stages "--stages 4793 --stages 4799 --stages 4805 --stages 4811 --stages 4817" --ideascale_url "https://cardano.ideascale.com"
# To get also the reviews add the --assesments parameter poiting to the reviews file
#  earthly -P +run --fund 12 --fund_group_id 95 --fund_campaign_id 415 --stages "--stages 4793 --stages 4799 --stages 4805 --stages 4811 --sta#  earthly -P +run --fund 12 --fund_group_id 95 --fund_campaign_id 415 --stages "--stages 4793 --stages 4799 --stages 4805 --stages 4811 --stages 4817" --ideascale_url "https://cardano.ideascale.com" --assesments "reviews.csv"
run:
    FROM +build
    # These args can be passed as earthly CLI arguments.
    ARG api_token
    ARG fund
    ARG fund_campaign_id
    ARG fund_group_id
    ARG stages
    ARG output_dir="./data"
    ARG ideascale_url="https://temp-cardano-sandbox.ideascale.com"
    ARG assessments= false

    # Reset the $output_dir
    RUN rm -rf $output_dir && mkdir -p $output_dir

    # Run the script
    IF [ "$assessments" = "false" ]
        RUN --no-cache --secret api_token python3 main.py --fund $fund \
            --ideascale-url $ideascale_url --fund-campaign-id $fund_campaign_id \
            --fund-group-id $fund_group_id $stages --output-dir $output_dir \
            --api-token $api_token
    ELSE
        RUN --no-cache --secret api_token python3 main.py --fund $fund \
            --ideascale-url $ideascale_url --fund-campaign-id $fund_campaign_id \
            --fund-group-id $fund_group_id $stages --output-dir $output_dir \
            --api-token $api_token --assessments $assessments
    END
    SAVE ARTIFACT $output_dir data AS LOCAL data
