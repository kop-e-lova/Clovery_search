import pytest
from settings import *
from Skill_search import *

#Базовый позитивный с обязательными параметрами
#S-API-Ss-01
#Pass
@pytest.mark.high
def test_skill_search_base_nesessary_fields():
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    #Проверка ожидаемой выгрузки сотрудников
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    assert list_e == ['Светлана Хохлова', 'Игорь Борисов', 'Семен Котов', 'Евгения Орлова']
    #Проверка на наличие нужных полей в ответе
    for n in response[0]['items']: assert "person_id" in n and "person_name" in n and "skills" in n
    #Проверка выгрузки навыков сотрудников и сверка их со списком навыков в запросе (list_skills_q)
    list_skills_q = ['2c901b0c-f1cb-41e9-b566-a53f1b89714f', '6796cfb9-a61c-48fd-ac9c-a395a001fad1', 'a3c1ef15-6d4f-4290-abee-62247c5465ff']
    list_skills_1 = [n['id'] for n in response[0]['items'][0]['skills']]
    list_skills_2 = [n['id'] for n in response[0]['items'][1]['skills']]
    list_skills_3 = [n['id'] for n in response[0]['items'][2]['skills']]
    list_skills_4 = [n['id'] for n in response[0]['items'][3]['skills']]
    assert list_skills_1 == list_skills_q and list_skills_2 == list_skills_q and list_skills_3 == list_skills_q and list_skills_4 == list_skills_q
    print(f'перечень навыков первого сотрудника: {list_skills_1}')
    print(f'перечень навыков второго сотрудника:{list_skills_2}')
    print(f'перечень навыков третьего сотрудника: {list_skills_3}')
    print(f'перечень навыков четвертого сотрудника: {list_skills_4}')
    #Проверка заголовков в ответе
    assert "'Content-Type': 'application/json', 'Content-Length': '2830', 'Connection': 'keep-alive'" in str(res_headers)


#Базовый позитивный со всеми опциональными параметрами
#S-API-Ss-02
@pytest.mark.high
def test_skill_search_base_optional_fields():
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data=None, some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    # Проверка ожидаемой выгрузки сотрудника
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    assert list_e == ['Игорь Борисов']
    #Проверка наличия полей ответа
    for n in response[0]['items']: assert "person_id" in n \
                                          and "person_name" in n and "skills" in n \
                                          and 'professions' in n and 'teams' in n and'assessment' in str(n['skills'])
    #Проверка перечня навыков сотрудника и сверка его со списком навыков в запросе

@pytest.mark.high
def test_ss_all_obl_one_optional():
    #S-API-Ss-03. Позитивный сценарий. Отправка запроса со всеми обязательными параметрами
    # и одним опциональным параметром profession_ids (в списке 1 profession_id)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ["bf603256-78ff-46c4-8eb3-43f1bb4b7175"],
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0,"assessment_to": 0.99}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    ex_list = ['Евгения Лязникова', 'Семен Котов']
    print(list_e)
    assert list_e == ex_list

@pytest.mark.high
def test_ss_all_obl_one_optional_several_profession():
    #S-API-Ss-04. Позитивный сценарий. Отправка запроса со всеми обязательными параметрами
    # и одним опциональным параметром profession_ids (в списке несколько profession_id)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ["3a4651a7-8bf0-4855-875b-5ff04e3fdf85",
                                                                              "bf603256-78ff-46c4-8eb3-43f1bb4b7175"],
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0,"assessment_to": 0.99}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Георгий Исаенко', 'Мария Недочетова', 'Евгения Лязникова', 'Семен Котов', 'Иван Афонин', 'Алексей Лыжин', 'Валерия Садчикова', 'Игорь Борисов']
    assert list_e == ex_list

@pytest.mark.high
def test_ss_all_obl_one_optional_team_ids_one_team_id():
    #S-API-Ss-05. Позитивный сценарий. Отправка запроса со всеми обязательными параметрами
    # и одним опциональным параметром team_ids (в списке 1 team_id)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d",
                                                                       "assessment_from": 0,"assessment_to": 0.99}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Алексей Лыжин', 'Евгения Лязникова', 'Иван Афонин', 'Мария Недочетова', 'Валерия Садчикова']
    assert list_e == ex_list

@pytest.mark.high
def test_ss_all_obl_one_optional_team_ids_several_team_ids():
    #S-API-Ss-06. Позитивный сценарий. Отправка запроса со всеми обязательными параметрами и одним
    # опциональным параметром team_ids (в списке несколько team_id)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                        "23a4363f-28d0-43e2-b66e-f2aedd4175ae"],
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d",
                                                                       "assessment_from": 0,"assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Алексей Лыжин', 'Светлана Хохлова', 'Евгения Орлова', 'Игорь Борисов', 'Евгения Лязникова', 'Мария Недочетова', 'Иван Афонин', 'Валерия Садчикова']
    assert list_e == ex_list


@pytest.mark.high
#@pytest.mark.skip
def test_ss_all_obl_one_optional_full_match_of_skills():
    #S-API-Ss-07. Позитивный сценарий. Отправка запроса со всеми обязательными параметрами и опциональным параметром
    # "full_match_of_skills": False. Без опциональных параметров profession_ids, team_ids, assessment_from, assessment_to
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "ab12549c-a157-4790-9ff0-83edbfd22a10"},
                                                                      {"skill_id": "a2a2a3ff-64cf-49b4-a44b-7e957dd5a41c"},
                                                                      {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "full_match_of_skills": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    #ex_list =
    #assert list_e == ex_list

@pytest.mark.high
#@pytest.mark.skip
def test_obligatory_and_optional_field_match_false():
    #S-API-Ss-08. Позитивный сценарий. Отправка запроса со всеми обязательными параметрами,
    # опциональными параметрами profession_ids, team_ids, assessment_from > 0, assessment_to < 1,
    # и опциональным параметром "full_match_of_skills": False
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ["3a4651a7-8bf0-4855-875b-5ff04e3fdf85"],
                                                           "team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                           "skills": [{"skill_id": "ab12549c-a157-4790-9ff0-83edbfd22a10",
                                                                       "assessment_from": 0,"assessment_to": 0.99},
                                                                      {"skill_id": "a2a2a3ff-64cf-49b4-a44b-7e957dd5a41c",
                                                                       "assessment_from": 0,"assessment_to": 0.99},
                                                                      {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1",
                                                                       "assessment_from": 0,"assessment_to": 0.99}],
                                                           "full_match_of_skills": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)

@pytest.mark.high
#@pytest.mark.skip
def test_obligatory_and_1_skill():
    #S-API-Ss-09. Отправка запроса со всеми обязательными параметрами, 1 навыком в поле skills
    # и опциональным параметром "full_match_of_skills": False
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "ab12549c-a157-4790-9ff0-83edbfd22a10",
                                                                       "assessment_from": 0,"assessment_to": 0.99}],
                                                           "full_match_of_skills": False})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Георгий Исаенко', 'Алексей Лыжин', 'Иван Афонин', 'Мария Недочетова', 'Семен Котов', 'Евгения Лязникова', 'Валерия Садчикова', 'Игорь Борисов']
    assert list_e == ex_list

@pytest.mark.medium
def test_skills_10():
    #S-API-Ss-10. Проверка граничных значений. Отправка запроса с параметрами: skills=10, assessment_from = 0, assessment_to = 1,
    # при этом skills соответствуют тестовым сотрудникам, assessment_from <= assessment тестовых сотрудников <= assessment_to.
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "ab12549c-a157-4790-9ff0-83edbfd22a10",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "a2a2a3ff-64cf-49b4-a44b-7e957dd5a41c",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "346b8edd-7e1b-4f9a-9787-76784a74884c",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "3044b169-6f04-47c6-9125-bea97f948fad",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "3fe2b72b-4cd3-4253-9e2e-c785d8cdeb95",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "aba23aa3-7b58-4b2d-b597-ab653b858de3",
                                                                       "assessment_from": 0,"assessment_to": 1},
                                                                      {"skill_id": "87251960-ab8d-4585-a45d-ab5b3f1fe250",
                                                                       "assessment_from": 0,"assessment_to": 1}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Георгий Исаенко', 'Алексей Лыжин', 'Мария Недочетова', 'Иван Афонин', 'Евгения Лязникова', 'Семен Котов', 'Валерия Садчикова', 'Игорь Борисов']
    assert list_e == ex_list

@pytest.mark.medium
def test_assessment_from_0_01_and_assessment_to_0_99():
    #S-API-Ss-11. Проверка граничных значений. Отправка запроса с обязательными параметрами
    # и assessment_from = 0.01, assessment_to = 0.99
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f",
                                                                       "assessment_from": 0.01,"assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Светлана Хохлова', 'Игорь Борисов', 'Семен Котов']
    assert list_e == ex_list

@pytest.mark.high
def test_1_skill_assessment_from_0_98():
    #S-API-Ss-12. Проверка граничных значений. Отправка запроса с обязательными параметрами:
    # 1 навыком в поле skills и assessment_from = assessment тестового сотрудника
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f",
                                                                       "assessment_from": 0.98}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Светлана Хохлова']
    assert list_e == ex_list

@pytest.mark.high
def test_1_skill_assessment_to_0_36():
    #S-API-Ss-13. Проверка граничных значений. Отправка запроса с обязательными параметрами:
    # 1 навыком в поле skills и assessment_to = assessment тестового сотрудника
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f",
                                                                       "assessment_to": 0.36}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Игорь Борисов', 'Семен Котов', 'Евгения Орлова']
    assert list_e == ex_list

@pytest.mark.high
def test_obl_fields_page_0_limit_50():
    #S-API-Ss-14. Отправка запроса с обязательными параметрами в установленных пределах
    # и параметрами в Query params: page = 0, limit = 50
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 0, "limit": 50},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Светлана Хохлова', 'Семен Котов', 'Игорь Борисов', 'Евгения Орлова']
    assert list_e == ex_list

@pytest.mark.high
def test_obl_fields_page_2_limit_49():
    #S-API-Ss-15. Отправка запроса с обязательными параметрами в установленных пределах
    # и параметрами в Query params: page = 2, limit = 49
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 2, "limit": 49},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found on this page', 'type': 'not_found'},)

@pytest.mark.high
def test_obl_fields_page_1_limit_5():
    #S-API-Ss-16. Отправка запроса с обязательными параметрами в установленных пределах
    # и параметрами в Query params: page = 1, limit = 5
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 1, "limit": 5},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Иван Афонин', 'Евгения Орлова', 'Светлана Хохлова', 'Игорь Борисов', 'Валерия Садчикова']
    assert list_e == ex_list

@pytest.mark.high
def test_obl_fields_page_4_limit_1():
    #S-API-Ss-17. Отправка запроса с обязательными параметрами в установленных пределах
    # и параметрами в Query params: page = 4, limit = 1
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 4, "limit": 1},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Евгения Лязникова']
    assert list_e == ex_list

@pytest.mark.high
def test_ss_upper_headers():
    #S-API-Ss-18. Отправка запроса с заголовками в верхем регистре
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers={'CONTENT-TYPE': 'APPLICATION/JSON',
                                                                             'ACCEPT': 'APPLICATION/JSON'},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Семен Котов', 'Светлана Хохлова', 'Игорь Борисов', 'Евгения Орлова']
    assert list_e == ex_list

@pytest.mark.high
def test_ss_mixed_headers():
    #S-API-Ss-19. Отправка запроса с заголовками в смешанном регистре
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers={'CONTENT-TYPE': 'application/json',
                                                                             'accept': 'APPLICATION/JSON'},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Семен Котов', 'Светлана Хохлова', 'Игорь Борисов', 'Евгения Орлова']
    assert list_e == ex_list

@pytest.mark.high
def test_ss_upper_url():
    #S-API-Ss-20. Отправка запроса с URL в верхнем регистре
    status, response, res_headers = skill_s.ssn(some_url="https://SEARCH.CORP.CLOVERI.com/api/search", some_headers=None,
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Семен Котов', 'Светлана Хохлова', 'Игорь Борисов', 'Евгения Орлова']
    assert list_e == ex_list

@pytest.mark.medium
def test_CORS_protocol():
    #S-API-Ss-21. Проверка на допустимость запроса OPTION для выполнения
# CORS protocol (отправка OPTION запроса с заголовками Access-Control-Request-Headers: authorization, content-type,
    # Access-Control-Request-Method: POST, Accept: */*, Origin: https://corp.cloveri.com)
    status, response, res_headers = skill_s.ssn(some_url="https://SEARCH.CORP.CLOVERI.com/api/search",
                                                some_headers={"Content-type": "application/json",
                                                              "Access-Control-Request-Headers": "authorization, content-type",
                                                              "Access-Control-Request-Method": "POST",
                                                              "Accept": "*/*",
                                                              "Origin": "https://corp.cloveri.com"},
                                                              some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Семен Котов', 'Светлана Хохлова', 'Игорь Борисов', 'Евгения Орлова']
    assert list_e == ex_list

@pytest.mark.medium
def test_ss_empty_list_in_professions():
    #S-API-Ss-92. Отправка запроса с пустым списком в поле profession_ids
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "profession_ids": [],
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    print(list_e)
    ex_list = ['Семен Котов', 'Светлана Хохлова', 'Игорь Борисов', 'Евгения Орлова']
    assert list_e == ex_list

#НЕГАТИВНЫЕ ТЕСТЫ

#НЕВЕРНОЕ ПОСТРОЕНИЕ ЗАПРОСА

#Запрос неверным методом
#S-API-Ss-22
@pytest.mark.medium
def test_skill_search_wrong_method():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {'page': 0, 'limit': 50}
    data = {
            "company_id": "b2aa983a-b49f-4e1a-b1dd-761be7588887",
            "profession_ids": ["c017cc4a-b91f-446d-bc8a-83b25fe39fe6"],
            "team_ids": [
                    "1bff37e4-6033-4563-9e49-35ecc7409eb0",
                    "db3ea579-79e1-4017-9c91-434fb0598eda"
            ],
            "skills": [
                    {
                        "skill_id": "f939b375-c183-4669-9586-7824190e5bef",
                        "assessment_from": 0,
                        "assessment_to": 0.9
                    }
                ]
            }
    res = requests.get(url=url_skill_search, headers=headers, params=params, json=data)
    status = res.status_code
    res_headers = res.headers
    try:
        response = res.json(),
    except json.decoder.JSONDecodeError:
        response = res.text
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status != 201
    assert status == 405
    assert "'person_id': " not in str(response[0])

    res = requests.patch(url=url_skill_search, headers=headers, params=params, json=data)
    status = res.status_code
    res_headers = res.headers
    try:
        response = res.json(),
    except json.decoder.JSONDecodeError:
        response = res.text
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status != 201
    assert status == 405
    assert "'person_id': " not in str(response[0])
    
    res = requests.put(url=url_skill_search, headers=headers, params=params, json=data)
    status = res.status_code
    res_headers = res.headers
    try:
        response = res.json(),
    except json.decoder.JSONDecodeError:
        response = res.text
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status != 201
    assert status == 405
    assert "'person_id': " not in str(response[0])
    
    res = requests.delete(url=url_skill_search, headers=headers, params=params, json=data)
    status = res.status_code
    res_headers = res.headers
    try:
        response = res.json(),
    except json.decoder.JSONDecodeError:
        response = res.text
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status != 201
    assert status == 405
    assert "'person_id': " not in str(response[0])

# Запросы с с неверным url и эндпоинтом
# #S-API-Ss-23,24
#Неверный url
@pytest.mark.medium
@pytest.mark.parametrize("urls", ["https://corp.cloveri.com/api/search",
                                  "https://search.corp.cloveri.com/api/skill"],
                         ids=['wrong url', 'wrong endpoint'])
def test_search_skills_wrong_urls(urls):
    status, response, res_headers = skill_s.ssn(some_url=urls, some_headers=None,
                                                    some_data=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status != 201
    assert status == 404 or status == 405
    assert "'id': " not in str(response[0])
    #assert "'Content-Type': 'text/html'" in str(res_headers) or "'Content-Type': 'text/html; charset=utf-8'" \
           #in str(res_headers)

@pytest.mark.high
def test_ss_wrong_content_type():
    #S-API-Ss-25. Попытка запроса с неверным типом данных в Headers (Content-Type, Accept)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers={"Accept": "application/json",
                                                                             "Content-Type": "text/css"},
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body'], 'msg': 'value is not a valid dict', 'type': 'type_error.dict'}]},)

@pytest.mark.medium
def test_ss_no_headers():
    #S-API-Ss-26. Попытка запроса с неверным типом данных в Headers (Content-Type, Accept)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers={},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200
    if status == 422:
        assert response == ({'detail': [{'loc': ['body'], 'msg': 'value is not a valid dict', 'type': 'type_error.dict'}]},)

@pytest.mark.medium
def test_body_text():
    #S-API-Ss-27. Попытка запроса с телом в формате text
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data=str({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body'], 'msg': 'value is not a valid dict', 'type': 'type_error.dict'}]},)

@pytest.mark.high
def test_wrong_field_skill():
    #S-API-Ss-28. Попытка запроса с отправкой в теле существующего поля с ошибкой (skill)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers={},
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skill": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.high
def test_wrong_field_skill():
    #S-API-Ss-29. Попытка запроса с отправкой в теле непредусмотренного поля (new_field)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers={},
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "new_field": "new_value"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

@pytest.mark.medium
def test_wrong_protocol():
    #S-API-Ss-30. Попытка запроса с неверным типом протокола http вместо https
    status, response, res_headers = skill_s.ssn(some_url="http://search.corp.cloveri.com/api/search", some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 404

@pytest.mark.medium
def test_double_fields_same_values():
    #S-API-Ss-31. Попытка отправки запроса с дублированием обязательных полей c одинаковыми значениями
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

@pytest.mark.medium
def test_double_fields_different_values():
    #S-API-Ss-32. Попытка отправки запроса с дублированием обязательных полей c одинаковыми значениями
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "company_id": "4b871f91-45aa-4a72-8cb5-417ef561307fg",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad2"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404 or status == 422 or status == 200
    if status == 422:
        assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

@pytest.mark.medium
def test_upper_fields_():
    #S-API-Ss-33-a. Попытка отправки запроса с дублированием обязательных полей c одинаковыми значениями
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"COMPANY_ID": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "SKILLS": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'skills'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.medium
def test_upper_skill_id_():
    #S-API-Ss-33-b. Отправка запроса с ключами обязательного поля skill_id в поле skills в верхем регистре
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"SKIL_ID": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.medium
def test_ss_no_body_empty_dict():
    #S-API-Ss-34-a. Отправка запроса без тела (один из вариантов - тело - пустой dict)
    #Вставить в чеклист этот кейс
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['body', 'skills'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.medium
def test_ss_no_body():
    # S-API-Ss-34. Отправка запроса без тела
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    res = requests.post(url=url_skill_search, headers=headers)
    status = res.status_code
    res_headers = res.headers
    try:
        response = res.json(),
    except json.decoder.JSONDecodeError:
        response = res.text
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

#Проверки на параметр запроса в Query params - page

@pytest.mark.medium
def test_page_wrong_format():
    #S-API-Ss-35. Попытка запроса с неверным форматом данных
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": "page_1", "limit": 5},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['query', 'page'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

@pytest.mark.medium
def test_page_empty():
    #S-API-Ss-36. Попытка запроса с пустым значением page
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": "", "limit": 5},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['query', 'page'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

@pytest.mark.medium
def test_page_negative():
    #S-API-Ss-37. Попытка запроса с отрицательным значением page
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": -1, "limit": 5},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['query', 'page'], 'msg': 'ensure this value is greater than or equal to 0', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 0}}]},)

@pytest.mark.high
def test_page_more_than_total():
    #S-API-Ss-38. Отправка запроса со значением в поле page, превышающем поле total (ожидаемого ответа)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 100, "limit": 5},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found on this page', 'type': 'not_found'},)

#проверки на параметр запроса в Query params - limit

@pytest.mark.high
def test_page_more_than_total():
    #S-API-Ss-38. Отправка запроса со значением в поле page, превышающем поле total (ожидаемого ответа)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 100, "limit": 5},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404

@pytest.mark.medium
def test_limit_wrong_format():
    #S-API-Ss-39. Попытка запроса с неверным форматом данных
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 0, "limit": "limit_5"},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['query', 'limit'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

@pytest.mark.medium
def test_limit_empty():
    #S-API-Ss-40. Попытка запроса с пустым значением
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 0, "limit": ""},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['query', 'limit'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]},)

@pytest.mark.medium
def test_limit_negative():
    #S-API-Ss-41. Попытка запроса с отрицательным значением
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 0, "limit": -1},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['query', 'limit'], 'msg': 'ensure this value is greater than or equal to 1', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 1}}]},)

@pytest.mark.medium
def test_limit_zero():
    #S-API-Ss-42. Проверка граничных значений. Попытка запроса со значением 0
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 0, "limit": 0},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['query', 'limit'], 'msg': 'ensure this value is greater than or equal to 1', 'type': 'value_error.number.not_ge', 'ctx': {'limit_value': 1}}]},)

@pytest.mark.medium
def test_limit_51():
    #S-API-Ss-43. Проверка граничных значений. Попытка запроса со значением 51
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 0, "limit": 51},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['query', 'limit'], 'msg': 'ensure this value is less than or equal to 50', 'type': 'value_error.number.not_le', 'ctx': {'limit_value': 50}}]},)

#проверки на параметр company_id в теле запроса
@pytest.mark.medium
def test_company_id_wrong_format():
    #S-API-Ss-44. Попытка запроса с неверным форматом данных (не UUID)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "company_id",
                                                            "skills": [{"skil_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}, {'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.high
def test_company_id_non_existant():
    #S-API-Ss-45. Попытка запроса с указанием несуществующего в БД значения company_id (корректный, но несуществующий UUID)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "00071f91-45aa-4a72-8cb5-417ef5613000",
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

@pytest.mark.high
def test_company_id_another():
    #S-API-Ss-46. Отправка запроса, в котором skills соответствуют тестовым сотрудникам, а company_id не соответствует
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef5613088",
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

@pytest.mark.medium
def test_company_incorrect():
    #S-API-Ss-47. Попытка запроса с указанием некорректного UUID (int вместо UUID), если поставить другой UUID,
    # то тест будет дублировать S-API-Ss-46 и код ответа будет 404
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": 123,
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

@pytest.mark.medium
def test_company_id_empty():
    #S-API-Ss-48. Попытка запроса с пустым значением
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "",
                                                            "skills": [{"skil_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}, {'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.medium
def test_company_id_None():
    #S-API-Ss-49. Попытка запроса с None значением company_id
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": None,
                                                            "skills": [{"skil_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}, {'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.high
def test_without_company_id():
    #S-API-Ss-50. Попытка запроса без поля company_id
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

#проверки на параметр skills в теле запроса

@pytest.mark.medium
def test_skills_wrong_format_dict():
    #S-API-Ss-51. Попытка запроса с неверным форматом данных (dict)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": {"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.medium
def test_skills_wrong_format_str():
    #S-API-Ss-51-1. Попытка запроса с неверным форматом данных (dict)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": str({"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"})})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.medium
def test_skills_empty_value():
    #S-API-Ss-52. Попытка запроса с пустым значением
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": ""}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

@pytest.mark.medium
def test_skills_None_value():
    #S-API-Ss-53. Попытка запроса с со значением None
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": None}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

@pytest.mark.high
def test_without_skills_field():
    #S-API-Ss-54. Попытка запроса без поля skills
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.high
def test_skills_empty_list():
    #S-API-Ss-55. Попытка запроса с пустым списком
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": []})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'At least one skill must be provided', 'type': 'value_error'}]},)

@pytest.mark.high
def test_skills_11_skils_in_list():
    #S-API-Ss-56. Проверка граничных значений. Попытка запроса с 11 навыками в списке в поле
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'Max 10 skills can be specified', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_skills_extra_field_in_list():
    #S-API-Ss-57. Попытка запроса с отправкой в поле skills непредусмотренного поля (skill_name)- в списке
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                                       {"skill_name": "developer"}]})

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 1, 'skill_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.medium
def test_skills_extra_field_in_dict():
    #S-API-Ss-57-1. Попытка запроса с отправкой в поле skills непредусмотренного поля (skill_name)- в словаре
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1",
                                                                        "skill_name": "developer"}]})

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422 or status == 200

@pytest.mark.high
def test_skill_id_and_assessment_in_body():
    #S-API-Ss-58. Попытка запроса с отправкой полей skill_id,
    # assessment_from, assessment_to  не в списке в поле skills, а напрямую в теле запроса
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1",
                                                           "assessment_from": 0.01, "assessment_to": 0.99})

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

#проверки на параметр skill_id  в теле запроса

@pytest.mark.medium
def test_wrong_format_skill_id():
    #S-API-Ss-59. Попытка запроса с неверным форматом данных (не UUID)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "123"}]})

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

@pytest.mark.high
def test_another_skill_id():
    #S-API-Ss-60. Попытка запроса с указанием несуществующего в БД значения skill_id (корректный, но несуществующий UUID)
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "0006cfb9-a61c-48fd-ac9c-a395a001f000"}]})

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

@pytest.mark.high
def test_not_matching_skill_id():
    #S-API-Ss-61. Отправка запроса, в котором company_id соответствует тестовым сотрудникам, а skill_id не соответствует
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9206451b-6bea-4f5a-904d-69d655f98e88"}]})

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

@pytest.mark.medium
def test_incorrect_skill_id():
    #S-API-Ss-62. Попытка запроса с указанием некорректного UUID
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9206451b6bea4f5a904d69d"}]})

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

@pytest.mark.medium
def test_empty_skill_id():
    #S-API-Ss-63. Попытка запроса с указанием пустого skill_id
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": ""}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

@pytest.mark.medium
def test_None_skill_id():
    #S-API-Ss-64. Попытка запроса с указанием None skill_id
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": None}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

@pytest.mark.high
def test_without_skill_id_with_assessment():
    #S-API-Ss-65. Попытка запроса без skill_id c asessment
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"assessment_from": 0.01, "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'skill_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.high
def test_without_skill_id_without_assessment():
    #S-API-Ss-65-1. Попытка запроса без skill_id без asessment
    #Добавить в чеклист
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                      "skills": []})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'At least one skill must be provided', 'type': 'value_error'}]},)

@pytest.mark.high
@pytest.mark.skip
def test_no_matching_skills():
    #S-API-Ss-65-121. Отправка запроса, в котором company_id соответствует тестовым сотрудникам, в skills
    # передается несколько навыков, при этом такого сочетания всех сразу навыков нет ни у одного тестового сотрудника
    #??? возвращает код 200
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "a3c1ef15-6d4f-4290-abee-62247c5465ff"},
                                                                      {"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f"},
                                                                      {"skill_id": "9206451b-6bea-4f5a-904d-69d655f98e36"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

#проверки на параметр assessment_from в теле запроса

@pytest.mark.medium
def test_assessment_from_wrong_format():
    #S-API-Ss-66. Попытка запроса с неверным форматом данных (str)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": "some_value",
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'value is not a valid float', 'type': 'type_error.float'}]},)

@pytest.mark.medium
def test_assessment_from_int():
    #S-API-Ss-67. Попытка запроса с неверным форматом данных (количество процентов(?), int)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 5,
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'assessment_from must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_from_empty():
    #S-API-Ss-68. Попытка запроса с пустым значением
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": "",
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'value is not a valid float', 'type': 'type_error.float'}]},)

@pytest.mark.medium
def test_assessment_from_None():
    #S-API-Ss-69. Попытка запроса с None значением a
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": None,
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({"detail":[{"loc":["body","skills",0,"assessment_from"],
                                    "msg":"none is not an allowed value","type":"type_error.none.not_allowed"}]}) \
           or response == ({"detail":[{"loc":["body","skills",0,"assessment_from"],
                                       "msg":"value is not a valid float","type":"type_error.float"}]})

@pytest.mark.medium
def test_assessment_from_negative():
    #S-API-Ss-71. Попытка запроса с негативным  значением assessment from
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": -0.01,
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'assessment_from must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_from_1_01():
    #S-API-Ss-72. Попытка запроса с 1.01  значением assessment from
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 1.01,
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [
        {'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'assessment_from must be a number between 0 and 1',
         'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_from_neg_0_009():
    #S-API-Ss-73. Проверка разрядности граничных значений. Попытка запроса со значением -0,009
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": -0.009,
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'assessment_from must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_from_1_009():
    #S-API-Ss-74. Проверка разрядности граничных значений. Попытка запроса со значением 1,009
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 1.009,
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'assessment_from must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_from_neg_0_001():
    #S-API-Ss-75. Проверка разрядности граничных значений. Попытка запроса со значением -0.001
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": -0.001,
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'assessment_from must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_from_1_001():
    #S-API-Ss-76. Проверка разрядности граничных значений. Попытка запроса со значением 1,001
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 1.001,
                                                                       "assessment_to": 0.99}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_from'], 'msg': 'assessment_from must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.high
def test_assessment_from_more_employee():
    #S-API-Ss-77. Проверка граничных значений. Отправка запроса с assessment_from > assessment тестового сотрудника
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9206451b-6bea-4f5a-904d-69d655f98e36",
                                                                       "assessment_from": 0.88}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

def test_assessment_from_0_871():
    #S-API-Ss-119. Отправка запроса с 3 знаками после запятой в значении assessment_from, при этом значение
    # assessment_from становится больше чем assessment тестового сотрудника. Проверка округления/не округления значений поля
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9206451b-6bea-4f5a-904d-69d655f98e36",
                                                                       "assessment_from": 0.871}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

#проверки на параметр assessment_to в теле запроса

@pytest.mark.medium
def test_assessment_to_wrong_format():
    #S-API-Ss-78. Попытка запроса с неверным форматом данных (str)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": "some_value"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response ==({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'value is not a valid float', 'type': 'type_error.float'}]},)

@pytest.mark.medium
def test_assessment_to_int():
    #S-API-Ss-79. Попытка запроса с неверным форматом данных (количество процентов(?), int)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": 5}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'assessment_to must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_to_empty():
    #S-API-Ss-80. Попытка запроса с пустым значением
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": ""}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'value is not a valid float', 'type': 'type_error.float'}]},)

@pytest.mark.medium
def test_assessment_to_None():
    #S-API-Ss-81. Попытка запроса с None значением
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": None}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({"detail": [{"loc": ["body", "skills", 0, "assessment_to"],
                                     "msg": "none is not an allowed value", "type": "type_error.none.not_allowed"}]}) \
           or response == ({"detail": [{"loc": ["body", "skills", 0, "assessment_to"],
                                        "msg": "value is not a valid float", "type": "type_error.float"}]})

@pytest.mark.medium
def test_assessment_to_negative():
    #S-API-Ss-83. Попытка запроса с негативным  значением assessment_to
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": -0.1}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'assessment_to must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_to_1_01():
    #S-API-Ss-84. Попытка запроса с 1.01  значением assessment from
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": 1.01}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'assessment_to must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_to_neg_0_009():
    #S-API-Ss-85. Проверка разрядности граничных значений. Попытка запроса со значением -0,009
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": -0.009}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'assessment_to must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_to_1_009():
    #S-API-Ss-86. Проверка разрядности граничных значений. Попытка запроса со значением 1,009
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": 1.009}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'assessment_to must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_to_neg_0_001():
    #S-API-Ss-87. Проверка разрядности граничных значений. Попытка запроса со значением -0.001
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": -0.001}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'assessment_to must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_assessment_to_1_001():
    #S-API-Ss-88. Проверка разрядности граничных значений. Попытка запроса со значением 1,001
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0.1,
                                                                       "assessment_to": 1.001}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills', 0, 'assessment_to'], 'msg': 'assessment_to must be a number between 0 and 1', 'type': 'value_error'}]},)

@pytest.mark.high
def test_assessment_to_less_employee():
    #S-API-Ss-89. Проверка граничных значений. Отправка запроса с assessment_to < assessment тестового сотрудника
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "19265e47-a076-4527-8abe-84230d5c2bec",
                                                                       "assessment_to": 0.10}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

def test_assessment_to_0_109():
    #S-API-Ss-120. Отправка запроса с 3 знаками после запятой в значении assessment_to, при этом значение
    # assessment_to становится меньше чем assessment тестового сотрудника. Проверка округления/не округления значений поля
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "19265e47-a076-4527-8abe-84230d5c2bec",
                                                                       "assessment_to": 0.109}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

#проверки на опциональный параметр profession_ids в теле запроса

@pytest.mark.medium
def test_profession_ids_wrong_format_tuple():
    #S-API-Ss-90. Попытка запроса с неверным форматом данных (tuple)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ("bf603256-78ff-46c4-8eb3-43f1bb4b7175"),
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c",
                                                                       "assessment_from": 0,"assessment_to": 0.99}]},
                                                some_params= None)

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'profession_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.medium
def test_profession_ids_wrong_format_dict():
    #S-API-Ss-90-1. Попытка запроса с неверным форматом данных (tuple)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": {"ids": "bf603256-78ff-46c4-8eb3-43f1bb4b7175"},
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c"}]},
                                                some_params= None)

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'profession_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.medium
def test_profession_ids_wrong_format_not_UUID():
    #S-API-Ss-91. Попытка запроса с неверным форматом данных (tuple)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ["123"],
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c"}]},
                                                some_params= None)

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'profession_ids', 0], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

@pytest.mark.medium
def test_profession_ids_empty():
    #S-API-Ss-93. Попытка запроса с пустым значением в списке
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": [""],
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c"}]},
                                                some_params= None)

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'profession_ids', 0], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

@pytest.mark.medium
def test_profession_ids_None():
    #S-API-Ss-94. Попытка запроса с None значением в списке
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": [None],
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c"}]},
                                                some_params= None)

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'profession_ids', 0], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

@pytest.mark.medium
def test_profession_ids_None():
    #S-API-Ss-95. Попытка запроса с указанием profession_id не в списке, а сразу под ключом поля profession_ids
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": "bf603256-78ff-46c4-8eb3-43f1bb4b7175",
                                                           "skills": [{"skill_id": "9fc08ce1-d22f-4ab9-8413-4100c2d03a7c"}]},
                                                some_params= None)

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'profession_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.high
def test_profession_ids_non_existant():
    #S-API-Ss-97. Попытка запроса с указанием несуществующих в БД значений profession_id в списке (корректные, но несуществующие UUID)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ["0008af9c-22d8-4bc6-a598-cb3ad035c000"],
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]},
                                                some_params= None)

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

@pytest.mark.high
def test_profession_ids_non_matching():
    #S-API-Ss-98. Отправка запроса, в котором обязательные параметры соответствуют тестовым сотрудникам,
    # а profession_id в списке в поле не соответствуют тестовым сотрудникам
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ["3a4651a7-8bf0-4855-875b-5ff04e3fdf85"],
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]},
                                                some_params= None)

    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404

#проверки на опциональный параметр team_ids в теле запроса

@pytest.mark.medium
def test_team_ids_wrong_format_tuple():
    #S-API-Ss-99. Попытка запроса с неверным форматом данных (tuple)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": ("4ae7df2a-a5dd-4267-aaa8-093b84031883"),
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.medium
def test_team_ids_wrong_format_dict():
    #S-API-Ss-99-1. Попытка запроса с неверным форматом данных (dict)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": {"ids": "4ae7df2a-a5dd-4267-aaa8-093b84031883"},
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.medium
def test_team_ids_ids_not_UUID():
    #S-API-Ss-100. Попытка запроса с неверным форматом team_id в списке в поле (не UUID в списке)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": [123],
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids', 0], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)


@pytest.mark.medium
def test_team_ids_empty_list():
    #S-API-Ss-101. Попытка запроса с пустым списком
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": [],
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'At least one team ID must be provided', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_team_ids_empty_value_in_list():
    #S-API-Ss-102. Попытка запроса с пустым значением в списке
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": [""],
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids', 0], 'msg': 'value is not a valid uuid', 'type': 'type_error.uuid'}]},)

@pytest.mark.medium
def test_team_ids_None_value_in_list():
    #S-API-Ss-103-a. Попытка запроса с None значением в списке
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": [None],
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids', 0], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]},)

@pytest.mark.medium
def test_team_ids_None_value_without_list():
    #S-API-Ss-103-b. Попытка запроса с None значением без списка
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": None,
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'At least one team ID must be provided', 'type': 'value_error'}]},)

@pytest.mark.medium
def test_team_ids_value_without_list():
    #S-API-Ss-104. Попытка запроса с указанием team_id не в списке, а сразу под ключом поля team_ids
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": "4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                           "skills": [{"skill_id": "ebb6f416-39dc-4faf-981b-86642deaa54d"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'value is not a valid list', 'type': 'type_error.list'}]},)

@pytest.mark.high
def test_team_ids_non_existing_UUID():
    #S-API-Ss-106. Попытка запроса с указанием несуществующих в БД значений team_id
    # в списке (корректные, но несуществующие UUID)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": ["0007df2a-a5dd-4267-aaa8-093b84031000"],
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

@pytest.mark.high
def test_team_ids_not_matching_UUID():
    #S-API-Ss-107. Отправка запроса, в котором обязательные параметры соответствуют тестовым сотрудникам,
    # а team_id в списке в поле не соответствуют тестовым сотрудникам
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)

#проверки на опциональный параметр
# соответствия хотя бы 1 навыку/соответствия всем выбранным навыкам в теле запроса ("full_match_of_skills")

@pytest.mark.medium
def test_full_match_of_skills_str():
    #S-API-Ss-121. Попытка запроса с неверным форматом данных (int)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "full_match_of_skills": "abc"},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'value is not a boolean', 'type': 'type_error'}]},)

@pytest.mark.medium
def test_full_match_of_skills_int():
    #S-API-Ss-121-1. Попытка запроса с неверным форматом данных (int)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "full_match_of_skills": 123},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'team_ids'], 'msg': 'value is not a boolean', 'type': 'type_error'}]},)

@pytest.mark.medium
def test_full_match_of_skills_empty():
    #S-API-Ss-122. Попытка запроса с пустым значением
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "full_match_of_skills": ""},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

@pytest.mark.medium
def test_full_match_of_skills_None():
    #S-API-Ss-123. Попытка запроса с со значением None
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "full_match_of_skills": None},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

@pytest.mark.medium
def test_full_match_of_skills_Yes():
    #S-API-Ss-124. Попытка запроса с со значением Yes
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}],
                                                           "full_match_of_skills": "Yes"},
                                                some_params= None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422

#проверки на перемену местами параметров
@pytest.mark.min
def test_company_id_in_query_params():
    #S-API-Ss-110. Попытка запроса с указанием поля company_id не в теле запроса, а в Query Params
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]},
                                                some_params={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f"})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.min
def test_company_id_in_headers():
    #S-API-Ss-111. Попытка запроса с указанием поля company_id не в теле запроса, а в headers
    status, response, res_headers = skill_s.sso(some_url=None,
                                                some_headers={"Content-type": "Application/json",
                                                              "Accept": "application/json",
                                                              "company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f"},
                                                some_data={"skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]},
                                                some_params=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'company_id'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.min
def test_skills_in_query_params():
    #S-API-Ss-112. Попытка запроса с указанием поля company_id не в теле запроса, а в Query Params
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f"},
                                                some_params={"skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]})
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'field required', 'type': 'value_error.missing'}]},)

@pytest.mark.min
def test_skills_in_headers():
    #S-API-Ss-113. Попытка запроса с указанием поля company_id не в теле запроса, а в Query Params
    status, response, res_headers = skill_s.sso(some_url=None,
                                                some_headers={"Content-type": "Application/json",
                                                              "Accept": "application/json",
                                                              "skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f"},
                                                some_params=None)
    print(f"\nCode: {status}")
    print(f"Response: {response}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert response == ({'detail': [{'loc': ['body', 'skills'], 'msg': 'field required', 'type': 'value_error.missing'}]},)