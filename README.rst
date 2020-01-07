pgbackup :snake:
========

CLI for backup remote PostgreSQL database either locally or to S3.

Preparing the Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Close repository: ``git clone git@github.com:djmilosev/Python3_Scripting_For_System_Engineers.git``
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver, and the destination.

S3 example w/ bucket name:

::

    $ pgbackup postgres://djordje@example.com:5432/example_db --driver s3 backups

Local example w/ local path:

::

    $ pgbackup postgres://djordje@example.com:5432/example_db --driver local /var/lib/example_db/backups/example_dump.sql 

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make

