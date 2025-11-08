from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_dict = tomli.loads(content)

        prettier = toml_dict["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(prettier["name"], prettier["description"], prettier["dependencies"], prettier["group"]["dev"]["dependencies"], prettier["authors"], prettier["license"])
