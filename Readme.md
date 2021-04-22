This website was constructed using the Flask framework for web development. Flask served to run the backend, while the frontend was developed using Bootstrap, 
a css frontend framework.

SQLite was the database used to store all applicable information from website


    Run Locally (Assuming python 3.9 is already installed)
    
1.) Download all the files from this repository
2.) Open the command window and navigate to the directory with the files via 'cd name_of_project_directory'
3.) Run the command 'pip install -r requirements.txt', it is recommend that you do this inside of a virtual enviroment 
    (See * https://docs.python.org/3/tutorial/venv.html) Additionally note, the commands needed to create a virtual enviroment 
    will vary from operating system to operating system.
4.) Run the command 'flask run', then navigate to localhost (copy 'https://localhost:8000' into your browser)


    Testing Information
1.) Tests will be run automatically through CircleCI
2.) To run tests locally, after following the steps from the previous section run 'pytest'
3.) To view testing results from CircleCI, after pushing code to the repository, 
    navigate to https://app.circleci.com/pipelines/github/zachk00/AED-Website?branch=main
4.) From the previous link their are two viewing options once you have selected build, 
    in the steps panel(see link 1), there will be a technical print out of the errors if applicable, or
    in the artifacts panel (see link 2 and 3), the user can view an html document report of the tests and any failures.
    These html documents will also inlcude meta data such as the time the tests were ran, how many tests, etc.
    
    
    Links
1.) https://app.circleci.com/pipelines/github/zachk00/AED-Website/198/workflows/bd53f75a-39c9-4d6c-90e4-6a78880fbe50/jobs/204/steps
2.) https://app.circleci.com/pipelines/github/zachk00/AED-Website/198/workflows/bd53f75a-39c9-4d6c-90e4-6a78880fbe50/jobs/204/artifacts
3.) https://189-333980191-gh.circle-artifacts.com/0/test-reports/report.html


