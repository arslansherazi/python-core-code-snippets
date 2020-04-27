"""
    Important Points::
    => arguments start with hyphen "-" are optional but hyphen is not part of argument name
"""
import argparse


def get_arguments_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-language',
        type=str,
        default='en'
    )
    parser.add_argument(
        'latitude',
        type=float,
        default=31.5204
    )
    parser.add_argument(
        'longitude',
        type=float,
        default=74.3587
    )
    return parser


if __name__ == '__main__':
    arguments_parser = get_arguments_parser()
    arguments_data = arguments_parser.parse_args()
    print('latitude::', arguments_data.latitude)
    print('longitude::', arguments_data.longitude)
    print('language::', arguments_data.language)
