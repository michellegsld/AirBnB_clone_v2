### README for web_flask ###
#### A directory within the Air_BnB_clone_v2 repo ####

| File Name | Description |
| --------- | ----------- |
| __init__.py | The file to make the folder a package. |
| 0-hello_route.py | Starts a Flask web application that must be listening on `0.0.0.0`, port `5000`. The option `strict_slashes=False` must be in the route definition. The route `/` displays "Hello HBNB!". |
| 1-hbnb_route.py | It continues off the previous file, adding the route `/hbnb` and displaying "HBNB". |
| 2-c_route.py | It continues off the previous file, adding the route `/c/<text>` and displaying “C ” followed by the value of the text variable (after replacing `_` with spaces). |
| 3-python_route.py | It continues off the previous file, adding the route `/python/(<text>)` and displaying “Python ”, followed by the value of the text variable (after replacing `_` with spaces). The text (and that slash) is optional as the default value of `text` is “is cool”. |
| 4-number_route.py | It continues off the previous file, adding the route `/number/<n>` and displaying “n is a number”, but only if `n` is an integer. |
| 5-number_template.py | It continues off the previous file, adding the route `/number_template/<n>` and displaying an HTML page but only if `n` is an integer. (`H1` tag: “Number: n” inside the tag `BODY`) |
| 6-number_odd_or_even.py | It continues off the previous file, adding the route `/number_odd_or_even/<n>` and displaying an HTML page but only if `n` is an integer. (`H1` tag: “Number: n is even|odd” inside the tag `BODY`) |
| templates | A folder containing the files `5-number.html` and `6-number_odd_or_even.html`. These are used in tasks 5 and 6 (files `5-number_template.py` and `6-number_odd_or_even.html`). |
