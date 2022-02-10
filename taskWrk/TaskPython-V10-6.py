# *** Сериализация


import json
import dataclasses

@dataclasses.dataclass
class A:
    
    x: int



data = {
    'a': A(5)
}

print(json.dumps(data))

#dump_all - пишет только индекс
#print(yaml.dump_all(data))



# End