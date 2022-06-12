import fire
from getpass import getpass

class Auth(object):
    def login(self, username=None):
        if username == None:
            username = input('Username: ')
        if username == None:
            print('A username is requered')
            return
        pw = getpass("Password: ")
        return username, pw
    
def login(self, username=None):
    if username == None:
        username = input('Username: ')
    if username == None:
        print('A username is requered')
        return
    pw = getpass("Password: ")
    return username, pw


def scrape_tag(tag='python', query_filter = "Votes", page=1, max_pages=50, pagesize=25):
    base_url = 'https://stackoverflow.com/questions/tagged/'
    datas = []
    for p in range(max_pages):
        page_num = p + 1
        url = f'{base_url}{tag}?tab={query_filter}&page={page_num}&pagesize={pagesize}'
        datas.append(url)
    return datas

class Pipeline(object):
    def __init__(self):
        self.scrape = scrape_tag
        self.auth = Auth()
        self.login = login

if __name__ == "__main__":
#     python cli_fire_pipeline.py scrape --tag "Javascript"
# python cli_fire_pipeline.py login --username justin
    fire.Fire(Pipeline)
