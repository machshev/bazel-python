package(default_visibility = ["//visibility:public"])

exports_files([
    "WORKSPACE",
    "python-requirements.txt",
])

load("@rules_python//python:pip.bzl", pip_compile="compile_pip_requirements")

pip_compile(
    name = "generate_requirements_txt",
    requirements_in = "//:requirements.in", # default
    requirements_txt = "//:requirements.txt", # default
    data = ["//pythontest:lib"],
)


load("@pypi//:requirements.bzl", "install_deps")

install_deps()


load("@pypi//:requirements.bzl", "entry_point")

alias(
    name = "bp",
    actual = entry_point(
        pkg = "bp",
        script = "bp",
    ),
)
