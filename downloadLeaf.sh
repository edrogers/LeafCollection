#!/bin/bash

nowdate=$(date +%s)

curl http://www.cityofmadison.com/streets/yardWaste/leaf/LeafWest.cfm -o /home/${USER}/LeafCollection/Leaf/${nowdate}-home.html
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_2.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map2.pdf
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_4.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map4.pdf
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_6.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map6.pdf
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_8.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map8.pdf
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_10.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map10.pdf

curl http://www.cityofmadison.com/streets/yardWaste/leaf/LeafEast.cfm -o /home/${USER}/LeafCollection/Leaf/${nowdate}-East-home.html
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_1.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map1.pdf
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_3.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map3.pdf
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_5.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map5.pdf
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_7.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map7.pdf
curl http://www.cityofmadison.com/streets/documents/leaf/LEAF_COLLECTION_DISTRICT_9.pdf -o /home/${USER}/LeafCollection/Leaf/${nowdate}-map9.pdf

sleep 60
/home/${USER}/LeafCollection/notifyLeaf.py

exit
