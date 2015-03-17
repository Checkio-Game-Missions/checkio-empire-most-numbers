from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations, validators

import settings
import settings_env
from tests import TESTS

Validator = validators.FloatEqualValidator

Validator.PRECISION = 3


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    VALIDATOR = Validator
    FUNCTION_NAME = "most_difference"
    ENV_COVERCODE = {
        "python_2": covercodes.py_unwrap_args,
        "python_3": covercodes.py_unwrap_args,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": representations.unwrap_arg_representation,
        "python_3": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation,
    }
