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
    
    # Extract the color from the response HTML
    html_content = response.data.decode()
    start_idx = html_content.find('background-color: ') + len('background-color: ')
    end_idx = html_content.find(';', start_idx)
    
    # If no valid color is found, set it to an empty string
    color_in_response = html_content[start_idx:end_idx] if start_idx != -1 and end_idx != -1 else ''
    
    # Validate the color
    if color_in_response not in VALID_COLORS:
        pytest.fail(f"Invalid color detected: {color_in_response}. Expected one of: {', '.join(VALID_COLORS)}")
    
    # Ensure the invalid color does not appear in the response
    assert response.status_code == 200
    assert f'background-color: {invalid_color};' not in html_content
    assert f'The background colour of this page is {invalid_color}!' not in html_content
