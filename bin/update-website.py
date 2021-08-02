import os
import json


def python_to_markdown(code):
    question = None
    if code.startswith('"""'):
        question = code.split('"""')[1].replace("\n", "<br>")
    elif code.startswith("#"):
        question = ""
        for line in code.split("\n"):
            if line.startswith("#"):
                question += line[1:]
            else:
                break

    if question is not None:
        return "## %q%\n```python\n%code%\n```\n".replace("%q%", question).replace("%code%", code)
    else:
        return ""


class Updater:
    def __init__(self, base_path, ignored_dirs=(), ignored_files=()):
        with open("./template.md", "r") as template:
            self.template = template.read()

        self.base_path = base_path
        self.ignored_dirs = ignored_dirs
        self.ignored_files = ignored_files

        self.sub_dirs, self.files, self.markdown = self.get_children()

        self.doc_path = self.base_path.replace("../", "../docs")

        self.update_website()

    def get_children(self):
        print("\033[32mGENERATING MARKDOWN...\033[0m")
        all_children = os.listdir(self.base_path)
        sub_dirs, files = [], []

        dir_markdown, file_markdown = "", ""

        for child in all_children:
            if os.path.isdir(f"{self.base_path}/{child}"):
                sub_dirs.append(child)
                if child not in self.ignored_dirs:
                    dir_markdown += f"- [{child.upper().replace('-', ' ')}]" \
                                    f"(./{child})\n"
            else:
                if child not in self.ignored_files:
                    files.append(child)
                    if child.endswith(".py"):
                        with open(f"{self.base_path}/{child}", "r") as source:
                            code = source.read()
                        file_markdown += python_to_markdown(code)

        markdown = self.template.replace("%structure%", dir_markdown + file_markdown)
        return sub_dirs, files,  markdown

    def update_website(self):
        with open(f"{self.doc_path}/index.md", "w") as index_file:
            index_file.write(self.markdown)

        for sub_dir in self.sub_dirs:
            if sub_dir not in self.ignored_dirs:
                if not os.path.exists(f"{self.doc_path}/{sub_dir}"):
                    os.mkdir(f"{self.doc_path}/{sub_dir}")

                Updater(f"{self.base_path}/{sub_dir}",
                        self.ignored_dirs,
                        self.ignored_files)

    def __repr__(self):
        return json.dumps(self.tree, indent="╞=>")


updater = Updater(
    "../",
    (
        "venv",
        ".idea",
        ".git",
        "docs",
        "bin",
        "test"
    ),
    (
        ".gitignore",
        "README.md"
    )
)

print("\033[32mDONE...\033[0m\n\n")
