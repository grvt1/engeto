This is a program created as part of the engeto.cz python academy.

Program is designed to extract data for 2017 czech elections for selected region
 and to export them into a .csv file.
 It is controlled via the main function election_scrapper which takes 2 arguments;
    1) link for selected region (e.g. https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103)
    2) file name where user wants the data to be extracted.
        - By default it will extract region name from the entered link and pastes it into the file name
    - program will let user know if one of the above is not correct format and quits the program

There are 3 folders for different modules:
    1) export - modules for exporting data to .csv
    2) results - here are the .csv and .json files located by default
    3) scrapping - all the modules that are needed for a successful scrapping

You can find all needed packages in the requirements.txt file.