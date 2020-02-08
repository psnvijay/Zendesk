from bcolors import Colors
from user import User
from organization import Organization
from ticket import Ticket
from whoosh.query import Term


class SearchZendesk:
    """
    Class to search users, tickets and organizations
    """
    def __init__(self):
        """
        Constructor for SearchZendesk class
        """
        self.main_choices = {
            1: "Select 1 to search Zendesk",
            2: "Select 2 to view a list of searchable fields",
            3: "Exit"
        }  # main menu choices

        self.sub_choices = {
            1: "Select 1 to search users",
            2: "Select 2 to search tickets",
            3: "Select 3 to search organizations",
            4: "Select 4 to go back to main menu"
        }  # search menu choices

        self.user = User()  # instantiates user class
        self.ticket = Ticket()  # instantiates ticket class
        self.organization = Organization()  # instantiates organization class

    def print_main_menu(self):
        """
        prints main menu
        """
        print(2 * "*", f"{Colors.BOLD}Select options: {Colors.ENDC}", 2 * "*", "\n")
        for (k, v) in self.main_choices.items():
            print(str(k) + ". " + v)
        print("\n")
        print(66 * "-")

    def print_sub_menu(self):
        """
        prints search menu
        """
        print("\n")
        print(2 * "*", f"{Colors.BOLD}Select from the following menu: {Colors.ENDC}", 2 * "*", "\n")
        for (k, v) in self.sub_choices.items():
            print(str(k) + ". " + v)
        print("\n")
        print(66 * "-")

    @staticmethod
    def print_results(results):
        """
        prints search results
        :param results: list of search results
        """
        for res in results:
            print("\n".join([(key + (30 - len(key)) * " " + str(value)) for (key, value) in res.items()]))
            print(80 * "-")

    def get_menu_response(self):
        """
        main method to input search queries and retrieve results
        :return: search results
        """
        print("\n")
        print(23 * "*", f"{Colors.BOLD}{Colors.BLUE}Welcome to Zendesk Search{Colors.ENDC}", 23 * "*")
        print("\n")

        main_loop = True
        sub_loop = True

        while main_loop:  # outer loop to receive main menu options
            self.print_main_menu()  # print main menu
            try:
                choice = int(input("Enter your choice [" + str(min(self.main_choices.keys())) + "-" + str(max(self.main_choices.keys())) + "]: "))
                if choice == 1:
                    while sub_loop:
                        self.print_sub_menu()  # print sub menu
                        try:
                            sub_choice = int(input("Enter your choice [" + str(min(self.sub_choices.keys())) + "-" + str(max(self.sub_choices.keys())) + "]: "))
                            if sub_choice == 1:  # search users
                                query = self.get_query(self.user.fields)
                                results = self.search_users(query)
                                self.print_results(results)
                            elif sub_choice == 2:  # search tickets
                                query = self.get_query(self.ticket.fields)
                                results = self.search_tickets(query)
                                self.print_results(results)
                            elif sub_choice == 3:  # search organization
                                query = self.get_query(self.organization.fields)
                                results = self.search_organizations(query)
                                self.print_results(results)
                            elif sub_choice == 4:  # terminate sub loop
                                sub_loop = False
                            else:
                                input("Wrong option selection. Enter any key to try again..")
                        except ValueError:
                            input("Wrong option selection. Enter any key to try again..")
                elif choice == 2:
                    self.user.print_fields()  # prints user fields
                    self.ticket.print_fields()  # prints ticket fields
                    self.organization.print_fields()  # prints organization fields
                elif choice == 3:
                    main_loop = False  # terminate main loop
                else:
                    input("Wrong option selection. Enter any key to try again..")
                print("\n")
            except ValueError:
                input("Wrong option selection. Enter any key to try again..")

    def search_users(self, query):
        """
        searches users for the given query
        :param query: Term query
        :return: search results
        """
        return self.user.search(query)

    def search_tickets(self, query):
        """
        searches tickets for the given query
        :param query: Term query
        :return: search results
        """
        return self.ticket.search(query)

    def search_organizations(self, query):
        """
        searches organizations for the given query
        :param query: Term query
        :return: search results
        """
        return self.organization.search(query)

    @staticmethod
    def get_query(fields):
        """
        Returns a term query from user input
        :param fields: list of searchable fields
        :return: Term query
        """
        field = input("Enter search term:")
        while field not in fields:
            print("Search term not found. Choose a search term from the following fields:\n" + "\n".join(fields) + "\n")
            field = input("Enter search term:")
        value = input("Enter search value:")
        return Term(field, value)


if __name__ == "__main__":
    SearchZendesk().get_menu_response()

