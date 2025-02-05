#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

print("Compile Program")
compile = raw_input("\nWrite Program name: ")
py_compile.compile(compile)
