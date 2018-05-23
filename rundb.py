import subprocess


def run():
    path = "~/MongoDB/"
    database_init_cmd = "mongod --dbpath "
    database_init_cmd += path
    subprocess.call(database_init_cmd, shell=True)


if __name__ == "__main__":
    run()
