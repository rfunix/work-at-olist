# Work at Olist

## Api Host -> https://agile-headland-13957.herokuapp.com

## How to locally running

### Requirements:
* Python3.5 + [https://www.python.org/]
* VirtualEnv
* Python PIP
* PostgreSQL [https://www.postgresql.org/]

### Steps:

1. Clone this repository
2. Create virtualenv using python 3.5 + e.g. virtualenv -p python3.5 envname
3. Install python dependencies: pip install -r requirements-local.txt
4. Create database.
5. Edit local.env file with your configurations.
6. Export env variables e.g. export $(cat local.env | xargs)
7. Run migration for create database tables e.g. python3.6 work-at-olist/manage.py migrate
8. Import Channel and Categories using test.csv file e.g. python3.6 work-at-olist/manage.py importcategories walmart test.csv
9. Start Api: python work-at-olist/manage.py runserver

## How to run tests:

```text
python3.6 work-at-olist/manage.py test api
```

## How to import Channels and Categories:

```text
python3.6 work-at-olist/manage.py importcategories {channel_name} {csv_file_path}
```

#### e.g.

```
python3.6 work-at-olist/manage.py importcategories "Magazine Luiza" test.csv
```

##### Observation: This csv file must have the "/" separator character.


## Api Endpoints:


#### List Channels.

```text
GET /api/channels/
```
##### Response:

```json
[
    {
        "name": "Magazine Luiza",
        "slug": "magazine-luiza"
    }
]
```

#### List all categories and subcategories of a channel.

```text
GET /api/channel-categories/{channel-slug}/
```

##### e.g.

```text
GET /api/channel-categories/magazine-luiza/
```

##### Response:

```json
[
    {
        "name": "Auto",
        "slug": "auto",
        "children": [
            {
                "name": "Cars",
                "slug": "cars",
                "children": [
                    {
                        "name": "Motor",
                        "slug": "motor",
                        "children": []
                    }
                ]
            }
        ]
    },
    {
        "name": "Books",
        "slug": "books",
        "children": [
            {
                "name": "Computers",
                "slug": "computers",
                "children": [
                    {
                        "name": "Applications",
                        "slug": "applications",
                        "children": []
                    },
                    {
                        "name": "Database",
                        "slug": "database",
                        "children": []
                    },
                    {
                        "name": "Programming",
                        "slug": "programming",
                        "children": []
                    }
                ]
            },
            {
                "name": "Foreign Literature",
                "slug": "foreign-literature",
                "children": []
            },
            {
                "name": "National Literature",
                "slug": "national-literature",
                "children": [
                    {
                        "name": "Fiction Fantastic",
                        "slug": "fiction-fantastic",
                        "children": []
                    },
                    {
                        "name": "Science Fiction",
                        "slug": "science-fiction",
                        "children": []
                    }
                ]
            }
        ]
    },
    {
        "name": "Computers",
        "slug": "computers",
        "children": [
            {
                "name": "Desktop",
                "slug": "desktop",
                "children": []
            },
            {
                "name": "Notebooks",
                "slug": "notebooks",
                "children": []
            },
            {
                "name": "Tablets",
                "slug": "tablets",
                "children": []
            }
        ]
    },
    {
        "name": "Games",
        "slug": "games",
        "children": [
            {
                "name": "Playstation 4",
                "slug": "playstation-4",
                "children": []
            },
            {
                "name": "XBOX 360",
                "slug": "xbox-360",
                "children": [
                    {
                        "name": "Accessories",
                        "slug": "accessories",
                        "children": [
                            {
                                "name": "Controller",
                                "slug": "controller",
                                "children": []
                            }
                        ]
                    },
                    {
                        "name": "Console",
                        "slug": "console",
                        "children": []
                    },
                    {
                        "name": "Games",
                        "slug": "games",
                        "children": []
                    }
                ]
            },
            {
                "name": "XBOX One",
                "slug": "xbox-one",
                "children": [
                    {
                        "name": "Accessories",
                        "slug": "accessories",
                        "children": []
                    },
                    {
                        "name": "Console",
                        "slug": "console",
                        "children": []
                    },
                    {
                        "name": "Games",
                        "slug": "games",
                        "children": []
                    }
                ]
            }
        ]
    }
]
```

#### Return a single category with their parent categories and subcategories.

```text
GET /api/category/{category-slug}/
```

##### e.g.

```text
GET /api/category/cars/
```

##### Response:

```json
[
   {
        "name": "Auto",
        "slug": "auto",
        "children": [
            {
                "name": "Cars",
                "slug": "cars",
                "children": [
                    {
                        "name": "Motor",
                        "slug": "motor",
                        "children": []
                    }
                ]
            }
        ]
    }
]
```

