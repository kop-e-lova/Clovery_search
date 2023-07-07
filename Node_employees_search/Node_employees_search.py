import requests
import json
from settings import *


class Node_employees_search():
    def __init__(self):
        pass

    def nes(self, wrong_url=None, wrong_headers=None, some_data=None):
        '''Метод поиска сотрудников узла и потомков'''
        if wrong_headers is None:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        else:
            headers = wrong_headers

        if wrong_url is None:
            url = url_node_employees_search
        else:
            url = wrong_url

        if some_data is None:
            data = {"node_id": node_id,
                    "project_id": project_id,
                    "item_type": item_type,
                    "item": item,
                    "page": 1,
                    "limit": 50,
                    "is_only": False}

        else:
            data = some_data

        res = requests.post(url, headers=headers, json=data)
        status = res.status_code
        res_headers = res.headers
        response = ""
        try:
            response = res.json(),
        except json.decoder.JSONDecodeError:
            response = res.text
        return status, response, res_headers

nes_s = Node_employees_search()