"""
The Singleton pattern ensures that only one instance of a class is created and provides a global point of access to that instance.

Here’s a simple and clean Python implementation using a class decorator (one of the Pythonic ways to do it):

⸻


"""

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MySingleton:
    def __init__(self, value):
        self.value = value

# Usage:
a = MySingleton(10)
b = MySingleton(20)

print(a.value)  # Output: 10
print(b.value)  # Output: 10 (same instance as 'a')
print(a is b)   # Output: True

"""
What’s happening here:
	•	The singleton decorator wraps your class and ensures that no matter how many times you instantiate it, you always get the same object.
	•	Even though b = MySingleton(20) looks like it’s making a new instance, it reuses the same one created by a = MySingleton(10).

⸻

Alternative: Singleton using __new__

This is more classic/OOP-style:
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MySingleton(Singleton):
    def __init__(self, value):
        self.value = value

# Usage:
a = MySingleton(10)
b = MySingleton(20)

print(a.value)  # 20 (note: __init__ runs every time!)
print(a is b)   # True

"""
 Caveat: In this pattern, __init__ still runs each time you instantiate, which can be confusing. The decorator approach is often clearer for many use cases.

⸻
if your app might run in a multi-threaded environment (like web servers).

Here’s a thread-safe Singleton using Python’s threading.Lock:
"""


import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()  # Ensures thread safety

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class MySingleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Usage:
a = MySingleton(10)
b = MySingleton(20)

print(a.value)  # Output: 10
print(b.value)  # Output: 10
print(a is b)   # Output: True

""" 
Why this works well:
	•	We use a metaclass (SingletonMeta) to control how the class is instantiated.
	•	The threading.Lock() ensures only one thread at a time can create the instance.
	•	This is a robust pattern and is a favorite in Python interviews when thread safety is needed.

Here’s a simple diagrammatic explanation of how the thread-safe Singleton pattern works in the last example

+-----------------------+
|     MySingleton       |
+-----------------------+
|  - value              |
+-----------------------+
|  __init__(value)      |
+-----------------------+
            |
            |
         (inherits)
            |
+-----------------------+
|   SingletonMeta       |
+-----------------------+
|  _instances (dict)    |
|  _lock (Lock)         |
+-----------------------+
|  __call__(*args)      |
+-----------------------+
            |
            |
       (at instantiation)
            |
            +--------------------------------------------------+
            |                                                  |
       Thread 1                                        Thread 2 (simultaneous)
            |                                                  |
      Acquire _lock                                    Wait for lock
            |                                                  |
  Check if class in _instances                      (blocked until lock released)
            |
   If not, create instance
            |
   Store in _instances
            |
   Release _lock
            |
      Return instance                                Now Thread 2 resumes:
                                                     - See instance already created
                                                     - Return existing instance


                                                     
✅ Key points:
	•	The metaclass (SingletonMeta) controls instantiation.
	•	The _lock ensures that only one thread can create the instance at a time.
	•	Other threads reuse the already-created instance once it exists.
                                                        
"""