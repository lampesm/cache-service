import wikipediaapi


class Wikipedia:
    def __init__(self, query) -> None:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        self.page_py = wiki_wiki.page(query)

    @property
    def get_information(self):
        if self.page_py.exists():
            return {
                "title": self.page_py.title,
                "summary": self.page_py.summary[0:60]
            }
        else:
            return False
