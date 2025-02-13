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

    - keyboard
    - requests
    - bs4
    - pandas
    - ipykernel
    - openai
    - tiktoken

-   `pandas==2.2.3`
-   `openpyxl==3.1.5`
-   `requests==2.32.3`
-   `beautifulsoup4==4.12.2`
-   `logging` (standard library)
-   `keyboard==0.13.5`
-   `ipykernel==6.29.5`
-   `tiktoken==0.8.0`
-   `openai==0.61.0`

You can install these packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

However it is recommended to install the packages from anaconda environment:

```
conda env create -f policy-analysis.yml
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
-   `export_html.py`: Save scraped html files to local disk.
-   `export_to_files.py`: The script to save the scraped data to an Excel or
    JSON file.
-   `policy_extract.py`: The script to scrape the policy documents from html
    files and save to a python dictionary for further processing.
-   `miscellaneous.py`: The script to other store miscellaneous functions.

In the analysis folder, it contains following 2 juptyer notebooks and output
data in JSON format:

-   `call_llm.ipynb`: This file calls locally deployed language model to
    generate the response for the given questions and save in JSON format.
-   `llm_response_analysis.ipynb`: This randomly selects the response from the
    generated JSON file and analyze the response.

## How to Use

To use the project, follow these steps:

1.  Clone the repository:

    ```bash
    git clone https://github.com/ChrisYangS/policy_analysis.git
    ```

2.  Install the required packages:

    Either by installing the packages from the `requirements.txt` file using
    pip:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, and it is recommended to install the packages from anaconda
    environment:

    ```
    conda env create -f policy-analysis.yml
    ```

3.  Actiavate the anaconda environment if you have installed the packages from
    anaconda environment:

    ```
    conda activate policy-analysis
    ```

4.  Run the `main.py` script once the packages are installed:

    ```bash
    python main.py
    ```

5.  Wait for the script to process the data and save it to an Excel file.
    -   All exported data will be saved in the
        `.\\output\otago_policies_%Y%m%d%H%M%S.xlsx` file.
    -   A log file will be saved in the
        `.\\output\policy_data_load_%Y%m%d%H%M%S.log` folder.
6.  Check the `otago_policies.xlsx` file for the processed data.
