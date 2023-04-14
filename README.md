# Python Common Install

This is a generalized requirements.txt to install common packages for python development. I will add packages as I need them. Using >= allows for forward compatibility to always install newest.

## Files

* `requirements.txt` has all of the python packages with descriptions
* `requirements.txt_backup` has all of the packages without descriptions - if that's more your thing
* `DescribePackagesAndReformat.py` is a script to convert a requirements.txt_backup style list into a requirements.txt style list, for after you `freeze` your system setup back into `requirements.txt` (see below)

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

OR: You can run `DescribePackagesAndReformat.py` to get back to ">=" while adding descriptions like the current file has. This will update and overwrite requirements.txt_backup as well.
