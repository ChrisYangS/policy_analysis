import pandas as pd
import openpyxl
import logging


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
