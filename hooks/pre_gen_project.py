import re
import sys


MODULE_REGEX = r'^[-_a-zA-Z][-_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_folder_name }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is not a valid name for a folder or git repo! No spaces or special characters allowed.' % module_name)
    # exits with status 1 to indicate failure
    sys.exit(1)


module_name2 = '{{ cookiecutter.set_up_git_repo }}'

if not (re.match(r'^y', module_name2, re.IGNORECASE)|re.match(r'^n', module_name2, re.IGNORECASE)):
    print('ERROR: Must answer yes or no (y or n) for whether to make a github repo %s.' % module_name2)
    # exits with status 1 to indicate failure
    sys.exit(1)
