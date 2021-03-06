import requests
import json


def test_get_post():
    json_correct_string = r"""
    {"userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}
    """
    correct_response_json = json.loads(json_correct_string)
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert (response.json() == correct_response_json), "The response is not correct"


def test_get_post_with_incorrect_url():
    response = requests.get(
        'https://jsonplaceholder.typicode.com/posts/3636%2',headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36'})
    assert (response.status_code == 404), "The response is not correct"


def test_get_null_post():
    json_correct_string = r"""
    {}
    """
    correct_response_json = json.loads(json_correct_string)
    response = requests.get('https://jsonplaceholder.typicode.com/posts/0')
    assert (response.json() == correct_response_json), "The response is not correct"


def test_post_valid_post():
    data = {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=data)
    assert (response.json() == data), "The response is not correct"


def test_post_with_invalid_id_field():
    data = {
        "title": "",
        "body": "bar",
        "userId": 10,
        "id": -1}
    correct_response = {
        "title": "",
        "body": "bar",
        "userId": 10,
        "id": 101
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=data)
    print(response.json())
    assert (response.json() ==
            correct_response), f"The response is not correct"


def test_post_empty_post():
    data = {}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=data)
    assert (response.json() == {'id': 101}), "The response is not correct"
