## Complete Labs 74 and 75

Run the following command:

`student@bchd:~$` `cd && wget https://raw.githubusercontent.com/csfeeser/Python/master/challenges/classdata.json -qO "classdata.json"`

```
[{"name":"Will","awesome":true,"favorites":{"movie":"Serenity","ice cream":"rocky road","color":"orange"}},{"name":"Justin","awesome":true,"favorites":{"movie":"John Wick","ice cream":"Coffee","color":"blue"}},{"name":"Chris","awesome":true,"number":15,"favorites":{"movie":"Star Wars","ice cream":"bacon","color":"purple"}},{"name":"Samekh","awesome":true,"number":14,"favorites":{"movie":"Requiem for a Dream","ice cream":"strawberry","color":"Ox Blood"}},{"name":"Cat","awesome":true,"number":13,"favorites":{"movie":"Mean Girls","ice cream":"Coffee","color":"green"}},{"name":"Nikko","awesome":true,"number":12,"favorites":{"movie":"Multiplicity","ice cream":"Superman","color":"black"}},{"name":"Marcos","awesome":true,"number":11,"favorites":{"movie":"The Last Airbender","ice cream":"bacon","color":"dark brown"}},{"name":"Mannie","awesome":true,"number":10,"favorites":{"movie":24,"ice cream":"vanilla","color":"blue"}}]
```

Do the following:

- Import the json file as a file object
- Add yourself to this list! If you're already in this list, add a fictional character :)
- Output the data as a YAML file.

## SOLUTION

```python
import json
import yaml

# open file with json, convert to python object
with open("classdata.json","r") as jsonfile:
    x= json.load(jsonfile)

# create new python dictionary to be added
new= {
      "name":"Chad",
      "awesome": False,
      "number": 0,
      "favorites":{
          "movie":"The Shawshank Redemption",
          "ice cream":"salted caramel",
          "color":"red"}
     }

# add to data read in from json file
x.append(new)

# open a yaml file and dump the changed data inside it
with open("classdataedit.yml","w") as yamlfile:
    yaml.dump(x, yamlfile)
```
