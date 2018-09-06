# ITEM CATALOG PROJECT

## Project Overview

An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.


## Steps to run this project

1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html).

2. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

3. Clone or download the Vagrant VM configuration file from [here](https://github.com/udacity/fullstack-nanodegree-vm).

4. Open the directory and navigate to the `vagrant/` sub-directory.

5. Open terminal, and type:

   ```bash
   vagrant up
   ```

6. Connect to the newly created VM by typing the following command:

   ```bash
   vagrant ssh
   ```
7. Navigate to the shared repository:
    ```bash
    cd /vagrant/catalog
    ```
8. Run this file to set-up the Database:
    ```bash
    python database_setup.py
    ```
9. Run this file to Initialize Database:
    ```bash
    python db_init.py
    ```
10. Run the application:
    ```bash
    python application.py
    ```
11. Open `http://localhost:8000/` on your local browser to access the application.
