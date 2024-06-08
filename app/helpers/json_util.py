import json
import inspect

# Add classes to this list
# Every class in this list needs to have classname, to_json(), and from_json()
CLASS_NAMES = ['OHLC', 'Order', 'KrakenOrder', 'GRIDBot', 'KrakenGRIDBot', 'Exchange', 'KrakenExchange', 'CoinbaseExchange', 'RobinhoodCryptoExchange']

class OHLC:
    """
    Example for any user-defined class
    """
    def __init__(self, open, high, low, close):
        self.classname = 'OHLC'
        self.open = open
        self.high = high
        self.low = low
        self.close = close
    
    def to_json(self):
        return vars(self)
    
    @classmethod
    def from_json(cls, json_data):
        # Get the parameters of the __init__ method
        init_params = inspect.signature(cls.__init__).parameters

        # Extract known attributes
        known_attributes = {param for param in init_params if param != 'self'}
        known_data = {k: v for k, v in json_data.items() if k in known_attributes}

        # Extract additional attributes
        additional_data = {k: v for k, v in json_data.items() if k not in known_attributes}

        # Create instance with known attributes
        instance = cls(**known_data)

        # Set additional attributes
        for key, value in additional_data.items():
            if isinstance(value, dict) and 'classname' in value and value['classname'] in CLASS_NAMES:
                exec(f'setattr(instance, key, {value["classname"]}.from_json(value))')
            else:
                setattr(instance, key, value)
        
        return instance

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        for class_name in CLASS_NAMES:
            if hasattr(obj, '__class__') and obj.__class__.__name__ == class_name:
                return obj.to_json()
        return super().default(obj)

class MyClass:
    """
    Example of any user-defined class that is going to be exported or imported
    """
    def __init__(self, var1, var2, var3):
        self.classname = 'MyClass'
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = 0
    
    def to_json_file(self, filename):
        data = vars(self)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, cls=CustomEncoder)
    
    @classmethod
    def from_json_file(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Get the parameters of the __init__ method
        init_params = inspect.signature(cls.__init__).parameters

        # Extract known attributes
        known_attributes = {param for param in init_params if param != 'self'}
        known_data = {k: v for k, v in data.items() if k in known_attributes}

        # Extract additional attributes
        additional_data = {k: v for k, v in data.items() if k not in known_attributes}

        # Create instance with known attributes
        instance = cls(**known_data)

        # Set additional attributes
        for key, value in additional_data.items():
            setattr(instance, key, cls.recursive_object_creation(value))
        
        return instance
    
    @classmethod
    def recursive_object_creation(cls, data):
        if isinstance(data, dict):
            if 'classname' in data and data['classname'] in CLASS_NAMES:
                # If the data is a dictionary with a 'classname' key, create an instance of the class
                obj = globals()[data['classname']](*[data[attr] for attr in inspect.signature(globals()[data['classname']]).parameters.keys() if attr != 'self'])
                for key, value in data.items():
                    if key != 'classname':
                        # Recursively set additional attributes
                        setattr(obj, key, cls.recursive_object_creation(value))
                return obj
            else:
                # If the data is a regular dictionary, recursively handle its values
                return {k: cls.recursive_object_creation(v) for k, v in data.items()}
        elif isinstance(data, list):
            # If the data is a list, recursively handle each element in the list
            return [cls.recursive_object_creation(item) for item in data]
        else:
            # Base case: return data as is
            return data

if __name__ == '__main__':
    # Example usage
    # Create an instance of MyClass
    obj = MyClass("value1", "value2", "value3")

    # Set additional attributes outside of the class definition
    obj.map = {'x': 0, 'y': 1}
    obj.data = [1, 2, 3, 4, 5]

    obj.ohlc = OHLC(1, 10, 0.5, 6)

    obj.ohlc.time = 1000

    obj.ohlc.extra_ohlc = OHLC(1, 2, 3, 4)
    obj.map['nested_ohlc'] = OHLC(9, 8, 7, 6)

    # Export to JSON file
    obj.to_json_file('my_class_data.json')

    # Import from JSON file
    imported_obj = MyClass.from_json_file('my_class_data.json')

    # Access the imported object's member variables and additional attributes
    print(imported_obj.classname)
    print(imported_obj.var1)
    print(imported_obj.var2)
    print(imported_obj.var3)
    print(imported_obj.var4)
    print(imported_obj.map)
    print(imported_obj.data)
    print(imported_obj.ohlc)

    print(imported_obj.ohlc.open)
    print(imported_obj.ohlc.time)
    print(imported_obj.ohlc.classname)
    print(imported_obj.ohlc.extra_ohlc.high)
    print(imported_obj.map['nested_ohlc'].high)
