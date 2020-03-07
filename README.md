## Overview

Tasked to automate the submission of Datasets and Resources from various Organizations throughout the municipality of the City of Denton to the Open Data CKAN website.



## Findings

- CKAN provides a front-end interface for users to upload datasets and resources, making data accessible to find, share, and use.

- the CKAN API provides two means for organizations to upload data:

  - as a data blob via the FileStore API
  - as a searchable ElasticSearch persistent query layer via the DataStore API

  

## Recommendations

1. **SQL Database Export -> DataStore API**
   
   - Data to upload to CKAN will be provided in CSV or JSON as a direct export from the current systems, and upcoming Denton DataWarehouse
   - Each Organization will determine what DataSets to upload, each DataSet containing specific Resources (files, external API endpoints, external URL's to display)
   - Each DataSet will be a SQL query, which will be exported and passed to the DataStore API for creation (of new files), or modification/syncing (of existing files)
   
   
2. **CSV Export -> DataStore API**
   -  less optimal/automated, but still viable
   -  CSV exported data passed to system administrator for adding to the CKAN website via the DataStore API



-----

**Resources**

**CKAN Terminology**

<u>FileStore</u>: allows users to upload data files to CKAN resources, and to upload logo images for groups and organizations

<u>DataStore</u>: provides an *ad hoc* database for storage of structured data from CKAN resources. Data can be pulled out of resource files and stored in the DataStore.

DataStore API](https://docs.ckan.org/en/latest/maintaining/datastore.html#the-datastore-api): search, filter and update the data, without having to download and upload the entire data file
