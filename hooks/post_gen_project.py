import sys, os
import re

#https://github.com/ConstantinoSchillebeeckx/cookiecutter-data-science thanks to this for some code

setup_git = True if '{{ cookiecutter.set_up_git_repo }}' == "Yes" else False

repo_name = '{{ cookiecutter.project_folder_name }}'


print ("\n***************************************************************************")
print ("Congrats! Your data analysis project directory has been created at: %s" %repo_name)


if setup_git:

    err = os.system('bash setup_git_repo.sh %s' %repo_name)
    if err: print "Error with GitHub repo setup!"
