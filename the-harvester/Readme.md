This is Harvester, a python script that allows you to harvest the web for emails that have been made public. This script is generally used as part of the initial tests to examine the digital footprint of a customer, and hence his/her vulnerability.

##### Testing it out up
Running 'python TheHarvester.py' shows you all the command options that are available for this script.


#### Feature 1
Say you want to find an email that ends with the domain '@google.com', you can run
'python TheHarvester.py -d google.com –b all'

#### Feature 2
If you want to be more specific, only search google.com for yahoo emails, you can run
'python theharvester.py -d yahoo.com -l 500 -b google'

Note: that the command above will limit your results to 500 results
