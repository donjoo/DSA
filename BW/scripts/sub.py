import subprocess

# Run a simple shell command
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print(result.stdout)  # prints the output of the command

output = subprocess.check_output(["echo", "Hello from subprocess"], text=True)
print(output)
process = subprocess.Popen(["ping", "-c", "2", "google.com"],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True)

stdout, stderr = process.communicate()
print("Output:", stdout)
print("Errors:", stderr)
