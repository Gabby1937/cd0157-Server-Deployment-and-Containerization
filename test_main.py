'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'myjwtsecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjMyMDE2MjksIm5iZiI6MTY2MTk5MjAyOSwiZW1haWwiOiJnYWJyaWVsam9obnNvbjE5MzdAZ21haWwuY29tIn0.iq_4MduGAxXIB7_QhO6grC0F-oiTFXpQnvx3IqpYl0Y'
EMAIL = 'gabrieljohnson1937@gmail.com'
PASSWORD = 'gj193752'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
