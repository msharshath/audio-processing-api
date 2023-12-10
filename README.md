**AUDIO PROCESSING API**

**Overview:**

The primary goal is to develop an API to audio file processing, encapsulated within a container and designed to cater to user needs. This API encompasses essential functionalities such as file uploading, downloading, and dynamic volume adjustment. The OpenAPI 2.0 standard serves as the foundation, guaranteeing a standardized structure and comprehensive documentation to facilitate seamless integration for users.

A crucial security measure is implemented through an authentication system utilizing API keys, ensuring controlled and secure access to the API. Positioned as a user-facing solution, the API prioritizes simplicity and efficiency, allowing users to effortlessly upload audio files for processing, dynamically adjust volume levels, and download the resulting audio files. The containerization aspect contributes to the API's versatility, enabling easy deployment and making it adaptable for a variety of audio processing applications.


![audio_api](https://github.com/msharshath/audio-processing-api/assets/32800505/7280b253-096c-4ae0-8c05-74506ffe2209)


**Use:**

This codebase serves as a versatile API tool, allowing users to elevate their audio files within a user-friendly digital environment. Whether the intent is to refine audio levels for enhanced clarity or seamlessly integrate audio processing into more diverse range of applications.

**Files Involved:**

index.html – Serves as a front end.

app.py – Serves as a backend and flask as server.

The frontend is anchored by index.html, which serves as the user interface. This HTML file incorporates elements of CSS and JavaScript, culminating in an engaging and responsive environment for users. 
On the backend, app.py takes the lead as the driving force, utilizing the Flask web framework and the PyDub library to expertly manage user authentication, process audio files, and handle API keys.

**Languages Used:**

The frontend harnesses the trio of HTML, CSS, JavaScript and Bootstrap to create a visually appealing interface, ensuring a seamless interaction between users and the Audio Processing App. Meanwhile, on the backend, Python takes the lead, providing the foundation for the robust functionalities encompassing secure authentication, efficient audio file processing, and adept error handling.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


**Setup Instructions:**

1.	Clone repository:

**git clone https://github.com/msharshath/audio-processing-api**

**cd audio-processing-app**

2.	Building docker image from Dockerfile:

**docker build -t audio-processing-api .**

3.	Run the docker container:
   
**docker run -p 8080:80 audio-processing-api**

4.	Access the api:
   
Open a web browser and go to **http://localhost:8080** to interact with the Audio Processing App.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**API Guidelines:**

**1.	Authentication:**

•	The Endpoint is /login.

•	Initiate authentication by sending a POST request to the /login endpoint.

•	Include a JSON payload with the `username` and `password` fields. Here, A predefined user only works as 

**Username: admin** and 

**Password: admin**

(Only these details will work)

•	A successful login will return a unique API key in the response.

•	If the same user logged in for second time, it asks to enter the API key.

**2.	API Key Submission:**

•	The Endpoint is /authenticate.

•	After receiving the API key, submit it for authentication by sending a POST request to the /authenticate endpoint.

•	If API key is already known, enter the API key.

•	Include a JSON payload with the username and ApiKey fields.

**3.	File Upload:**

•	The Endpoint is /upload.

•	Use the API key obtained during authentication to upload an audio file.

•	Send a POST request to the /upload endpoint with the audio file attached.

•	The server will respond with a message indicating the success or failure of the upload.

**4.	Adjust Volume:**

•	The Endpoint is /adjust.

•	Adjust the volume of the uploaded audio file by sending a POST request to the `/adjust` endpoint.

•	Include a JSON payload with the volumeLevel field representing the desired volume adjustment in dBFS.

**5.	Download Audio:**

•	The Endpoint is /download.

•	After adjusting the volume, initiate a GET request to the /download endpoint to retrieve the processed audio file.

•	The file will be returned as an attachment with the name "adjusted_new_audio.mp3".

**6.	Logout:**

•	The Endpoint is from (Client-Side).

•	Securely terminate the session by clicking the "Logout" button on the client-side.

•	This action resets the application and requires re-authentication for further API access.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Structure of audio-processing-api directory:**

**audio_processing_api/**

├──── Readme.doc - Documentation for your project, providing guidance on setup and usage. 

├──── app.py - Main Python file containing the code for your web application.

├──── Openapi.yaml - Specification file describing the structure of your API.

├──── test_api.py - File with unit tests for your API.

├──── Dockerfile - Instructions for building a Docker image of your application.

├──── requirements.txt - List of dependencies required for your application.

├──── backup_copy.txt - Backup text file, possibly containing a copy of api code.

├──── templates/ - Directory containing HTML, CSS, JavaScript for API UI.

│         └──── index.html


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Working process:**

1.	The audio-processing-app.git is cloned.
   
Command: **git clone https://github.com/msharshath/audio-processing-api**

2.	Open the Visual studio console of terminal to create a docker image.
   
Command: **docker build -t audio-processing-api .**  

(. defines current path, t defines image tag)

![image](https://github.com/msharshath/audio-processing-api/assets/32800505/f1183beb-0357-4e96-aa2b-5a5f7aa2e9ca)

3.	Now, Create docker container using the created docker image(Step -2) – audio-processing-api
   
Command: **docker run -p 8080:80 audio-processing-api**

(p - flag is used to map ports between the host system and the Docker container)

(8080:80 means that port 8080 on the host machine is being mapped to port 80 inside the Docker container)

 ![image](https://github.com/msharshath/audio-processing-api/assets/32800505/5ca8a841-8815-4a5f-8f3f-f74501962da3)


4.	Now, open **http://localhost:8080**  in web browser.

Its look like the below page, to enter the Username and Password.

By default, the only user can login is Username: **admin**, Password: **admin**

![image](https://github.com/msharshath/audio-processing-api/assets/32800505/90c92cce-08c0-4861-9ee1-776daece1f17)

 
5.	As you are a new user, it gives you API key.

![image](https://github.com/msharshath/audio-processing-api/assets/32800505/6adada0a-a409-4822-b1f3-68a002b6025e)
 
User should enter the obtained API key in API key field and clicks on **submit**.

![image](https://github.com/msharshath/audio-processing-api/assets/32800505/26d82349-d3aa-49ab-a6cf-cd7465a81e3a)

 
6.	Once submitted, A upload section will be shown where user can upload audio file and click on submit.
   
If successful, it throws a message as **File Uploaded Successfully**.

![image](https://github.com/msharshath/audio-processing-api/assets/32800505/b536d3fd-1d44-4a84-8c1d-25afe47ddd1a)
 
The audio files are moved to backend storing them in a temporary storage for further process.

7.	According to the user requirement, Enter the volume and click on button for a condition either increase or decrease the volume of audio file.
   
For an example, here a **volume of 4 to be increased**.

If it successful, it prints a message as **Audio adjusted successfully**.

![image](https://github.com/msharshath/audio-processing-api/assets/32800505/7fe53c55-3c48-467c-a7dd-537ce5b346fe)

8.	Once the last step is successful, User can download the adjusted audio file using Download Audio button. When button is clicked, Audio file will download automatically.

![image](https://github.com/msharshath/audio-processing-api/assets/32800505/085ed622-78fd-492f-bd28-68ffba9969ae)

9.	The downloaded audio file works with user selected volume.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**How is the API key generated?**

The built-in Python module secrets is used to produce cryptographically safe random numbers, but it can also be used in other ways. You might suggest that you could generate these random numbers using the random module, but the secrets module has access to the most secure source of randomness that your computer can supply. This makes it ideal for a wide range of applications, including password management, authentication, and security tokens.

**import secrets**

The following are the functions which are used to generate secure tokens.

**secrets.token_bytes([nbytes=None])**: Return a secure random byte string containing the number of bytes. If n-bytes are not supplied, a reasonable default gets used.

**secrets.token_urlsafe([nbytes=None])**: Return a secure random URL-safe text string, containing n-bytes random bytes. Use this method to generate secure hard-to-guess URLs.

Here, I used **secrets.token_urlsafe(32)**, to generate random text string of **32 bytes**  which is acts like a API unique key.

In the way our application works, when someone tries to log in using the **`/login`** endpoint, the system checks their username and password. Right now, we're keeping things simple by using a fixed username **('admin')** and password **('admin')**. If the login is successful, the system then looks to see if the user already has an API key. 

If they do, the user is told to stick with their current key. If not, a new, strong, and random API key is created for them using the **`secrets.token_urlsafe(32)`** function. This new key is then linked to the user's information in the system. The user gets a response saying whether a new API key was made or if they should use their existing one. 

It's important to note that in a real-world situation, we'd typically use more advanced security measures and storage methods for user data and API keys. 

However, as it stands, there's a limitation: when the server is turned off and back on, it treats everyone, including the 'admin,' as a new user, and any previously generated API keys are reset. To address this, a more permanent storage solution, like a database, would be needed to keep user data intact across server restarts.

Furthermore, handling API keys would probably include factors like setting expiration periods for tokens, regularly changing keys through rotation, and adopting secure storage practices. These measures are implemented to minimize potential security threats.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
**How are the volume adjustment process works?**

In the **`/adjust`** endpoint from app.py code, the process of adjusting audio volume begins by extracting the desired volume level from the JSON data received in the HTTP - POST request. It validates the volume level to ensure it is a valid numeric value. Subsequently, the code identifies the latest uploaded audio file from the audio_storage dictionary, where keys represent file names, and values represent timestamps of when the files were uploaded.

Once the latest audio file is determined, the actual audio content is retrieved from **audio_storage**. If the audio content is unavailable, an error response is returned. Following this, the code enters a placeholder section where the audio adjustment logic should be implemented. In the given code, the adjust_audio_volume function is called, passing the retrieved audio content and the desired volume level as parameters.

Inside the adjust_audio_volume function, the audio content is converted into an AudioSegment using the **`pydub`** library. 

Pydub is an easy to comprehend, well-designed Python library for audio modification. Pydub is a staple tool for creating simple audio scripts.

These could include:
1.	Loading and storing many audio file formats.
2.	Audio can be separated or appended in segments.
3.	Combining audio from two separate audio files.
4.	Altering the audio levels or pan settings.
5.	Featuring simple effects like filters.
6.	rendering audio tones.
   
The volume adjustment is then performed by adding the specified volume level to the audio. This step simulates adjusting the volume. The adjusted audio is logged for reference, and the content is exported as an MP3 file. The adjusted audio content is then updated in the audio_storage dictionary.

It's crucial to emphasize that the logic used here is a placeholder, and for effective audio processing, it should be replaced with the appropriate processing code. Additionally, the exact audio adjustment logic may vary based on specific requirements, such as normalization, equalization, or compression, and should be implemented accordingly.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Docker Overview:**

Docker is a containerization platform that allows developers to package applications and their dependencies into standardized units called containers. Containers provide a consistent and isolated environment, ensuring that applications run reliably across different computing environments.

Use of Docker:

1. **Portability**: Docker enables the creation of lightweight and portable containers, allowing applications to run consistently across various environments.
2. **Isolation**: Containers encapsulate applications and their dependencies, preventing conflicts and ensuring a clean runtime environment.
3. **Efficiency**: Docker optimizes resource utilization by sharing the host OS kernel, resulting in faster startup times and reduced overhead.
4. **Scalability**: Applications can be easily scaled by deploying multiple instances of containers, providing a flexible and scalable architecture.
   
Purpose of Dockerfile:

A Dockerfile is a script that contains instructions for building a Docker image. It defines the steps to set up the environment, install dependencies, and configure the application within a container.

**Commands**:

1.	To know docker installed or not: **docker –version**
2.	Create docker image: **docker build -t (tag_name)** (Dockerfile_location)
3.	Check available docker images: **docker images**
4.	Remove docker image: **docker rmi -f (docker_image_name)**
5.	Create and run docker container: **docker run -p 8080:80 (docker_image_name)**
   
  	(8080:80 means that port 8080 on the host machine is being mapped to port 80 inside the Docker container)
  	
6.	Check docker running docker containers: **docker ps**
7.	Check available docker containers: **docker ps -a**
8.	Start the docker container: **docker start (docker_container_name)**
9.	Enter into docker container: **docker exec -it (docker_container_name) /bin/bash**
10.	To exit from docker container: **exit**
11.	Stop the docker container: **docker stop (docker_container_name)**
12.	Delete docker container: **docker rm (docker_container_name)**

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**API Documentation: - Openapi.yaml**

To use this as API documentation, Open website and copy & paste this Openapi. Yaml code to website console: 

1.	https://app.apiary.io/audioprocessingapi/editor 
2.	https://editor.swagger.io/
3.	https://editor-next.swagger.io/

The provided YAML code outlines the Swagger documentation for an Audio Processing API. This API offers a versatile solution for manipulating audio files, specializing in volume adjustment. The documentation describes key features, such as user authentication, file upload, volume adjustment, and download capabilities. Users can authenticate through the **'/login'** endpoint, receive a unique API key, upload audio files, adjust volume via the **'/adjust'** endpoint, and download the processed audio file.

The API leverages the Flask framework and PyDub library, ensuring seamless audio processing tasks. The Swagger documentation includes details on each endpoint, specifying the expected input parameters, responses, and potential error messages. The **'/login'** endpoint handles user authentication, **'/upload'** facilitates audio file uploads, **'/adjust'** adjusts audio volume, and **'/download'** enables users to retrieve the adjusted audio file.

The documentation provides clarity on the API's functionality, workflow, and expected interactions. It emphasizes simplicity and ease of integration, making it suitable for diverse audio processing applications. Additionally, security measures are outlined, with API keys used for authentication. Standard error responses are defined for scenarios like invalid API keys, unauthorized access, file not found, invalid volume levels, and no selected files. Overall, the YAML code offers a comprehensive overview of the Audio Processing API and serves as a helpful guide for developers. 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Test cases: - test_api.py**

The unit testing suite comprises three functions. The **`setUp`** function initializes a test client for controlled HTTP request simulation, while **`tearDown`** cleans up files created during testing. The **`test_login_success`** function assesses the login route with valid credentials, expecting a 200 status, True 'success,' and an 'apiKey.' Conversely, `test_login_failure` checks the response to incorrect credentials, anticipating a 401 status. Lastly, **`test_adjust_audio`** focuses on the **'/adjust'** route, testing volume adjustment with different file path specifications. 

setUp Function:

The setup function initializes a test client for the Flask application, facilitating the simulation of HTTP requests for testing purposes. This ensures that each test case starts with a clean environment, preventing interference between different tests.

tearDown Function:

The tearDown function acts as a cleanup mechanism after each test case execution. It ensures that any files created during the tests, such as "adjusted_new_audio.mp3" and "test.mp3," are removed. This guarantees that the testing environment remains pristine.

test_login_success Function:

The test_login_success function evaluates the login route with correct credentials. It sends a POST request to the '/login' endpoint with the username **'admin'** and password **'admin'**. The test asserts that the response status code is 200, the 'success' attribute in the returned JSON is True, and an 'apiKey' is present in the response data.

test_login_failure Function:

The test_login_failure function assesses the login route when incorrect credentials are provided. It sends a POST request to the '/login' endpoint with the username **('admin')** and an incorrect password **('Admin')**.

The test expects a response status code of 401, indicating authentication failure. The response content is printed for further inspection.

test_adjust_audio Function:

The test_adjust_audio function checks the '/adjust' route, specifically focusing on volume adjustment. It uploads an audio file named "Sample_Audio.mp3" using two different methods for specifying the file path. Subsequently, it sends a POST request to '/adjust' with a volume adjustment level of 3. The test asserts that the response status code is 200, and the response data contains the 'message' attribute.
