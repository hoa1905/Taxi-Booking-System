import re


def check_email(email):
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )

    if re.fullmatch(regex, email):
        email_result = True
    else:
        email_result = False
    return email_result


def check_phone(mobile):
    regex = re.compile("^(?:0|\+?84)\s?(?:\d\s?){9,11}$")

    if re.fullmatch(regex, mobile):
        mobile_result = True
    else:
        mobile_result = False
    return mobile_result


def check_credit(credit):
    regex = re.compile("(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}")

    if re.fullmatch(regex, credit):
        credit_result = True
    else:
        credit_result = False
    return credit_result


def name_validation(name):
    regex = re.compile(
        "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"
    )

    if re.fullmatch(regex, name):
        name_result = True
    else:
        name_result = False
    return name_result


def password_validation(password):
    regex = re.compile(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )

    if re.fullmatch(regex, password):
        password_result = True
    else:
        password_result = False
    return password_result
