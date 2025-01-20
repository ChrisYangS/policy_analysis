import logging
import json
import time

# -------------------------------LOAD CONFIGURATION FILE------------------------------
# Load the configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)
# Access the ALL_POLICE_URL from the configuration
ALL_POLICE_URL = config["ALL_POLICE_URL"]

# Configure logging to save to a file
# logging.basicConfig(
#     filename=f"./output/policy_data_load_{time.strftime("%Y%m%d%H%M%S",time.localtime())}.log",
#     level=logging.INFO,
# )
import sys

sys.path.insert(0, "./utilities/")
from console_prompt import print_message_and_progressing_bar


import requests
from bs4 import BeautifulSoup


# read the ALL_POLICE_URL and get the urls of all the policies
def get_policies(policy_type: str) -> dict:
    # get the page
    page = requests.get(ALL_POLICE_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # create a dictatory to store the names of the policies and urls
    found_policies = []
    # locate all elements under ul class="basic-search__list"
    ul = soup.find("ul", class_="basic-search__list")
    # under ul , locate h3 header starts of "Code of Practice" and then find all links at another h3 level just after it

    processed_policies = 0
    for h3 in ul.find_all("h3"):
        if h3.text.startswith(policy_type):
            policies_list = h3.find_next("ul").find_all("a")
            num_policies = len(policies_list)
            for a in policies_list:
                policies_dict = {}
                policies_dict["policy type"] = policy_type
                policies_dict["name"] = a.text
                policies_dict["url"] = a["href"]
                found_policies.append(policies_dict)
                processed_policies += 1
                print_message_and_progressing_bar(
                    f"Reading {a.text} data from website...",
                    processed_policies / num_policies * 100,
                )

    return found_policies


def get_policy_scope(soup: BeautifulSoup, policy: dict) -> dict:
    h2_location = soup.find(
        "h2", string=lambda text: "Organisational scope" in text if text else False
    )
    dict = {}
    if h2_location:
        policy_content = h2_location.find_next("p")
        dict["name"] = policy["name"]
        dict["url"] = policy["url"]
        if policy_content:
            dict["policies_scope"] = policy_content.get_text()
        else:
            dict["policies_scope"] = "Organisational Scope not found"
    else:
        dict["policies_scope"] = "Organisational scope not found"
        print(
            f"\nWARNING: Organisational scope not found for {policy['name']}! URL is {policy['url']}\n"
        )
        logging.info(
            f"\nWARNING: Organisational scope not found for {policy['name']}! URL is {policy['url']}\n"
        )
    return dict


def get_policy_purpose(soup: BeautifulSoup, policy: dict) -> dict:
    h2_location = soup.find(
        "h2", string=lambda text: "Purpose" in text if text else False
    )
    dict = {}
    if h2_location:
        policy_content = h2_location.find_next("p")
        dict["name"] = policy["name"]
        dict["url"] = policy["url"]
        if policy_content:
            try:
                dict["policies_purpose"] = (
                    f"{policy_content.get_text()} \n{policy_content.find_next('ol').get_text()}"
                )
            except:
                dict["policies_purpose"] = policy_content.get_text()
        else:
            dict["policies_purpose"] = "Policy Purpose not found"
    else:
        dict["policies_purpose"] = "Policy Purpose not found"
        print(
            f"\nWARNING: Policy Purpose not found for {policy['name']}! URL is {policy['url']}\n"
        )
        logging.info(
            f"\nWARNING: Policy Purpose not found for {policy['name']}! URL is {policy['url']}\n"
        )
    return dict


def get_policy_contents(soup: BeautifulSoup, policy: dict) -> dict:
    h2_location = soup.find(
        "h2", string=lambda text: "Content" in text if text else False
    )
    dict = {}
    if h2_location:
        policy_content = h2_location.find_next("ol", class_="list-with-headings")
        dict["name"] = policy["name"]
        dict["url"] = policy["url"]
        contents = []
        for sibling in h2_location.find_next_siblings():
            if sibling.name == "h2":
                break
            contents.append(sibling.get_text())
        dict["policies_contents"] = "\n".join(contents)
    else:
        dict["policies_contents"] = "Policy Contents not found"
        print(
            f"\nWARNING: Policy Contents not found for {policy['name']}! URL is {policy['url']}\n"
        )
        logging.info(
            f"\nWARNING: Policy Contents not found for {policy['name']}! URL is {policy['url']}\n"
        )
    return dict


def get_policy_details(policies_list: list) -> list:
    processed = 0
    total_process = len(policies_list)
    # empty list to store the scope of the policie_scope
    policy_contents = []
    for policy in policies_list:
        # page = requests.get(policy["url"])
        try:
            # open the policy local html file
            with open(policy["url"], "r") as file:
                page = file.read()
                soup = BeautifulSoup(page, "html.parser")
        except:
            print(f"\nERROR: {policy['name']} file not found! URL is {policy['url']}\n")
            logging.error(
                f"\nERROR: {policy['name']} file not found! URL is {policy['url']}\n"
            )
            continue

        purpose = get_policy_purpose(soup, policy)["policies_purpose"]
        scope = get_policy_scope(soup, policy)["policies_scope"]
        content = get_policy_contents(soup, policy)["policies_contents"]
        policy_detail_dict = {}
        policy_detail_dict["policy type"] = policy["policy type"]
        policy_detail_dict["name"] = policy["name"]
        policy_detail_dict["url"] = policy["url"]
        policy_detail_dict["scope"] = scope
        policy_detail_dict["purpose"] = purpose
        policy_detail_dict["content"] = content
        policy_contents.append(policy_detail_dict)
        processed += 1
        print_message_and_progressing_bar(
            f"Reading {policy['name']} contents from website...",
            processed / total_process * 100,
        )
    return policy_contents


# guidelines_list = get_policies(policy_type="Guidelines")
# plan_strategies_list = get_policies(policy_type="Plans & Strategies")
# policies_list = get_policies(policy_type="Policies")
# procedure_list = get_policies(policy_type="Procedures")
# regulations_list = get_policies(policy_type="Regulations")
# statues_list = get_policies(policy_type="Statutes")

# guideline_contents = get_policy_details(guidelines_list)
# plan_strategies_contents = get_policy_details(plan_strategies_list)
# policies_contents = get_policy_details(policies_list)
# procedure_contents = get_policy_details(procedure_list)
# regulations_contents = get_policy_details(regulations_list)
# statues_contents = get_policy_details(statues_list)

# TODO: save in an file processor file
# import pandas as pd
# import openpyxl


# def save_policies_to_excel(file_name: str, st_name: str, *lists):
#     combined_list = []
#     for lst in lists:
#         combined_list.extend(lst)

#     df = pd.DataFrame(combined_list)

#     with pd.ExcelWriter(
#         file_name,
#         engine="openpyxl",
#         mode="a",
#     ) as writer:
#         df.to_excel(
#             writer,
#             sheet_name=st_name,
#             index=False,
#             header=True,
#             startrow=0,
#             startcol=0,
#             freeze_panes=(1, 0),
#         )

#     print(f"\nSUCCESS: {st_name} is saved to {file_name}")
#     logging.info(f"\nSUCCESS: {st_name} is saved to {file_name}")


# ----------------------------------ON MAIN ------------------------
