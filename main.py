import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.recycleview import RecycleView


class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        url_wiki = "https://fr.wikipedia.org/wiki/Les_1001_albums_qu%27il_faut_avoir_%C3%A9cout%C3%A9s_dans_sa_vie"
        page = requests.get(url_wiki)
        soup = BeautifulSoup(page.content, 'html.parser')

        titres_annees = soup.find_all("span", class_="mw-headline")

        for index, titre in enumerate(titres_annees[2:10]):
            list_wthout_sort = []

            # sélectionne tous les tableaux par décénnie précédés par une balise h3
            tab_by_decade = soup.select("h3 + table")[index]
            # sélectionne chaque ligne dans chaque tableau
            cases_td = tab_by_decade.select("td")

            for case in cases_td:
                # si la case ne contient pas de lien (None) alors affiche le contenu (n° de la ligne + année)
                if case.a is None:
                    case = case.string.strip()
                # sinon affiche le titre du lien
                else:
                    case = case.a.get("title")

                # tableau contenant toutes les cases
                list_wthout_sort.append(case)

            # fonction permettant de créer des sous-listes de 4 éléments (n° de la ligne, auteur, titre, année)
            lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
            list_decade = lol(list_wthout_sort, 4)

            # affichage du titre (nom de la décénnie + tous les albums de la décennie)
            print(titre.string.upper())
            for line in list_decade:
                print(line)


class MusinderApp(App):
    def build(self):
        return RV()


MusinderApp().run()

