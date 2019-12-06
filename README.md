# AWS Sustainability Hackathon

Code in support of using Amazon Sustainability Data Initiative (ASDI) data, specifically Sentinal-2) for analyzing deforestation in Brazil.

This repo provides scripts that download and process the satellite imagery for a given month and spatial location. From this imagery, the forest cover is calculated and stored. Using the API, a user can optain the forest cover values to make temporal comparisons.

## The existing solution uses the following steps:

*   Sentinal-2 imagery is pulled using the SentinalHub API tool.
*   Imagery is stored in Amazon S3 for each time stamp, including
    *    Normalized difference vegetation index (NDVI) image, which is the a RGB image, where green indicates forest cover. 
    *   Cloud cover masks
*   From S3, the data is analyzed using the following method:
    *   For each timestamp, the cloud cover mask is used to remove pixels from the NDVI image.
    *   The number of tree cover pixels (green) are counted. We know both raster datasets are at a 10 meter resolution so the area of the tree cover can be converted to relatable area (football fields)
*   AWS Lambda is used to run the solution at scale.
*   The API takes the user input for month and spatial location and saves the resulting counts to S3 output.

## Further development of the solution would include:

*   Pulling data directly from ASDI, rather than using the SentinalHub. The raw data need preprocessing, including calculation of NDVI, which that was already completed in SentinalHub.
*    Using Artificial Intelligence techniques, predicting pixel values instead of masking out cloud cover.
*    Predicting when the deforestation is going to happen using Relation Learning.
    *   This could be used to relocate all the people from unsustainable areas to the nearest sustainable location



## Limitations:

*   Most of the images couldn't cover complete area because of cloud cover.
*   There is a chance of  NDVI value being corrupted.
*   Masking RGB image using Cloud cover is naive way of solving a problem.
