# Test Users Login Information

All test users have the password: **`Password_1`**

## Available Test Accounts:

1. **traceh38@gmail.com**
   - Role: Superuser/Admin
   - Name: test superuser
   - Password: `Password_1`

2. **testuser1@testuser.com**
   - Role: Regular user
   - Name: test user1
   - Password: `Password_1`

3. **testuser2@testuser.com**
   - Role: Regular user
   - Name: test user2
   - Password: `Password_1`

4. **testuser3@testuser.com**
   - Role: Regular user
   - Name: test user3
   - Password: `Password_1`

## Loading Fixtures

To load the test data:
```bash
python3 manage.py loaddata accounts/fixtures/test_users.json
python3 manage.py loaddata accounts/fixtures/initial_skills.json
python3 manage.py loaddata accounts/fixtures/profiles.json
```