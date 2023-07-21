import requests
import json
from settings import *


class SkillSearch():
    def __init__(self):
        pass

    def ssn(self, some_url=None, some_headers=None, some_data=None):
        '''Метод поиска по навыкам только с обязательными полями'''
        if some_headers is None:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        else:
            headers = some_headers

        if some_url is None:
            url = url_skill_search
        else:
            url = some_url

        if some_data is None:
            data = {
                'company_id': company_id,
                'skills': skills
            }
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


    def sso(self, some_url=None, some_headers=None, some_data=None, some_params=None):
        '''Метод поиска по навыкам со всеми опциональными полями'''
        if some_headers is None:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        else:
            headers = some_headers

        if some_url is None:
            url = url_skill_search
        else:
            url = some_url

        if some_data is None:
            data = {
                'company_id': company_id,
                'professions_ids': profession_ids,
                'team_ids': team_ids,
                'skills': skills_1,
                'full_match_of_skills': True
                }
        else:
            data = some_data

        if some_params is None:
            params = {'page': 0, 'limit': 50}
        else:
            params = some_params

        res = requests.post(url, headers=headers, json=data, params=params)
        status = res.status_code
        res_headers = res.headers
        response = ""
        try:
            response = res.json(),
        except json.decoder.JSONDecodeError:
            response = res.text
        return status, response, res_headers

skill_s = SkillSearch()
