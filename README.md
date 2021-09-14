# Polls API - test for job

### Docker instalation

- clone repo
```sh
git clone https://github.com/jlomuk/test_api.git
```
- move in directory "test_api"

```sh
cd test_api
```
- create .env and  enter enviroment values
```sh
touch .env
```
**Example env file:**
```sh
SECRET_KEY=1dsfdfhe6w!tetfg43325thuth2l(x@54565)))mt6pykq1diq%i0-=5(y-to9yos8m&0svzfv
DEBUG=0
ALLOWED_HOSTS=['*']
POSTGRES_DB=polls
POSTGRES_USER=admin
POSTGRES_PASSWORD=adminpass
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
- start docker-compose 

```sh
docker-compose up
```
- after start docker containers,  the site will be available on http://127.0.0.1:8000/



#### Documentation API:
go to http://127.0.0.1:8000/swagger

#### account SuperUser:
**admin: admin**
