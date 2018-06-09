# project-koff-web

Mobile app available [here](https://github.com/dinoilic/project-koff-ma)

## Setup

Create a file *project\_koff\_web/config/\_\_init\_\_.py* with 
following content:

```
from .local import Local
from .production import Production

GOOGLE_API_KEY = 'YOUR_API_KEY'
```
