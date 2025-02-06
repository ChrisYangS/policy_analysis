# application entry point

import sys

sys.path.insert(0, "./utilities/")
import keyboard
import logging
import os
import time
from utilities.policies_extract import get_policies, get_policy_details
from export_html import save_policies_to_html

from utilities.export_to_files import create_excel_output_file, create_json_output_file

if __name__ == "__main__":
    # Configure logging to save to a file
    logging.basicConfig(
        filename=f"./output/policy_data_load_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )
    try:
        # Check user if want to extract data from the website
        print("\nDo you want to extract data from the website? (y/n)")
        user_input = input()
        if user_input.lower() == "y":
            print("\nExtracting data from the website...")
            logging.info("\nExtracting data from the website...")
            # -------------read the ALL_POLICE_URL and get the urls of all the policies-----------
            guidelines_list = get_policies(policy_type="Guidelines")
            plan_strategies_list = get_policies(policy_type="Plans & Strategies")
            policies_list = get_policies(policy_type="Policies")
            procedure_list = get_policies(policy_type="Procedures")
            regulations_list = get_policies(policy_type="Regulations")
            statues_list = get_policies(policy_type="Statutes")
            # save the policies to html files
            save_policies_to_html(guidelines_list, "Guidelines")
            save_policies_to_html(plan_strategies_list, "Plans & Strategies")
            save_policies_to_html(policies_list, "Policies")
            save_policies_to_html(procedure_list, "Procedures")
            save_policies_to_html(regulations_list, "Regulations")
            save_policies_to_html(statues_list, "Statutes")
            print("\nAll policies are saved to HTML files.")
            logging.info("\nAll policies are saved to HTML files.")

        # then extract data from the saved html files
        print("\nExtracting data from the saved HTML files...")
        logging.info("\nExtracting data from the saved HTML files...")
        output_file_path = "./output/html"
        # get the policy details from the saved html files

        for folder in os.listdir(output_file_path):
            # recreate the policy list dictionary similar to the get_policies function
            match folder:
                case "Guidelines":
                    guidelines_list = []
                    for file in os.listdir(f"{output_file_path}/{folder}"):
                        if file.endswith(".html"):
                            guidelines_list.append(
                                {
                                    "policy type": "Guidelines",
                                    "name": file.replace(".html", ""),
                                    "url": f"{output_file_path}/{folder}/{file}",
                                }
                            )
                case "Plans & Strategies":
                    plan_strategies_list = []
                    for file in os.listdir(f"{output_file_path}/{folder}"):
                        if file.endswith(".html"):
                            plan_strategies_list.append(
                                {
                                    "policy type": "Plans & Strategies",
                                    "name": file.replace(".html", ""),
                                    "url": f"{output_file_path}/{folder}/{file}",
                                }
                            )
                case "Policies":
                    policies_list = []
                    for file in os.listdir(f"{output_file_path}/{folder}"):
                        if file.endswith(".html"):
                            policies_list.append(
                                {
                                    "policy type": "Policies",
                                    "name": file.replace(".html", ""),
                                    "url": f"{output_file_path}/{folder}/{file}",
                                }
                            )
                case "Procedures":
                    procedure_list = []
                    for file in os.listdir(f"{output_file_path}/{folder}"):
                        if file.endswith(".html"):
                            procedure_list.append(
                                {
                                    "policy type": "Procedures",
                                    "name": file.replace(".html", ""),
                                    "url": f"{output_file_path}/{folder}/{file}",
                                }
                            )
                case "Regulations":
                    regulations_list = []
                    for file in os.listdir(f"{output_file_path}/{folder}"):
                        if file.endswith(".html"):
                            regulations_list.append(
                                {
                                    "policy type": "Regulations",
                                    "name": file.replace(".html", ""),
                                    "url": f"{output_file_path}/{folder}/{file}",
                                }
                            )
                case "Statutes":
                    statues_list = []
                    for file in os.listdir(f"{output_file_path}/{folder}"):
                        if file.endswith(".html"):
                            statues_list.append(
                                {
                                    "policy type": "Statutes",
                                    "name": file.replace(".html", ""),
                                    "url": f"{output_file_path}/{folder}/{file}",
                                }
                            )
                case _:
                    raise ValueError("Invalid folder name")

        # Load policy details from the saved html files
        guideline_contents = get_policy_details(guidelines_list)
        plan_strategies_contents = get_policy_details(plan_strategies_list)
        policies_contents = get_policy_details(policies_list)
        procedure_contents = get_policy_details(procedure_list)
        regulations_contents = get_policy_details(regulations_list)
        statues_contents = get_policy_details(statues_list)
        print("\nAll policy data is extracted.")
        logging.info("\nAll policy data is extracted.")
        # Check which file format does the user want to save the data: excel, json or both
        print(
            "\nPlease select the file format to save the data by typing the number: \n1. excel, \n2. json or \n3. both"
        )
        user_input = input()
        if user_input == "1":
            create_excel_output_file(
                guidelines_list,
                plan_strategies_list,
                policies_list,
                procedure_list,
                regulations_list,
                statues_list,
                guideline_contents,
                plan_strategies_contents,
                policies_contents,
                procedure_contents,
                regulations_contents,
                statues_contents,
            )
        elif user_input == "2":
            create_json_output_file(
                guideline_contents,
                plan_strategies_contents,
                policies_contents,
                procedure_contents,
                regulations_contents,
                statues_contents,
            )
        elif user_input == "3":
            create_excel_output_file(
                guidelines_list,
                plan_strategies_list,
                policies_list,
                procedure_list,
                regulations_list,
                statues_list,
                guideline_contents,
                plan_strategies_contents,
                policies_contents,
                procedure_contents,
                regulations_contents,
                statues_contents,
            )
            create_json_output_file(
                guideline_contents,
                plan_strategies_contents,
                policies_contents,
                procedure_contents,
                regulations_contents,
                statues_contents,
            )
        else:
            raise ValueError("Invalid user input")

    except Exception as e:
        print(f"\nCRITICAL FAILURE:{e}")
        logging.error(f"\nCRITICAL FAILURE: {e}")
        # stop this application
        sys.exit(1)

    # ----------------------LOOPING TILL 'q' IS PRESSED---------------------
    # exit application when press 'q'
    while True:
        print('\n Press "q" to exit the application')
        if keyboard.read_event().name == "q":
            break
        else:
            print(f"Invalid key pressed: {keyboard.read_event().name}")
