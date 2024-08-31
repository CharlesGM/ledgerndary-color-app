import os
import pytest
from app import app

# Define a list of valid colors for testing
VALID_COLORS = {'white', 'black', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta'}

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_valid_color(client):
    for color in VALID_COLORS:
        # Set the environment variable for the test
        os.environ['PAGE_COLOUR'] = color
        
        response = client.get('/')
        
        assert response.status_code == 200
        assert f'background-color: {color};'.encode() in response.data
        assert f'The background colour of this page is {color}!'.encode() in response.data

def test_home_page_invalid_color(client):
    # Set an invalid color
    invalid_color = 'notacolor'
    os.environ['PAGE_COLOUR'] = invalid_color
    
    response = client.get('/')
    
    # Check that the response uses the default color (white) for invalid colors
    assert response.status_code == 200
    assert b'background-color: white;' in response.data
    assert b'The background colour of this page is white!' in response.data
