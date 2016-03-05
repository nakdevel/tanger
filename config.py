'''
Created on 5 de mar. de 2016

@author: jr
'''

import os
basedir = os.path(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '*- H1rd 2 g533SS K3y__#'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
          'development':    DevelopmentConfig,

          'default':        DevelopmentConfig
          }



