import datetime
from flask import request,jsonify, abort, json
from classes.services.daumService import DaumService

daumService = DaumService()

class DaumController:
    def getRealSearchWordList(self):
        return daumService.getRealSearchWordList()

if __name__ == '__main__':
    ctrl = DaumController()
    print(ctrl.getRealSearchWordList())