import pytest
from http.client import HTTPConnection


@pytest.mark.parametrize(
    'path',
    [
        '/posts/',
        '/posts/1/',
        '/polls/',
        '/polls/1/',
    ]
)
def test_get_requests(path: str):
    conn = HTTPConnection('localhost:8000')
    conn.request('GET', path)
    response = conn.getresponse()
    conn.close()
    assert response.status == 200, \
        f'On request to http://localhost:8000/posts/ with method GET bad response status ({response.status})'


@pytest.mark.parametrize(
    'method',
    [
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
    ]
)
def test_requests_to_posts_app_with_unsupported_methods(method: str):
    conn = HTTPConnection('localhost:8000')
    conn.request(method, '/posts/')
    response = conn.getresponse()
    conn.close()
    assert response.status // 100 == 4, \
        f'On request to http://localhost:8000/posts/ with method {method} bad response status ({response.status})'
