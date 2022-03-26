# DevHaven Icons

SVG icons of various programming languages, software, and widely used frameworks.

This API aims to provide official logos of all the major programming languages, software, and frameworks in one place.

## Endpoints

- Testing and Documentation

```
/docs
```

- Languages in svg format

```
/svg
/svg/{lang}?width={width}&height={height}
```

## Development

- Create an environment and install the requirements

```
python -m venv venv
pip install -r requirements.txt
```

- run the app using uvicorn with `reload` flag

```
uvicorn main:app --reload
```

- If you install any other dependecies, add it to `requirements.txt` file using:

```
pip freeze > requirements.txt
```

- Deployed to Heroku and using a [cron-job](cron-job.org) to keep the API running
