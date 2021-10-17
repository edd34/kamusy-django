# API Kamusy

In this file you will find documentation about the Kamusy API.
The base API URL is http://kamusy.yt:8000

## 1. Language component

### a. Get all languages

-     GET: /languages

Description : return a JSON containing all languages in the database
Example : [http://kamusy.yt:8000/languages/](http://kamusy.yt:8000/languages/)

## 2. Word component

### a. Get all words

-     GET: /words/

Description : return a JSON containing all words in the database
Example : [http://kamusy.yt:8000/words/](http://kamusy.yt:8000/words/)

### b. Fuzzy search a word

-     GET: /find-words/<str:pattern>/<int:language_src_id>/

Description : fuzzy search words in the language identified by `language_id` and with string pattern `string`
Example : [http://kamusy.yt:8000/find-words/som/1/](http://kamusy.yt:8000/find-words/som/1/)

## 3. Translation component

The translation object have the following structure :

```json
[
{"id": 1129,
"word_source_name": "usoma",
"word_destination_name": "lire",
"language_source_name": "mahorais",
"language_destination_name": "fran\u00e7ais",
"word_source": 1065,
"language_source": 1,
"word_destination": 1066,
"language_destination": 2},
...
]
```

It is a list of json.

_NB : if a translation doesn't exist in the database, an empty list is returned :_ `[]`

### a. Get all translations

-     GET: /translations/

Description : return a JSON containing all translations in the database
Example : [http://kamusy.yt:8000/translations/](http://kamusy.yt:8000/translations/)

### b. Translate one word from a language to another

-     GET: /get-translation/<int:word_id>/<int:language_src_id>/<int:language_dst_id>/

Description : Return the translation of one word from a source language to a destination language.
Example : [http://kamusy.yt:8000/get-translation/1065/1/2/](http://kamusy.yt:8000/get-translation/1065/1/2/)
This example will return

```json
[
  {
    "id": 1129,
    "word_source_name": "usoma",
    "word_destination_name": "lire",
    "language_source_name": "mahorais",
    "language_destination_name": "fran\u00e7ais",
    "word_source": 1065,
    "language_source": 1,
    "word_destination": 1066,
    "language_destination": 2
  },

  {
    "id": 1131,
    "word_source_name": "usoma",
    "word_destination_name": "\u00e9tudier",
    "language_source_name": "mahorais",
    "language_destination_name": "fran\u00e7ais",
    "word_source": 1065,
    "language_source": 1,
    "word_destination": 1067,
    "language_destination": 2
  },

  {
    "id": 1389,
    "word_source_name": "usoma",
    "word_destination_name": "apprendre",
    "language_source_name": "mahorais",
    "language_destination_name": "fran\u00e7ais",
    "word_source": 1065,
    "language_source": 1,
    "word_destination": 1286,
    "language_destination": 2
  }
]
```

Translation of word `usoma` from mahorais to french will return 3 words : `lire`, `étudier` and `apprendre`.
