# FullStackAppWithFlaskandReact
### VM Environment :
```console
1. Creating VM Environment
- python3 -m venv venv
2. To activate the VM :
-source venv/bin/activate
3. How to deactivate :
- deactivate 
4. How to see all the installed dependencies : 
- pip list
5. HoW to save all dependencsies :
- pip freeze> requirements.txt
6. How to install all depepdenicies ( if i am trying to install the app in another machine) :
-pip install -r requirements.txt
7. How to delete a venv :
- rm -rf venv
```



### Frontend 
```console
The command npm create vite@latest frontend -- --template react is used to create a new project using Vite, a modern build tool for web development, with a React template.
- npm create vite@latest frontend -- --template react

Now run:
-cd frontend
-sudo npm install
-sudo npm run dev
```

### Backend 


#### Installing Flask:
```console
1. To install Flask
- pip install Flask
2.To check if its install correctly
- pip show Flask
```

### Important Dependencies that need to be imported
```console
#### flask_sqlalchemy 
flask_sqlalchemy is an extension for Flask that adds support for SQLAlchemy, a powerful Object Relational Mapper (ORM) for SQL databases.
	•	What It Does:
	•	SQLAlchemy allows you to interact with databases using Python objects instead of writing raw SQL queries.

#### flask_cors
What It Is: flask_cors is an extension for Flask that adds support for Cross-Origin Resource Sharing (CORS) in your Flask application.
	•	What It Does:
	•	CORS is a security feature implemented by web browsers that restricts web pages from making requests to a domain different from the one that served the web page. For example, if your frontend is hosted on http://localhost:3000 and your backend API is on http://localhost:5000, browsers will block the request unless CORS is properly configured.
```
