# Links Service

#### This program is an API service for managing user links and link collections. Here are the main functions it provides:

1. **User registration and authentication:** User can register, authenticate, change or reset password.

2. **Link management:** User can add links by passing only the URL, and the service automatically gets the rest of the data.

3. **Collection Management:** The user can create, edit, view and delete link collections. Collections have a name, description and creation and modification dates.

## Usage

#### Launch requirement:

+ Docker

#### Installation:

1. Launching a container.

    ```
    docker compose up -d
    ````

2. Open a terminal inside the application container.

    ```
    docker compose exec app bash
    ```

3. Applying migrations.

    ```
    ./manage.py migrate
    ```
4. Create an administrator.

    ```
    ./manage.py createsuperuser
    ```
5. Launch the application

    ```
    ./manage.py runserver 0.0.0.0:8000
    ```

#### Test data:

+ **Password for all users:** 12345678

+ You need to be in the terminal of the app container

    ```
    ./manage.py loaddata all_data.json
    ```
