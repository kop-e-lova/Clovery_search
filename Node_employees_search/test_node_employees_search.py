import pytest
import requests
import json
from Node_employees_search import *


#Базовый позитивный без класса
def test_node_employee_search_base():
    url = "https://api.cloveri.skroy.ru/api/node_employees_search/"
    headers = {"Accept": "application/json",
               "Content-type": "application/json"}
    data = {"node_id": 2919, "project_id": project_id,"item_type": item_type,
            "item": item, "page": 1, "limit": 50, "is_only_node": False}
    res = requests.post(url, headers=headers, json=data)
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

def test_nes_base_positive():
    #S - API - NE - 1 - БАЗОВЫЙ ПОЗИТИВНЫЙ ТЕСТ
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    # Проверка на наличие нужных полей в ответе
    for n in response[0]['response']: assert "first_name" in n and "last_name" in n and "last_name" in n \
                                             and "mobile_number" in n and "email" in n and "profession_list" in n \
                                             and "team_list" in n and "grade_list" in n
    # Проверка ожидаемой выгрузки сотрудников
    list_e = [n['last_name'] for n in response[0]['response']]
    print(list_e)
    expected_list = ['Орлова', 'Хохлова', 'Борисов', 'Лыжин', 'Афонин', 'Недочетова', 'Лязникова', 'Садчикова']
    assert list_e == expected_list

def test_nes_without_optional_fields():
    #S - API - NE - 02 - Без опциональных полей
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": "3e3028cd-3849-461b-a32b-90c0d6411daa",
                                                            "item_type": "orgstructureM",
                                                            "item": "pytest"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_nes_is_only_true():
    #S - API - NE - 3 - is_only_node = True
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,"project_id": project_id,
                                                            "item_type": item_type, "item": item,
                                                            "page": 1,"limit": 50, "is_only_node": True})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_nes_node_without_descendants_with_teams():
    #S - API - NE - 04 - Отправка запроса с указанием node_id узла без потомков,
    # к которому привязаны команды и сотрудники. Поиск по умолчанию по узлу с потомками.
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2921,
                                                           "project_id": project_id, "item_type": item_type,
                                                           "item": item, "page": 1, "limit": 50, "is_only_node": True})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert response == ({'response': [{'first_name': 'Евгения', 'last_name': 'Орлова', 'region': None, 'mobile_number': '+7 925 371 01 30', 'email': 'e.orlova.sm@gmail.com', 'profession_list': ['HR-специалист'], 'team_list': ['Команда "Шайба"'], 'grade_list': ['Младший специалист']}, {'first_name': 'Светлана', 'last_name': 'Хохлова', 'region': 'Москва', 'mobile_number': None, 'email': 'hohlovamail@gmail.com', 'profession_list': ['HR-специалист'], 'team_list': ['Команда "Шайба"'], 'grade_list': ['Младший специалист']}, {'first_name': 'Игорь', 'last_name': 'Борисов', 'region': 'Тольятти', 'mobile_number': '+7 917 656 86 82', 'email': 'bdv100001@mail.ru', 'profession_list': ['Product-менеджер', 'HR-специалист'], 'team_list': ['Команда "Шайба"'], 'grade_list': ['Специалист']}], 'page': 1, 'limit': 50, 'total': 3},)

def test_nes_node_with_descendants_with_teams():
    #S - API - NE - 05 - Отправка запроса с указанием node_id узла, к которому не привязаны команды и сотрудники,
    # но имеющего потомков с привязанными командами и сотрудниками. Поиск по умолчанию по узлу с потомками.
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2934, "project_id": project_id,
                                                           "item_type": item_type, "item": item,
                                                           "page": 1, "limit": 50, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert response == ({'response': [{'first_name': 'Алексей', 'last_name': 'Лыжин', 'region': 'Москва', 'mobile_number': '+7 915 459 62 66', 'email': 'alexlyzhin@gmail.com', 'profession_list': ['IT-предприниматель', 'Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Без оценки']}, {'first_name': 'Иван', 'last_name': 'Афонин', 'region': None, 'mobile_number': None, 'email': 'ivan_afonin@gmail.com', 'profession_list': ['Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Старший специалист']}, {'first_name': 'Мария', 'last_name': 'Недочетова', 'region': None, 'mobile_number': None, 'email': 'maria_nedochetova@example.com', 'profession_list': ['Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Специалист']}, {'first_name': 'Евгения', 'last_name': 'Лязникова', 'region': None, 'mobile_number': None, 'email': 'evgenia_lazhnikova@example.com', 'profession_list': ['Project-менеджер', 'Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Младший специалист']}, {'first_name': 'Валерия', 'last_name': 'Садчикова', 'region': None, 'mobile_number': None, 'email': 'valeria_sadchikova@example.com', 'profession_list': ['Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Стажер']}], 'page': 1, 'limit': 50, 'total': 5},)


def test_page2_limit49():
    #S-API-NE-66
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919, "project_id": project_id,
                                                             "item_type": item_type,"item": item,
                                                             "page": 2, "limit": 49,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found on this page', 'type': 'not_found'},)

def test_page2_limit5():
    #S-API-NE-67
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919, "project_id": project_id,
                                                           "item_type": item_type, "item": item,
                                                           "page": 2, "limit": 5, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert response == ({'response': [{'first_name': 'Мария', 'last_name': 'Недочетова', 'region': None, 'mobile_number': None, 'email': 'maria_nedochetova@example.com', 'profession_list': ['Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Специалист']}, {'first_name': 'Евгения', 'last_name': 'Лязникова', 'region': None, 'mobile_number': None, 'email': 'evgenia_lazhnikova@example.com', 'profession_list': ['Project-менеджер', 'Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Младший специалист']}, {'first_name': 'Валерия', 'last_name': 'Садчикова', 'region': None, 'mobile_number': None, 'email': 'valeria_sadchikova@example.com', 'profession_list': ['Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Стажер']}], 'page': 2, 'limit': 5, 'total': 8},)


def test_page5_limit1():
    #S-API-NE-68
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919, "project_id": project_id,
                                                           "item_type": item_type, "item": item,
                                                           "page": 5, "limit": 1, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert response == ({'response': [{'first_name': 'Иван', 'last_name': 'Афонин', 'region': None, 'mobile_number': None, 'email': 'ivan_afonin@gmail.com', 'profession_list': ['Product-менеджер'], 'team_list': ['Команда "Зубило"'], 'grade_list': ['Старший специалист']}], 'page': 5, 'limit': 1, 'total': 8},)

def test_nes_upper_URL():
    #S - API - NE - 06 - Отправка запроса с URL в верхнем регистре
    status, response, res_headers = nes_s.nes(wrong_url="https://API.CLOVERI.SKROY.ru/api/node_employees_search/", wrong_headers=None,
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_nes_upper_headers():
    #S - API - NE - 07 - Отправка запроса с заголовками в верхнем регистре
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={'CONTENT-TYPE': 'APPLICATION/JSON', 'ACCEPT': 'APPLICATION/JSON'},
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_nes_mixed_headers():
    #S - API - NE - 08 - Отправка запроса с заголовками в верхнем регистре
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={'CONTENT-TYPE': 'application/json', 'accept': 'APPLICATION/JSON'},
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200

#NEGATIVE_TESTS

def test_nes_wrong_url():
    #S-API-NE-10 - неверный URL
    #Запрос не проходит- SSLError
    status, response, res_headers = nes_s.nes(wrong_url="https://skroy.ru/api/node_employees_search/", wrong_headers=None,
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404

def test_nes_wrong_endpoint():
    #S-API-NE-11 - неверный Эндпоинт
    status, response, res_headers = nes_s.nes(wrong_url="https://api.cloveri.skroy.ru/api/node_employees_searc/", wrong_headers=None,
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404

def test_nes_wrong_content_type():
    #S-API-NE-12 - Content-Type": "application/xml
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={"Accept": "application/json",
                                                                             "Content-Type": "application/xml"},
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body'], 'msg': 'value is not a valid dict', 'type': 'type_error.dict'}]},)

def test_nes_no_headers():
    #S-API-NE-13 - Запрос без заголовков
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

def test_nes_wrong_protocol():
    #S-API-NE-14 - Запрос с неверным типом протокола: http вместо https - skip
    status, response, res_headers = nes_s.nes(wrong_url="http://api.cloveri.skroy.ru/api/node_employees_search/", wrong_headers={},
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    #assert status == 404

#S-API-NE-15, S-API-NE-16  - skip, S-API-NE-17 - cancelled

def test_nes_error_from_service_teems_employees():
    #S-API-NE-18 - Запрос с имитированием получения ошибки в ответе от сервиса Сотрудники команд
    #Привязана несуществующая команда: ["6d020bb3-05ae-4380-8a1c-8273bfe54300"]
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data={
  "node_id": 3043, "project_id": project_id, "item_type": item_type, "item": item,
  "page": 1, "limit": 50, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

#Параметр node_id

def test_nes_wrong_format_node_id():
    #S-API-NE-19 -Запрос с указанием node_id неверного формата
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data={
  "node_id": "node", "project_id": project_id, "item_type": item_type,"item": item,
  "page": 1, "limit": 50, "is_only_node": False
})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'node_id'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_nes_non_existant_node_id():
    #S-API-NE-20 -Запрос с указанием несуществующего node_id
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data={"node_id": 999999999999999,
                                                           "project_id": project_id, "item_type": item_type,
                                                           "item": item, "page": 1, "limit": 50, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'does not exist object(s)'},)

def test_nes_non_empty_node_id():
    #S-API-NE-21 -Запрос с указанием пустого значения node_id
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data={"node_id": "", "project_id": project_id,
                                                           "item_type": item_type, "item": item,
                                                           "page": 1, "limit": 50, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'node_id'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_nes_non_None_node_id():
    #S-API-NE-22 -Запрос с указанием None значения node_id
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data={"node_id": None,"project_id": project_id,
                                                           "item_type": item_type, "item": item,
                                                           "page": 1, "limit": 50, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'node_id'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_nes_no_descendants_no_teams():
    #S-API-NE-23 -Запрос с указанием node_id узла без потомков, к которому не привязаны команды
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data={"node_id": 2933, "project_id": project_id,
                                                           "item_type": item_type, "item": item,
                                                           "page": 1, "limit": 50, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

def test_nes_empty_team():
    #S-API-NE-24 -Запрос с указанием node_id узла без потомков, к которому не привязаны сотрудники (привязана пустая команда)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data={"node_id": 2982,"project_id": project_id,
                                                           "item_type": item_type, "item": item,
                                                           "page": 1, "limit": 50, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

def test_nes_empty_team():
    #S-API-NE-24-1 Запрос с указанием node_id узла без поля team_ids в атрибутах узла
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={},
                                                some_data={"node_id": 210, "project_id": project_id,
                                                           "item_type": item_type, "item": item,
                                                           "page": 1, "limit": 50, "is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

def test_nes_attributes_of_node_is_none():
    #S-API-NE-69
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 3045,
                                                            "project_id": project_id,
                                                            "item_type": item_type, "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

#Обязательные параметры запроса

def test_nes_obligatory_params_in_query_params():
    #S-API-NE-25 Запрос с отправкой в query_params обязательных параметров project_id, item_type, item
    url = "https://api.cloveri.skroy.ru/api/node_employees_search/"
    headers = {"Accept": "application/json",
               "Content-type": "application/json"}
    data = {"node_id": 2919,
            "page": 1,
            "limit": 50,
            "is_only_node": False}
    params = {"project_id": "3e3028cd-3849-461b-a32b-90c0d6411daa",
            "item_type": "orgstructureM",
            "item": "pytest"}
    res = requests.post(url, headers=headers, json=data, params=params)
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
    assert response == ({'detail': [{'loc': ['body', 'project_id'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'item_type'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'item'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_nes_obligatory_params_in_headers():
    #S-API-NE-26 Запрос с указанием обязательных параметров project_id, item_type, item в headers
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers={"project_id": "3e3028cd-3849-461b-a32b-90c0d6411daa",
                                                            "item_type": "orgstructureM", "item": "pytest"},
                                                some_data={"node_id": 2919,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'project_id'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'item_type'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'item'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_nes_obligatory_params_in_url():
    #S-API-NE-27 Запрос с указанием обязательных параметров project_id, item_type, item в headers
    status, response, res_headers = nes_s.nes(wrong_url="https://api.cloveri.skroy.ru/api/node_employees_search/project_id=3e3028cd-3849-461b-a32b-90c0d6411daa/item_type=orgstructureM/item=pytest/",
                                              wrong_headers=None,
                                              some_data={"node_id": 2919,"page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Not Found'},)

#S-API-NE-28 - cancelled

def test_nes_upper_keys_parameters():
    #S-API-NE-29
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "PROJECT_ID": project_id,
                                                            "ITEM_TYPE": item_type, "ITEM": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'project_id'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'item_type'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'item'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_nes_wrong_one_key_name():
    #S-API-NE-30 Запрос с ошибочным указанием одного из обязательных параметров (project_ids вместо project_id)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919, "project_ids": project_id,
                                                            "item_type": item_type, "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'project_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_nes_extra_field():
    #S-API-NE-31 Запрос с ошибочным указанием одного из обязательных параметров (project_ids вместо project_id)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type, "item": item,
                                                           "extra_field": "",
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200
    if status == 422:
        assert response == ({'errors': ['field extra_field not allowed']})

def test_nes_double_params_equal_values():
    #S-API-NE-32 Запрос с дублированием обязательных параметров в теле запроса (c одинаковыми значениями)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": "3e3028cd-3849-461b-a32b-90c0d6411daa",
                                                           "project_id": "3e3028cd-3849-461b-a32b-90c0d6411daa",
                                                            "item_type": "orgstructureM","item_type": "orgstructureM",
                                                           "item": "pytest", "item": "pytest",
                                                           "extra_field": "",
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

def test_nes_double_params_other_values():
    #S-API-NE-33 Запрос с дублированием обязательных параметров в теле запроса (c разными значениями)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": "3e3028cd-3849-461b-a32b-90c0d6411daa",
                                                           "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dab",
                                                            "item_type": "orgstructureM","item_type": "orgstructureL",
                                                           "item": "pytest", "item": "pytest1",
                                                           "extra_field": "",
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'does not exist object(s)'},)

#Project_id
def test_nes_no_project_id():
    #S-API-NE-34 Запрос без указания обязательного параметра project_id
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            #"project_id": "3e3028cd-3849-461b-a32b-90c0d6411daa",
                                                            "item_type": item_type, "item": item,
                                                           "extra_field": "",
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'project_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_nes_None_project_id():
    #S-API-NE-35 Запрос со значением project_id=None
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": None, "item_type": item_type,
                                                           "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'project_id'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_nes_empty_project_id():
    #S-API-NE-36 Запрос с пустым значением project_id
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919, "project_id": "",
                                                            "item_type": item_type, "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'project_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

def test_nes_wrong_format_project_id():
    #S-API-NE-37 Запрос с неверным форматом project_id
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": "project_id",
                                                            "item_type": item_type, "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'project_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

def test_nes_wrong_non_existant_project_id():
    #S-API-NE-38 Запрос с несуществующим project_id
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": "4e3028cd-3849-461b-a32b-90c0d6411daa",
                                                            "item_type": item_type, "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'does not exist object(s)'},)

def test_nes_wrong_another_project_project_id():
    #S-API-NE-39 Запрос с  project_id из другого проекта
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dab",
                                                            "item_type": item_type, "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'does not exist object(s)'},)

#Item_type
def test_nes_without_item_type():
    #S-API-NE-40 Запрос без item_type
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            #"item_type": item_type,
                                                           "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'item_type'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_nes_None_item_type():
    #S-API-NE-41 Запрос co значением None item_type
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": None,
                                                           "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'item_type'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_nes_empty_item_type():
    #S-API-NE-42 Запрос c пустым значением item_type
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": "",
                                                           "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': "['field item_type must not be empty']"},)

def test_nes_wrong_format_item_type():
    #S-API-NE-43 Запрос c неверным форматом значения item_type
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": 123,
                                                           "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 404
    if status == 404:
        assert response == ({'detail': 'does not exist object(s)'},)

def test_nes_non_existant_item_type():
    #S-API-NE-44 Запрос c несуществующим значением item_type
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": "orgstructureSome",
                                                           "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 404
    if status == 404:
        assert response == ({'detail': 'does not exist object(s)'},)

def test_nes_another_project_item_type():
    #S-API-NE-45 Запрос c  item_type из другого проетка
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": "orgstructureL",
                                                           "item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 404
    if status == 404:
        assert response == ({'detail': 'does not exist object(s)'},)

#Item

def test_no_item():
    #S-API-NE-46 Запрос без указания обязательного параметра item
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           #"item": item,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'item'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

def test_None_item():
    #S-API-NE-47 Запрос со значением item=None
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": None,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'item'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_empty_item():
    #S-API-NE-48 Запрос со значением item=""
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": "",
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': "['field item must not be empty']"},)

def test_wrong_format_item():
    #S-API-NE-49 Запрос с неверным форматом значения item=
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": 123,
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 404
    if status == 404:
        assert response == ({'detail': 'does not exist object(s)'},)

def test_non_existant_item():
    #S-API-NE-50 Запрос с несуществующим item=
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": "test",
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 404
    if status == 404:
        assert response == ({'detail': 'does not exist object(s)'},)

def test_another_project_item():
    #S-API-NE-51 Запрос с item из другого проекта
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": "start_project",
                                                            "page": 1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 404
    if status == 404:
        assert response == ({'detail': 'does not exist object(s)'},)

#Проверки по параметру team_ids в атрибутах узла
def test_team_ids_None():
    #S-API-NE-70 Запрос со значением team_ids=None
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 3046,
    "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dba",
    "item_type": "orgstructure",
    "item": "start_project",
     "page": 1,
     "limit": 50,
     "is_only_node": False
     })
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

def test_team_ids_Empty():
    #S-API-NE-71 Запрос со значением team_ids=None
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 3047,
    "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dba",
    "item_type": "orgstructure",
    "item": "start_project",
     "page": 1,
     "limit": 50,
     "is_only_node": False
     })
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

def test_team_ids_wrong_format_in_list():
    #S-API-NE-72 Попытка запроса с неверным форматом team_id в списке в поле (не UUID в списке)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 3048,
    "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dba",
    "item_type": "orgstructure",
    "item": "start_project",
     "page": 1,
     "limit": 50,
     "is_only_node": False
     })
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

def test_team_ids_wrong_format_in_list():
    #S-API-NE-73 Попытка запроса с пустым значением в списке team_ids": ["",""]
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 3049,
    "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dba",
    "item_type": "orgstructure",
    "item": "start_project",
     "page": 1,
     "limit": 50,
     "is_only_node": False
     })
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

def test_team_ids_null():
    #S-API-NE-74 Попытка запроса со значением Null в списке (team_id=Null)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 3050,
    "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dba",
    "item_type": "orgstructure",
    "item": "start_project",
     "page": 1,
     "limit": 50,
     "is_only_node": False
     })
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

def test_team_ids_str():
    #S-API-NE-75 Попытка запроса с указанием team_id не в списке, а сразу под ключом поля team_ids
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 3051,
    "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dba",
    "item_type": "orgstructure",
    "item": "start_project",
     "page": 1,
     "limit": 50,
     "is_only_node": False
     })
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

def test_team_ids_dict():
    #S-API-NE-76 Запрос с team_ids неверного формата (не list): "team_ids": {"id": "4ae7df2a-a5dd-4267-aaa8-093b84031883"}
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 3052,
    "project_id": "3e3028cd-3849-461b-a32b-90c0d6411dba",
    "item_type": "orgstructure",
    "item": "start_project",
     "page": 1,
     "limit": 50,
     "is_only_node": False
     })
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service TreeMicroservice returned an empty team_ids'},)

#Page
def test_page_None():
    #S-API-NE-53 Запрос со значением поля "page"=None
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":None, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_page_empty():
    #S-API-NE-54 Запрос со значением поля "page"=""
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":"", "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_page_negative():
    #S-API-NE-55 Запрос со значением поля "page"=""
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":-1, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'ensure this value is greater than or equal to 0', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 0}}]},)

def test_page_more_than_tolal():
    #S-API-NE-56 Отправка запроса со значением в поле page, превышающем поле total (ожидаемого ответа)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":100, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found on this page', 'type': 'not_found'},)

def test_page_wrong_format():
    #S-API-NE-57 Запрос с со значением поля "page" недопустимого формата
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":"one", "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'page'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_page_zero():
    #S-API-NE-57-1 Запрос со значением, выходящим за пределы допустимых граничных: page=0
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":0, "limit": 50,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': '1 validation error for RequestServiceSearchEmployees\npage\n  ensure this value is greater than or equal to 1 (type=value_error.number.not_ge; limit_value=1)'},)

#limit
def test_limit_None():
    #S-API-NE-57-3 Запрос со значением поля "limit"=None
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": None,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_limit_empty():
    #S-API-NE-57-4 Запрос со значением поля "limit"=""
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": "","is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_limit_negative():
    #S-API-NE-58 Запрос с отрицательным значением поля "limit"
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": -1,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'ensure this value is greater than or equal to 1', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 1}}]},)

def test_limit_wrong_format_str():
    #S-API-NE-59 Запрос с со значением поля "limit" недопустимого формата (str)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": "fifty","is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

def test_limit_wrong_format_float_49_9():
    #S-API-NE-60 Запрос с со значением поля "limit" недопустимого формата (float)
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": 49.9,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

def test_limit_zero():
    #S-API-NE -61 Запрос со значением, выходящим за пределы допустимых граничных: limit=0
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": 0,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'ensure this value is greater than or equal to 1', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 1}}]},)

def test_limit_51():
    #S-API-NE -62 Запрос со значением, выходящим за пределы допустимых граничных: limit=51
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": 51,"is_only_node": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'limit'], 'msg': 'ensure this value is less than or equal to 50', 'type': 'value_error.number.not_le', 'ctx': {'limit_value': 50}}]},)

#Параметр is_only_node
def test_is_only_node_None():
    #S-API-NE -63 Запрос со значением поля None
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": 50,"is_only_node": None})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'is_only_node'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

def test_is_only_node_empty():
    #S-API-NE -64 Запрос со значением поля ""
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": 50,"is_only_node": ""})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert status == ({'detail': [{'loc': ['body', 'is_only_node'], 'msg': 'value could not be parsed to a boolean', 'type': 'type_error.bool'}]},)

def test_is_only_node_wrong_format():
    #S-API-NE -65a Запрос со значением поля ""
    status, response, res_headers = nes_s.nes(wrong_url=None, wrong_headers=None,
                                                some_data={"node_id": 2919,
                                                            "project_id": project_id,
                                                            "item_type": item_type,
                                                           "item": item,
                                                            "page":1, "limit": 50,"is_only_node": "is_only_node"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'is_only_node'], 'msg': 'value could not be parsed to a boolean', 'type': 'type_error.bool'}]},)
