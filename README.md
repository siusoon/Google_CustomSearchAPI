# Google_CustomSearchAPI

The Google Image Search API has been officially deprecated as of May 26, 2011. Google recommends its users to use the Custome Search Engine. This repository demonstrates how to connect with the custom search API in PERL and Javascript (p5.js). 

## Steps:
1. Check out [Custom Search API](https://developers.google.com/custom-search/)
2. Get a key [here](https://developers.google.com/custom-search/json-api/v1/overview)
3. Create a new search engine id: https://cse.google.com/all

## Screenshots:
PERL:

<img src="https://github.com/siusoon/Google_CustomSearchAPI/blob/master/screenshot_cgiResult.png" width = "500">

p5js:

<img src="https://github.com/siusoon/Google_CustomSearchAPI/blob/master/flowers.gif">

## Notes:
1. Replace your own API key, Engine ID (cx) and Query parameters
2. For the PERL script, I used macport and installed CPAN, LWP and JSON.
  - See here for [CPAN](http://www.cpan.org/modules/INSTALL.html).
  - See here for [macports](https://guide.macports.org/).
  - Terminal commands for LWP and JSON: sudo cpan JSON, sudo cpan JSON::Parse.
