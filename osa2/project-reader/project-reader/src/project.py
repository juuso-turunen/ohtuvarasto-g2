class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_list(self, dependencies):
        return "\n" + "\n".join(list(map(lambda x: f"- {x}", dependencies))) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"

            f"\n\nAuthors: {self._stringify_list(self.authors)}"

            f"\n\nDependencies: {self._stringify_list(self.dependencies)}"

            f"\n\nDevelopment dependencies: {self._stringify_list(self.dev_dependencies)}"
        )
