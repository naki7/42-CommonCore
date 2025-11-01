#!/bin/bash
find *.sh -print | sed 's|.*/||; s|\.sh$||'
