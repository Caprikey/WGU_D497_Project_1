D497 - Data Wrangling - Project 1 Ruberic

# Project: Real World Data Wrangling with Python

## Code Quality and Submission Phase

| Criteria	| Submission Requirements |
|--------|---------|
| Does the code work? | All code is functional (i.e. no errors are thrown by the code). Warnings are okay, as long as they are not a result of poor coding practices. |
| The student has uploaded a .zip folder containing their Jupyter Notebook for code review, and their datasets (file/link) for running the code. | Students’ .zip folder must contain the following: <ul><li> A Jupyter Notebook with completed code </li><li>Source datasets or a .txt file containing the links to the datasets, if data is downloaded manually</li><li>the data gathering code in the notebook, if data is gathered programmatically, </li><li>the raw datasets that are stored locally</li><li> the final cleaned dataset (after variables are combined) that is stored locally.</li></ul> |
|  The project shows thorough documentation of justification of wrangling decisions. | For each stage of the process, students must explain: <ul><li>Their justifications behind the method used for gathering, assessment, cleaning, storing, answering the research question.</li><li>Write code comments for code readability</li></ul> All code and text blocks in the notebook denoted “FILL IN” should be filled in by the student. <br />In the last section of the notebook, “Answering the Research Question”, there must be at least 2 plots generated. |


## Gathering, Assessment, and Cleaning

| Criteria	| Submission Requirements 
|--------|---------|
| The project has a proper explanation of the problem statement. | Students write 2-4 full sentences explaining the kind of problem they will want to look at and the datasets they will be wrangling for this project. |
| The student has gathered at least two separate datasets using two different data gathering methods. |  Students should pick at least two different gathering methods from the list below: <ul><li>Download data manually</li><li>Programmatically downloading files</li><li>Gather data by accessing APIs</li><li>Gather and extract data from HTML files using BeautifulSoup</li><li>Extract data from a SQL database</li></ul>Students must then gather at least two datasets. Each dataset must have at least two variables and have greater than 500 data samples within each dataset.<br />For each dataset, students must describe in 2-3 full sentences:<ul><li>Why they picked the dataset</li><li>The gathering method</li><li>The names and significance of the variables in the dataset.</li></ul> For applicable data gathering methods, such as parsing HTML, extracting SQL data, and programmatic API access, students must show their work (e.g., if using an API to download the data, please include a snippet of your code in the notebook). <br /> Students must load the dataset programmatically into this notebook. |
| The student assesses the datasets for quality and tidiness. | Students should list two data quality issues and two tidiness issues with the datasets they have selected. For each data issue, they should: <ul><li>Briefly describe the issue they find.</li><li>Assess the issue visually and programmatically using the methods discussed in the course (e.g., df.head(), df.describe()).</li><li>Justify the assessment methods.</li></ul>List of data quality issues: <ul><li>Completeness</li><li> Validity</li><li> Accuracy</li><li> Consistency</li><li> Uniqueness</li></ul>|
| The student cleans the data issues they identified with the explanation and justifications. | Students should clean the dataset to solve the 4 issues corresponding to data quality and tidiness in the assessment step. For each issue cleaned, they must: <ul><li>Include justifications for the cleaning method used and cleaning decisions. </li><li>Use either the visual or programmatical method to validate that the cleaning was successful </li></ul>|
| Remove unnecessary variables and combine datasets | Students must remove unnecessary variables for their analysis and combine their datasets. After combining the data, the final dataset must have at least 4 variables. | 

## Data Storage and Answering the Research Question

| Criteria	| Submission Requirements 
|--------|---------|
|Students must update their data store. | Update your database/data store with the cleaned data <ul><li>Students must maintain different instances/versions of data (raw data and cleaned data)</li><li>Students must name their dataset files informatively</li><li>Students must ensure both the raw and cleaned data are saved to their database/data store </li></ul>**Note**: Students are not required to use a relational/non-relational database store. |
| Students will define and answer a short research question. | Students must use the final cleaned data to answer the question they raised from the problem statement in Step 1. <br />Students must produce at least two visualizations using the cleaned data and explain how they help the student answer the question (in 1-2 full sentences). | 
| Students must identify next steps for the project. | In 2-4 sentences, students must describe what actions they would take if they had more time to complete the project.| 