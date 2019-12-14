import lxml.html
import requests


def get_request(url, num):
    return requests.get("{}?page={}".format(url, num))


def get_companies(doc, pattern):
    companies = doc.xpath('//*[@class="startupCard__details__name"]/text()')
    return companies


def set_companies(ret_companies, companies):
    return [ ret_companies.append(company.rstrip('\n')) for company in companies ]


def get_all_companies():
    ret_companies = []

    for num in range(1, 20):
        page = get_request("https://betalist.com/regions/australia", num)
        doc = lxml.html.fromstring(page.content)

        # Get list of companies from the web
        companies = get_companies(doc, '//*[@class="startupCard__details__name"]/text()')

        # set the companies in the list to get appended
        set_companies(ret_companies, companies)

    return ret_companies


print(get_all_companies())
