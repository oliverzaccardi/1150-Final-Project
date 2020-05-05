import requests
from bs4 import BeautifulSoup

get_HTML = requests.get(
    'https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid'
    '=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue=OPEN_PLUS_WA'
    'ITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL&credits=&instr'
    'uctor=&keyword=&begindate=&site=&resultNumber=250')

parse_HTML = BeautifulSoup(get_HTML.text, 'html.parser')
data = parse_HTML.find_all('table')
results = data[4]
table_data = results.find_all('td')

records = []
for result in results:
    id_number = table_data[2].contents[0]

    course_number = table_data[4].contents[0]

    section_number = table_data[5].contents[0]

    course = results.select('div>a')[3]
    course_name = course.contents[0]

    day = results.find('abbr')
    course_day = day.contents[0]

    time = table_data[9].text

    course_credits = table_data[10].text

    instructor = table_data[12].text
    records.append((id_number, course_number, section_number, course_name, course_day, time, course_credits,
                    instructor))
print(records)
# TODO
#  extract spreadsheet column titles and data
