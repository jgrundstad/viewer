__author__ = 'Jason Grundstad'
from django.conf import settings
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
import json



MD_ANDERSON_URL = 'https://pct.mdanderson.org/#/home'
MD_ANDERSON_OUTFILE = settings.LINKS_OUT + 'mdanderson.json'


def scrape_mdanderson():
    """
    Scrape the rendered mdanderson page for gene names, create a .json
     of links
    :rtype : dict
    """
    gene_list = dict()
    d = Display(visible=0, size=(800,600)) # requires xvfb for headless mode
    d.start()
    driver = webdriver.Firefox()
    driver.get(MD_ANDERSON_URL)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for a_tag in soup.find_all("a", {'class':'ng-binding'}):
        gene_list[a_tag.text] = "{}/{}?section=Overview".format(
            MD_ANDERSON_URL,
            a_tag.text)
    gene_list_json = json.dumps(gene_list)
    with open(MD_ANDERSON_OUTFILE, 'w') as f:
        json.dump(gene_list_json, f)

    driver.quit()
    d.stop()


def main():
    scrape_mdanderson()


if __name__ == '__main__':
    main()
