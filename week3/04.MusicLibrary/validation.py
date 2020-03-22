class Validation:
    @staticmethod
    def validate_that_arguments_are_not_empty_strings(title, artist, album, length):
        if title == "" or artist == "" or album == "" or length == "":
            raise ValueError("Arguments cannot missed or be empty strings")

    @staticmethod
    def validate_length(length):
        if ':' not in length or (':' in length and len(length) <= 3):
            raise ValueError("Length should be in format 'hh:mm:ss'")
