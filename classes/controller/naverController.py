import datetime

from classes.services.naverService import NaverService

naverService = NaverService()

class NaverController:
    def getNewsList(self):
        return {
            "date"    : datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S'),
            "topic"   : naverService.getRealNewsTopicList(),
            "section" : naverService.getManySeeNewsSection(),
            "sex"     : naverService.getManySeeNewsSex(),
            "age"     : naverService.getManySeeNewsAge()
        }
