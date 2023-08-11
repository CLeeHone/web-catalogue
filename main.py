import ApplicationLauncher
import os

if __name__ == '__main__':
    print(os.getenv('PYTHON_MONGODB_URI'))
    ApplicationLauncher.launch_app()
