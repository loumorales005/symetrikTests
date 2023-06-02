import pytest
import requests
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestLinks:
    def test_validate_broken_links(self, setup):
        a = 1
        broken_links = []
        link_list = setup.find_elements(By.TAG_NAME, "a")
        print(f"Yes?: {link_list[0].text}")
        print(f"\n{len(link_list)} " + "total links found")
        for link in link_list:
            # Getting URL from each element
            href = link.get_attribute('href')
            # Getting and validating http response -> 200 = OK
            response = requests.head(href)
            if response.status_code != 200:
                print(f"Broken URL {a}: {href} --- Code: {response.status_code}")
                # We add all broken links to a list
                broken_links.append(link)
            a = a + 1
            # Test will fail if there's links in the list
        assert len(broken_links) == 0, f"There are {len(broken_links)} broken links"
