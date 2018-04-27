from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
class DaumService:
    '''
    [A-01] 실시간 이슈 검색어
    '''
    def getRealSearchWordList(self):
        html = Util.getHtml('https://search.daum.net')

        # 01. 실시간 이슈 검색어
        ranks = html.find("div", class_='hotissue_layer')
        data = {
            "title" : ranks.find("h2",{"id":"liveIssueTitle"}).string,
            "time"  : ranks.find("span", class_='txt_standard').string.replace("기준", " 기준"),
            "data"  : []
        }

        for rank in ranks.find_all("div", {"class":"rank_cont", "aria-hidden":"true"}):
            data['data'].append({
                "rank" : rank.find_all("span",class_='ir_wa')[0].string,
                "status" : rank.find_all("span",class_='ir_wa')[1].string,
                "url" : rank.find("a").get('href'),
                "word" : rank.find("a").get_text(),
            })
        return data


class Util:
    @staticmethod
    def getHtml(url):
        page = urlopen(url).read()
        return BeautifulSoup(page, "html.parser")


if __name__ == '__main__':
    service = DaumService()
    print('[A-01] 실시간 검색어'), print(service.getRealSearchWordList()), print()


'''
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://blog.naver.com/koys007/221225372448
'''