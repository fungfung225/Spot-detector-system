from inspect import signature, Parameter
from libs.Log import *


class FunctionPipeline(Debugable):

    def __init__(self):
        super().__init__()
        self.function_pipeline = {}
        self.function_params = {}

    def execute_functions(self):
        for k, func in self.function_pipeline:
            func(**self.function_params[k])

    def execute_pipeline(self, init_state):
        current_state = init_state
        for k, func in self.function_pipeline.items():
            current_state = func(current_state, **self.function_params[k])
            if current_state is None:
                print(func.__name__)
            assert current_state is not None
        return current_state

    def add_func(self, func, param_dict: dict):
        idx = len(self.function_pipeline)
        self.function_pipeline[idx] = func
        self.init_func_param(idx, param_dict)
        self.log_debug_msg(func.__name__, "added with params:", param_dict)
        return idx

    def init_func_param(self, func_idx, param_dict: dict):
        idx = func_idx
        func = self.function_pipeline[func_idx]
        self.function_params[idx] = dict()
        for p_name, p_value in signature(func).parameters.items():
            if param_dict is not None and p_name in param_dict:
                self.function_params[idx][p_name] = param_dict[p_name]
            elif p_value.default is not Parameter.empty:
                self.function_params[idx][p_name] = p_value.default

    def update_func_params(self, func_idx: int, param_dict: dict):
        func = self.function_pipeline[func_idx]
        for p_name, p_value in signature(func).parameters.items():
            if p_name in param_dict:
                self.function_params[func_idx][p_name] = param_dict[p_name]

    def update_func_param(self, func_idx: int, param_name: str, param_value):
        self.function_params[func_idx][param_name] = param_value

    def replace_func(self, func_idx, func, param_dict: dict):
        self.function_pipeline[func_idx] = func
        self.init_func_param(func_idx, param_dict)
