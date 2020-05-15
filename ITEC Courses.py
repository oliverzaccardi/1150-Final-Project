"""1150 final project. This program uses the beautiful soup library to parse through the MCTC ITEC course
search results page and add course information to aN excel spreadsheet"""
# imports requests library
import requests
# imports beautiful soup library
from bs4 import BeautifulSoup
# opens excel library
from openpyxl import Workbook

# search results page url
url = (
    'https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid'
    '=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue=OPEN_PLUS_WA'
    'ITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL&credits=&instr'
    'uctor=&keyword=&begindate=&site=&resultNumber=250')

# gets response form url
response = requests.get(url)
# uses html.parser to parse html of web page
soup = BeautifulSoup(response.content, 'html.parser')
# finds all "table" tags and assigns them to course_table variable
course_table = soup.find_all('table', id='resultsTable')
# first item in course_table
course_table = course_table[0]

# opens workbook
workbook = Workbook()
# first worksheet in workbook
worksheet = workbook.active
# titles worksheet
worksheet.title = 'ITEC Courses'

# adds header to first row
worksheet.cell(1, 1, 'ID #')
worksheet.cell(1, 2, 'Course Number')
worksheet.cell(1, 3, 'Section Number')
worksheet.cell(1, 4, 'Course Title')
worksheet.cell(1, 5, 'Day Class Meets')
worksheet.cell(1, 6, 'Time Class Meets')
worksheet.cell(1, 7, 'Credits')
worksheet.cell(1, 8, 'Instructor')
# sets spreadsheet rows = 2 to skip header row
ss_row = 2
# searches course_table for tr tags
for row in course_table.find_all('tr'):
    # empty list to loop over rows in table and add data to list
    data = []
    # adds data to list
    for cell in row.find_all('td'):
        data.append(cell.text.strip())
    # removes empty strings from list
    for result in data:
        if result == '':
            data.remove(result)
    # adds data from list to spreadsheet
    if len(data):
        worksheet.cell(ss_row, 1, data[0])
        worksheet.cell(ss_row, 2, data[2])
        worksheet.cell(ss_row, 3, data[3])
        worksheet.cell(ss_row, 4, data[4])
        worksheet.cell(ss_row, 5, data[6])
        worksheet.cell(ss_row, 6, data[7])
        worksheet.cell(ss_row, 7, data[8])
        worksheet.cell(ss_row, 8, data[10])
        ss_row += 1
# saves workbook
workbook.save('itec_courses.xlsx')

"""Thanks again for the help and a great semester! """
