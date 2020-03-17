# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration for test sessions.

This is a configuration file for use with `nox <https://nox.thea.codes/>`__.

This particular configuration is modelled after the configuration for the
`google-cloud-biguery
<https://github.com/googleapis/python-bigquery/blob/master/noxfile.py>`__
package.
"""

import os

import nox


PYTHON_VERSION = "3.7"
BLACK_PATHS = ("data_validation", "tests", "noxfile.py", "setup.py")


@nox.session(python=PYTHON_VERSION)
def lint(session):
    """Run linters.
    Returns a failure if the linters find linting errors or sufficiently
    serious code quality issues.
    """

    session.install("black==19.10b0", "flake8")
    session.install("-e", ".")
    session.run("flake8", "data_validation")
    session.run("flake8", "tests")
    session.run("black", "--check", *BLACK_PATHS)


@nox.session(python=PYTHON_VERSION)
def lint_setup_py(session):
    """Verify that setup.py is valid."""

    session.run("python", "setup.py", "check", "--strict")


@nox.session(python=PYTHON_VERSION)
def blacken(session):
    """Run black.
    Format code to uniform standard.
    """
    # Pin a specific version of black, so that the linter doesn't conflict with
    # contributors.
    session.install("black==19.10b0")
    session.run("black", *BLACK_PATHS)