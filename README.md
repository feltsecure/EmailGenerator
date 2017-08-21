# EmailGenerator
Python script to generate email addresses from names and domain name

### Command Line Arguments
Email generator takes 4 arguments:
1. A file which contains names line by line.
2. A domain name
3. An output file (default is emaillistoutput.txt)
4. A email creation method (default is "fn.ln") which will be one of the followings:

    - ```"fn"``` for ```firstname@domain```
    - ```"ln"``` for ```lastname@domain```
    - ```"fnln"``` for ```first_namelast_name@domain```
    - ```"fn.ln"``` for ```firstname.lastname@domain```
    - ```"filn"``` for ```firstinitiallast_name@domain```
    - ```"fi.ln"``` for  ```firstinitial.lastname@domain```
    - ```"fnli"``` for ```firstnamelastinitial@domain```
    - ```"fn.li"``` for ```firstname.lastinitial@domain```
    - ```"fili"``` for ```firstinitiallastinitial@domain```
    - ```"fi.li"``` for ```firstinitial.lastinitial@domain```
    - ```"lnfn"``` for ```lastnamefirstname@domain```
    - ```"ln.fn"``` for ```lastname.firstname@domain```
    - ```"lnfi"``` for ```lastnamefirstinitial@domain```
    - ```"ln.fi"``` for ```lastname.firstinitial@domain```
    - ```"lifn"``` for ```lastinitialfirstname@domain```
    - ```"li.fn"``` for ```lastinitial.firstname@domain```
    - ```"lifi"``` for ```lastinitialfirstinitial@domain```
    - ```"li.fi"``` for ```lastinitial.firstinitial@domain```
    - ```"fimiln"``` for ```firstinitialmiddleinitiallastname@domain```
    - ```"fimi.ln"``` for ```firstinitialmiddleinitial.lastname@domain```
    - ```"fnmiln"``` for ```firstnamemiddleinitiallastname@domain```
    - ```"fn.mi.ln"``` for ```firstname.middleinitial.lastname@domain```
    - ```"fnmnln"``` for ```firstnamemiddlenamelastname@domain```
    - ```"fn.mn.ln"``` for ```firstname.middlename.lastname@domain```
    - ```"fn-ln"``` for ```firstname-lastname@domain```
    - ```"fi-ln"``` for ```firstinitial-lastname@domain```
    - ```"fn-li"``` for ```firstname-lastinitial@domain```
    - ```"fi-li"``` for ```firstinitial-lastinitial@domain```
    - ```"ln-fn"``` for ```lastname-firstname@domain```
    - ```"ln-fi"``` for ```lastname-firstinitial@domain```
    - ```"li-fn"``` for ```lastinitial-firstname@domain```
    - ```"li-fi"``` for ```lastinitial-firstinitial@domain```
    - ```"fimi-ln"``` for ```firstinitialmiddleinitial-lastname@domain```
    - ```"fn-mi-ln"``` for ```firstname-middleinitial-lastname@domain```
    - ```"fn-mn-ln"``` for ```firstname-middlename-lastname@domain```
    - ```"fn_ln"``` for ```firstname_lastname@domain```
    - ```"fi_ln"``` for ```firstinitial_lastname@domain```
    - ```"fn_li"``` for ```firstname_lastinitial@domain```
    - ```"fi_li"``` for ```firstinitial_lastinitial@domain```
    - ```"ln_fn"``` for ```lastname_firstname@domain```
    - ```"ln_fi"``` for ```lastname_firstinitial@domain```
    - ```"li_fn"``` for ```lastinitial_firstname@domain```
    - ```"li_fi"``` for ```lastinitial_firstinitial@domain```
    - ```"fimi_ln"``` for ```firstinitialmiddleinitial_lastname@domain```
    - ```"fn_mi_ln"``` for ```firstname_middleinitial_lastname@domain```
    - ```"fn_mn_ln"``` for ```firstname_middlename_lastname@domain```
    
### Run
```python emailGenerator.py -d DOMAIN_NAME -f INPUT_FILE -m METHOD -o OUTPUT_FILE```

Example:
```python emailGenerator.py -d "feltsecure.com" -f names.txt -m "fnln" -o output.txt```

### Python Version
2.7.13
