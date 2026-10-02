# Venari

Venari is a Django storefront project centered on a product catalog and shopping experience. The supplied archive contains page templates for browsing products, reading articles, signing in, and moving through a four step checkout flow. Its Django configuration references a custom `base` application for the site's routes, user model, and cart context, but that application's source code is absent from the archive.

> **Archive status:** This snapshot is incomplete and cannot run as provided. The `base/` app and `static/` assets are missing. The descriptions below distinguish the pages and database structure in the archive from features whose backend implementation could not be verified.

## Project contents

- **Storefront templates:** home page variants, product categories, product grids and lists, product detail, and search form markup.
- **Shopping templates:** cart, delivery, payment, and receipt screens under `templates/checkout-1.html` through `checkout-4.html`.
- **Editorial pages:** blog grids and lists, article, and ideas templates.
- **Other pages:** about, contact, login, error page, and navigation/footer template.
- **Django configuration:** project settings, URL routing, ASGI and WSGI entry points, and `manage.py`.
- **SQLite database:** a bundled `db.sqlite3` whose schema includes tables for products, categories, brands, suppliers, ratings, and a custom user model. The archive does not include the model or view code for these tables.

Templates show interface elements for search, accounts, carts, and checkout. Because `base/` is absent, their request handling, authentication flows, and payment behavior cannot be confirmed from this archive.

## Tech stack

- Python and Django (settings were generated with Django 5.0.2)
- SQLite for the configured local database
- Django templates for rendered storefront pages
- Static CSS, JavaScript, and image references in the templates; the referenced `static/` directory is not present in the archive

## Repository layout

```text
Venari/                  Django project configuration and URL routing
templates/               Storefront, account, editorial, and checkout templates
templates/register_addons/  Registration related template fragments
manage.py                 Django management command entry point
db.sqlite3                Included SQLite database
LICENSE                   Apache License 2.0 text
```

## Running locally

First restore the missing `base/` Django app and the `static/` directory. You will also need the project's dependency list or the dependencies used by that app: no `requirements.txt` or `pyproject.toml` was included. The archived `pyvenv.cfg` refers to a machine specific Python installation and is not a substitute for a portable dependency file.

Once the missing source and assets have been restored, a typical local setup is:

```bash
python -m venv .venv
# Activate the virtual environment for your shell.
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

These commands assume you have restored or created `requirements.txt` and the app's migration files. Django's development server normally opens at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The repository includes a database snapshot; back it up before applying migrations or replacing it.

## Missing pieces and deployment notes

- `Venari/settings.py` installs `base.apps.BaseConfig`, uses `base.User` as its user model, and registers two `base.context_processor` functions.
- `Venari/urls.py` includes `base.urls` and references `base.views.page_404`. Django cannot start without the missing app.
- Templates reference images, stylesheets, and scripts that need the missing `static/` assets.
- The supplied settings enable `DEBUG` and contain a hardcoded development secret key. Configure a new secret through an environment variable, disable debug, set allowed hosts, and review static/media settings before deployment.
- The included `db.sqlite3` may contain local application data. Inspect and sanitize it before publishing or sharing the repository.

## License

The archive includes an [Apache License 2.0](LICENSE) file. Check the rights and attribution for any third party template and assets before distributing them.
