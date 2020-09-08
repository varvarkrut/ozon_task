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
    print(correct_response_json)
    print(response.json())
    assert (response.json() == correct_response_json), "The response is not correct"


def test_get_post_incorrect_url():
    response = requests.get(
        'https://jsonplaceholder.typicode.com/posts/3636%2')
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


def test_post_invalid_post():
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 10,
        "id": ""}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=data)
    assert (response.status_code ==
            400), f"Was recieved {response.status_code} code, while 400 expected"


def test_post_empty_post():
    data = {}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=data)
    assert (response.json() == {'id': 101}), "The response is not correct"
