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
row = 2
for row in course_table.find_all('tr'):
    data = []
    for cell in row.find_all('td'):
        data.append(cell.text.strip())
    for result in data:
        if result == '':
            data.remove(result)
    worksheet.cell(row, 1, data[0])
    worksheet.cell(row, 2, data[2])
    worksheet.cell(row, 3, data[3])
    worksheet.cell(row, 4, data[4])
    worksheet.cell(row, 5, data[6])
    worksheet.cell(row, 6, data[7])
    worksheet.cell(row, 7, data[8])
    worksheet.cell(row, 8, data[10])
    row += 1
workbook.save('itec_courses.xlsx')
