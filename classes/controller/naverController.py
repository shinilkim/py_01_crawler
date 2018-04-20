from flask import request
from flask import request,jsonify, abort, json
import datetime, time

from classes.services.naverService import NaverService

naverService = NaverService()

class NaverController:
    def __init__(self):
        print('NaverController')

    def getNewsList(self, request):
        return {
            "date"    : datetime.datetime.now(),
            "topic"   : naverService.getRealNewsTopicList(),
            "section" : naverService.getManySeeNewsSection(),
            "sex"     : naverService.getManySeeNewsSex(),
            "age"     : naverService.getManySeeNewsAge()
        }
