from bs4 import BeautifulSoup
import requests


def play():
    url = "https://www.otago.ac.nz/administration/policies/policy-collection/procedures-for-advising-students-of-teaching-and-final-examination-arrangements-during-adverse-weather-conditions"
    # scrap the website url above
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    h2_location = soup.find(
        "h2", string=lambda text: "Organisational scope" in text if text else False
    )
    dict = {}
    if h2_location:
        # dict["name"] = policy["name"]
        # dict["url"] = policy["url"]
        try:
            # get all p tags between the h2_location and the next h2 tag
            paragraphs = []
            for sibling in h2_location.find_next_siblings():
                if sibling.name == "h2":
                    break
                paragraphs.append(sibling.getText())
            dict["policies_scope"] = "\n".join(paragraphs)
        except:
            dict["policies_scope"] = policy_content.getText()
    else:
        dict["policies_scope"] = "Organisational scope not found"
        print(
            f"\nWARNING: Organisational scope not found for {policy['name']}! URL is {policy['url']}\n"
        )
        logging.info(
            f"\nWARNING: Organisational scope not found for {policy['name']}! URL is {policy['url']}\n"
        )
    return dict


if __name__ == "__main__":
    print(play())
