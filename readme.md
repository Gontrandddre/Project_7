# GrandPy Bot
------------------


# Table of contents

* [Summary](#summary)
* [Technologies](#technologies)
* [Set-Up](#set-up)
* [External-Ressources](#external-ressources)


## Summary

This application allows users to have an anecdote about a place.

To do so, they will just have to ask GrandPy who will give an answer.

At this moment u can visualize site on: https://flask-grandpybot-gda.herokuapp.com/

**STATUT**: Production

**Version:**
- Version 1: 2020

**Team:**
- Developer: Gontrand Daudré
- Mentor: Alexandre


## Technologies

- Python 3
- Flask
- Bootstrap 4
- HTML5
- CSS3
- Pipenv (Virtual environment Python)

## Set-up

Macos environment:

### Install Homebrew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" 
```

[Link to have more détails](https://brew.sh/)

### Install Python 3

```
brew install python
```

[Link to have more détails](https://docs.python-guide.org/starting/install3/osx/)

### Install a virtual environment library

```
brew install pipenv
```

or

```
pip install pipenv
```

[Link to have more détails](https://pypi.org/project/pipenv/)

### Create your key access Googlemaps API

After create your key, import in your environment:

```
export GG_APP_ID=<key>
```

To verify if your key exist:

```
printenv
```

### SSH keys

#### Checking for existing SSH keys

1. Visualize .ssh folder:

```
ls -a
```

if existing, go into folder:

```
cd .ssh
```

2. Visualize ssh keys:

```
cat id_rsa.pub
```

and

```
cat id_rsa
```

#### Generate SSH keys (if not existing)

1. Open local shell and copy/paste:

```
ssh-keygen
```

2. Accept proposal path.

3. Enter password or not (2 times).

4. Verify the existence of public keys:

```
cd .ssh
```

and

```
ls .ssh
```

5. Access to public keys:

```
cat id_rsa.pub
```

and

```
cat id_rsa
```


## Create your safety environment

### Local

1. Create a folder for the project:

```
mkdir MyDirectory
```

2. Under this folder:

```
cd MyDirectory
```

3. Create a virtual environment:

```
pipenv shell
```

### GitHub

1. Checking ssh keys on GitHub:

- Copy id_rsa.pub (cf.[SSH keys](###ssh-keys))
- Paste id_rsa.pub on your Github add a SSH key.

[Link for more details](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

2. Clone project with ssh keys into your project folder:

```
git clone <url github>
```

[Link for more details](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)

3. Install pipfile on your virtual environment:

```
pipenv install
```

### Update settings for development envrionment
XXX To define XXX
DEV
PROD

### Launch web app

1. Before launch, select right folder(where manage.py is present):

```
cd Project_name
```

2. Launch web app:

```
python3 run.py
```

Then open web app on your local server: 127.0.0.1:8000


### To participate in the project

1. Under develop branch:

```
git checkout develop
```

2. Create branch feature or hotfix & under the branch:

```
git checkout [-b] feature [if branch not existing]
```

3. Make modifications.

4. Test:

```
project3 pytest [file test]
```

5. Commit:

```
git add <files with modifications>
```

and
```
git commit -m "message"
```
6. Push on Github:

```
git push origin -u <name-feature/hotfix/etc.-github>
```

7. Pull request on GitHub.


## External-Ressources

### Heroku

App deployement

[link to Heroku!](https://heroku.com)
