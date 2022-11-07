import sys, os
from datetime import datetime as dt, date, timedelta, time as _time
from typing import Pattern
from pybeans import AppTool
import json
import time
import random
import io


class ClipUtil(AppTool):
    def __init__(self):
        super(ClipUtil, self).__init__('CLIP')
        self._session = None


    def random(self):
        return random.Random().random()


at = ClipUtil()