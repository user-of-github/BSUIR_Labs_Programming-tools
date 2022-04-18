## ___Packer__ — a library for easy auto-serialization of different kinds of Python objects_

&nbsp;

### Project structure:

![](scheme.svg)

### Idea of my project:

#### JSON:

All kinds of objects are transformed to dictionary. Even primitives.   
Example: `var: int = 42` => `{ type: 'int', value: 42}`. Complex objects are simplified and transformed to dictionaries
of primitives. And dictionary with usual primitives can be easily serialized just with `str(dictionary)`.  
Now about decoding. I have a string with a view like: `'{ "type": "int", "value": 42}'`. I parse it with my self-made
JSON-parser and form the same dictionary as I had before serialization. Then this dictionary is computed — and I receive an object.  
&nbsp;

###### © 2022 | BSUIR
