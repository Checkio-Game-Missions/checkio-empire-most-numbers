from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations, validators, ENV_NAME


import settings_env
from tests import TESTS

Validator = validators.FloatEqualValidator

Validator.PRECISION = 3


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    VALIDATOR = Validator
    DEFAULT_FUNCTION_NAME = "most_difference"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "mostDifference"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: covercodes.py_unwrap_args,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: representations.unwrap_arg_representation,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation,
    }
