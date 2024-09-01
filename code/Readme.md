## Tasks Accomplished

- [x] **3D Data Visualization:** User can provide EtherCalc link to get 3d scatter plots.
- [x] **Geospatial Data Mapping:** User can provide link elevation data to get 3D Elevation surface maps.

## Technology Stack

This project leverages the following technologies:

- **[Django](https://www.djangoproject.com/):** Used for creating the Back End of the platform.
- **[Plotly](https://plotly.com/):** Straightforward graphing library used for 3d plotting
- **[D3](https://d3js.org/):** Used to load and parse the CSV data form the the ethercalc spreadsheets link.

## Key Features

- **Feature 1:** Three types of Interactive 3D Graphs for EtherCalc spreadsheet link.
- **Feature 2:** Users can share their visualization on the home page of the website.
- **Feature 3:** Login and Register implemented.
- **Feature 4:** Persistent storage with the help of an SQL database and the django backend.
- **Feature 5:** Logged in users can edit their previously created visualization and provide new data at any point.
- **Feature 6:** User can select plotting variables on the graphs according to their data.

## Local Setup Instructions

Follow these steps to run the project locally 
Requirements:
    - Python
    - pip

Use the command mentioned for your OS on each step (if applicable).

1. **Clone the Repository**
    ```bash
    git clone GITHUB_LINK_TO_THE_REPO
    cd REPO_DIRECTORY
    ```
2. **Initialize the virtual environment**
    Windows:
    ```bash
    cd REPO_DIRECTORY/code
    python -m venv env_name
    ```
    Mac:
    ```bash
    cd REPO_DIRECTORY\code
    python -m venv env_name
    ```

3. **Activate the virtual environment**
    Windows:
    ```bash
    env_name\Scripts\activate
    ```
    Mac:
    ```bash
    source env_name/bin/activate
    ```

   
4. **Install Django**
    ```bash
    pip install django
    ```

4. **Start the local server**
    ```bash
    cd datavisual
    python manage.py runserver
    ```
Now the server should be running the web app on http://127.0.0.1:8000/ .

