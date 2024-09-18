load("@aspect_rules_py//py:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])


py_library(
    name="lib",
    srcs=glob(include=["**"], exclude=["**/__pycache__"]),
)
