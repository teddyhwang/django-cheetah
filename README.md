Django Cheetah - Front End Project Driven by Django
===================================================

## Introduction

Django Cheetah is a starting template to use for front-end only projects.
Utilize the powerful template engine Django uses with the comfort of compiling
assets using django-pipeline and django-require.

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
1. Create your virtual environment for this project`virtualenv env_{{
project_name }}` this is a local virtual environment and should not be committed
into the svn repository (proset svn:ignore has already been made to the folder)
1. `source env_{{ project_name }}/bin/activate` - This is a very important step and
should be done before starting the server at all times
1. `pip install -r requirements.txt` - do not use `sudo` here as you are
installing dependencies in your local environment
1. `python manage.py runserver 0:8000` - server should be running on
`http://localhost:8000/`

## Editing HTML Templates

1. Django was chosen because of its excellent [templating system](https://docs.djangoproject.com/en/dev/ref/templates/).
All templates can be found in `{{ project_name }}/templates/`

## Editing media assets

1. All media assets can be found in `{{ project_name }}/static/`
1. All `.less` files will be automatically compiled into CSS files on pageload -
each individual CSS file will be created for the ones listed in:
`site/ecommerce/settings_pipeline.py`

## Adding in a new HTML page on Django

1. There are three files that need to be edited when adding a new page from the
`site/staticpages` folder: `views.py`, `urls.py`, `renderers.py`.
1. Add a new definition in `views.py`. Definitions in python need to be
separated by an underscore and dashes should not be used. Pass in `request` and
then the name of the HTML template relative to the `template` folder. For
example, a new page titled "About Us" would like like this:

        def about_us(request):
            return render(request, 'about-us.html')

1. Add a new urlpattern in `urls.py`'. A urlpattern will have `url(r'URL_NAME',
'VIEW DEFINITION', 'UNIQUE_NAME_FOR_URL')`. Continuing with the "About Us" page,
the urlpattern would look like this:

        url(r'about-us.html', 'about_us', name='about-us'),

1. Add in the new url into `renderers.py`. This file helps Django export the
static HTML when the build command is initiated. `/about-us.html` would be added
to continue the example from above.

## Add in a new mediator for requirejs

1. From the `site` folder, run `make addmediator page=YOUR_PAGE_NAME` e.g.
`make addmediator page=homepage`
1. This will add in the build and config files for the new page
1. Add in the page mediator reference into `REQUIRE_STANDALONE_MODULES` in
`settings.py`

## Export static HTML Files and Compile Assets for Prodution

1. From the `site/` folder, run `make`
1. All HTML views will be exported into `site/www`
1. All compiled assets will be found in `site/www/media` - the assets for
production use can be found in `site/www/media/compiled/`

## Tips, Tricks and Known Issues

- Add `${debian_chroot:+($debian_chroot)}` as the prefix in your `PS1` in
`~/.bashrc`. This will reveal which environment you are active on
- `deactivate` to leave your virtualenv environment
- `make` will only work on Mac OSX because of the use of `sed` which is
  different between Debian and Ubuntu
- the contents of `www` (html and assets) are purposefully ignored from the
  repository. This is the build folder and as such should only be used for
deployments.
- The site should be tested with compiled assets before being deployed - use the
  Django service while in development and then browse the `www` folder to test
that none of the compression or minifications broke anything
