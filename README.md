Django Cheetah - Front End Project Driven by Django
===================================================

## Introduction

Django Cheetah is a starting template to use for front-end projects. This is
ideal for any project that requires providing front-end static HTML templates
and associated media assets to another team that will integrate into a separate
back-end system.

Consider this as a toolkit for you to utilize the powerful template engine Django
provideas as well as having all the asset management taken care of (compiling
CSS, JS assets and organizing requirejs optimization builds).

## Quick Install

    mkdir <project_name>
    cd <project_name>
    virtualenv env_<project_name>
    source env_<project_name>/bin/active
    django-admin.py startproject --template=https://github.com/teddyhwang/django-cheetah/zipball/master <project_name>
    cd <project_name>
    pip install -r requirements.txt

## Out of the Box

This template comes with the following tools out of the box and ready to use:

- LESS
- jQuery
- requirejs and almondjs for optimization
- underscorejs
- modernizr
- django-pipeline
- django-require
- django-medusa

## Requirements

See below for beginner's guide on installing the below requirements

- LESS compiler
- uglifyjs compiler
- YUI compressor

## Editing HTML Templates

1. Django was chosen because of its excellent [templating system](https://docs.djangoproject.com/en/dev/ref/templates/).
All templates can be found in `<project_name>/templates/`

## Editing media assets

1. All media assets can be found in `<project_name>/static/`
1. All `.less` files will be automatically compiled into CSS files on pageload -
each individual CSS file will be created for the ones listed in:
`<project_name>/settings_pipeline.py`

## Adding in a new static HTML page in Django

1. There are three files that need to be edited when adding a new page from the
`<project_name>` folder: `views.py`, `urls.py`, `renderers.py`.
1. Add a new definition in `views.py`. Definitions in python need to be
separated by an underscore and dashes should not be used. Pass in `request` and
then the name of the HTML template relative to the `template` folder. For
example, a new page titled "Contact Us" would like like this:

        def contact_us(request):
            return render(request, 'contact-us.html')

1. Add a new urlpattern in `urls.py`'. A urlpattern will have `url(r'URL_NAME',
'VIEW DEFINITION', 'UNIQUE_NAME_FOR_URL')`. Continuing with the "About Us" page,
the urlpattern would look like this:

        url(r'contact-us.html', 'contact_us', name='contact-us'),

1. Add in the new url into `renderers.py`. This file helps Django export the
static HTML when the build command is initiated. `/contact-us.html` would be added
to continue the example from above.

## Add in a new mediator for requirejs

**WARNING** this assumes that the site has multiple pages and every page will
have its own minified JS asset. This is most likely not the ideal and will be
refactored heavily in the near future.

1. From the `<project_name>` folder, run `make addmediator page=YOUR_PAGE_NAME` e.g.
`make addmediator page=homepage`
1. This will add in the build and config files for the new page
1. Add in the page mediator reference into `REQUIRE_STANDALONE_MODULES` in
`settings.py`

## Export static HTML Files and Compile Assets for Prodution

**WARNING** this is a very poor method of building the project as it uses `sed`
to turn `DEBUG` to `False` and then back to `True` once the build finishes. The
plan is to create a django management command that can automate all of this.

1. Edit `Makefile` and replace `{{ project_name }}` with the same name used
above when installing the project.
1. Type `make` from terminal to build the files.
1. All HTML views will be exported into `www`
1. All compiled assets will be found in `www/static` - the assets for
production use can be found in `www/static/compiled/`

## Beginner's Setup to Django

1. Install [homebrew](http://mxcl.github.com/homebrew/) `ruby -e "$(curl -fsSL
https://raw.github.com/mxcl/homebrew/go)"`
1. Run the command `brew install python --with-brewed-openssl` from terminal
1. Ensure `/usr/local/bin` is the first line in the file `/etc/paths` so that
the recently installed version of Python is used
1. Confirm above by running `which python` - output should be
`/usr/local/bin/python`
1. Install virtualenv `sudo easy_install virtualenv`
1. Install pip `sudo easy_install pip`
1. Install nodejs `brew install node`
1. Install less compiler `sudo npm install -g lessc`
1. Install YUI Compressor `brew install yuicompressor`
1. Install uglify `sudo npm install -g uglifyjs`
1. Create your virtual environment for this project`virtualenv
env_<project_name>` this is a local virtual environment and should not be committed
into the svn repository (proset svn:ignore has already been made to the folder)
1. `source env_<project_name>/bin/activate` - This is a very important step and
should be done before starting the server at all times
1. `pip install -r requirements.txt` - do not use `sudo` here as you are
installing dependencies in your local environment
1. `python manage.py runserver 0:8000` - server should be running on
`http://localhost:8000/`

## Tips, Tricks and Known Issues

- `deactivate` to leave your virtualenv environment
- `make` will only work on Mac OSX because of the use of `sed` which is
  different between Debian and Ubuntu
- the contents of `www` (html and assets) are purposefully ignored from the
  repository. This is the build folder and as such should only be used for
deployments.
- The site should be tested with compiled assets before being deployed - use the
  Django service while in development and then browse the `www` folder to test
that none of the compression or minifications broke anything
