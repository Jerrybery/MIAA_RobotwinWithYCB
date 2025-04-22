import sys
sys.path.append("/home/jerry/code/RoboTwin")
sys.path.append("/home/jerry/code/RoboTwin/envs")
from envs import *
import importlib
def class_decorator(task_name):
    envs_module = importlib.import_module(f'envs.{task_name}')
    try:
        env_class = getattr(envs_module, task_name)
        env_instance = env_class()
    except ModuleNotFoundError:
        raise SystemExit("No such task")
    return env_instance
def main():
    task_name = "obj_obs" # Replace with the desired task name
    task = class_decorator(task_name)
    task.setup_demo()
    task.visualize()
if __name__ == "__main__":
    main()