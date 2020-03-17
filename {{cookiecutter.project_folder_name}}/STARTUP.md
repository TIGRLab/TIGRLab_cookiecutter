How to make a github repo
==============================================

*Note: please feel free to delete this file once you have successfully created your repo*

On github
---------------
Go to github.
Log in to your account.
Click the new repository button in the top-right.
Type in the repository name, which is: {{cookiecutter.project_folder_name}}
Decide whether you want the repository to be public or private.
Do _NOT_ select "initialize this repository with a readme"
Click create repository


On your own system
-----------
Type:

```
git init
git add .
git commit -m "first commit!"
git remote add origin https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_folder_name}}
git push -u origin master
```
