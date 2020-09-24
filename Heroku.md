# Heroku Deployment

## Python Poetry Buildpack

The Python Poetry Buildpack prepares the build to be processed by a Python buildpack such as heroku/python by generating ```requirements.txt``` and runtime.txt from ```poetry.lock```.

To set up the use of several buildpacks from the Heroku CLI use ```buildpacks:add```:

```bash
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
```

_Reference: [https://elements.heroku.com/buildpacks/moneymeets/python-poetry-buildpack](https://elements.heroku.com/buildpacks/moneymeets/python-poetry-buildpack)_