import requests
from bs4 import BeautifulSoup

get_HTML = requests.get(
    'https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid'
    '=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue=OPEN_PLUS_WA'
    'ITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL&credits=&instr'
    'uctor=&keyword=&begindate=&site=&resultNumber=250')

parse_HTML = BeautifulSoup(get_HTML.text, 'html.parser')
results = parse_HTML.find_all('div', attrs={'class': 'meta'})

# TODO
#  extract spreadsheet column titles and data
