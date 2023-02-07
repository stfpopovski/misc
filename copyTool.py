def file_copy():
    src = input(r"Enter source path: ")
    dst = input(r"Enter destination path: ")

    import subprocess
    subprocess.call(["xcopy", src, dst])

    import requests
    response = requests.get("http://localhost:7778/cache/info")
    resp = response.json()
    dirty_bytes = resp["dirtyBytes"]

    while dirty_bytes != 0:
        print("Waiting for background cloud upload to finish...")
        response = requests.get("http://localhost:7778/cache/info")
        resp = response.json()
        dirty_bytes = resp["dirtyBytes"]

    else:
        print(f"Background cloud upload finished with {response} and dirtyBytes value of: {dirty_bytes}")
        print("Sending PUT request...")
        put_response = requests.put("http://localhost:7778/app/sync")
        print(f"PUT request finished with {put_response}")
