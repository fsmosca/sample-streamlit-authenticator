# Sample Streamlit authenticator

Authenticates users to use the multi-page [streamlit](https://streamlit.io/) app using [streamlit-authenticator library](https://github.com/mkhorasani/Streamlit-Authenticator). This sample app can survive page reloads courtesy from streamlit-authenticator library.

![image](https://github.com/fsmosca/sample-streamlit-authenticator/assets/22366935/727cf7af-555f-4f21-aeed-f8ddca8c28aa)

## A. Register page with role

![image](https://github.com/fsmosca/sample-streamlit-authenticator/assets/22366935/6f3b60fb-9657-44e1-aa9c-e81a3f1e7dee)

## B. Saving users info in config.yaml

If you deploy an app in streamlit community cloud, and you accept registration, do not save the config.yaml file in that streamlit container because there is no guarantee that the file will be saved. You can save it in other cloud storage such as Deta space.

## C. Credentials

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
