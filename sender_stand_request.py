import configuration
import requests
import data

def post_new_user(): # Функция создания нового пользователя
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)

def post_new_client_kit(kit_name, auth_token): #Функция создания набора
    kit_body = data.kit_body.copy()
    kit_body["name"] = kit_name
    headers_kit = data.headers_kit.copy()
    headers_kit["Authorization"] = "Bearer "+auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)

def post_new_client_kit_empty_body(auth_token): #Функция создания набора
    kit_body = data.empty_body.copy()
    headers_kit = data.headers_kit.copy()
    headers_kit["Authorization"] = "Bearer "+auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)
