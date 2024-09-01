# Flask Web Page Color App

This is a simple Python Flask web application that displays a web page with a background color defined by an environment variable. The app includes a validation mechanism to ensure the color is one of the predefined valid colors.

## Features
Display a web page with a background color set by the **PAGE_COLOUR** environment variable.
Validate the PAGE_COLOUR environment variable to ensure it is one of the allowed colors.
Return a 400 Bad Request error if an invalid color is provided.

## Valid Colors
The following colors are considered valid:

- white
- black
- red
- green
- blue
- yellow
- cyan
- magenta


## Project Structure

    ├── .github/workflow.yml        # GitHub Actions workflow file
    ├── Dockerfile                  # Dockerfile for containerizing the app
    ├── README.md                   # Project README file
    ├── app.py                      # Main Flask application
    ├── requirements.txt            # Python dependencies
    └── tests
        └── test_app.py             # Unit test for validating PAGE_COLOUR

## Getting Started
### Prerequisites
- Python 3.9+
- Flask
- Docker (optional for containerization)
- GitHub Actions (for CI/CD)

### Installing Dependencies
Install the required Python packages using pip:

    pip install -r requirements.txt

### Running the Application
To run the Flask application locally:

- Set the environment variable/color in th e Dockerfile as it will also be used for tagging
- Run:
            
        python app.py

Visit http://127.0.0.1:8080 in your web browser to see the web page.

### Running Unit Tests
The project includes a unit test to validate the PAGE_COLOUR environment variable.

To run the unit test, you have to be in the tests/ folder. Then run:

    python -m unittest discover -s . -p "test_app.py"

The test checks if the value of PAGE_COLOUR is among the valid colors. If the color is invalid, the test will fail.

### Dockerization
The application can be containerized using Docker. The Dockerfile is included in the project.

#### Building the Docker Image

    docker build -t flask-web-app .

#### Running the Docker Container

    docker run -e PAGE_COLOUR=blue -p 8080:8080 flask-web-app

### Continuous Integration with GitHub Actions
The project includes a GitHub Actions workflow (workflow.yml) that automates the following:

1. Checkout: Retrieves the code from the repository.
2. Setup Python: Sets up Python 3.9 in the CI environment.
3. Install Dependencies: Installs the required Python packages.
4. Extract and Validate PAGE_COLOUR:
    - Extracts the PAGE_COLOUR value from the Dockerfile.
    - Validates if the extracted PAGE_COLOUR is a valid color. The workflow fails if an invalid color is found.
 5. Build and Push Docker Image:
    - Builds the Docker image using the Dockerfile.
    - Tags the docker image with the PAGE_COLOR variable and pushes the Docker image to Docker Hub.
6. Update Remote Repository:
    - Commits changes (if any) and pushes them to the remote repository.

#### GitHub Actions Workflow
The workflow.yml file defines the CI pipeline for this project. Below is a summary of its functionality:

- Extract PAGE_COLOUR from Dockerfile: The workflow extracts the PAGE_COLOUR value from the Dockerfile.
- Validate PAGE_COLOUR: If PAGE_COLOUR is not part of the predefined valid colors, the workflow will fail.
- Build and Push Docker Image: The workflow builds the Docker image and pushes it to Docker Hub.
- Update Remote Repository: The workflow commits any changes and updates the remote repository.

This ensures that invalid color configurations are caught early in the CI pipeline, maintains the integrity of the application, and keeps the Docker image and remote repository updated.

## Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.