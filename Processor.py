import json
import narrator

from rich.table import Table
from rich.console import Console
from inventory import FixtureSpec

# Do not alter -----------------------------------------------
class Processor(FixtureSpec):

    def __init__(self):
        super().__init__()
        self.filename = "records/data.json"
        self.data = self.__load()

    def __load(self) -> dict:
        fh = open(self.filename, "r")
        return json.load(fh)
    
    def write(self) -> None:
        with open(self.filename, "w") as fh:
            json.dump(self.data, fh, indent=4)

    def display_menu(self) -> any:
        n = narrator.Narrator()
        q = narrator.Question({
            "question": "\nOperation to perform:\n",
            "responses": [
                {"choice": "1 row retrieval ", "outcome": 1},
                {"choice": "2 add to a row ", "outcome": 2},
                {"choice": "3 add a column ", "outcome": 3},
                {"choice": "4 remove from row ", "outcome": 4},
                {"choice": "5 save file ", "outcome": 5},
                {"choice": "6 print table ", "outcome": 6},
                {"choice": "7 quit", "outcome": False}
            ]
        })
        return q.ask()
    
    def display_table(self) -> None:
        cols = list(self.data[0].keys())
        table = Table(title="term-world CITIZEN DATA")
        for col in cols:
            table.add_column(col)
        for row in self.data:
            entry = [str(item) for item in list(row.values())]
            table.add_row(*entry)
        console = Console()
        console.print(table)
# Do not alter -----------------------------------------------


def main():

    # Do not alter -------------------------------------------
    obj = Processor()
    data = obj.data
    response = obj.display_menu()
    # Do not alter -------------------------------------------

if __name__ == "__main__":
    main()