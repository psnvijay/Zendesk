# Zendesk
A command line interface (CLI) application to search users, tickets and organizations. This application has been built using Python version 3.  

### Setup instructions:
1. Clone the repository:
```bash
git clone git@github.com:psnvijay/Zendesk.git
``` 

2. Make sure `Python 3.7` is being used to run the application. 
    - `brew` can be used to install it if necessary: ```brew cask install anaconda```
    

3. Install the dependencies:
```bash
pip install -r requirements.txt 
```

4. Run the setup script:
```bash
python setup.py
```

5. Run the application:
```bash
python search_menu.py
```

### Usage:
1. The application can be used to search the following fields for users, tickets & organizations.  
```bash
*********************** Welcome to Zendesk Search ***********************


** Select options:  ** 

1. Select 1 to search Zendesk
2. Select 2 to view a list of searchable fields
3. Exit


------------------------------------------------------------------
Enter your choice [1-3]: 2
------------------------------------------------------------------
User fields:
id
url
external_id
name
alias
created_at
active
verified
shared
locale
timezone
last_login_at
email
phone
signature
organization_id
tags
suspended
role 

------------------------------------------------------------------
------------------------------------------------------------------
Ticket fields:
status
assignee_id
via
description
tags
url
external_id
created_at
submitter_id
priority
due_at
organization_id
has_incidents
id
type
subject 

------------------------------------------------------------------
------------------------------------------------------------------
Organization fields:
id
url
external_id
name
domain_names
created_at
details
shared_tickets
tags 

------------------------------------------------------------------

```

2. You can search one field as shown below: 
```bash 

*********************** Welcome to Zendesk Search ***********************


** Select options:  ** 

1. Select 1 to search Zendesk
2. Select 2 to view a list of searchable fields
3. Exit


------------------------------------------------------------------
Enter your choice [1-3]: 1


** Select from the following menu:  ** 

1. Select 1 to search users
2. Select 2 to search tickets
3. Select 3 to search organizations
4. Select 4 to go back to main menu


------------------------------------------------------------------
Enter your choice [1-4]: 1
Choose from the following fields:
id
url
external_id
name
alias
created_at
active
verified
shared
locale
timezone
last_login_at
email
phone
signature
organization_id
tags
suspended
role

Enter search term:id
Enter search value:10
Choose from the following fields:
id
url
external_id
name
alias
created_at
active
verified
shared
locale
timezone
last_login_at
email
phone
signature
organization_id
tags
suspended
role

Enter search term or press enter to search:
Searching users for (id:10)
active                        True
alias                         Mr Webb
created_at                    2016-02-08T04:32:38 -11:00
email                         webbvinson@flotonic.com
external_id                   f744706e-df3d-4d51-ad18-c63e41be5cc0
id                            10
last_login_at                 2014-12-26T04:54:30 -11:00
locale                        en-AU
name                          Kari Vinson
organization_id               105
phone                         8235-883-140
role                          end-user
shared                        True
signature                     Don't Worry Be Happy!
suspended                     False
tags                          ['Moraida', 'Beechmont', 'Jeff', 'Starks']
timezone                      Germany
url                           http://initech.zendesk.com/api/v2/users/10.json
verified                      False
--------------------------------------------------------------------------------

```
3. It can also be used to search multiple fields at the same time:
```bash

*********************** Welcome to Zendesk Search ***********************


** Select options:  ** 

1. Select 1 to search Zendesk
2. Select 2 to view a list of searchable fields
3. Exit


------------------------------------------------------------------
Enter your choice [1-3]: 1


** Select from the following menu:  ** 

1. Select 1 to search users
2. Select 2 to search tickets
3. Select 3 to search organizations
4. Select 4 to go back to main menu


------------------------------------------------------------------
Enter your choice [1-4]: 3
Choose from the following fields:
id
url
external_id
name
domain_names
created_at
details
shared_tickets
tags

Enter search term:shared_tickets 
Enter search value:True
Choose from the following fields:
id
url
external_id
name
domain_names
created_at
details
shared_tickets
tags

Enter search term or press enter to search:details 
Enter search value:Non profit
Choose from the following fields:
id
url
external_id
name
domain_names
created_at
details
shared_tickets
tags

Enter search term or press enter to search:
Searching organizations for (shared_tickets:True AND details:Non profit)
created_at                    2016-03-15T03:08:47 -11:00
details                       Non profit
domain_names                  ['translink.com', 'netropic.com', 'earthplex.com', 'zilencio.com']
external_id                   197f93c0-1729-4c82-9bb0-143e978f06ce
id                            110
name                          Kindaloo
shared_tickets                True
tags                          ['Chen', 'Melton', 'Stafford', 'Landry']
url                           http://initech.zendesk.com/api/v2/organizations/110.json
--------------------------------------------------------------------------------
created_at                    2016-04-10T11:12:35 -10:00
details                       Non profit
domain_names                  ['comstar.com', 'zytrex.com', 'austech.com', 'enervate.com']
external_id                   33c4e38d-bfa3-4b12-9bb6-6f547524cf33
id                            122
name                          Geekfarm
shared_tickets                True
tags                          ['Hensley', 'Garza', 'Roberts', 'Vega']
url                           http://initech.zendesk.com/api/v2/organizations/122.json
--------------------------------------------------------------------------------
created_at                    2016-05-11T12:16:15 -10:00
details                       Non profit
domain_names                  ['unisure.com', 'boink.com', 'quinex.com', 'poochies.com']
external_id                   15c21605-cbc6-440f-8da2-6e1601aed5fa
id                            124
name                          Bitrex
shared_tickets                True
tags                          ['Lott', 'Hunter', 'Beasley', 'Glass']
url                           http://initech.zendesk.com/api/v2/organizations/124.json
--------------------------------------------------------------------------------

```




