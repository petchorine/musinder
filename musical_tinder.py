import requests
from bs4 import BeautifulSoup

url_first_page = "https://www.listchallenges.com/1001-albums-you-must-hear-before-you-die-2016"
url_wiki = "https://fr.wikipedia.org/wiki/Les_1001_albums_qu%27il_faut_avoir_%C3%A9cout%C3%A9s_dans_sa_vie"

page = requests.get(url_wiki)
soup = BeautifulSoup(page.content, 'html.parser')

################################################################################
titres_annees = soup.find_all("span", class_="mw-headline")

for titre in titres_annees[2:10]:
    print((titre.string).upper())


################################################################################
# cases = soup.select("h3 + table td")
#
# list_wthout_sort = []
# list_1001 = []
#
# for case in cases:
#     if case.a == None:
#         # strip() supprime les retours à la ligne de fin et de début de chaîne.
#         # supprime également les espaces blancs des deux côtés de la chaîne.
#         case = case.string.strip()
#     else:
#         case = case.a.get("title")
#
#     list_wthout_sort.append(case)
#
#
# lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
#
# list_1001 = lol(list_wthout_sort, 4)


# for line in list_1001:
#     print(line)

################################################################################
list_wthout_sort = []
list_annees_50 = []

tab_by_decade = soup.select("h3 + table")[0]
cases_td = tab_by_decade.select("td")


for case in cases_td:
    if case.a == None:
        case = case.string.strip()
    else:
        case = case.a.get("title")

    list_wthout_sort.append(case)

lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
list_annees_50 = lol(list_wthout_sort, 4)


# print((titres_annees[2].string).upper())

for line in list_annees_50:
   print(line)