import requests

INST_ID = "94d32b14-8b42-48a6-bd26-31ffd21dff04"

timeInterval = "2019-12-01/2019-12-01"

image_request=f"https://services.sentinel-hub.com/ogc/wms/{INST_ID}?showLogo=false&service=WMS&request=GetMap&layers=CLOUDCOVERMASK&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&maxcc=100&time={timeInterval}&height=512&width=512&srs=EPSG%3A3857&bbox={{bbox-epsg-3857}}"


# cloud cover image requests

image_request="https://services.sentinel-hub.com/ogc/wms/94d32b14-8b42-48a6-bd26-31ffd21dff04?showLogo=false&service=WMS&request=GetMap&layers=TRUE_COLOR&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&maxcc=100&time=2017-05-19/2017-05-19&height=512&width=512&srs=EPSG%3A3857&bbox=-7259683.198412901,-1076233.358255282,-7240115.319171894,-1056665.4790142775"
req = requests.get(image_request)
open('cloud.jpeg', 'wb').write(req.content)

#nvdi image requests

image_requests =