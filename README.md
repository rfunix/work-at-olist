
#### How to import Channels and Categories:

```text
python work-at-olist/manage.py importcategories {channel_name} {csv_file_path}
```

##### e.g.

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

