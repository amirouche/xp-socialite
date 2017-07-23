all:
	@echo "Héllo, World!"

backend:
	adev runserver socialite/web.py --no-debug-toolbar > /dev/null

lint:
	@pylint socialite

database-repl:
	sudo -u postgres psql socialite

database-reset:
	sudo -u postgres dropdb socialite
	sudo -u postgres createdb socialite

build-doc:
	cd doc && make html
	firefox doc/build/html/index.html

upstream:
	mkdir upstream
	git clone https://github.com/MagicStack/asyncpg upstream/asyncpg
	git clone https://github.com/aio-libs/aiohttp upstream/aiohttp
	hg clone https://bitbucket.org/ollyc/yoyo upstream/yoyo
