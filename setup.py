import os
import json
from codecs import open
from setuptools import setup, find_packages
from setuptools.command.install import install
from zendesk.indexer import UserIndexer, TicketIndexer, OrganizationIndexer



class PostInstallCommand(install):
    """
    Post-installation for installation mode.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__)) + "/zendesk/data/json/"

    def run(self):
        print("running indexing")
        self.index_data()
        install.run(self)

    def index_user_data(self):
        user_data_path = self.base_dir + "users.json"
        with open(user_data_path) as f:
            user_data = json.load(f)
        user_indexer = UserIndexer()
        user_indexer.index(user_data)

    def index_ticket_data(self):
        ticket_data_path = self.base_dir + "tickets.json"
        with open(ticket_data_path) as f:
            ticket_data = json.load(f)
        ticket_indexer = TicketIndexer()
        ticket_indexer.index(ticket_data)

    def index_organization_data(self):
        organization_data_path = self.base_dir + "organizations.json"
        with open(organization_data_path) as f:
            organization_data = json.load(f)
        organization_indexer = OrganizationIndexer()
        organization_indexer.index(organization_data)

    def index_data(self):
        self.index_user_data()
        self.index_ticket_data()
        self.index_organization_data()


try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

reqs = 'requirements.txt'
requirements = []
for r in parse_requirements(reqs, session='search'):
    requirements.append(str(r.req))

setup(
    name='zendesk',
    version='0.0.1',
    description='CLI application to search Zendesk''s users, tickets and organizations.',
    url='https://github.com/psnvijay/Zendesk',
    author='Vijay Pappu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7'
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    keywords='Search',
    packages=find_packages("."),
    package_data={'zendesk': ['data/json/*',
                              'data/schema/*',
                              'data/index/user/*',
                              'data/index/ticket/*',
                              'data/index/organization/*']},
    include_package_data=True,
    install_requires=requirements
)

