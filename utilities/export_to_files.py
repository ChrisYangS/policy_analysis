import pandas as pd
import openpyxl
import logging
import time
import json


def save_policies_to_excel(file_name: str, st_name: str, *lists):
    combined_list = []
    for lst in lists:
        combined_list.extend(lst)

    df = pd.DataFrame(combined_list)

    with pd.ExcelWriter(
        file_name,
        engine="openpyxl",
        mode="a",
        if_sheet_exists="replace",
    ) as writer:
        df.to_excel(
            writer,
            sheet_name=st_name,
            index=False,
            header=True,
            startrow=0,
            startcol=0,
            freeze_panes=(1, 0),
        )

    print(f"\nSUCCESS: {st_name} is saved to {file_name}")
    logging.info(f"\nSUCCESS: {st_name} is saved to {file_name}")


def save_policies_to_json(file_name: str, *lists):

    output_dict = {}
    for lst in lists:
        # Check if the key exists, if not, create an empty list
        if lst[0]["policy type"] not in output_dict:
            output_dict[lst[0]["policy type"]] = []

        # Append to the list
        for item in lst:
            output_dict[lst[0]["policy type"]].append(item)

    with open(file_name, "w") as f:
        # create and save output_dict to json file
        json.dump(output_dict, f)

    print(f"\nSUCCESS: All policies are saved to {file_name}")
    logging.info(f"\nSUCCESS: All policies are saved to {file_name}")


def create_excel_output_file(
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
):
    # -------------save the data to an excel file-------------------------------------
    file_name = (
        f"./output/otago_policies_{time.strftime("%Y%m%d%H%M%S",time.localtime())}.xlsx"
    )
    # crease an empty excel file
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "PolicyHeader"
    wb.save(file_name)

    print(f"\nExcel file {file_name} is created. Now saving data to the file...")
    logging.info(f"\nExcel file {file_name} is created. Now saving data to the file...")

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


def create_json_output_file(
    guideline_contents,
    plan_strategies_contents,
    policies_contents,
    procedure_contents,
    regulations_contents,
    statues_contents,
):
    file_name = (
        f"./output/otago_policies_{time.strftime('%Y%m%d%H%M%S',time.localtime())}.json"
    )
    save_policies_to_json(
        file_name,
        guideline_contents,
        plan_strategies_contents,
        policies_contents,
        procedure_contents,
        regulations_contents,
        statues_contents,
    )
    print(f"\nAll policies are saved to {file_name}")
    logging.info(f"\nAll policies are saved to {file_name}")
    print(
        f'\n A log file is created at ./output/policy_data_load_{time.strftime("%Y%m%d%H%M%S",time.localtime())}.log'
    )
