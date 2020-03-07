"""
Script to create a new dataset with a resource onto Denton's 
Open Data portal
"""


from pathlib import Path

from ckanapi import RemoteCKAN


# Set user agent
ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

# Read data file to be uploaded
with open(Path.cwd() / 'data' / 'MOCK_DATA.csv', 'rb') as data:
    mysite = RemoteCKAN('https://data.cityofdenton.com/', apikey='[INSERT API KEY HERE]', user_agent=ua)

    # Create the dataset
    mysite.action.package_create(
        name='mock-data',
        title='Mock Data',
        private=True,
        owner_org='tech-services',
    )

    # Upload a resource to the dataset
    mysite.action.resource_create(
        package_id='mock-data',
        url='dummy-value',  # ignored but required by CKAN<2.6
        name='Mock Data',
        upload=data,
        format='CSV'
    )
