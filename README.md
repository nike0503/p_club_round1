This repository contains 2 python files, scraping.py and csv_json.py.

The scraping.py takes a url of form https://summerofcode.withgoogle.com/archive/{year}/projects/, where year can be any valid year(of which archives exist), and scrapes this page extracting name, organization and project which are then printed to a csv file names GSOC_archive_{year}.num in the format name, organization, project(without any headings or column names).
To run this program, it requires at most one additional command line argument, the url. If no url is given, then the default year  2019 is used, otherwise the year in the url is used(if that link exists), otherwise a msg is displayed telling that is url is not correct.
Also, it is required that the url is stricly similar to https://summerofcode.withgoogle.com/archive/{year}/projects/, or the program will not run and ask the user to enter url in the specified format.
If more than 1 arguments are given, then also the user is informed of this mistake.

The csv_json.py file needs a csv and a json file(in this given order only) as command line arguments, and it then displays the non_official names in the csv file, and the details of the common official names in the csv and json files.If the user provides incorrect number of arguments, he is informed. 
