```
Menu = quart_imp.auth/generate_salt
Title = generate_salt - quart_imp.auth
```

```python
from quart_imp.auth import generate_salt
```

```python
generate_salt(length: int = 4) -> str
```

---

Generates a string of (length) characters of punctuation.

The Default length is 4.

For use in password hashing and storage of passwords in the database.

##### Example:

```python
generate_salt()  # >>> '*!$%'
```

```python
@app.route('/register', methods=['GET', 'POST'])
async def register():
    if request.method == "POST":
        ...
        salt = generate_salt()
        password = request.form.get('password')
        encrypted_password = encrypt_password(password, salt)
        ...

        user = User(
            username=username,
            email=email,
            password=encrypted_password,
            salt=salt
        )
        ...
```

