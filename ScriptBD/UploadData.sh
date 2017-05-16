#!/bin/bash
if [ "$1" != "" ]
then
    mongoimport --db Reclamoscl --collection reclamos --type json --file $1 --jsonArray
else
    printf "File directory is needed.\n./ScriptBD.sh <file_directory>\n"
fi
