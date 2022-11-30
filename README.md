# Flask Layer Architecture Project Example

# Project installation
To install the project package, run the following command:

    pip install -r requirements.txt


# Project usage
## Setting environment variables
Before running the project, you must create a ```.env``` file in the root directory of the project as a copy of ```.env.example```. 

## Running the project
To run the project you can use either the command ```flask run``` or ```python app.py```

# Compile the project as executable file
To compile the project as executable file, you should install ```pyinstaller``` and ```tinyaes``` with the following command:

    pip install pyinstaller tinyaes

Then, run the following command (this step should be done only when code is changed):

    pyinstaller -Fw --key FR85.qkZNquEW,67QT*Z9aGko,Ba7tP# app.py

After that, you should add the following code just before ```pyz``` variable assignation, so the statics files can be added to the executable file:

    def extra_datas(mydir):
        def rec_glob(p, files):
            import os
            import glob
            for d in glob.glob(p):
                if os.path.isfile(d):
                    files.append(d)
                rec_glob("%s/*" % p, files)

        files = []
        rec_glob("%s/*" % mydir, files)
        extra_datas = []
        for f in files:
            extra_datas.append((f, f, 'DATA'))
        return extra_datas

    a.datas += extra_datas('app/static')
    a.datas += extra_datas('app/templates')

Finally, you can run the following command to create the final .exe file:

    pyinstaller app.spec