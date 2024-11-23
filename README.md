# Policy Analysis Project

This project is designed to analyze various policy documents, including
guidelines, plans, strategies, policies, procedures, regulations, and statutes.
The project uses Python to scrape, process, and store data from these documents
into an Excel file.

## Features

-   Scrape policy documents from provided URLs.
-   Extract specific sections and content from the documents.
-   Combine data from multiple lists into a single Excel file.
-   Save the processed data into an Excel sheet for further analysis.

## Requirements

The project requires the following Python packages:

-   `pandas==2.2.3`
-   `openpyxl==3.1.5`
-   `requests==2.32.3`
-   `beautifulsoup4==4.12.2`
-   `logging` (standard library)

You can install these packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Structure

The project consists of the following files:

-   `main.py`: The main script to run the project.
-   `config.json`: The configuration file to store the URLs and sections to
    scrape.
-   `README.md`: The project's README file.

In the utilies folder, the project contains the following files:

-   `console_prompt.py`: The script to user interface with the user, i.e.
    progressing complete percentage update
-   `export_to_excel.py`: The script to export the processed data to an Excel
    file.
-   `policies_extractor.py`: The script to extract data from the policy
    documents.

## How to Use

To use the project, follow these steps:

1.  Clone the repository:

    ```bash
    git clone
    ```

2.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the `main.py` script:

    ```bash
    python main.py
    ```

4.  Wait for the script to process the data and save it to an Excel file.
    -   All exported data will be saved in the
        `.\\output\otago_policies_%Y%m%d%H%M%S.xlsx` file.
    -   A log file will be saved in the
        `.\\output\policy_data_load_%Y%m%d%H%M%S.log` folder.
5.  Check the `otago_policies.xlsx` file for the processed data.
