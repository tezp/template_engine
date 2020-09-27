# Template Engine :

0. Install required pip packages.
```bash
  pip3 install -r requirements.txt
```
1. Run seperate store_system_template.py file to store templates.
```bash
  python3 store_system_template.py
```
2. Start django server.
```bash
   python3 manage.py runserver
```
3. Post request :
```bash
   curl -X POST  http://127.0.0.1:8000/te/customer/1/templates 
```
4. Get request :
```bash
   curl http://127.0.0.1:8000/te/customer/1/templates 
```
5. Run Testcase
```bash
   python3 manage.py test
