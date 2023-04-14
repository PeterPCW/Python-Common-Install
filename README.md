# Python Common Install requirements.txt

## Note

This is a generalized requirements.txt to install common packages for python development. I will add packages as I need them. Using >= allows for forward compatibility to always install newest.

## Usage

After syncing this will install the newest version of all packages listed.

```bash
pip install -U -r requirements.txt
```

## Update

After install you can use `freeze` to update the file.

```bash
pip freeze > requirements.txt
```

Note: You will have to Find -> Replace All "==" with ">=" to get back to the forward compatible state.

OR: You can run `DescribePackagesAndReformat.py` to get back to ">=" while adding descriptions like the current file has.
