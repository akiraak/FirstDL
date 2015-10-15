#!/bin/sh
#rsync --dry-run -avz --delete --exclude-from=./deploy_exclude ./ akiraak@10.0.1.10:~/projects/FirstDL/ 
rsync -avz --delete --exclude-from=./deploy_exclude ./ akiraak@10.0.1.10:~/projects/FirstDL/ 

