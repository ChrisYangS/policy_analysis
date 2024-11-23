# application entry point
import sys

sys.path.insert(0, "./utilities/")
import keyboard
import logging
import time
import openpyxl
import os
from utilities.policies_extract import get_policies, get_policy_details

from utilities.export_to_excel import save_policies_to_excel

if __name__ == "__main__":
    # Configure logging to save to a file
    logging.basicConfig(
        filename=f"./output/policy_data_load_{time.strftime("%Y%m%d%H%M%S",time.localtime())}.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )
    try:
        # -------------read the ALL_POLICE_URL and get the urls of all the policies-----------
        guidelines_list = get_policies(policy_type="Guidelines")
        plan_strategies_list = get_policies(policy_type="Plans & Strategies")
        policies_list = get_policies(policy_type="Policies")
        procedure_list = get_policies(policy_type="Procedures")
        regulations_list = get_policies(policy_type="Regulations")
        statues_list = get_policies(policy_type="Statutes")

        guideline_contents = get_policy_details(guidelines_list)
        plan_strategies_contents = get_policy_details(plan_strategies_list)
        policies_contents = get_policy_details(policies_list)
        procedure_contents = get_policy_details(procedure_list)
        regulations_contents = get_policy_details(regulations_list)
        statues_contents = get_policy_details(statues_list)

        # -------------save the data to an excel file-------------------------------------
        file_name = f"./output/otago_policies_{time.strftime("%Y%m%d%H%M%S",time.localtime())}.xlsx"
        # crease an empty excel file
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "PolicyHeader"
        wb.save(file_name)

        print(f"\nExcel file {file_name} is created. Now saving data to the file...")
        logging.info(
            f"\nExcel file {file_name} is created. Now saving data to the file..."
        )

        save_policies_to_excel(
            file_name,
            "PolicyHeader",
            guidelines_list,
            plan_strategies_list,
            policies_list,
            procedure_list,
            regulations_list,
            statues_list,
        )
        print(f"\nPolicyHeader is saved to excel file {file_name}.")
        logging.info(f"\nPolicyHeader is saved to excel file {file_name}.")

        save_policies_to_excel(
            file_name,
            "PolicyDetails",
            guideline_contents,
            plan_strategies_contents,
            policies_contents,
            procedure_contents,
            regulations_contents,
            statues_contents,
        )
        print(f"\nPolicyDetails is saved to excel file {file_name}.")
        logging.info(f"\nPolicyDetails is saved to excel file {file_name}.")
        print("\n All policy data is extracted and saved to excel file.")
        print(
            f'\n A log file is created at ./output/policy_data_load_{time.strftime("%Y%m%d%H%M%S",time.localtime())}.log'
        )
    except Exception as e:
        # try to remove the output file if it is created
        try:
            os.remove(file_name)
        except:
            pass
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
