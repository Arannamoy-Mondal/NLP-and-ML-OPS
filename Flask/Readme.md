### Flask with minimal requirement



### API Base: http://127.0.0.1
### API endpoints:
- /home
- /about
- /index
- /static/script.js


## Use JS,CSS file in flask.

- 1: Create file in `static` folder.
- 2: Link it from `templates` folder.  

## Changing the Static Folder and URL Path

```py
app = Flask(
    __name__,
    static_folder='assets',           # Physical folder on disk
    static_url_path='/files'          # URL path to access those files
)
```

```css
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```
