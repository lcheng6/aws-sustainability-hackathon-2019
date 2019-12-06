import requests
import boto3

#this is just to download images into s3
def getImages:
    INST_ID = "94d32b14-8b42-48a6-bd26-31ffd21dff04"

    timeIntervals = ["2019-05-04/2019-05-04", "2019-05-09/2019-05-09", "2019-05-14/2019-05-14", "2019-05-19/2019-05-19", "2019-05-24/2019-05-24", "2019-05-29/2019-05-29"]
    timeInterval = timeIntervals[0]

    image_request=f"https://services.sentinel-hub.com/ogc/wms/{INST_ID}?showLogo=false&service=WMS&request=GetMap&layers=CLOUDCOVERMASK&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&maxcc=100&time={timeIntervals}&height=512&width=512&srs=EPSG%3A3857&bbox={{bbox-epsg-3857}}"


    # cloud cover image requests, spread over 10 observeration periods.

    layerName='TRUE_COLOR'
    layerName='CLOUDCOVERMASK'
    index = 0
    for timeInterval in timeIntervals:

        #example request
        image_request="https://services.sentinel-hub.com/ogc/wms/94d32b14-8b42-48a6-bd26-31ffd21dff04?showLogo=false&service=WMS&request=GetMap&layers=TRUE_COLOR&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&maxcc=100&time=2017-05-19/2017-05-19&height=512&width=512&srs=EPSG%3A3857&bbox=-7259683.198412901,-1076233.358255282,-7240115.319171894,-1056665.4790142775"
        image_request=f"https://services.sentinel-hub.com/ogc/wms/{INST_ID}?showLogo=false&service=WMS&request=GetMap&layers={layerName}&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&maxcc=100&time={timeInterval}&height=512&width=512&srs=EPSG%3A3857&bbox=-7259683.198412901,-1076233.358255282,-7240115.319171894,-1056665.4790142775"

        print(image_request)
        req = requests.get(image_request)
        print(req)

        open(f"/tmp/cloud-{index}.jpeg", 'wb').write(req.content)

        index = index + 1

    #nvdi image requests

    layerName='NDVI_CUSTOMIZED'
    index = 0
    for timeInterval in timeIntervals:

        #example request
        image_request="https://services.sentinel-hub.com/ogc/wms/94d32b14-8b42-48a6-bd26-31ffd21dff04?showLogo=false&service=WMS&request=GetMap&layers=TRUE_COLOR&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&maxcc=100&time=2017-05-19/2017-05-19&height=512&width=512&srs=EPSG%3A3857&bbox=-7259683.198412901,-1076233.358255282,-7240115.319171894,-1056665.4790142775"

        image_request=f"https://services.sentinel-hub.com/ogc/wms/{INST_ID}?showLogo=false&service=WMS&request=GetMap&layers={layerName}&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&maxcc=100&time={timeInterval}&height=512&width=512&srs=EPSG%3A3857&bbox=-7259683.198412901,-1076233.358255282,-7240115.319171894,-1056665.4790142775"

        print(image_request)
        req = requests.get(image_request)
        print(req)

        open(f"/tmp/nvdi-customized-{index}.jpeg", 'wb').write(req.content)

        index = index + 1

def upload_images_to_s3:
    s3_client = boto3.client('s3')
    bucket = os.environ
    s3_client.upload_file(file_name, bucket, object_name)