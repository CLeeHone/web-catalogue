# Python-Flask MongoDB Web Catalog
This project aimed to demonstrate the flexibility of MongoDB databases for storing unstructured data, or for creating databases whose schema might change in the future. This web catalog allows users to create a new object type and store it in the database. A user can then view all items, or hone in on a specific one,  view its details, and leave a review.
## Authors
* Chloe Lee-Hone
* Parham Barati
## Catalog Examples
| Running | Program |
|---------|---------|
| ![image](https://github.com/CLeeHone/python-mongodb-web-catalogue/assets/67878819/5bb1f97b-32f4-48c4-8eea-228cfb4db124) | ![image](https://github.com/CLeeHone/python-mongodb-web-catalogue/assets/67878819/5b59e558-1939-41cd-ac6f-88bcfc44f724) | 
| ![image](https://github.com/CLeeHone/python-mongodb-web-catalogue/assets/67878819/c2173943-6034-4e19-b495-4aa046c7dbe4) | ![image](https://github.com/CLeeHone/web-catalogue/assets/67878819/641dc631-8555-4db3-be4a-713b4c2be081) |
## Class Description
* **Main.py**: The main entry point of the program. Uses the ApplicationLauncher class to start the Python-Flask program.  
* **View.py**: Houses all the application’s views, or pages. Determines the redirections and events that occur following a user’s actions.  
* **DTO.py**: The Data Transfer Object communicates with the database. It is used to retrieve and insert data.  
* **BusinessLogic.py**: The layer between the DTO and the View. Any manipulation of data would occur in this layer.   
* **ApplicationLauncher.py**: This class is used in the main method to launch the program.
## Python UML
![image](https://github.com/CLeeHone/python-mongodb-web-catalogue/assets/67878819/915139a3-cde0-4ef9-9f9f-9ee2ed60b491)
## Database Item Schema
![image](https://github.com/CLeeHone/python-mongodb-web-catalogue/assets/67878819/39a8105c-0976-41a3-8820-c76f1be93124)
