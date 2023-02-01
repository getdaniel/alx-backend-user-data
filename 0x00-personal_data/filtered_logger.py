#!/usr/bin/env python3
""" Personal Data."""
import logging
from mysql.connector import connect
from os import getenv
import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ Returns the log message obfuscated."""
    extract, replace = (patterns['extract'], patterns['replace'])
    return re.sub(extract(fields, separator), replace(redaction), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class."""

    REDACTION = "***"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize the RedactingFormatter class."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log Record."""
        msg = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)

        return txt


def get_logger() -> logging.Logger:
    """ Creates a logger."""
    logger = logging.getLogger('user_data')
    stream_handler = loging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PIP_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)

    return logger

def get_db():
    """ Connects to secure database."""
    db_host = getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = getenv("PERSONAL_DATA_DB_NAME", "")
    db_user = getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connection = connect(
        host=db_host,
        port=3306,
        user=db_user,
        password=db_pwd,
        database=db_name,
    )

    return connection
