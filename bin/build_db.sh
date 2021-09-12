#!/usr/bin/env bash
DIR=techtrends

{
    test -s ${DIR}/database.db &&
        echo ">>> Database already created!"
} ||
    {
        echo -n ">>> Building database..."
        cd ${DIR} && python init_db.py
        echo "done!"
    }
