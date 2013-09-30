## Scripts for work with multiple git repositories.

**utils.py**
Here you should specify directory in which you are going to store cloned projects (WORKSPACE_DIR).
And directory for log files (OUTPUT_DIR).

**clone.py**
Clones all repositories listed in doc/repos.txt to WORKSPACE_DIR specified in utils.py.

**commit.py**
Commits all changes of projects located in WORKSPACE_DIR.

**push.py**
Pushes all changes of projects located in WORKSPACE_DIR

**pull.py**
Pulles all changes of projects located in WORKSPACE_DIR