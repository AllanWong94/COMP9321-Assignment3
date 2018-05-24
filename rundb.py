import subprocess
import platform

def mac_run():
    path = "~/MongoDB/"
    database_init_cmd = "mongod --dbpath "
    database_init_cmd += path
    subprocess.call(database_init_cmd, shell=True)

def win_run():
    # path = ""
    pass

def lin_run():
    pass

def run():
    sys = platform.system()
    if sys == "Darwin":
        mac_run()
    elif sys == "Windows":
        win_run()
    elif sys == "Linux":
        lin_run()

if __name__ == "__main__":
    run()
    # print(platform.system())
    print("database running")