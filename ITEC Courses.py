import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = (
    'https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid'
    '=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue=OPEN_PLUS_WA'
    'ITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL&credits=&instr'
    'uctor=&keyword=&begindate=&site=&resultNumber=250')

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
course_table = soup.find_all('table', id='resultsTable')
course_table = course_table[0]

workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'ITEC Courses'

worksheet.cell(1, 1, 'ID #')
worksheet.cell(1, 2, 'Course Number - Section Number')
worksheet.cell(1, 3, 'Course Title')
worksheet.cell(1, 4, 'Day Class Meets')
worksheet.cell(1, 5, 'Time Class Meets')
worksheet.cell(1, 6, 'Credits')
worksheet.cell(1, 7, 'Instructor')

data = []
for row in course_table.find_all('tr'):
    for cell in row.find_all('td'):
        data.append(cell.text.strip())


for result in data:
    if result == '':
        data.remove(result)

for index, result in enumerate(data):
    row = index + 2
    worksheet.cell(row, 1, result)


workbook.save('itec_courses.xlsx')
print(data)

# TODO: figure out how to get rid of extra characters and add data to spreadsheet
