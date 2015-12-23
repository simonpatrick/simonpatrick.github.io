#!/bin/bash

tom_catalog="jenkins"

PRECESS_NUM=$(ps -ef |grep "$tom_catalog" |grep -v "grep" |wc -l)

# get pid
#pid 
