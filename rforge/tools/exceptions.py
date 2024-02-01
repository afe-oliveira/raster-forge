class ErrorMessages:
    __TEMPLATE = "ERROR: {message}"

    @classmethod
    def file_not_found(cls, file_path: str):
        return cls.__TEMPLATE.format(message=f"File '{file_path}' not found.")

    @classmethod
    def bad_input(cls, name: str, expected_type: str, provided_type: str = None):
        if provided_type is not None:
            return cls.__TEMPLATE.format(
                message=f"'{name}' is {provided_type}, but it must be {expected_type}."
            )
        else:
            return cls.__TEMPLATE.format(message=f"'{name}' must be {expected_type}.")
