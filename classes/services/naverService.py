from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
class NaverService:
    '''
    [A-01] 네이버 실시간 뉴스 토픽
    '''
    def getRealNewsTopicList(self):
        html = Util.getHtml('http://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111')
        ranks = html.find("ol", {"id":'newstopic_news'})
        list = []
        for rank in ranks.find_all("li"):
            #print(rank)
            data = {
                # href속성:Y / id속성:N / 빈공백제거
                "title" : rank.find("a", href=True, id=False).find("strong").get_text(" ", strip=True),
                "rank"  : rank.find("a").find("em").get_text(),
                "url"   : rank.a['href']
            }
            list.append(data)
        return list
    '''
    [A-02] 많이 본 뉴스(섹션별)
    '''
    def getManySeeNewsSection(self):
        html = Util.getHtml('http://m.news.naver.com/rankingList.nhn?type=section')
        ranks = html.find("div", {"class":"news","id":"ct"}).find_all("div", {"class":"ranking_news"})
        list = []
        for rank in ranks:
            list.append({
                "title": rank.find("div").find("div").find("h2").get_text(),
                "news": Util.getInfo(rank)
            })
        return list

    '''
    [A-03] 많이 본 뉴스(남녀별)
    '''
    def getManySeeNewsSex(self):
        list = []
        # 01. 남성이 더 많이 본 뉴스        
        html = Util.getHtml('http://m.news.naver.com/rankingList.nhn?type=gender&typeValue=male')
        ranks = html.find("div", {"class":"news","id":"ct"}).find("div", {"class":"ranking_news"})
        list.append({
            "title": ranks.find("ul", {"class":"p_section2"}).find("li",{"class":"on"}).find("a").get_text(),
            "news": Util.getInfo(ranks)
        })
        # 02. 여성이 더 많이 본 뉴스
        html = Util.getHtml('http://m.news.naver.com/rankingList.nhn?type=gender&typeValue=female')
        ranks = html.find("div", {"class": "news", "id": "ct"}).find("div", {"class": "ranking_news"})
        list.append({
            "title": ranks.find("ul", {"class":"p_section2"}).find("li",{"class":"on"}).find("a").get_text(),
            "news": Util.getInfo(ranks)
        })

        return list
    '''
    [A-04] 많이 본 뉴스(연령별)
    '''
    def getManySeeNewsAge(self):
        list = []
        # 01. 연령별 > 10대
        html = Util.getHtml('http://m.news.naver.com/rankingList.nhn?type=age&typeValue=10')
        ranks = html.find("div", {"class":"news","id":"ct"}).find("div", {"class":"ranking_news"})
        list.append({
            "title": '10대',
            "news": Util.getInfo(ranks)
        })
        # 02. 연령별 > 20대
        html = Util.getHtml('http://m.news.naver.com/rankingList.nhn?type=age&typeValue=20')
        ranks = html.find("div", {"class": "news", "id": "ct"}).find("div", {"class": "ranking_news"})
        list.append({
            "title": '20대',
            "news": Util.getInfo(ranks)
        })
        # 03. 연령별 > 30~40대
        html = Util.getHtml('http://m.news.naver.com/rankingList.nhn?type=age&typeValue=30')
        ranks = html.find("div", {"class": "news", "id": "ct"}).find("div", {"class": "ranking_news"})
        list.append({
            "title": '30~40대',
            "news": Util.getInfo(ranks)
        })
        # 04. 연령별 > 50대 이상
        html = Util.getHtml('http://m.news.naver.com/rankingList.nhn?type=age&typeValue=50')
        ranks = html.find("div", {"class": "news", "id": "ct"}).find("div", {"class": "ranking_news"})
        list.append({
            "title": '50대 이상',
            "news": Util.getInfo(ranks)
        })
        return list

class Util:
    @staticmethod
    def getHtml(url):
        page = urlopen(url).read()
        return BeautifulSoup(page, "html.parser")

    @staticmethod
    def getInfo(rank):
        news = []
        for li in rank.find("ul", {"class": "commonlist"}).find_all("li"):
            try:
                news.append({
                "url": 'http://m.news.naver.com/' + li.a['href'],
                "rank": li.i.get_text(),
                "count": re.sub('[^0-9]', '', li.find("div", {"class": "commonlist_tx_visit"}).get_text()),
                "title": li.find("div", {"class": "commonlist_tx_headline"}).get_text(),
                "img": li.img['src']
                })
            except TypeError as e:
                print(e)
        return news

if __name__ == '__main__':
    naver = NaverService()
    #print('[A-01] 네이버 실시간 뉴스 토픽'), print(naver.getRealNewsTopicList()), print()
    #print('[A-02] 많이 본 뉴스(섹션별)'), print(naver.getManySeeNewsSection())
    #print('[A-03] 많이 본 뉴스(남녀별)'), print(naver.getManySeeNewsSex())
    print('[A-04] 많이 본 뉴스(연령별)'), print(naver.getManySeeNewsAge())

'''
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://blog.naver.com/koys007/221225372448
'''