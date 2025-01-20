import logging
import requests
from bs4 import BeautifulSoup
import os
from miscellaneous import sanitize_filename
from console_prompt import print_message_and_progressing_bar


def save_policies_to_html(
    policies_list: list, policy_type: str, output_file_path: str = "./output/html"
):
    processed = 0
    output_file_path = f"{output_file_path}/{policy_type}"
    total_process = len(policies_list)
    for policy in policies_list:
        policy_url = policy["url"]
        # convert and remove any special characters from the policy name to create a file name
        policy_name = sanitize_filename(policy["name"])
        # Exporting the request website url to HTML file
        policy_html = requests.get(policy_url)
        soup = BeautifulSoup(policy_html.content, "html.parser")
        # check if output_file_path exosts, if not create it
        if not os.path.exists(output_file_path):
            os.makedirs(output_file_path)
        # start writing the content to the file
        with open(f"{output_file_path}/{policy_name}.html", "w") as file:
            file.write(str(soup))
        processed += 1

        print_message_and_progressing_bar(
            f"Exporting {policy_name} to HTML file...", processed / total_process * 100
        )
    print(f"\n{processed} out of {total_process} {policy_type} processed.")
    logging.info(f"\n{processed} out of {total_process} {policy_type} processed.")
