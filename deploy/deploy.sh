#!/bin/sh
rsync -avz --delete --exclude-from=./exclude ../ akiraak@10.0.1.10:~/projects/FirstDL/ 

