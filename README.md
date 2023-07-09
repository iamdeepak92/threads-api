# Threads API

This is a Flask application that provides several routes for fetching user information and data from the Threads API. The application exposes the following routes:

## Route 1: Fetch userid by username

- **Endpoint**: `/userid/<username>`
- **Method**: GET
- **Description**: Fetches the user ID by providing the username.
- **Parameters**:
  - `<username>`: The username of the user.
- **Response**: Returns a JSON object with the `userid` of the user.
- **Example**: `http://localhost:3000/userid/johndoe`

## Route 2: Fetch user profile by userid

- **Endpoint**: `/userprofile/<userid>`
- **Method**: GET
- **Description**: Fetches the user profile by providing the user ID.
- **Parameters**:
  - `<userid>`: The ID of the user.
- **Response**: Returns the user profile data as a JSON object.
- **Example**: `http://localhost:3000/userprofile/12345`

## Route 3: Fetch threads or posts of userid

- **Endpoint**: `/threads/<userid>`
- **Method**: GET
- **Description**: Fetches the threads or posts of a user by providing the user ID.
- **Parameters**:
  - `<userid>`: The ID of the user.
- **Response**: Returns the threads or posts data as a JSON object.
- **Example**: `http://localhost:3000/threads/12345`

## How to Run

1. Make sure you have Python installed (version 3.6 or later).
2. Install the required dependencies by running the following command:
   ```
   pip install flask requests
   ```
3. Save the program code to a file named `app.py`.
4. Open a terminal or command prompt and navigate to the directory where the `app.py` file is located.
5. Run the application by executing the following command:
   ```
   python app.py
   ```
6. The server will start running on `http://localhost:3000`.

Note: You can change the `port` variable in the code to use a different port if needed.

## Error Handling

If any error occurs during the API requests or processing, the server will return a JSON response with an `"error"` key and an appropriate error message. The HTTP status code will be 500 (Internal Server Error).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
