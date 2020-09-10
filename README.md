# Purbeurre

Purbeurre is a website which allows anyone to find a surrogate to an unhealthy product, and saving the surrogate.
To be able to save the different surrogates to the products you want an alternative for, you must be signed-in.
Purbeurre is written in Python 3 with Django, Javascript with Jquery, HTML5 and CSS3 with Bootsrap.
The project is hosted by Heroku

## External resources

The project rely on Openfoodfacts API.

## Dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to 
install all the dependencies. Here are the steps :

1. Open the command prompt.  
2. cd to the directory where requirements.txt is located.  
3. Run this command in your shell:  

```bash
pip install -r requirements.txt
```


## Configuration :

You will need to provide theses environment variables :

DATABASE_URL : the database url   
SECRET_KEY : the Django secret key, do not use the one in settings.py in production   
EMAIL_USER : the email address used by the project, if needed (not used at the moment)   
EMAIL_PASSWORD: the password for the email address used  
ENV : Set to "production" when online, when in development set to 'development'   
ALLOWED_HOSTS : as the project is hosted on Heroku, ".herokuapps.com" is set, change to whatever hosting provider you're
using

You may also need to change the file **Procfile** located at the root level to your specifications.

Once transferred to your host, you will need to use theses commands:

   
_In order to set the database:_    
```bash
python3 manage.py migrate 
```

_In order to initialise the database with the products provided by the OpenFoodFact API:_

```bash
python3 manage.py initdb
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to 
discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Copyleft](https://www.gnu.org/licenses/copyleft.fr.html)