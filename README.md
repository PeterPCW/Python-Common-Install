# Python Common Install requirements.txt

## Note

This is a generalized requirements.txt to install common packages for python development. I will add packages as I need them. Using >= allows for forward compatibility to always install newest.

## Usage

Run: "pip install -U -r requirements.txt"

Then: "python freeze > requirements.txt" to update, but afterward you have to Find -> Replace All "==" with ">=".