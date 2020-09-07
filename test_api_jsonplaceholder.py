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


def test_get_comment():
    json_correct_string = r"""
    {"postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"}
    """
    correct_response_json = json.loads(json_correct_string)
    response = requests.get('https://jsonplaceholder.typicode.com/comments/1')
    assert (response.json() == correct_response_json), "The response is not correct"

def test_get_album():
    json_correct_string = r"""
    {"userId": 1,
    "id": 1,
    "title":"quidem molestiae enim"
    }
    """
    correct_response_json = json.loads(json_correct_string)
    response = requests.get('https://jsonplaceholder.typicode.com/albums/1')
    assert (response.json() == correct_response_json), "The response is not correct"


def test_post_post():
    data = {'title':'foo','body':'bar','userId':1,'id':101}
    response = requests.post('https://jsonplaceholder.typicode.com/posts',json=data)
    assert (response.json() == data), "The response is not correct"
    

def test_post_comment():
    data ={"name":"foo","emal":"bar","body":"test", "id":501,"postID":1}
    response = requests.post('https://jsonplaceholder.typicode.com/comments',json=data)
    assert (response.json() == data), "The response is not correct"


def test_post_album():
    data ={"userID":10,"id":101,"title":"foo"}
    response = requests.post('https://jsonplaceholder.typicode.com/albums',json=data)
    assert (response.json() == data), "The response is not correct"
