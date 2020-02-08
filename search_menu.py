from bcolors import bcolors
from user import User
from organization import Organization
from ticket import Ticket
from whoosh.query import Term


class SearchZendesk:

    def __init__(self):
        self.main_choices = {
            1: "Select 1 to search Zendesk",
            2: "Select 2 to view a list of searchable fields",
            3: "Exit"
        }

        self.sub_choices = {
            1: "Select 1 to search users",
            2: "Select 2 to search tickets",
            3: "Select 3 to search organizations",
            4: "Select 4 to go back to main menu"
        }

        self.user = User()
        self.ticket = Ticket()
        self.organization = Organization()

    def print_main_menu(self):
        print(2 * "*", f"{bcolors.BOLD}Select options: {bcolors.ENDC}", 2 * "*", "\n")
        for (k, v) in self.main_choices.items():
            print(str(k) + ". " + v)
        print("\n")
        print(66 * "-")

    def print_sub_menu(self):
        print("\n")
        print(2 * "*", f"{bcolors.BOLD}Select from the following menu: {bcolors.ENDC}", 2 * "*", "\n")
        for (k, v) in self.sub_choices.items():
            print(str(k) + ". " + v)
        print("\n")
        print(66 * "-")

    @staticmethod
    def print_results(results):
        for res in results:
            print("\n".join([(key + (30 - len(key)) * " " + str(value)) for (key, value) in res.items()]))
            print(80 * "-")

    def get_menu_response(self):
        print("\n")
        print(23 * "*", f"{bcolors.BOLD}Welcome to Zendesk Search{bcolors.ENDC}", 23 * "*")
        print("\n")

        main_loop = True
        sub_loop = True

        while main_loop:
            self.print_main_menu()
            try:
                choice = int(input("Enter your choice [" + str(min(self.main_choices.keys())) + "-" + str(max(self.main_choices.keys())) + "]: "))
                if choice == 1:
                    while sub_loop:
                        self.print_sub_menu()
                        try:
                            sub_choice = int(input("Enter your choice [" + str(min(self.sub_choices.keys())) + "-" + str(max(self.sub_choices.keys())) + "]: "))
                            if sub_choice == 1:
                                query = self.get_query(self.user.fields)
                                results = self.search_users(query)
                                self.print_results(results)
                            elif sub_choice == 2:
                                query = self.get_query(self.ticket.fields)
                                results = self.search_tickets(query)
                                self.print_results(results)
                            elif sub_choice == 3:
                                query = self.get_query(self.organization.fields)
                                results = self.search_organizations(query)
                                self.print_results(results)
                            elif sub_choice == 4:
                                sub_loop = False
                            else:
                                input("Wrong option selection. Enter any key to try again..")
                        except ValueError:
                            input("Wrong option selection. Enter any key to try again..")
                elif choice == 2:
                    self.user.print_fields()
                    self.ticket.print_fields()
                    self.organization.print_fields()
                elif choice == 3:
                    main_loop = False
                else:
                    input("Wrong option selection. Enter any key to try again..")
                print("\n")
            except ValueError:
                input("Wrong option selection. Enter any key to try again..")

    def search_users(self, query):
        return self.user.search(query)

    def search_tickets(self, query):
        return self.ticket.search(query)

    def search_organizations(self, query):
        return self.organization.search(query)

    @staticmethod
    def get_query(fields):
        field = input("Enter search term:")
        while field not in fields:
            print("Search term not found. Choose a search term from the following fields:\n" + "\n".join(fields) + "\n")
            field = input("Enter search term:")
        value = input("Enter search value:")
        return Term(field, value)


if __name__ == "__main__":

    SearchZendesk().get_menu_response()

