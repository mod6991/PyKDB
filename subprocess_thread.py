import subprocess
import threading
import time

stdout = None
stderr = None

def background_calculation():
    global stdout
    global stderr

    # time.sleep(5)

    process = subprocess.Popen(['cmd', '/c', 'ping 127.0.0.1'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()


def main():
    thread = threading.Thread(target=background_calculation)
    thread.start()

    # wait here for the result to be available before continuing
    thread.join()

    print("stdout: ", stdout.decode())
    print("stderr: ", stderr.decode())

if __name__ == '__main__':
    main()