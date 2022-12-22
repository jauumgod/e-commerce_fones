# TUTORIAL DO DANILO PAIXÃO COM IMPLEMENTAÇÃO DE LOGIN COM PYTHON
BIBLIOTECAS USADAS
```
from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
```


![image](https://user-images.githubusercontent.com/69704112/209177673-1192f96a-fece-4451-91af-aab7fdf65482.png)
