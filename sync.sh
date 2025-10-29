#!/usr/bin/bash

wget2 \
    --accept=html,htm \
    --adjust-extension \
    --convert-links \
    --domains=linux-sunxi.org \
    --mirror \
    --no-parent \
    --page-requisites \
    --random-wait \
    --retry-on-http-error=403 \
    --timestamping \
    --wait=1 \
    --reject-regex='/File:|/index\.php|/Special:|/Talk:|/User:|/User_talk:|/Template:|/Category:|action=edit|action=history' \
    --user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0" \
    https://linux-sunxi.org/Main_Page
