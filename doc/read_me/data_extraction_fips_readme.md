# State County City FIPS 

## Third Party Source
    ## SimpleMaps.com 
        # CSV download

    ## Terms state I have to reference their website, 
        # Reference Link
        # https://simplemaps.com/data/us-cities


# FCC Gov
    # FIPS for state and County only. Text file hosted. 
        # https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt


# Transportation.gov
# https://data.transportation.gov/Railroads/State-County-and-City-FIPS-Reference-Table/eek5-pv8d/about_data

    # API Endpoint
        # JSON or CSV

        # API Link:
        # https://data.transportation.gov/resource/eek5-pv8d.json
    
        # API Documentation
        # https://dev.socrata.com/foundry/data.transportation.gov/eek5-pv8d
    
        # How to query more than 1000 rows of a dataset
        #https://support.socrata.com/hc/en-us/articles/202949268-How-to-query-more-than-1000-rows-of-a-dataset
    
    
        # Needs App Token
            # Created Login.Gov Account
    
            # App Token
            # G9y46iRQiv4jix5v8fCATdd2B
    
        # Will require that I use Offset due to default limit of 1000
        # I could probabaly modify my UFO Data code to work with this. 
        # Dataset has a total of 39,792 rows. 

    # Also have local csv file download of the dataset


    # Dataset contains 9 columns
        # State Name 
        # County Name
        # City Name
        # State Code
        # State FIPS Code
        # County Code
        # StCnty FIPS Code 
        # City Code
        # StCntyCity FIPS Code





    # Dev docs On Query Commands
        # Link: https://dev.socrata.com/docs/queries/

        # If I'm doing URL encoding, I would just need to add a to the end of the url. For python, I will need to add the filter condition as an argument to the client get function [client.get9()]
        
            # Get Row Count using Sodapy/Socrata
                # Add "?$select=count(*)" to the end of the get request (? is added if it's the first filter, & is added after each filter to add an additional. )
                    # https://data.transportation.gov/resource/eek5-pv8d.json?$select="count(*)"


            #So I believe what I will need to do to hadnle the query limit is increment an offset with the limit arguement. 
                # 'offset' assigned to the end of the previous query limit. 
                    # first run: client.get("client", limit="2000", offset="0")
                    # second run: client.get("client", limit="2000", offset="2000")

            

    