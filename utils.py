import subprocess
import os
import datetime
import time


class Utils:

    WORKSPACE_DIR = "/home/kate/itis3/workspace/"
    OUTPUT_DIR = "/home/kate/itis3/logs/"

    def __init__(self):
        pass

    # creats output file with timestamp in it's name
    def create_output_file(self, filename):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
        return open(os.path.join(self.OUTPUT_DIR, filename + st), 'w')

    #crawls subdirectories and calls given command
    def call(self, command):
        with self.create_output_file(command[1]) as f:
            dir_list = os.listdir(self.WORKSPACE_DIR)
            for repo in dir_list:
                repo_full_path = os.path.join(self.WORKSPACE_DIR, repo)
                if os.path.isdir(repo_full_path):
                    os.chdir(repo_full_path)
                    f.write('\n--------- ' + repo + ' -------------\n')
                    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = proc.communicate()
                    f.write(out)
                    f.write(err)
                    os.chdir(self.WORKSPACE_DIR)