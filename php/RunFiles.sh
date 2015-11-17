#!/bin/sh
echo Starting
for file in /home/www/cs373-idb/php/*.php;do
   echo Running `basename "$file"`
   php `basename "$file"`
done
echo Done
