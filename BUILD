package(default_visibility = ["//visibility:public"])

exports_files([
    "WORKSPACE",
    "python-requirements.txt",
])

load("@rules_uv//uv:pip.bzl", "pip_compile")
load("@rules_uv//uv:venv.bzl", "create_venv")
#load("@rules_python//python:pip.bzl", pip_compile="compile_pip_requirements")

pip_compile(
    name = "generate_requirements_txt",
    requirements_in = "//:requirements.in", # default
    requirements_txt = "//:requirements.txt", # default
    data=["//pythontest:lib"],
)

create_venv(
    name = "create_venv",
    requirements_txt = "//:requirements.txt", # default
    data=["//pythontest:lib"],
)

