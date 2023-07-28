import psutil

def proc_list():
    all_processes = psutil.process_iter(['pid', 'name', 'username'])
    print(f"{'PID':<8}{'NAME':<40}{'USERNAME'}")
    print("=" * 60)
    for process in all_processes:
        pid = process.info['pid']
        name = process.info['name']
        username = process.info['username']
        print(f"{pid:<8}{name:<40}{username}")

if __name__ == "__main__":
    proc_list()
