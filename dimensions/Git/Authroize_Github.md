The issue could be that Github isn't present in your ~/.ssh/known_hosts file.

Append GitHub to the list of authorized hosts
```bash
ssh-keyscan -H github.com >> ~/.ssh/known_hosts
```
