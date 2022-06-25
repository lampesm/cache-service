from typing import Union, Dict

import wikipediaapi


class Wikipedia:
    def __init__(self, query) -> None:
        wiki_wiki = wikipediaapi.Wikipedia("en")
        self.page_py = wiki_wiki.page(query)

    @property
    def get_information(self) -> Union[Dict, bool]:
        try:
            if self.page_py.exists():
                return {"title": self.page_py.title, "summary": self.page_py.summary[0:60]}
            else:
                return False
        except Exception as e:
            print(f"error: {e}")
            return False
