#!/usr/bin/env bash

{
    test -e ./database.db &&
        echo ">>> Database already created!"
} ||
    {
        echo -n ">>> Building database..."
        python ./init_db.py
        echo "done!"
    }
