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
# class_name_and_IDnum = results.find_all('div', attrs={'class': 'meta'})
# print(class_name_and_num)
# day = results.find_all('abbr')
# print(day)
# time_and_room_num = results.find_all('div', attrs={'style': 'white-space: nowrap;overflow: hidden;'})
# print(time_and_room_num)
table_data = results.find_all('td')
print(table_data)
# TODO
#  extract spreadsheet column titles and data

