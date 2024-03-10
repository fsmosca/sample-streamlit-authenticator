# sample-streamlit-authenticator
Authenticates users to use the streamlit App.

## Credentials

```
username: jsmith, password: abc
username: rbriggs, password: def
```

*config.yaml*

username jsmith being an admin has access to all pages such as page1 and page2. While rbriggs being a user as role can only access page2.

```
cookie:
  expiry_days: 30
  key: some_signature_key
  name: some_cookie_name
credentials:
  usernames:
    jsmith:
      email: jsmith@gmail.com
      logged_in: false
      name: John Smith
      password: $2b$12$qgpdymNsKCf9Hjwg.NSXiO9/ItCdKVNoJBWQf6EAk9n73HgkAJmEC
      role: admin
    rbriggs:
      email: rbriggs@gmail.com
      logged_in: false
      name: Rebecca Briggs
      password: $2b$12$uON60sh.2IdIk4cka2YILuRo4kQai.pU8McK/owmmJ.QawK85GrdK
      role: user
preauthorized:
  emails:
  - melsby@gmail.com
```
