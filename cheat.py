def generate_script(lines=4000):
    script = """\
# This is an example script with {} lines.

def main():
    print("Hello, this is line 1")

""".format(lines)

    for i in range(2, lines + 1):
        script += f'    print("This is line {i}")\n'

    return script

if __name__ == "__main__":
    script_content = generate_script()
    with open("long_script.py", "w") as file:
        file.write(script_content)
