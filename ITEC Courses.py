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
worksheet.cell(1, 2, 'Course Number')
worksheet.cell(1, 3, 'Section Number')
worksheet.cell(1, 4, 'Course Title')
worksheet.cell(1, 5, 'Day Class Meets')
worksheet.cell(1, 6, 'Time Class Meets')
worksheet.cell(1, 7, 'Credits')
worksheet.cell(1, 8, 'Instructor')

for row in course_table.find_all('tr'):
    data = []
    for cell in row.find_all('td'):
        data.append(cell.text.strip())
    for result in data:
        if result == '':
            data.remove(result)
    print(data)

workbook.save('itec_courses.xlsx')
