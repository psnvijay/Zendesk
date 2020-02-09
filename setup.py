import json
import os
from indexer import UserIndexer, TicketIndexer, OrganizationIndexer


def index_user_data():
    base_dir = os.getcwd() + "/data/json/"
    user_data_path = base_dir + "users.json"

    with open(user_data_path) as f:
        user_data = json.load(f)

    user_indexer = UserIndexer()
    user_indexer.index(user_data)


def index_ticket_data():
    base_dir = os.getcwd() + "/data/json/"
    ticket_data_path = base_dir + "tickets.json"

    with open(ticket_data_path) as f:
        ticket_data = json.load(f)

    ticket_indexer = TicketIndexer()
    ticket_indexer.index(ticket_data)


def index_organization_data():
    base_dir = os.getcwd() + "/data/json/"
    organization_data_path = base_dir + "organizations.json"

    with open(organization_data_path) as f:
        organization_data = json.load(f)

    organization_indexer = OrganizationIndexer()
    organization_indexer.index(organization_data)


def setup():
    index_user_data()
    index_ticket_data()
    index_organization_data()
    


if __name__ == "__main__":
    setup()
