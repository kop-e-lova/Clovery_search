import pytest
from Team_members import *

def test_tm_base_positive():
    # S-API-TM-01 - БАЗОВЫЙ ПОЗИТИВНЫЙ ТЕСТ
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    #!!! дописать assert на response

def test_tm_teams_without_employees():
    # S-API-TM-02 - Отправка запроса с указанием списка команд, к которым не привязаны сотрудники.
    # Получение пустого списка в ответе
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["6d020bb3-05ae-4380-8a1c-8273bfe543b5"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

def test_tm_teams_one_team():
    # S-API-TM-03 - Проверка граничных значений. Отправка запроса с 1 командой в списке team_ids
    # Получение пустого списка в ответе
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_teams = [n['team_list'] for n in response[0]['response']]
    print(list_teams)
    assert ['Команда "Зубило"'] in [n for n in list_teams]

def test_tm_optional_fields():
    # S-API-TM-03 - Отправка запроса с обязательными параметрами
    # в установленных пределах и параметрами в теле: page = 1, limit = 50
    # Получение пустого списка в ответе
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 1, "limit": 50})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert "page" and "limit" in response[0]
    assert response[0]["page"] == 1
    assert response[0]["limit"] == 50

def test_tm_optional_fields_2_49():
    # S-API-TM-05 - Отправка запроса с обязательными параметрами
    # в установленных пределах и параметрами в теле: page = 2, limit = 49
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 2,"limit": 49})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found on this page', 'type': 'not_found'},)

def test_tm_optional_fields_2_5():
    # S-API-TM-06 - Отправка запроса с обязательными параметрами
    # в установленных пределах и параметрами в теле: page = 2, limit = 49
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae"],
                                                      "page": 2,"limit": 5})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert response == ({'response': [{'first_name': 'Евгения', 'last_name': 'Орлова', 'region': None, 'mobile_number': '+7 925 371 01 30', 'email': 'e.orlova.sm@gmail.com', 'profession_list': ['HR-специалист'], 'team_list': ['Команда "Шайба"'], 'grade_list': ['Младший специалист']}, {'first_name': 'Светлана', 'last_name': 'Хохлова', 'region': 'Москва', 'mobile_number': None, 'email': 'hohlovamail@gmail.com', 'profession_list': ['HR-специалист'], 'team_list': ['Команда "Шайба"'], 'grade_list': ['Младший специалист']}, {'first_name': 'Игорь', 'last_name': 'Борисов', 'region': 'Тольятти', 'mobile_number': '+7 917 656 86 82', 'email': 'bdv100001@mail.ru', 'profession_list': ['Product-менеджер', 'HR-специалист'], 'team_list': ['Команда "Шайба"'], 'grade_list': ['Специалист']}], 'page': 2, 'limit': 5, 'total': 8},)

def test_tm_optional_fields_5_1():
    # S-API-TM-07 - Отправка запроса с обязательными параметрами
    # в установленных пределах и параметрами в теле: page = 2, limit = 49
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae"],
                                                      "page": 5,"limit": 1})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert response == ({'response': [{'first_name': 'Валерия', 'last_name': 'Садчикова', 'region': None, 'mobile_number': None, 'email': 'valeria_sadchikova@example.com', 'profession_list': ['Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Стажер']}], 'page': 5, 'limit': 1, 'total': 8},)

def test_tm_several_teams_one_is_not_in_base():
    # S-API-TM-51 - Отправка запроса с указанием в списке нескольких команд, часть из которых существует в БД,
    # а 1 не существует в БД. Получение списка сотрудников по существующим в БД командам в ответе,
    # ошибка не вызывается
    #в ответе все 10 сотрудников команд Зубило, Шайба, Отчеты Кловери
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae",
                                                                   "f11bfb79-e627-487d-b541-1b911f833186",
                                                                   "f11bfb79-e627-487d-b541-1b911f833100"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_teams = [n ['team_list'] for n in response[0]['response']]
    print(list_teams)
    #Сделать через список через set и сравнить с заданным. Но в списке значения в списке. Нужно конвертировать

def test_tm_upper_URL():
    # S-API-TM-08 - Отправка запроса с URL в верхнем регистре
    status, response, res_headers = tm.tms(some_url="https://API.CLOVERI.SKROY.ru/api/employee_search/",
                                           some_headers=None,some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_tm_upper_headers():
    # S-API-TM-09 - Отправка запроса с заголовками в верхнем регистре
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers={'CONTENT-TYPE': 'APPLICATION/JSON', 'ACCEPT': 'APPLICATION/JSON'},some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_tm_mixed_headers():
    # S-API-TM-10 - Отправка запроса с заголовками в смешанном регистре
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers={'CONTENT-TYPE': 'application/json', 'accept': 'APPLICATION/JSON'},
                                           some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

#Негативные тесты

def test_tm_wrong_method():
    #S-API-TM-012 Запрос неверным методом
    url = "https://api.cloveri.skroy.ru/api/employee_search/"
    headers = {"Accept": "application/json",
               "Content-type": "application/json"}
    data = {"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883", "23a4363f-28d0-43e2-b66e-f2aedd4175ae"]}
    res = requests.get(url, headers=headers, json=data)
    status = res.status_code
    res_headers = res.headers
    response = ""
    try:
        response = res.json(),
    except json.decoder.JSONDecodeError:
        response = res.text
    #return status, response, res_headers
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 405
    assert response == ({'detail': 'Method Not Allowed'},)

@pytest.mark.skip
def test_tm_wrong_url():
    # S-API-TM-13 - Отправка запроса с неверным URL
    #SSLError
    status, response, res_headers = tm.tms(some_url="https//api.clover.skroy.ru",
                                           some_headers=None, some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404

def test_tm_wrong_endpoint():
    # S-API-TM-14 - Отправка запроса с неверным endpoint
    status, response, res_headers = tm.tms(some_url="https://api.cloveri.skroy.ru/api/employee_searc/",
                                           some_headers=None, some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404

def test_tm_wrong_content_type():
    # S-API-TM-15 - Отправка запроса с неверным content_type

    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers={"Accept": "application/json",
                                                                             "Content-Type": "text/css"},
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                       "23a4363f-28d0-43e2-b66e-f2aedd4175ae"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body'], 'msg': 'value is not a valid dict', 'type': 'type_error.dict'}]},)

def test_tm_body_str():
    # S-API-TM-16 - Отправка запроса с неверным content_type

    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data=str({"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                       "23a4363f-28d0-43e2-b66e-f2aedd4175ae"]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body'], 'msg': 'value is not a valid dict', 'type': 'type_error.dict'}]},)

def test_tm_no_body():
    # S-API-TM-17 - Отправка запроса без тела
    url = "https://api.cloveri.skroy.ru/api/employee_search/"
    headers = {"Accept": "application/json",
               "Content-type": "application/json"}
    res = requests.post(url, headers=headers)
    status = res.status_code
    res_headers = res.headers
    response = ""
    try:
        response = res.json(),
    except json.decoder.JSONDecodeError:
        response = res.text
    # return status, response, res_headers
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_tm_no_headers():
    # S-API-TM-18 - Отправка запроса без заголовков
    url = "https://api.cloveri.skroy.ru/api/employee_search/"
    data = {"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883", "23a4363f-28d0-43e2-b66e-f2aedd4175ae"]}
    res = requests.post(url,  json=data)
    status = res.status_code
    res_headers = res.headers
    response = ""
    try:
        response = res.json(),
    except json.decoder.JSONDecodeError:
        response = res.text
    # return status, response, res_headers
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

@pytest.mark.skip
def test_tm_wrong_protocol():
    # S-API-TM-19 - Отправка запроса с неверным протоколом
    status, response, res_headers = tm.tms(some_url="http://api.cloveri.skroy.ru/api/employee_search/",
                                           some_headers=None, some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    #assert status == 404

#Обязательные параметры (тело)
def test_tm_Upper_keys():
    # S-API-TM-20 - Запрос с указанием ключей обязательных параметров в верхнем регистре
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"TEAM_IDS": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae",
                                                                   "f11bfb79-e627-487d-b541-1b911f833186"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_tm_wrong_field_name():
    # S-API-TM-21 - Запрос с ошибочным указанием одного из обязательных параметров (teams_id вместо team_ids)
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"teams_id": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae",
                                                                   "f11bfb79-e627-487d-b541-1b911f833186"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_tm_extra_field():
    # S-API-TM-22 - Запрос с указанием в теле запроса непредусмотренного данным запросом поля
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae",
                                                                   "f11bfb79-e627-487d-b541-1b911f833186"],
                                                      "extra_field": "extra_field"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

def test_tm_double_parametres_equal_values():
    # S-API-TM-23 - Запрос с дублированием обязательных параметров в теле запроса(c одинаковыми значениями)
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae",
                                                                   "f11bfb79-e627-487d-b541-1b911f833186"],
                                                      "team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae",
                                                                   "f11bfb79-e627-487d-b541-1b911f833186"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

def test_tm_double_parametres_different_values():
    # S-API-TM-24 - Запрос с дублированием обязательных параметров в теле запроса(c разными значениями)
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={
                                               "team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883", "23a4363f-28d0-43e2-b66e-f2aedd4175ae", "f11bfb79-e627-487d-b541-1b911f833186"],
                                               "team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031884", "23a4363f-28d0-43e2-b66e-f2aedd4175af", "f11bfb79-e627-487d-b541-1b911f833187"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404 or status == 200
    if status == 404:
        assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

#Параметр team_ids

def test_tm_team_ids_empty_dict():
    # S-API-TM-31 - Запрос с дублированием обязательных параметров в теле запроса(c разными значениями)
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_tm_team_ids_None():
    # S-API-TM-32 - Запрос со значением team_ids=None
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": None})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_tm_team_ids_empty():
    # S-API-TM-33 - Запрос со значением team_ids=""
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": ""})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.skip
def test_tm_team_ids_empty_list():
    # S-API-TM-34 - Запрос со значением team_ids - пустой список
    #Оставить до поиска по БД
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": []})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

def test_tm_team_ids_not_uuid_in_list():
    # S-API-TM-35 - Попытка запроса с неверным форматом team_id в списке в поле (не UUID в списке)
    #Оставить до поиска по БД
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": [2,3]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids', 0], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}, {'loc': ['body', 'team_ids', 1], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)


def test_tm_team_ids_two_empty_values_in_list():
    # S-API-TM-36 - Попытка запроса с пустыми значениями в списке
    #Оставить до поиска по БД
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": ["",""]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids', 0], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}, {'loc': ['body', 'team_ids', 1], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

def test_tm_team_ids_None_in_list():
    # S-API-TM-37 - Попытка запроса со значением None в списке
    #Оставить до поиска по БД
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": [None]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids', 0], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_tm_team_ids_string_uuid():
    # S-API-TM-38 - Попытка запроса со значением team_ids - str c UUID
    #Оставить до поиска по БД
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": "4ae7df2a-a5dd-4267-aaa8-093b84031883"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

def test_tm_team_ids_string_uuid():
    # S-API-TM-39 - Запрос с team_ids неверного формата (не list)
    #Оставить до поиска по БД
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": {"team_ids":"4ae7df2a-a5dd-4267-aaa8-093b84031883"}})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

def test_tm_team_ids_non_existant():
    # S-API-TM-40 - Запрос с несуществующими team_ids
    #Оставить до поиска по БД
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031999"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

def test_tm_team_ids_double():
    # S-API-TM-53 - Запрос с несколькими повторяющимися team_id в списке в поле team_ids
    #Оставить до поиска по БД
    status, response, res_headers = tm.tms(some_url=None,
                                           some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae",
                                                                   "f11bfb79-e627-487d-b541-1b911f833186",
                                                                   "4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                   "23a4363f-28d0-43e2-b66e-f2aedd4175ae",
                                                                   "4ae7df2a-a5dd-4267-aaa8-093b84031883"]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

#Параметр page
def test_page_str():
    #S - API - TM - 42
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": "one_page", "limit": 50})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_page_dict():
    #S - API - TM - 42-1
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": [1], "limit": 50})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_page_empty():
    #S - API - TM - 43
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": "", "limit": 50})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_page_negative():
    #S - API - TM - 44
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": -1, "limit": 50})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'ensure this value is greater than or equal to 1', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 1}}]},)

def test_page_zero():
    #S - API - TM - 52
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 0, "limit": 50})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'ensure this value is greater than or equal to 1', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 1}}]},)

def test_page_10_limit_5():
    #S - API - TM - 45
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 10, "limit": 5})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found on this page', 'type': 'not_found'},)

#Параметр limit
def test_limit_string():
    #S - API - TM - 46
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 1, "limit": "three"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_limit_list():
    #S - API - TM - 46-1
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 1, "limit": [50]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_limit_empty():
    #S - API - TM - 47
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 1, "limit": ""})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_limit_negative():
    #S - API - TM - 48
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 1, "limit": -1})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'ensure this value is greater than or equal to 1', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 1}}]},)

def test_limit_zero():
    #S - API - TM - 49
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 1, "limit": 0})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'ensure this value is greater than or equal to 1', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 1}}]},)

def test_limit_51():
    #S - API - TM - 50
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "page": 1, "limit": 51})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'ensure this value is less than or equal to 50', 'type': 'value_error.number.not_le', 'ctx': {'limit_value': 50}}]},)

# проверки на параметр фильтрации поиска first_name
def test_first_name_int():
    #S - API - TM - 54
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "first_name": 1})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_first_name_empty_str():
    #S - API - TM - 55
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "first_name": ""})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_first_name_None():
    #S - API - TM - 56
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "first_name": None})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_first_name_James():
    #S - API - TM - 57
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "first_name": "James"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

#Last_name
def test_last_name_int():
    #S - API - TM - 58
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "last_name": 1})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_last_name_empty_str():
    #S - API - TM - 59
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "last_name": ""})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_last_name_None():
    #S - API - TM - 60
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "last_name": None})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_last_name_Afonina():
    #S - API - TM - 61
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "last_name": "Афонина"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

#Profession

def test_profession_int():
    #S - API - TM - 62
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "profession": 1})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_profession_empty_str():
    #S - API - TM - 63
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "profession": ""})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_profession_None():
    #S - API - TM - 64
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "profession": None})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_profession_HR_():
    #S - API - TM - 65
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                       "profession": "HR-специалист"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

def test_wrong_pair_first_last_name():
    #S - API - TM - 66
    status, response, res_headers = tm.tms(some_url=None, some_headers=None,
                                           some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                      "first_name": "Иван",
                                                      "last_name": "Лыжин",
                                                      "profession": "Product-менеджер"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422