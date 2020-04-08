**OPENTARGETS TAKE-HOME CODING TEST**

**<u>Problem A - query a REST API</u>**

The goal of this test is to assess your ability to query a remote documented REST API, fetch and analyse the data, and test your code to specifications.
 You will use our targetvalidation.org REST API, which is documented at https://docs.targetvalidation.org/programmatic-access/rest-api and at https://platform-api.opentargets.io/v3/platform/docs/swagger-ui

We would like you to build a program that can query our REST API to get a data value labelled as association_score.overall for a given target ID or disease ID. As explained in the API documentation, target IDs can be specified in the Ensembl Gene ID format (eg. ENSG00000157764) while disease IDs are specified in the Experimental Factor Ontology format (eg. EFO_0002422). 

Your code should: 

❏  Query the https://platform-api.opentargets.io/v3/platform/public/association/filter REST API endpoint to get the target to disease association information. The target parameter can be used to query for target-related information (eg. use the string ENSG00000157764 as a target id) and the `disease` parameter can be used to query for disease-related information (eg. use the string EFO_0002422 as a disease id).

❏  From the returned JSON object parse for each entry, the value returned at association_score.overall

❏  Print out to stdout the maximum, minimum, average and standard deviation values of association_score.overall

❏  Parse the arguments passed from the command line so that:

❏  my_code_test -t ENSG00000157764 will run an analysis for a target

❏  my_code_test -d EFO_0002422 will run an analysis for a disease

❏  my_code_test --test will run a suite of tests:

❏  The suite of the test should check the output for my_code_test -t ENSG00000157764

❏  It should also test the output for my_code_test -d EFO_0002422

❏  and it should test the output for my_code_test -d EFO_0000616



*<u>**Solution A - query a REST API**</u>*

For improvement UX/UI in program was added suggestion feature. If there is no any results for output,  program will suggest to user all targets or diseases that starts with similar letter (see screenshots below).

![suggest_target](https://user-images.githubusercontent.com/55881774/78833858-7b389980-79e5-11ea-97d4-8511f0f82d80.png)

Fig. 01. Suggestion for target



![suggest_disease](https://user-images.githubusercontent.com/55881774/78833775-52b09f80-79e5-11ea-8502-0cdb3d86cfac.png)

Fig. 02. Suggestion for disease

In coding test proposed to test program output but it can be more useful to test not the whole output for program but specific functions. Since the program interface or result representation can be changed.

***<u>Notes for part A:</u>***

It can be more useful to add feature for using local copy of json-file. It means that first time file will be downloaded and next time control sum of local and remote file will be compared (under the assumption that data updates not every few minutes). In this case network load will be decreased.

Second thing - it also can be useful to add a fuzzy search for targets and disease. Fuzzy searching allows for flexibly matching a string with partial  input, useful for filtering data very quickly based on lightweight user  input.



**<u>Problem B - parse a JSON dump</u>**

The goal of this problem is to parse quickly and efficiently large data files and to calculate statistics on the data extracted. The work is a simplified and representative version of much of the Extract-Transform-Load work that we do at Open Targets. 

First, you should download our _evidence_ data from 
https://storage.cloud.google.com/open-targets-data-releases/17.12/17.12_evidence_data.json.gz 

This file contains a series of JSON objects, each representing an evidence linking a target to a disease or more than one diseases. 

**First part**:

We want you to write a program that: 

1. For each JSON object in the file, parse target.id, disease.id and score.association_score 
2. For each target.id, disease.id pair calculates the median and the top 3 association_score. 
3. Outputs the resulting table in CSV format, sorted in ascending order by the median value of the association_score 

**Second part:**

Each JSON object in the file defines a connection between a target and a disease. Since there are ~30,000 targets and ~8,000 diseases, different targets will be connected to the same disease. 

You should expand your program from the first part of the problem to use the same data and count how many target-target pairs share a connection to at least two diseases. 



***<u>Solution B - parse a JSON dump</u>***

***First part***:

In this solution was realized two ways for process source file. First option is processing without any third-party libraries. Second option is processing with third-party library called "ijson", since "reinventing the wheel is not valued" (c). For both ways added calculation script execution time.

***Second part:***

Program functions was expanded for search target-target pairs share a connection to at least two diseases ("ijson" library is used). 

***<u>Notes for part B:</u>***

Source file 17.12_evidence_data.json constains multiple json-objects but it has not valid json structure. So, for processing this we need to define boundaries of each json-object. It means that processing this file is similar to process big text file with all disadvantages of it. There are two ways for increase performance. First way - add small fixes in this file (delete all "\n", add "[" to the begin and "]" to the end of file for creation a json-file without syntax erros). Second way - split source file to multiple json-objects. All ways allow us work with json-file as native. First way gives us opportunities for using third-party libraries for processing json-file (like bigjson, ujson etc.) and using AsyncIO. Second way gives us opportunities for using multithreading and GPU-acceleration. For example the one of most popular CPU for servers Xeon E5-2689 v3 has 10 cores and 20 threads with 3.1 GHz by each core, which allows process 20 json-files instantly without large HDD delays and gives us true multithreading (not like asynchronous way). Similar advantages can be achieved with GPU-acceleration (that's enough GTX 1060). The most critical thing in all cases is HDD reading speed. The best way to solve this problem - use SSD hard drive (preferably with NVME support).
