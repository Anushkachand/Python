# PyJokes Module
- **pyjokes** is a fun Python module used to generate programming jokes. It’s mostly used for entertainment, demos, or learning Python modules.

1. Install Module (Pyjokes)

-  pip install Module name 
 eg: 
 ```
 pip install pyjokes
 ```

### Exmple:
```
    import pyjokes
    
    joke = pyjokes.get_joke()
    print(joke)
```
👉 Output example:
```
    Why do programmers prefer dark mode? Because light attracts bugs!
```
### Get caategory of Jokes
📌 Categories:
- neutral
- chuck

```
 import pyjokes

 <!-- Categories of jokes -->
 jokes = pyjokes.get_jokes(catgory = 'netural')
 print(jokes)
```

4. Get Multiple Jokes
```
import pyjokes

jokes = pyjokes.get_jokes()

for j in jokes:  
    print(j)
```    

5. Language Support 🌍
```
import pyjokes

joke = pyjokes.get_joke(language='en')
print(joke)
```

📌 Languages:
- en (English)
- de (German)
- es (Spanish)
