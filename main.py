import pars
import postgres

if __name__ == '__main__':
    postgres.drop_sql()
    postgres.create_sql()
    pars.sanic_start()
