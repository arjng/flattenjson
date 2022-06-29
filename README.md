# Flatten JSON 

a program that takes a JSON object as input and outputs a flattened version of the JSON object, with keys as the path to every terminal value in the JSON
structure. 

Takes input via stdin.

Assumptions:
1. The input JSON will not contain arrays
2. All keys named in the original object will be simple strings without ‘.’ characters

## Usages:
```
echo '<Json string>'' | python3 flatten_json.py
```

```
cat ex.json | python3 flatten_json.py
```

```
python3 flatten_json.py
<Json String>
<EOF>
```

## Example 1
### Command 
```
echo '{
"a": 1,
"b": true,
"c": {
"d": 3,
"e": "test"
} }
' | python3 flatten_json.py
```

### Output 
```
{"a": 1, "b": true, "c.d": 3, "c.e": "test"}
```

## Example 2
### Command line

    cat ex.json | python3 flatten_json.py


### ex.json
```
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test",
        "f": {"x": "fast", "y": 3, "c": {"d": false}, "e": 2},
        "g": {"1": 3, "2": true},
        "h": 2
    },
    "y": "x"
}
```

### Output
```
    {
		    "a": 1,
		    "b": True,
		    "c.d": 3,
		    "c.e": "test",
		    "c.f.x": "fast",
		    "c.f.y": 3,
		    "c.f.c.d": False,
		    "c.f.e": 2,
		    "c.g.1": 3,
		    "c.g.2": True,
		    "c.h": 2,
		    "y": "x",
		}
```		