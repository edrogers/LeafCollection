#!/bin/bash

nowdate=$(date +%s)

curl http://www.cityofmadison.com/streets/yardWaste/brush/brushWest.cfm -o /home/${USER}/LeafCollection/Brush/${nowdate}-home.html
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_2.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map2.pdf
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_4.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map4.pdf
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_6.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map6.pdf
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_8.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map8.pdf
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_10.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map10.pdf

curl http://www.cityofmadison.com/streets/yardWaste/brush/brushEast.cfm -o /home/${USER}/LeafCollection/Brush/${nowdate}-East-home.html
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_1.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map1.pdf
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_3.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map3.pdf
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_5.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map5.pdf
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_7.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map7.pdf
curl http://www.cityofmadison.com/streets/documents/brush/BRUSH_COLLECTION_DISTRICT_9.pdf -o /home/${USER}/LeafCollection/Brush/${nowdate}-map9.pdf

sleep 60
/home/${USER}/LeafCollection/notifyBrush.py

exit
