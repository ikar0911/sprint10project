import sender_stand_request
import data

def positive_assert(kit_name):
    user_response = sender_stand_request.post_new_user() #Создание пользователя
    kit_auth_token = user_response.json()["authToken"] #Передача автотокена
    kit_response = sender_stand_request.post_new_client_kit(kit_name, kit_auth_token) #Вызов функции создания набора
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name

def negative_assert_code_400(kit_name):
    user_response = sender_stand_request.post_new_user() #Создание пользователя
    kit_auth_token = user_response.json()["authToken"] #Передача автотокена
    kit_response = sender_stand_request.post_new_client_kit(kit_name, kit_auth_token) #Вызов функции создания набора
    assert kit_response.status_code == 400


def test_positive_one_letter_in_name():
    positive_assert("а")

def test_positive_511_letters_in_name():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_negative_null_letter_in_name():
    negative_assert_code_400("")

def test_negative_512_letters_in_name():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_positive_eng_letters_in_name():
    positive_assert("QWErty")

def test_positive_rus_letters_in_name():
    positive_assert("Мария")

def test_positive_symbols_in_name():
    positive_assert("№%@")

def test_positive_spaces_in_name():
    positive_assert(" Человек и КО ")

def test_positive_number_in_name():
    positive_assert("123")

def test_negative_empty_body_in_name():
    user_response = sender_stand_request.post_new_user() #Создание пользователя
    kit_auth_token = user_response.json()["authToken"] #Передача автотокена
    kit_response = sender_stand_request.post_new_client_kit_empty_body(kit_auth_token)
    assert kit_response.status_code == 400

def test_negative_type_param_name_not_string():
    negative_assert_code_400(123)

