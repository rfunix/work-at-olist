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
8. Import Channel and Categories using test.csv file e.g. python work-at-olist/manage.py importcategories walmart test.csv
9. Start Api: python work-at-olist/manage.py runserver


## How to import Channels and Categories:

```text
python work-at-olist/manage.py importcategories {channel_name} {csv_file_path}
```

#### e.g.

```
python work-at-olist/manage.py importcategories walmart test.csv
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
        "id": 1,
        "name": "walmart"
    }
]
```

#### List all categories and subcategories of a channel.

```text
GET /api/channel-categories/{channel-name}/
```

##### e.g.

```text
GET /api/channel-categories/walmart/
```

##### Response:

```json
[
    {
        "name": "Auto",
        "children": [
            {
                "name": "Cars",
                "children": [
                    {
                        "name": "Motor",
                        "children": []
                    }
                ]
            }
        ]
    },
    {
        "name": "Books",
        "children": [
            {
                "name": "Computers",
                "children": [
                    {
                        "name": "Applications",
                        "children": []
                    },
                    {
                        "name": "Database",
                        "children": []
                    },
                    {
                        "name": "Programming",
                        "children": []
                    }
                ]
            },
            {
                "name": "Foreign Literature",
                "children": []
            },
            {
                "name": "National Literature",
                "children": [
                    {
                        "name": "Fiction Fantastic",
                        "children": []
                    },
                    {
                        "name": "Science Fiction",
                        "children": []
                    }
                ]
            }
        ]
    },
    {
        "name": "Computers",
        "children": [
            {
                "name": "Desktop",
                "children": []
            },
            {
                "name": "Notebooks",
                "children": []
            },
            {
                "name": "Tablets",
                "children": []
            }
        ]
    },
    {
        "name": "Games",
        "children": [
            {
                "name": "Playstation 4",
                "children": []
            },
            {
                "name": "XBOX 360",
                "children": [
                    {
                        "name": "Accessories",
                        "children": [
                            {
                                "name": "Controller",
                                "children": []
                            }
                        ]
                    },
                    {
                        "name": "Console",
                        "children": []
                    },
                    {
                        "name": "Games",
                        "children": []
                    }
                ]
            },
            {
                "name": "XBOX One",
                "children": [
                    {
                        "name": "Accessories",
                        "children": []
                    },
                    {
                        "name": "Console",
                        "children": []
                    },
                    {
                        "name": "Games",
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
GET /api/category/{category}/
```

##### e.g.

```text
GET /api/category/Cars/
```

##### Response:

```json
[
    {
        "name": "Auto",
        "children": [
            {
                "name": "Cars",
                "children": [
                    {
                        "name": "Motor",
                        "children": []
                    }
                ]
            }
        ]
    }
]
```

