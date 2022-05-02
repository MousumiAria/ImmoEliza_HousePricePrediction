# Immo_Eliza_scraping

Immo_Eliza_scraping is a project intended to gather as much readable data as possible for the pseudo realestate company called ImmoEliza. With this project, we were tasked to gather field attributes from as many (~10000) houses in Belgium. Field attributes include information like locality, type of property, price, area, no. of rooms, no. of bathrooms etc.

The python file included here is written to scrap a website for such information/field attributes, convert them into a json object for each individual house and append it to a .CSV file.
Once we have a .CSV file the data is cleaned and converted to a readable dataset.

This data is exclusive to houses within Belgium, but can be changed given you have a source from which a list of links can be created for your needs.

## Installation

In order to run this program, make sure you have the python packages: Pandas, selenium and BeautifulSoup, json installed. If you do not wish to run this programme and simply want it to understand how the data was arrived at then these packages will not be necessary.


## Usage

This program is used to scrap for data regarding an online accessible server; primarily regarding housing but could be altered to work for similar purposes.
Once the Data is scrapped, a dataset is created in the form of a readable .CSV file.


## Contributors
This project was performed by Mohammed Bouazzaoui, Anzeem Arief and Mousumi Sen. You are welcome to append and make changes to the source code with intentions of making it more efficient or so for it to suit your needs. Please do create a branch and request for approvals before you make changes!
