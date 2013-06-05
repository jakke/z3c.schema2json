# can't do these imports in the package __init__ 
# because of namespace availability issues
from z3c.schema2json._schema2json import serialize
from z3c.schema2json._schema2json import serialize_to_dict
from z3c.schema2json._schema2json import deserialize
